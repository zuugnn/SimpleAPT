import json
import requests
import pandas as pd


def request_header(down_url):
    h = {
        "Connection": "keep-alive",
        "Host": "new.land.naver.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    }

    r = requests.get(down_url, headers=h)
    r.encoding = "utf-8-sig"
    rr = json.loads(r.text)
    return rr


def get_regions(code):
    down_url = "https://new.land.naver.com/api/regions/list?cortarNo=" + code
    temp = request_header(down_url)
    temp = pd.DataFrame(temp["regionList"])[["cortarNo", "cortarName"]]
    temp = temp.to_dict("records")
    return temp


cate = [[], [], [], []]
cate_info = {}
sido_list = [
    {
        "cortarNo": "1100000000",
        "centerLat": 37.566427,
        "centerLon": 126.977872,
        "cortarName": "서울시",
        "cortarType": "city",
    }
]
cate_info["cateName"] = "집 구하기"
cate_info["parentName"] = ""
cate_temp = dict(cate_info)
cate[0].append(cate_temp)

for m in range(len(sido_list)):
    sido_name = sido_list[m]["cortarName"]
    gungu_list = get_regions(sido_list[m]["cortarNo"])
    gungu_cnt = len(gungu_list)
    cate_info["cateName"] = sido_name
    cate_info["parentName"] = "집 구하기"
    cate_temp = dict(cate_info)
    cate[1].append(cate_temp)
    # 해당 시의 모든 구
    for j in range(gungu_cnt):
        gungu_name = gungu_list[j]["cortarName"]
        print(gungu_name, j + 1, "/", gungu_cnt)
        dong_list = get_regions(gungu_list[j]["cortarNo"])
        dong_cnt = len(dong_list)
        cate_info["cateName"] = gungu_name
        cate_info["parentName"] = sido_name
        cate_temp = dict(cate_info)
        cate[2].append(cate_temp)
        # 해당 구의 모든 동
        for k in range(dong_cnt):
            dong_name = dong_list[k]["cortarName"]
            print("  ", dong_name, dong_list[k]["cortarNo"], k + 1, "/", dong_cnt)
            cate_info["cateName"] = dong_name
            cate_info["parentName"] = gungu_name
            cate_temp = dict(cate_info)
            cate[3].append(cate_temp)
# print(cate)

with open("./res/categoryInfo.js", "w", encoding="UTF-8") as f:
    f.write("var categoryInfo = ")
with open("./res/categoryInfo.js", "a", encoding="UTF-8") as f:
    json.dump(cate, f, indent="\t", ensure_ascii=False)

