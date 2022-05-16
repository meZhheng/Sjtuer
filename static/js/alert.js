window.alert = function(msg){
	let zIndex = 999999;							//修改弹出层z-index,应为最顶层,避免被覆盖
	let desColor = '#fff'						//提示信息字体颜色
	let style = `
        <style class="mask-style">
            .box-sizing{
                box-sizing: border-box;
            }
            .alertMask{
                position: fixed;	/*生成绝对定位的元素，相对于浏览器窗口进行定位*/
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                z-index: `+zIndex+`;
                transition: 0.5s;
            }
            .alertContainer{
                min-width: 100px;	/*容器最小240px*/
                max-width: 160px;	/*容器最大320px*/
                height: 40px;
                border-radius: 4px;
                color: `+desColor+`;
                overflow: hidden;		
                background: #333333;	
                opacity: 0.8;				
                padding: 12px 30px;	
            }
            .alertDes{
                text-align: center;
                letter-spacing: 1px;
                font-size: 14px;
                line-height: 18px;
                color: `+desColor+`;
            }
        </style>
	`;

	let head = document.getElementsByTagName('head')[0];
	head.innerHTML += style		//头部加入样式,注意不可使用document.write()写入文件,否则出错

	const body = document.getElementsByTagName('body')[0];

	let alertMask = document.createElement('div');
	let alertContainer = document.createElement('div');
	let alertDes = document.createElement('span');

	body.append(alertMask);
	alertMask.classList.add('alertMask');
	alertMask.classList.add('box-sizing');

	alertMask.append(alertContainer);
	alertContainer.classList.add('alertContainer');
	alertContainer.classList.add('box-sizing');

	alertContainer.append(alertDes);
	alertDes.classList.add('alertDes');
	alertDes.classList.add('box-sizing');

	//加载提示信息
	alertDes.innerHTML = msg;
	//关闭当前alert弹窗
	function alert_closed(){
		body.removeChild(alertMask);
		let maskStyle = head.getElementsByClassName('mask-style')[0];
		head.removeChild(maskStyle);	//移除生成的css样式
	}
	setTimeout(function(){alert_closed();},1000);
}