# 北京疫情封控小区可视化

目前北京的疫情通告以文字为主，缺乏直观的展示。这个仓库根据“北京本地宝”每日发布的封控区通告，通过百度地图API查询出封控区的经纬度位置，并绘制成地图，希望可以为疫情下的生活带来一些便利。

因为构建过程中的某些步骤存在一些不确定性（例如解析封控区地名），因此所获得结果并不完全准确，只是试图从全局角度提供一些参考。

### 访问地址
[北京疫情封控区地图](https://maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075)

<iframe
    src="https://maplab.amap.com/share/mapv/272589e85e2eb5c8861ad9a4f7e08075"
    width="600" 
    height="300" 
    frameborder="0" 
    scrolling="no">
</iframe>

### 构建步骤
1. 从"北京本地宝"网站获取封控区名单，滤除不必要字符；
2. 解析并提取出封控区地名；
3. 通过百度地图API，获取每个封控区地名对应的经纬度，因为可视化的部分选择了高德地图，注意需要将经纬度从“百度坐标系（bd09）”转换为“火星坐标系（gcj02）”；
4. 将数据上传至高德地图开放平台并创建地图。

### TODO
- [ ] 差异化展示每日新增的数据，以反映疫情发展的趋势
- [ ] 完善地名解析部分，提高准确率