$(function(){
    // ***********************************首页轮播图 
    function lunbo(){
        // 获取所有图片li
        var imgs = $(".banner").children(".list_img").find("li");
        // 获取所有小圆点li
        var dots = $(".banner").children(".list_dot").find("li");
        // console.log(imgs);
        // 获取图片长度
        var imglen = $(".banner").find("img").length;
        //console.log(imglen);
        var num = 0;
        // 创建定时器  每3秒自动轮播
        var timer = setInterval(change,3000);
        function change(){
            num ++;
            if(num == imglen){
                num = 0;
            }
            dots.eq(num).addClass("active").siblings().removeClass("active");
            imgs.eq(num).fadeIn().siblings().fadeOut();
        }
        // 当鼠标移入banner区域时清除定时器  显示左右按钮
        $(".banner").mouseenter(function(){
            clearInterval(timer);
            $(".banner").children("span").css("display","block")
        })
        // 当鼠标移出banner区域时还原定时器（注意是还原不是重新声明） 隐藏左右按钮
        $(".banner").mouseleave(function(){
            timer = setInterval(change,3000);
            $(".banner").children("span").css("display","none")
        })
        // 点击左边按钮时 切换到上一张图片
        $("#pre").click(function(){
            num --;
            if(num == -1){
                num = imglen - 1;
            }
            dots.eq(num).addClass("active").siblings().removeClass("active");
            imgs.eq(num).fadeIn().siblings().fadeOut();
        });
        // 点击右边按钮 切换到下一张图片
        $("#next").click(function(){
            num ++;
            if(num == imglen){
                num = 0;
            }
            dots.eq(num).addClass("active").siblings().removeClass("active");
            imgs.eq(num).fadeIn().siblings().fadeOut();
        })
        // 鼠标移入小圆点 显示对应图片
        dots.mouseenter(function(){
            // 获取当前小圆点的索引值
            num = $(this).index();
            dots.eq(num).addClass("active").siblings().removeClass("active");
            imgs.eq(num).fadeIn().siblings().fadeOut();
        })
    }
    lunbo();
// ******************************* 购物车页面功能
    function shopcar(){
        // 当点击增加按钮时 商品数量增加 小计总额也同时增加
        var subtotal = null;
        $(".number .add").click(function(){
            // 先获取当前商品数量
            var n = $(this).siblings(".Products_num").val();
            // 获取当前商品单价
            var price = $(this).parents(".num_price").siblings(".unit_price").text();
            //console.log(price);
            n ++;
            // 商品数量
            $(this).siblings(".Products_num").val(n)
            // console.log(n);
            // 计算商品小计 结果保留两位小数
            subtotal = (price * n).toFixed(2);
            $(this).parents(".num_price").siblings(".subtotal").text(subtotal);
            getSum()
        });
        // 当点击减少按钮时 商品数量增加 小计总额也同时减少
        $(".number .reduce").click(function(){
            var n = $(this).siblings(".Products_num").val();
            // 获取当前商品单价
            var price = $(this).parents(".num_price").siblings(".unit_price").text();
            n --;
            if(n == 0) return;
            $(this).siblings(".Products_num").val(n)
            // 计算商品小计 结果保留两位小数
            subtotal = (price * n).toFixed(2);
            $(this).parents(".num_price").siblings(".subtotal").text(subtotal);
            getSum()
        });
        // 给表单添加一个change事件
        $(".Products_num").change(function(){
            // 先获取表单值
            var n = $(this).val();
            if(n < 1){
                n = 1;
                $(this).val("1");
            }
            // 获取当前商品单价
            var price = $(this).parents(".num_price").siblings(".unit_price").text();
            // 计算商品小计 结果保留两位小数
            subtotal = (price * n).toFixed(2);
            $(this).parents(".num_price").siblings(".subtotal").text(subtotal);
            getSum()
        });

        // 计算总数量和总价
        function getSum() {
            var num = 0;
            var subTotal = 0;
            // 计算商品数量
            $(".Products_num").each(function(index,dom){
                num += parseInt($(dom).val());
            });
            console.log(num);
            $(".payment .sum").html(num);
            // 计算商品总价
            $(".subtotal").each(function(index,dom){
                subTotal += parseInt($(dom).text());
            });
            console.log(subTotal);
            $(".payment .total").html(subTotal.toFixed(2));
        }
        getSum()
        // 购物车表单全选功能
        // 给全选按钮添加点击事件
        $(".inputAll").change(function(){
            // 将全选按钮的checked值赋给其他按钮
            $(".checks,.inputAll").prop("checked",$(this).prop("checked"));
            // 当按钮被选中时 添加背景颜色
            if($(this).prop("checked")){
                $(".checks").parents("li").css("backgroundColor","pink");
            }else {
                $(".checks").parents("li").css("backgroundColor","");
            }
        });
        $(".checks").change(function(){
            // 当按钮被选中时 添加背景颜色
            if($(this).prop("checked")){
                $(this).parents("li").css("backgroundColor","pink");
            }else {
                $(this).parents("li").css("backgroundColor","");
            }
            var checkLength = $(".checks:checked").length;
            if($(".checks").length == checkLength) {
                $(".inputAll").prop("checked",true);
            }else {
                $(".inputAll").prop("checked",false);
            }
        });

        // 删除商品功能
        // 删除选中的商品
        $(".del").click(function() {
            $(".checks:checked").parents("li").remove();
            getSum()
        });
        // 删除所有商品
        $(".empty").click(function(){
            $(".shopProducts").empty();
            getSum()
        });
        // 删除当前商品
        $(".delCur").click(function(){
            $(this).parents("li").remove();
            getSum()
        });
    }
    shopcar()

    // ******************** 侧栏回到顶部
    // function backTop() {
    //     var sideBar = document.querySelector('#sideBar');
    //     var oimg = document.querySelector('#sideBar img');
    //     window.onscroll = function() {
    //         if(window.pageYOffset >= 500) {
    //             sideBar.style.display = 'block';
    //         }else {
    //             sideBar.style.display = 'none';
    //         }
    //     }
    //     oimg.onmouseover = function(){
    //         this.src = './images/top.gif';
    //         this.onclick = function() {
    //             // $("body,html").animate({scrollTop:"0"});
    //             document.documentElement.scrollTop = 0;
    //             // window.scroll(0,0);
    //         }
    //     }
    // }
    // backTop();
})