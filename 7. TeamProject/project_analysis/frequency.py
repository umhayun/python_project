def frequency(country):
    
    import pandas as pd
    raw_total=pd.read_excel('country/'+country+'.xlsx')
    tags_total=[]
    for tags in raw_total['tags']:
        tags=tags[2:-2]
        tags_list=tags.split("', '")
    
    for tag in tags_list:
        if tag=='':
            continue
        tags_total.append(tag)
    from collections import Counter    
    tag_counts=Counter(tags_total)
    STOPWORD=[]
    if country=='japan':
        STOPWORD=['#일본여행','#맛스타그램','#카페스타그램','#일본맛집','#일본','#사진계정맞팔','#여행에미치다','#맛집','#여행스타그램']
    elif country=='america':
        STOPWORD=['#미국여행','#미국맛집','#미국','#맛집','#먹방']
    elif country=='china':
        STOPWORD=['#중국여행','#중국맛집','#중국','#맛스타그램','#여행사진','#해외여행','#차이홍중국어','#신당동중국어','#여행스타그램','#여행에미치다','#셀스타그램','#먹스타그램','#맞팔','#신당동중국어원어민']
    elif country=='vietnam':
        STOPWORD=['#베트남여행','#베트남맛집','#베트남','#여행스타그램','#소통','#맛스타그램','#먹스타그램']
    elif country=='taiwan':
        
    import re
    p=re.compile('#[^가-힣]+')
    tags_total_selected=[]
    for tag in tags_total:
        m=p.match(tag)
        if tag not in STOPWORD:
            if m==None:
                tags_total_selected.append(tag)
    tag_counts_selected=Counter(tags_total_selected)
    return tag_counts_selected