dict1 = {"hello" :1 , "bye":2}
dict2 = {"good" :3,"bad":4}
dict3 = {"excellent":1,"poor":9}
combined = {**dict1 , **dict2 , **dict3}
print(combined)