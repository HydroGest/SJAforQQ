from bs4 import BeautifulSoup
import json,requests,re,os,traceback
from mirai import GroupMessage,Mirai, WebSocketAdapter, FriendMessage, Plain
import projects,sja,compare
from mirai.models import Forward,ForwardMessageNode

def get_json_info(page_html):
    soup=BeautifulSoup(page_html,'html.parser')
    original_json=soup.find_all(id='__NEXT_DATA__')
    #print(original_json[0])
    pattern = re.compile(r'<[^>]+>',re.S)
    result = pattern.sub('', str(original_json[0]))
    return result
    
#QQ机器人登录部分，无需理会    
bot=Mirai(
    qq=12345,
    adapter=WebSocketAdapter(
        verify_key='xxxxxx', 
        host='localhost',
        port=8088
    )
)

@bot.on(GroupMessage)
async def compareProject(event:GroupMessage):
    if '/比对' in str(event.message_chain) and str(event.message_chain)[0]=='/':
        await bot.send(event,'正在尝试比对作品......')
        message=str(event.message_chain).split(' ')
        try:
            url1,url2=message[1],message[2]
        except:
            return bot.send(event,'错误！用法："/比对 <作品1链接或ID> <作品2链接或ID>"')
        if '/community/main/compose' in url1:
            urlType='project'
        elif '666J' in str(url1):
            url1='https://world.xiaomawang.com/community/main/compose/'+str(url1)
            urlType='project'
        if '/community/main/compose' in url2:
            urlType='project'
        elif '666J' in str(url2):
            url2='https://world.xiaomawang.com/community/main/compose/'+str(url2)
            urlType='project'
        try:
            
            json_data1=json.loads(get_json_info(requests.get(url1).text))
            json_data2=json.loads(get_json_info(requests.get(url2).text))
            print('作品获取成功，开始比对.....')
            project=json_data1['props']['initialState']['detail']['composeInfo']
            md5=str(os.path.basename(project['fileKey']))
            data1=compare.get_project(projects.download(md5))
            project=json_data2['props']['initialState']['detail']['composeInfo']
            md5=str(os.path.basename(project['fileKey']))
            data2=compare.get_project(projects.download(md5))
            #print(data1,data2)
            result=compare.get_diff(data1,data2)
            msg_chain=[
                '作品%s与作品%s的比对结果：\n'%(os.path.basename(url1),os.path.basename(url2)),
                '平均相似度：%s\n'%result['similarity'],
                '-------统计-------\n',
                '总计%s处修改，其中作品1较作品2有：\n'%result['diff_num'],
                '- 新增%s个积木；\n'%result['add'],
                '- 删除%s个积木；\n'%result['remove'],
                '- 替换%s个积木；\n'%result['replace'],
                '作品2中作品1的积木含量：%s\n'%result['include_num'],
                '详细可以使用SJA查询。'
            ]
            
            print('源码分析成功')
            Str = "".join(msg_chain)
            print(Str)
            return bot.send(event,Str)
        except Exception as e:
            traceback.print_exc()
            return bot.send(event,'错误！获取作品数据失败，作品不存在。报错信息：%s'%repr(str(e)))
        
        

@bot.on(GroupMessage)
async def SJA(event:GroupMessage):
    if '/SJA' in str(event.message_chain) and str(event.message_chain)[0]=='/':
        await bot.send(event,'正在分析作品......')
        message=str(event.message_chain).split(' ')
        try:
            url=message[1]
        except:
            return bot.send(event,'错误！用法："/SJA <作品链接或ID>"')
        if '/community/main/compose' in url:
            urlType='project'
        elif '666J' in str(url):
            url='https://world.xiaomawang.com/community/main/compose/'+str(url)
            urlType='project'
        try:
            
            json_data=json.loads(get_json_info(requests.get(url).text))
            print('作品获取成功')
            project=json_data['props']['initialState']['detail']['composeInfo']
            md5=str(os.path.basename(project['fileKey']))
            result=sja.analyze(projects.download(md5))
            print('源码分析成功')
        except Exception as e:
            return bot.send(event,'错误！获取作品数据失败，作品不存在。报错信息：%s'%repr(str(e)))
        msg_chain=[
        '作品%s的分析数据：\n'%os.path.basename(url),
        '大小：%s字节\n' % str(result['size']),
        '角色数: %s\n' % str(result['spriteNum']-1),
        '变量数: %s\n' % str(result['variables']),
        '积木数: %s\n' % str(result['blocksNum']),
        '-------统计-------\n',
        '运动: '+str(result['blocks']['motion'])+' 占比：'+str(int(result['blocks']['motion']/result['blocksNum']*10000)/100)+'%\n',
        '外观: '+str(result['blocks']['looks'])+' 占比：'+str(int(result['blocks']['looks']/result['blocksNum']*10000)/100)+'%\n',
        '声音: '+str(result['blocks']['sound'])+' 占比：'+str(int(result['blocks']['sound']/result['blocksNum']*10000)/100)+'%\n',
        '事件: '+str(result['blocks']['event'])+' 占比：'+str(int(result['blocks']['event']/result['blocksNum']*10000)/100)+'%\n',
        '控制: '+str(result['blocks']['control'])+' 占比：'+str(int(result['blocks']['control']/result['blocksNum']*10000)/100)+'%\n',
        '侦测: '+str(result['blocks']['sensing'])+' 占比：'+str(int(result['blocks']['sensing']/result['blocksNum']*10000)/100)+'%\n',
        '运算: '+str(result['blocks']['operator'])+' 占比：'+str(int(result['blocks']['operator']/result['blocksNum']*10000)/100)+'%\n',
        '数据: '+str(result['blocks']['data'])+' 占比：'+str(int(result['blocks']['data']/result['blocksNum']*10000)/100)+'%\n',
        '模块: '+str(result['blocks']['procedures'])+' 占比：'+str(int(result['blocks']['procedures']/result['blocksNum']*10000)/100)+'%\n',
        '音乐: '+str(result['blocks']['music'])+' 占比：'+str(int(result['blocks']['music']/result['blocksNum']*10000)/100)+'%\n',
        '画笔: '+str(result['blocks']['pen'])+' 占比：'+str(int(result['blocks']['pen']/result['blocksNum']*10000)/100)+'%\n',
        '其他: '+str(result['blocks']['others'])+' 占比：'+str(int(result['blocks']['others']/result['blocksNum']*10000)/100)+'%'
        ]
        Str = "".join(msg_chain)
        print(Str)
        return bot.send(event,Str)
bot.run(port=7767)