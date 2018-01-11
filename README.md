# weathers(spider)
### models:html5lib(or lxml),requests,BeautifulSoup
### Purpose:Getting the weather information of China from http://www.weather.com.cn/ by python
### ording to the code,we analysis the tags,split them and obtain information what we want.
```
  provice:{
    city,
    min_temperature，
    others...(you can obtain any information from the url(http://www.weather.com.cn/))
  }
```
### some results:
```dictionary
{"北京": [{"city": "北京", "min_temp": "-10"}, {"city": "海淀", "min_temp": "-9"}, {"city": "朝阳", "min_temp": "-11"}, {"city": "顺义", "min_temp": "-9"}, {"city": "怀柔", "min_temp": "-14"}, {"city": "通州", "min_temp": "-9"}, {"city": "昌平", "min_temp": "-10"}, {"city": "延庆", "min_temp": "-16"}, {"city": "丰台", "min_temp": "-10"}, {"city": "石景山", "min_temp": "-9"}, {"city": "大兴", "min_temp": "-11"}, {"city": "房山", "min_temp": "-10"}, {"city": "密云", "min_temp": "-14"}, {"city": "门头沟", "min_temp": "-9"}, {"city": "平谷", "min_temp": "-14"}, {"city": "东城", "min_temp": "-11"}, {"city": "西城", "min_temp": "-9"}]}
{"天津": [{"city": "天津", "min_temp": "-9"}, {"city": "武清", "min_temp": "-12"}, {"city": "宝坻", "min_temp": "-13"}, {"city": "东丽", "min_temp": "-10"}, {"city": "西青", "min_temp": "-10"}, {"city": "北辰", "min_temp": "-12"}, {"city": "宁河", "min_temp": "-14"}, {"city": "和平", "min_temp": "-9"}, {"city": "静海", "min_temp": "-11"}, {"city": "津南", "min_temp": "-12"}, {"city": "滨海新区", "min_temp": "-9"}, {"city": "河东", "min_temp": "-9"}, {"city": "河西", "min_temp": "-9"}, {"city": "蓟州", "min_temp": "-14"}, {"city": "南开", "min_temp": "-9"}, {"city": "河北", "min_temp": "-9"}, {"city": "红桥", "min_temp": "-9"}]}
{"河北": [{"city": "石家庄", "min_temp": "-7"}, {"city": "保定", "min_temp": "-11"}, {"city": "张家口", "min_temp": "-16"}, {"city": "承德", "min_temp": "-17"}, {"city": "唐山", "min_temp": "-15"}, {"city": "廊坊", "min_temp": "-10"}, {"city": "沧州", "min_temp": "-10"}, {"city": "衡水", "min_temp": "-9"}, {"city": "邢台", "min_temp": "-7"}, {"city": "邯郸", "min_temp": "-7"}, {"city": "秦皇岛", "min_temp": "-15"}]}
{"山西": [{"city": "太原", "min_temp": "-13"}, {"city": "大同", "min_temp": "-22"}, {"city": "阳泉", "min_temp": "-10"}, {"city": "晋中", "min_temp": "-15"}, {"city": "长治", "min_temp": "-9"}, {"city": "晋城", "min_temp": "-7"}, {"city": "临汾", "min_temp": "-7"}, {"city": "运城", "min_temp": "-7"}, {"city": "朔州", "min_temp": "-21"}, {"city": "忻州", "min_temp": "-16"}, {"city": "吕梁", "min_temp": "-14"}]}
{"内蒙古": [{"city": "呼和浩特", "min_temp": "-17"}, {"city": "包头", "min_temp": "-18"}, {"city": "乌海", "min_temp": "-16"}, {"city": "乌兰察布", "min_temp": "-19"}, {"city": "通辽", "min_temp": "-20"}, {"city": "赤峰", "min_temp": "-18"}, {"city": "鄂尔多斯", "min_temp": "-14"}, {"city": "巴彦淖尔", "min_temp": "-18"}, {"city": "锡林郭勒", "min_temp": "-25"}, {"city": "呼伦贝尔", "min_temp": "-32"}, {"city": "兴安盟", "min_temp": "-20"}, {"city": "阿拉善盟", "min_temp": "-13"}]}
{"香港": [{"city": "香港", "min_temp": "11"}]}
{"澳门": [{"city": "澳门", "min_temp": "9"}]}
{"台湾": [{"city": "台北", "min_temp": "6"}, {"city": "高雄", "min_temp": "11"}, {"city": "台中", "min_temp": "6"}]}
```
