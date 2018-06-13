# -*- coding:utf-8 -*-  
from flask import Flask, make_response, json
app = Flask(__name__)

@app.route('/1')
def hello1():
    return 'Hello'#当只有一个字符串返回，会自动转换为状态码为200， MIME 类型是text/html的response对象

@app.route('/2')
def hello11():
    test={'key1':'value1','key2':'value2'}
    return json.dumps(test)#返回json格式文件

@app.route('/3')
def hello2():
    return 'Hello3',200,{"key":"value"}#当返回多个字段时,会智能对照,MIME 类型是text/html的response对象,字典里的东西会被当成headers

@app.route('/4')
def hello3():
 rsp = make_response('hello4') #这个方法生成了一个response对象
 rsp.mimetype = 'text/plain'
 rsp.headers['key'] = 'value'
 rsp.set_cookie('user','wang')#这个值可以用接下来访问的request.cookies来取得
 return rsp #使用make_response来处理response

if __name__ == '__main__':
    app.run(debug=True)
