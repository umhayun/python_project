## 인스타 크롤링 함수 실행
import instar
china=['중국여행','중국맛집']
japan=['일본여행','일본맛집']
america=['미국여행','미국맛집']
taiwan=['태국여행','태국맛집']
vietnam=['베트남여행','베트남맛집']
words_list={'china':china,'japan':japan,'america':america,'taiwan':taiwan,'vietnam':vietnam}
import pandas as pd
for key in words_list:
    data=instar.crawling(words_list[key])
    results_df=pd.DataFrame(data)
    results_df.columns=['content','date','like','place','tags']
    results_df.to_excel('country/'+key+'.xlsx',index=False)