## 나라별 경보 지도 제작 함수
# 단계별 지도와 통합 지도 제작
def test(level):
    import pandas as pd
    import folium
    import json
    import folium
    geo_path='data/World_Countries__Generalized_.geojson'
    geo_data=json.load(open(geo_path,encoding='utf8'))
    lvl=pd.read_excel('data/나라별경보.xlsx')
    if level>0:
        lvl=lvl.loc[lvl['level']==level,['country','eng','level','total','rank']]
    map = folium.Map(location = [35.762887375145795, 84.08313219586536], zoom_start = 2,
                max_bounds = True, tiles='Stamen Toner',
                    min_lat = -84,
                max_lat = 84, min_lon = -175, max_lon = 187)

    m=folium.Choropleth(geo_data=geo_data,
                        data=lvl,
                        nan_fill_color='white',
                        line_color='white',
                        columns=['eng','level'],
                        line_opacity=0,
                        line_weight=-0,
                        fill_color='Set1',                                                   
                        key_on='properties.AFF_ISO').add_to(map)
    return m.save(f'level{level}.html')



