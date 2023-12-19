from flask import Flask, render_template

from templates.data_view import DataView

# 创建Flask应用程序实例
app = Flask(__name__)


# 定义路由及视图函数
@app.route('/index')
def index():
    # 生成饼状图
    view.scene_classify_pie()
    # 打开index.html
    return render_template('index.html')


# 启动程序
if __name__ == '__main__':
    view = DataView()
    app.run('0.0.0.0', 8000, debug=True)
