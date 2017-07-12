$(function(){

	$.ajaxSetup({async:false});

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;

	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
		alert(num);
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;

		}
		else
		{
			$('#user_name').next().hide();
			error_name = false;
			$.get('/user/register_check2/',{'uname':$('#user_name').val()},function (data) {
				if (data.check == '1'){
					$('#user_name').next().html('用户名以存在');
					$('#user_name').next().show();
					error_name = true;
                }
            })

		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			$.alert('注册成功，请尽情的享用吧！！！');
			return true;
		}
		else
		{
			return false;
		}

	});


	(function ($) {
            $.extend({
                _isalert: 0,
                alert: function () {
                    if (arguments.length) {
                        $._isalert = 1;
                        $.confirm.apply($, arguments);
                    }
                },
                confirm: function () {
                    var args = arguments;
                    if (args.length && (typeof args[0] == 'string') && !$('#alert_overlay').length) {
                        if (!$('#alert_style').length) $('body').append('<style id="alert_style" type="text/css">#alert_overlay{position:fixed;width:100%;height:100%;top:0;left:0;z-index:999;background:#000;filter:alpha(opacity=5);opacity:.05}#alert_msg{position:fixed;width:400px;margin-left:-201px;left:50%;top:20%;z-index:1000;border:1px solid #aaa;box-shadow:0 2px 15px rgba(0,0,0,.3);background:#37ab40}#alert_content{padding:20px;font-size:14px;text-align:left;color:#fff}#alert_buttons{padding:10px;border-top:1px solid #aaa;text-align:right;box-shadow:0 1px 0 #fff inset;background:#eee;-moz-user-select:none;-webkit-user-select:none;-ms-user-select:none}#alert_buttons .alert_btn{padding:5px 12px;margin:0 2px;border:1px solid #aaa;background:#eee;cursor:pointer;border-radius:2px;font-size:14px;outline:0;-webkit-appearance:none}#alert_buttons .alert_btn:hover{border-color:#bbb;box-shadow:0 1px 2px #aaa;background:#eaeaea}#alert_buttons .alert_btn:active{box-shadow:0 1px 2px #aaa inset;background:#e6e6e6}</style>');
                        var dialog = $('<div id="alert_overlay"></div><div id="alert_msg"><div id="alert_content">' + args[0] + '</div><div id="alert_buttons"><button class="alert_btn alert_btn_ok">确定</button><button class="alert_btn alert_btn_cancel">取消</button></div></div>');
                        if ($._isalert) dialog.find('.alert_btn_cancel').hide();
                        dialog.on('contextmenu', function () {
                            return !1;
                        }).on('click', '.alert_btn_ok', function () {
                            dialog.remove() && (typeof args[1] == 'function') && args[1].call($, !0);
                        }).on('click', '.alert_btn_cancel', function () {
                            dialog.remove() && (typeof args[1] == 'function') && args[1].call($, !1);
                        }).appendTo('body');
                    }
                    $._isalert = 0;
                }
            });
        })($);


	function sleep(numberMillis) {
		var now = new Date();
		var exitTime = now.getTime() + numberMillis;
		while (true) {
		now = new Date();
		if (now.getTime() > exitTime)
		return;
			}
		}


$(".reg_sub").click(function () {


        	});





})