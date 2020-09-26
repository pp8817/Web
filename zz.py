import requests  # 웹스크래핑 하게 해주는 패키지


indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=\
python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=\
&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch") # 원하는 사이트 지정하기

print(indeed_result.text)  # 해당 사이트의 HTML 정보 가져오기

