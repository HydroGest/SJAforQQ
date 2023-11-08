import io
import zipfile
import json

def load_project(file_name):
# 打开文件
    with open(file_name, 'rb') as project_file:
        # 读取文件内容
        project_data = project_file.read()
    # 使用io.BytesIO将project_data包装成输入流
    project_bytes = io.BytesIO(project_data)
    # 打开zip压缩包
    with zipfile.ZipFile(project_bytes) as project:
        # 读取project.json文件
         with project.open('project.json') as project_json:
            # 读取文件内容并打印
            project_json_data=project_json.read()
            return project_json_data

def analyze(project_data):
    project_json=json.loads(project_data)
    sprite_nums=len(project_json['targets'])
    blocks={
        'motion':0,
        'looks':0,
        'sound':0,
        'event':0,
        'control':0,
        'sensing':0,
        'operator':0,
        'data':0,
        'procedures':0,
        'music':0,
        'pen':0,
        'others':0
    }
    block_counts=0
    variables=0
    for sprite in project_json['targets']:
        variables += len(sprite['variables'])+len(sprite['lists'])
        block_counts += len(sprite['blocks'])
        for block in sprite['blocks']:
            try:
                opcode=sprite['blocks'][block]['opcode']
                block_type=opcode.split('_')[0]
                if block_type not in blocks:
                    blocks['others']+=1
                else:
                    blocks[block_type]+=1
            except:
                pass
    size=len(project_data.encode())
    return {
        'size':size,
        'spriteNum':sprite_nums,
        'variables':variables,
        'blocksNum':block_counts,
        'blocks':blocks
    }
    

'''
result=analyze(load_project('project.sb3'))
print('角色数: %s' % str(result['spriteNum']-1))
print('变量数: %s' % str(result['variables']))
print('积木数: %s' % str(result['blocksNum']))
print('-------统计-------')
print('运动: '+str(result['blocks']['motion'])+' 占比：'+str(int(result['blocks']['motion']/result['blocksNum']*10000)/100)+'%')
print('外观: '+str(result['blocks']['looks'])+' 占比：'+str(int(result['blocks']['looks']/result['blocksNum']*10000)/100)+'%')
print('声音: '+str(result['blocks']['sound'])+' 占比：'+str(int(result['blocks']['sound']/result['blocksNum']*10000)/100)+'%')
print('事件: '+str(result['blocks']['event'])+' 占比：'+str(int(result['blocks']['event']/result['blocksNum']*10000)/100)+'%')
print('控制: '+str(result['blocks']['control'])+' 占比：'+str(int(result['blocks']['control']/result['blocksNum']*10000)/100)+'%')
print('侦测: '+str(result['blocks']['sensing'])+' 占比：'+str(int(result['blocks']['sensing']/result['blocksNum']*10000)/100)+'%')
print('运算: '+str(result['blocks']['operator'])+' 占比：'+str(int(result['blocks']['operator']/result['blocksNum']*10000)/100)+'%')
print('数据: '+str(result['blocks']['data'])+' 占比：'+str(int(result['blocks']['data']/result['blocksNum']*10000)/100)+'%')
print('模块: '+str(result['blocks']['procedures'])+' 占比：'+str(int(result['blocks']['procedures']/result['blocksNum']*10000)/100)+'%')
print('音乐: '+str(result['blocks']['music'])+' 占比：'+str(int(result['blocks']['music']/result['blocksNum']*10000)/100)+'%')
print('画笔: '+str(result['blocks']['pen'])+' 占比：'+str(int(result['blocks']['pen']/result['blocksNum']*10000)/100)+'%')
print('其他: '+str(result['blocks']['others'])+' 占比：'+str(int(result['blocks']['others']/result['blocksNum']*10000)/100)+'%')
'''

