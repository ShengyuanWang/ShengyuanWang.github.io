---
layout: post
title: "React Notes"
subtitle: "Reflection #01"
date: 2023-01-10
author: "SWang"
tags: [React]
---

# 组件

### 01-class 组件

```
import React from "react";

class App extends React.Component {
  render() {
    return (<div>hello react Component</div>)
  }
}

export default App
```

### 02-函数式组件

```
function App() {
    return <div>
        hello function Component
    </div>
}
//无状态组件
/**
 * 16.8 无状态
 * 16.8 react hooks
 */
export default App
```

> 在 React 16.8 版本之前是无状态组件，在 16.8 版本之后增添了 react hooks 方法来实现状态

### 03-组件的嵌套

```
import React, { Component } from "react";

class Child extends Component {
  render() {
    return <div> Child</div>;
  }
}

class Navbar extends Component {
  render() {
    return (
      <div>
        Navbar
        <Child></Child>
      </div>
    );
  }
}

function Swiper() {
  return <div>Swiper</div>;
}

const Tabbar = () => {
  return <div>Tabbar</div>;
};

export default class App extends Component {
  render() {
    return (
      <div>
        <Navbar></Navbar>
        <Swiper></Swiper>
        <Tabbar></Tabbar>
      </div>
    );
  }
}
```

> 注意这里 function 也可以使用 es6 箭头函数写法更加直观方便

### 04-组件的样式

```
import React, { Component } from "react";
import "./css/01-index.css"; //导入css, webpack支持

export default class App extends Component {
  render() {
    var myname = "kerwin";
    return (
      <div>
        {10 + 20}-{myname}
        <div className="active">222222</div>
        <label htmlFor="username">UserName: </label>
        <input type="text" id="username"></input>
      </div>
    );
  }
}

```

> 在 return 里面放上{}证明这里面是一个表达式，不是简单的 html 字符

# 事件绑定

### 事件绑定#01

```
import React, { Component } from "react";

export default class App extends Component {
  a = 100

  render() {
    return (
      <div>
        <input></input>
        <button
          onClick={() => {
            console.log("click1");
          }}
        >
          add1
        </button>

        <button onClick={this.handleClick2}>add2</button>
        <button onClick={this.handleClick3}>add3</button>
        <button
          onClick={() => {
            this.handleClick4();
          }}
        >
          add4
        </button>
      </div>
    );
  }

  handleClick2() {
    console.log("click2");
  }

  handleClick3 = () => {
    console.log("click3");
  };

  handleClick4 = () => {
    console.log("click4");
  };
}
```

> 在这里我们把每一个 button 都绑定上 onClick 时间，并且介绍了四种 onClick 引入的方式，这里的区别只是 this 的指向问题，当指向出错，我们可以用 bind 方法去绑定，并且这里最推荐使用第四种绑定方式

# Ref

```
import React, { Component } from "react";

export default class App extends Component {
  a = 100;
  myref = React.createRef();
  render() {
    return (
      <div>
        <input ref={this.myref}></input>
        <button
          onClick={() => {
            console.log("click1", this.myref.current.value);
          }}
        >
          add1
        </button>
      </div>
    );
  }
}
```
