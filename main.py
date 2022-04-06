from datetime import datetime, date
import requests
import json
import pandas as pd


def request_header(down_url, apt_code="a"):
    h = {
        "Connection": "keep-alive",
        "Host": "new.land.naver.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    }
    if apt_code != "a":
        h["authorization"] = (
            "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2"
            "NDQ3MzAyNTIsImV4cCI6MTY0NDc0MTA1Mn0.uiVk2CqAsklkHe0vvQ_vQTArkrOLqZJgkIScO0ypiZQ"
        )
        h["Referer"] = "https://new.land.naver.com/complexes/" + apt_code

    r = requests.get(down_url, headers=h)
    r.encoding = "utf-8-sig"
    rr = json.loads(r.text)
    return rr


def get_sido_info():
    """
    down_url = 'https://new.land.naver.com/api/regions/list?cortarNo=0000000000'
    temp = request_header(down_url)
    temp = list(pd.DataFrame(temp["regionList"])["cortarNo"])
    """
    temp = [
        {
            "cortarNo": "1100000000",
            "centerLat": 37.566427,
            "centerLon": 126.977872,
            "cortarName": "서울시",
            "cortarType": "city",
        }  # , {"cortarNo": "4100000000", "centerLat": 37.274939, "centerLon": 127.008689, "cortarName": "경기도", "cortarType": "city"}
    ]
    return temp


"""
{"regionList":[
    {"cortarNo":"1100000000","centerLat":37.566427,"centerLon":126.977872,"cortarName":"서울시","cortarType":"city"},
    {"cortarNo":"4100000000","centerLat":37.274939,"centerLon":127.008689,"cortarName":"경기도","cortarType":"city"},
    {"cortarNo":"2800000000","centerLat":37.456054,"centerLon":126.705151,"cortarName":"인천시","cortarType":"city"},
    {"cortarNo":"2600000000","centerLat":35.180143,"centerLon":129.075413,"cortarName":"부산시","cortarType":"city"},
    {"cortarNo":"3000000000","centerLat":36.350465,"centerLon":127.384953,"cortarName":"대전시","cortarType":"city"},
    {"cortarNo":"2700000000","centerLat":35.87139,"centerLon":128.601763,"cortarName":"대구시","cortarType":"city"},
    {"cortarNo":"3100000000","centerLat":35.5386,"centerLon":129.311375,"cortarName":"울산시","cortarType":"city"},
    {"cortarNo":"3600000000","centerLat":36.592907,"centerLon":127.292375,"cortarName":"세종시","cortarType":"city"},
    {"cortarNo":"2900000000","centerLat":35.160032,"centerLon":126.851338,"cortarName":"광주시","cortarType":"city"},
    {"cortarNo":"4200000000","centerLat":37.885399,"centerLon":127.72975,"cortarName":"강원도","cortarType":"city"},
    {"cortarNo":"4300000000","centerLat":36.636149,"centerLon":127.491238,"cortarName":"충청북도","cortarType":"city"},
    {"cortarNo":"4400000000","centerLat":36.63629,"centerLon":126.68957,"cortarName":"충청남도","cortarType":"city"},
    {"cortarNo":"4700000000","centerLat":36.518504,"centerLon":128.437796,"cortarName":"경상북도","cortarType":"city"},
    {"cortarNo":"4800000000","centerLat":35.238343,"centerLon":128.6924,"cortarName":"경상남도","cortarType":"city"},
    {"cortarNo":"4500000000","centerLat":35.820433,"centerLon":127.108875,"cortarName":"전라북도","cortarType":"city"},
    {"cortarNo":"4600000000","centerLat":34.816358,"centerLon":126.462443,"cortarName":"전라남도","cortarType":"city"},
    {"cortarNo":"5000000000","centerLat":33.488976,"centerLon":126.498238,"cortarName":"제주도","cortarType":"city"}
]}
"""


def get_gungu_info(sido_code):
    down_url = "https://new.land.naver.com/api/regions/list?cortarNo=" + sido_code
    temp = request_header(down_url)
    temp = pd.DataFrame(temp["regionList"])[["cortarNo", "cortarName"]]
    temp = temp.to_dict("records")
    """
    # 강남구만
    temp = [
        {
            "cortarNo": "1168000000",
            "centerLat": 37.517408,
            "centerLon": 127.047313,
            "cortarName": "강남구",
            "cortarType": "dvsn",
        }
    ]
    """

    return temp


def get_dong_info(gungu_code):
    down_url = "https://new.land.naver.com/api/regions/list?cortarNo=" + gungu_code
    temp = request_header(down_url)
    temp = pd.DataFrame(temp["regionList"])[["cortarNo", "cortarName"]]
    temp = temp.to_dict("records")
    return temp


def get_apt_list(dong_code):
    down_url = (
        "https://new.land.naver.com/api/regions/complexes?cortarNo="
        + dong_code
        + "&realEstateType=APT&order="
    )
    temp = request_header(down_url)
    try:
        temp = list(pd.DataFrame(temp["complexList"])["complexNo"])
    except:
        temp = []
    return temp


def get_apt_info(apt_code):
    down_url = (
        "https://new.land.naver.com/api/complexes/"
        + apt_code
        + "?sameAddressGroup=false"
    )
    temp = request_header(down_url, apt_code)
    return temp


def get_Cafe24_cate():
    h = {
        "authority": "kresca.cafe24.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    }
    r = requests.get(
        "https://kresca.cafe24.com/exec/front/Product/SubCategory", headers=h
    )
    r.encoding = "utf-8-sig"
    rr = json.loads(r.text)
    return rr


def get_HTHF(i, v):
    HT = {"HT001": "개별난방", "HT002": "중앙난방", "HT005": "지역난방"}
    HF = {"HF001": "도시가스", "HF002": "열병합", "HF003": "기름"}
    if i == "T":
        a = HT.get(v)
    else:
        a = HF.get(v)
    return a


cate = get_Cafe24_cate()

marker = []

sido_list = get_sido_info()
for m in range(len(sido_list)):
    sido_name = sido_list[m]["cortarName"]
    gungu_list = get_gungu_info(sido_list[m]["cortarNo"])
    gungu_apt_list = []  # 초기화
    gungu_cnt = len(gungu_list)
    # 해당 시의 모든 구
    for j in range(gungu_cnt):
        gungu_name = gungu_list[j]["cortarName"]
        print(gungu_name, j + 1, "/", gungu_cnt)
        dong_list = get_dong_info(gungu_list[j]["cortarNo"])
        dong_apt_list = []
        all_dong = []
        dong_cnt = len(dong_list)
        # 해당 구의 모든 동
        for k in range(dong_cnt):
            dong_name = dong_list[k]["cortarName"]
            print("  ", dong_name, dong_list[k]["cortarNo"], k + 1, "/", dong_cnt)
            apt_list = get_apt_list(dong_list[k]["cortarNo"])
            apt_list_data = []
            apt = []

            marker_info = {}

            apt_cnt = len(apt_list)
            """
            if apt_cnt > 5:
                apt_cnt = 5
            """
            # 해당 동의 모든 아파트
            for n in range(apt_cnt):
                # print("     아파트 수:", n + 1, "/", apt_cnt)

                apt = get_apt_info(apt_list[n])
                apt_detail_temp = apt["complexDetail"]
                apt_detail_pd = pd.DataFrame()

                # 자체 상품코드     진열상태	판매상태	상품분류 번호	상품분류 신상품영역	상품분류 추천상품영역   상품명	영문 상품명    모델명	상품 요약설명	상품 상세설명
                # 소비자가	공급가	상품가	판매가  옵션사용	품목 구성방식	옵션 표시방식	옵션입력	옵션 스타일     필수여부	제조일자	검색엔진최적화(SEO) 검색엔진 노출 설정
                complexNo = str(apt_detail_temp.get("complexNo"))
                apt_detail_pd.loc[n, "자체 상품코드"] = complexNo
                apt_detail_pd.loc[n, "진열상태"] = "Y"
                apt_detail_pd.loc[n, "판매상태"] = "Y"

                dong = str(apt_detail_temp.get("address"))  # 행정동
                dong_array = dong.split()
                cate_array1 = ["23", "25"]  # 미진열, 집 구하기
                for d in range(len(dong_array)):
                    for c in range(len(cate)):
                        if cate[c]["name"] == dong_array[d]:
                            cate_array1.append(str(cate[c]["cate_no"]))
                apt_detail_pd.loc[n, "상품분류 번호"] = "|".join(cate_array1)

                cate_array2 = []
                for i in range(len(cate_array1)):
                    cate_array2.append("N")
                apt_detail_pd.loc[n, "상품분류 신상품영역"] = "|".join(cate_array2)
                apt_detail_pd.loc[n, "상품분류 추천상품영역"] = "|".join(cate_array2)

                complexName = str(apt_detail_temp.get("complexName"))
                print("     ", complexName)
                apt_detail_pd.loc[n, "상품명"] = complexName
                apt_detail_pd.loc[n, "영문 상품명"] = (
                    str(apt_detail_temp.get("latitude"))
                    + ","
                    + str(apt_detail_temp.get("longitude"))
                )
                apt_detail_pd.loc[n, "모델명"] = dong

                totalHouseholdCount = str(
                    (lambda x: x + "세대" if x else None)(
                        str(apt_detail_temp.get("totalHouseholdCount"))
                    )
                )
                totalDongCount = str(
                    (lambda x: "총 " + x + "동" if x else None)(
                        str(apt_detail_temp.get("totalDongCount"))
                    )
                )

                totalHouseCnt = totalHouseholdCount + "(" + totalDongCount + ")"

                useApproveYmd = str(apt_detail_temp.get("useApproveYmd"))
                useApproveYmd_a = []
                if useApproveYmd:
                    useApproveY = useApproveYmd[0:4]
                    useApprovem = useApproveYmd[4:6]
                    useApproved = useApproveYmd[6:8]

                    useApproveYmd_a = [
                        useApproveY,
                        useApprovem,
                        useApproved,
                    ]
                    useApproveYmd_dot = ".".join(filter(None, useApproveYmd_a))
                else:
                    useApproveYmd_dot = ""

                supplyArea = str(
                    (lambda x: x + "㎡" if x else None)(
                        str(apt_detail_temp.get("minSupplyArea"))
                    )
                ) + str(
                    (lambda x: "~" + x + "㎡" if x else None)(
                        str(apt_detail_temp.get("maxSupplyArea"))
                    )
                )

                summary_a = [
                    totalHouseholdCount,
                    totalDongCount,
                    useApproveYmd_dot,
                    supplyArea,
                ]
                summary = "/".join(filter(None, summary_a))

                apt_detail_pd.loc[n, "상품 요약설명"] = summary

                lowFloor = str(
                    (lambda x: x + "층" if x else None)(
                        str(apt_detail_temp.get("lowFloor"))
                    )
                )
                highFloor = str(
                    (lambda x: "/" + x + "층" if x else None)(
                        str(apt_detail_temp.get("highFloor"))
                    )
                )
                useApprove_Y = str((lambda x: x + "년" if x else None)(useApproveY))
                useApprove_m = str(
                    (lambda x: " " + x + "월" if x else None)(useApprovem)
                )
                useApprove_d = str(
                    (lambda x: " " + x + "일" if x else None)(useApproved)
                )
                parkingPossibleCount = str(
                    (lambda x: x + "대" if x else None)(
                        str(apt_detail_temp.get("parkingPossibleCount"))
                    )
                )
                parkingCountByHousehold = str(
                    (lambda x: "(세대당 " + x + "대)" if x else None)(
                        str(apt_detail_temp.get("parkingCountByHousehold"))
                    )
                )
                batlRatio = str(
                    (lambda x: x + "%" if x else None)(
                        str(apt_detail_temp.get("batlRatio"))
                    )
                )
                btlRatio = str(
                    (lambda x: x + "%" if x else None)(
                        str(apt_detail_temp.get("btlRatio"))
                    )
                )
                constructionCompanyName = str(
                    apt_detail_temp.get("constructionCompanyName")
                )
                heatMethodType = get_HTHF(
                    "T", apt_detail_temp.get("heatMethodTypeCode")
                )
                heatFuelType = get_HTHF("F", apt_detail_temp.get("heatFuelTypeCode"))
                heat = ", ".join(filter(None, (heatMethodType, heatFuelType)))
                managementOfficeTelNo = str(
                    apt_detail_temp.get("managementOfficeTelNo")
                )
                address = (
                    apt_detail_temp.get("address")
                    + " "
                    + str(apt_detail_temp.get("detailAddress"))
                )
                roadaddress = (
                    apt_detail_temp.get("roadAddressPrefix")
                    + " "
                    + str(apt_detail_temp.get("roadAddress"))
                )
                pyoengNames = str(
                    (lambda x: x + "㎡" if x else None)(
                        str(apt_detail_temp.get("pyoengNames"))
                    )
                )

                apt_detail_pd.loc[n, "상품 상세설명"] = (
                    """<table class="infoTable_wrap">
                        <caption>
                            단지 정보
                        </caption>
                        <tbody>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">세대수</th>
                                <td class="table_td">"""
                    + totalHouseCnt
                    + """</td>
                                <th class="table_th" scope="row">저/최고층</th>
                                <td class="table_td">"""
                    + lowFloor
                    + highFloor
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">사용승인일</th>
                                <td class="table_td">"""
                    + useApprove_Y
                    + useApprove_m
                    + useApprove_d
                    + """</td>
                                <th class="table_th" scope="row">총주차대수</th>
                                <td class="table_td">"""
                    + parkingPossibleCount
                    + parkingCountByHousehold
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">용적률</th>
                                <td class="table_td">"""
                    + batlRatio
                    + """</td>
                                <th class="table_th" scope="row">건폐율</th>
                                <td class="table_td">"""
                    + btlRatio
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">건설사</th>
                                <td class="table_td" colspan="3">"""
                    + constructionCompanyName
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">난방</th>
                                <td class="table_td" colspan="3">"""
                    + heat
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">관리사무소</th>
                                <td class="table_td" colspan="3">"""
                    + managementOfficeTelNo
                    + """</td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">주소</th>
                                <td class="table_td" colspan="3">
                                    <p class="address">"""
                    + address
                    + """</p>
                                    <p class="address">"""
                    + roadaddress
                    + """</p>
                                </td>
                            </tr>
                            <tr class="infoTable_item">
                                <th class="table_th" scope="row">면적</th>
                                <td class="table_td" colspan="3">
                                    <div class="table_td_area">"""
                    + pyoengNames
                    + """</div>
                                </td>
                            </tr>
                        </tbody>
                    </table>"""
                )

                apt_detail_pd.loc[n, "소비자가"] = 0
                apt_detail_pd.loc[n, "공급가"] = 0
                apt_detail_pd.loc[n, "상품가"] = 0
                apt_detail_pd.loc[n, "판매가"] = 0
                """
                apt_detail_pd.loc[n, "옵션사용"] = "Y"
                apt_detail_pd.loc[n, "품목 구성방식"] = "T"
                apt_detail_pd.loc[n, "옵션 표시방식"] = "C"
                apt_detail_pd.loc[n, "옵션입력"] = (
                    "거래방식{매매|전월세}//면적{" + pyoengNames.replace(", ", "|") + "}"
                )
                apt_detail_pd.loc[n, "옵션 스타일"] = "R,R"
                apt_detail_pd.loc[n, "필수여부"] = "F|F"
                """
                apt_detail_pd.loc[n, "검색엔진최적화(SEO) 검색엔진 노출 설정"] = "N"

                apt_list_data.append(apt_detail_pd)

                # 마커 정보
                marker_info["dong"] = dong
                marker_info["complexName"] = complexName
                marker_info["complexNo"] = complexNo
                marker_info["totalHouseholdCount"] = totalHouseholdCount
                marker_info["totalDongCount"] = totalDongCount
                marker_info["useApproveYmd"] = useApproveYmd_dot
                marker_info["address"] = address
                marker_info["roadAddress"] = roadaddress
                marker_info["grd_la"] = apt_detail_temp.get("latitude")
                marker_info["grd_lo"] = apt_detail_temp.get("longitude")
                marker_info["supplyArea"] = supplyArea

                # list, dict 같은 구조체는 메모리값을 참조하여 같은 값만 저장되므로 새로운 구조체에 값을 복사해준다.
                marker_temp = dict(marker_info)
                marker.append(marker_temp)

            if len(apt_list_data) > 0:
                dong_apt_list.append(pd.concat(apt_list_data))

        gungu_apt_list = pd.concat(dong_apt_list, ignore_index=True)
        gungu_apt_list.to_csv(
            "./DEV/SimpleAPT/data/" + sido_name + " " + gungu_name + ".csv",
            encoding="CP949",
            index=False,
        )

with open("./DEV/SimpleAPT/res/complexMarkerInfo.js", "w", encoding="UTF-8") as f:
    f.write("var complexMarkerInfo = ")
with open("./DEV/SimpleAPT/res/complexMarkerInfo.js", "a", encoding="UTF-8") as f:
    json.dump(marker, f, indent="\t", ensure_ascii=False)

