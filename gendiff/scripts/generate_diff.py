# # gendiff/scripts/generate_diff.py

# from gendiff.scripts.read import read_file


# def generate_diff(file_path1, file_path2):
#     data1 = read_file(file_path1)
#     data2 = read_file(file_path2)

#     diff = {}
#     keys = sorted(set(data1.keys()) | set(data2.keys()))

#     for key in keys:
#         if key not in data1:
#             diff[key] = {'status': 'added', 'value': data2[key]}
#         elif key not in data2:
#             diff[key] = {'status': 'removed', 'value': data1[key]}
#         elif data1[key] != data2[key]:
#             diff[key] = {'status': 'modified', 'old_value': data1[key], 'new_value': data2[key]}
#         else:
#             diff[key] = {'status': 'unchanged', 'value': data1[key]}
    
#     #print(diff)
    
    
#     return diff