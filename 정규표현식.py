import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033 : 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group())

text2 = "에러 1122 : 레퍼런스 오류\n 에러 1033 : 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)
print(mc)

text3 = "문의사항이 있으면 032-232-3245으로 연락 주시기 바랍니다."
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text3)
phonenumber = matchobj.group()
print(phonenumber)

text4 = "문의사항이 있으면 032-232-3245으로 연락 주시기 바랍니다."
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text4)
areaCode= matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)

text5 = "문의사항이 있으면 032-232-3245으로 연락 주시기 바랍니다."
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
matchobj = regex.search(text5)
areaCode= matchobj.group("area")
num = matchobj.group("num")
fullNum = matchobj.group()
print(areaCode, num)