from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__, static_folder='static')
@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""  # 默认输出为空字符串
    if request.method == 'POST':
        params = [
            request.form['path'],
            request.form['disk'],
            request.form['thread'],
            request.form['warmuptime'],
            request.form['runtime']
        ]
        command = ['./hello'] + params
        print("Executing command:", ' '.join(command))  # 打印即将执行的命令
        # 捕获命令输出
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        print(output)  #变量打印也正确啊
    return render_template('index.html', output=output)
#add 路由
@app.route('/home')
def home():
    print("Navigating to home.")
    return render_template('home.html')

@app.route('/hba')
def hba():
    return render_template('hba.html')

@app.route('/raid')
def raid():
    return render_template('raid.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在0.0.0.0上监听，允许同网段的设备访问

