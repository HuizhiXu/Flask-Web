# 基本知识

1. 基本流程大白话：客户端向服务器发送一个请求，服务器拍了拍应用程序，应用程序做出反应， 然后把响应返回给服务器，服务器把这个响应返回给客户端。

所有Flask程序必须有一个程序实例。

Flask调用视图函数后，会将视图函数的返回值作为响应的内容，返回给客户端。一般情况下，响应内容主要是字符串和状态码。

当客户端想要获取资源时，一般会通过浏览器发起HTTP请求。此时，Web服务器使用WSGI（Web Server Gateway Interface）协议，把来自客户端的所有请求都交给Flask程序实例。WSGI是为 Python
语言定义的Web服务器和Web应用程序之间的一种简单而通用的接口，它封装了接受HTTP请求、解析HTTP请求、发送HTTP，响应等等的这些底层的代码和操作，使开发者可以高效的编写Web应用。

程序实例使用Werkzeug来做路由分发（URL请求和视图函数之间的对应关系）。根据每个URL请求，找到具体的视图函数。
在Flask程序中，路由的实现一般是通过程序实例的route装饰器实现。route装饰器内部会调用add_url_route()方法实现路由注册。

调用视图函数，获取响应数据后，把数据传入HTML模板文件中，模板引擎负责渲染响应数据，然后由Flask返回响应数据给浏览器，最后浏览器处理返回的结果显示给客户端。

3. WSGI是什么？ WSGI(Web server gateway interface，读作"wiz-ghee")
   WSGI是在Web服务器和Web应用程序之间的一种接口，它封装了接收HTTP请求、解析HTTP请求、发送HTTP和响应这些功能。服务器用WSGI， 把接收自客户端的请求都转交给这个应用程序处理。
4. 什么是路由分发？ 路由是指URL请求和视图函数之间的对应关系。 路由分发是指根据每个URL请求，找到具体的视图函数。 route()装饰器把一个视图函数绑定到对应的URL上。
5. 应用程序使用Werkzeug来做
6.
7. 渲染数据是干啥？  
   应用程序会返回HTML页面。在使用中这个HTML页面里面的数据会根据传入的参数不同发生不同的变化。 当HTML代码保存到单独的文件中时，我们没法再使用字符串格式化或拼接字符串的方法在HTML代码中插入变量，
   这时我们需要使用模板引擎（template engine）。 借助模板引擎，我们可以再HTML文件中使用特殊的语法来标记变量， 这类包含固定内容和动态部分的可重用文件称为模板（template）。
   模板引擎的作用就是读取并执行模板中的特殊语法标记，并根据传入的数据将变量替换为实际值，输出最终的HTML页面，这个过程被称为渲染（rendering）。

Flask默认使用的模板引擎是jinja2，他是一个功能齐全的python模板引擎，输了设置变量，还允许我们在模板中添加if判断，执行for迭代，调整函数等，以各种方式 控制模板的输出。

对于jinja2来说，模板可以是任何格式的纯文本文件，比如HTML、XML、CSV等。

6.

视图函数返回的HTML数据往往要根据参数动态生成。

7. 局部上下文

# Web服务器

```python

from flask import Flask  # 导入Flask类

app = Flask(__name__)  # 这就是用来处理请求的应用程序


@app.route("/hello/")  # route装饰器来告诉Flask什么样的URL应该触发这个方法
def hello():
    return "<p>Hello,World</p>"


if __name__ == '__main__':
    app.run(debug=True)  # run函数让应用运行在本地服务器， debug = True会在代码变更时自动重新载入

```

问题：为什么在创建Flask应用的时候传入__name__参数呢？ 回答：
"__name__"取决于单独应用启动或者模块导入。 在单一模块中，__name__是模块文件名（一般为"__main__"），在导入到其他文件中时，__name__就是运行的文件名。

问题：路由里面的url要不要带斜线？ @app.route("/hello") ：只支持 http://127.0.0.1:5000/hello  
@app.route("/hello/)：同时支持http://127.0.0.1:5000/hello 和http://127.0.0.1:5000/hello/

问题：FLASK_APP是什么？

# 前端知识

HTML: 内容 css: 样式设置 Javas-Script: 交互（逻辑）

## HTML

创建一个html会出现下面的内容：

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
</head>
<body>

</body>
</html>
```

### 编辑head

`<head>`元素包含浏览器标签页中不可见的网站相关信息。
`<!DOCTYPE html>`  表示此HTML文档包含HTML5代码。  
`meta` 提供网站的描述信息。 元数据定义有关 HTML 文档的数据，例如字符集、脚本以及在其中打开网页的浏览器。

`<meta charset="UTF-8">`是告知浏览器此页面属于什么字符编码格式。  
`<meta http-equiv="X-UA-Compatible" content="IE=edge">` 这句话其实是指定浏览器按某种方式渲染， Compatible是“兼容的”意思，Edge模式告诉IE以最高级模式渲染文档。  
`<meta name="viewport" content="width=device-width, initial-scale=1.0">`这一句保证当前的 viewport变成ideal viewport。

viewport是浏览器上(也可能是一个app中的webview)用来显示网页的那部分区域。    
content属性值 :

     width:可视区域的宽度，值可为数字或关键词device-width

     height:同width

     intial-scale:页面首次被显示是可视区域的缩放级别，取值1.0则页面按实际尺寸显示，无任何缩放

     maximum-scale=1.0, minimum-scale=1.0;可视区域的缩放级别，

     maximum-scale用户可将页面放大的程序，1.0将禁止用户放大到实际尺寸之上。

     user-scalable:是否可对页面进行缩放，no 禁止缩放

`<body>`元素包含user在其浏览器中该课件的网站内容。

### 编辑body

body中的元素和属性：  
`<h1>`  标题元素  
`<p>`段落元素  
`<li>`列表项  
`<ul>`无序列表     
`id` 属性（在 `<p>` 元素中使用）可用于样式化单个元素      
`class` 属性（在 `<li>` 元素中使用）用于样式化同一类的所有元素

```html

<body>
<h1>Task List</h1>
<p id="msg">Current tasks:</p>
<ul>
    <li class="list">Add visual styles</li>
    <li class="list">Add light and dark themes</li>
    <li>Enable switching the theme</li>
</ul>

</body>

```

## 把内容和样式结合起来

有两种方法，第一种是在HTML页面中编写CSS，这个称为"内部CSS"。（一般不采用这种方法）  
第二种：  
使用一个单独的CSS页面，然后连接到HTML页面。这种叫做外部样式表。 操作：在<title>元素后面添加一个空白行，键入`link`，然后回车。 然后将`href`更新为`href="main.css"`
这样就将main.css里面的样式应用到了本html里面。

```html
<title>Title</title>
<link rel="stylesheet" href="main.css">


```

## CSS

main.css里面洗的就是CSS规则。 CSS 规则是将样式应用于 HTML 元素的方式。

规则的组成：

- 一个选择器，例如body 和ul
- 一对大括号
- 一个样式声明列表，用于确定所选元素的样式。  

ul 选择器选择页面中的 `<ul>` HTML 元素，以对其应用样式。 
声明为 font-family: helvetica 并确定样式应该是什么。  
“属性名称”为 font-family，“值”为 helvetica。

```css
body {
    font-family: monospace;
}

ul {
    font-family: helvetica;
}
```

### id选择器和类选择器
- .list是一个类选择器。每个包含设置为list的class属性的HTML元素都将获得在此选择器中
定义的样式。
- `#msg`是一个ID选择器。将其id属性设置为msg的HTML元素将获得在此选择器中定义的样式。
```css

.list {
    list-style: square;
}

#msg {
    font-family: monospace;
}
```

### 根选择器（放在css的顶部）

:root 选择器表示 HTML 页面中的 <html> 元素。  
:root 选择器在 CSS 规则中定义一组全局 CSS 变量，然后
可以在其他 CSS 规则中使用这些变量。
例如在root中定义三个颜色变量，然后在body中使用。  


```css
:root {
  --green: #00FF00;
  --white: #FFFFFF;
  --black: #000000;
}

body {
    background: var(--bg);
    color:var(--fontColor);
    font-family: helvetica;
}
```
## 把内容和交互结合起来
方法一：在html文件汇总添加javascript程序。（依然不推荐）  
方法二：使用一个单独的js文件，然后在HTML文件中链接它。
操作：在body结束元素之前，输入`<script src>"app.js"</script>`。
`<script>` 元素可以放在 `<head>` 中或 `<body>` 中的其他位置。  
`<noscript>`是一个容错功能，元素可用于在停用 JavaScript 时显示消息。  

通过`<noscript>`元素，代码
可以检测并规划功能何时不受支持或者不可用。  
```html

<script src>"app.js"</script>
<noscript>You need to enable JavaScript to view the full site.</noscript>
</body>

```

## Javascript
是一种可以添加交互性的编程语言。
例如我们要加一个转换theme的按钮，那么首先就在html中写一个button元素，然后在
css文件中添加响应的位置长宽高以及颜色，最后就在js文件中添加事件处理程序。


## 使用开发人员工具查看页面

1. 右键单击网页并选择“检查”以打开开发人员工具，或尝试以下快捷方式：

- 按“开发人员工具”的键盘快捷方式 F12。

- 在 Windows 和 Linux 上按 Ctrl+Shift+I，在 Mac 上按 Option+Command+I。

2. 选择“元素”选项卡。 将鼠标移到“元素”选项卡中显示的 HTML 元素上，然后展开各种元素的内容。

开发人员工具中的“元素”选项卡将显示在浏览器中呈现的文档对象模型 (DOM)。 调试时，查看浏览器如何解释你的源代码通常十分重要。

# 其他

## 字符编码

“utf-8”是一种字符编码。charset=”utf-8”是告知浏览器此页面属于什么字符编码格式，下一步浏览器做好“翻译”工作。常见的字符编码有：gb2312、gbk、unicode、utf-8。

各个字符编码含义： gb2312：代表国家标准第2312条，其中是不包含繁体的（虽然咱们不怎么使用繁体了，但是台湾还在使用繁体啊。那怎么办呢？）。 gbk：国家标准扩展版（增加了繁体，包含所有亚洲字符集）。
unicode：万国码（字面意思你也懂的）。 utf-8：unicode的升级版。

# 参考

1. https://flask-chs.readthedocs.io/zh_CN/master/quickstart.html
2. 局部上下文 https://blog.csdn.net/barrysj/article/details/51519254
3. 《使用 HTML、CSS 和 Javascript 构建简单的网站》 - Microsoft Learn https://learn.microsoft.com/zh-cn/training/modules/build-simple-website/3-html-basics
4. 《Web 入门教程》 - MDN