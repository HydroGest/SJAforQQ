# -- coding: utf-8 --**
import json_tools,json

def json_diff(json_1, json_2):
    return json_tools.diff(json_1, json_2)

def get_project(project_data):
    #project_data=project_data.decode()
    #print(type(project_data))
    project_json=json.loads(project_data)
    return project_json['targets']

def get_blocks(project_data):
    block_counts=0
    for sprite in project_data:
        block_counts += len(sprite['blocks'])
    return block_counts

def get_diff(project1,project2):
    diffs=json_diff(project1,project2)
    replace,remove,add=0,0,0
    #print(diffs)
    for diff in diffs:
        if 'replace' in diff:
            if 'blocks' in diff['replace']:
                replace+=1
        if 'remove' in diff:
            if 'blocks' in diff['remove']:
                remove+=1
        if 'add' in diff:
            if 'blocks' in diff['add']:
                add+=1
    source=get_blocks(project1)
    new=get_blocks(project2)
    include_num=(source-remove-replace)/new
    diff_num=replace+remove+add
    total_num=source+new
    #print(total_num)
    similarity=(total_num/2-diff_num)/(total_num/2)
    if similarity>1:
        similarity=1
    if similarity<0:
        similarity=0
    return {
        'include_num':include_num,
        'similarity':similarity,
        'diff_num':diff_num,
        'replace':replace,
        'remove':remove,
        'add':add
    }

    