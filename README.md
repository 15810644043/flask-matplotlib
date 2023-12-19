# Flask+matplotlib,生成饼状图输出到网页----记录

1. 生成饼状图
   [data_view.py](templates%2Fdata_view.py)
2. 生成饼状图并输出到网页
   [web_index.py](web_index.py)

3.启动服务：web_index.py
```
python web_index.py
```
4.访问网页：http://localhost:8000/index

# 报错注意：

    错误1：jinja2.exceptions.TemplateNotFound: index.html
    解决方案：render_template函数是解析templates文件夹下面的html页面，需要手动创建templates文件夹，并把index.html文件存入
    
    错误2：index.html，直接使用src='images/1.png'写法,找不到要加载的图片
    解决方案：在index.html中，img标签的src属性，需要写成这样：src="{{ url_for('static', filename='images/1.png') }}"


