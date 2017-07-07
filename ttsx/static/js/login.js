 $(function () {

        $.ajaxSetup({
            data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            async:false,
        });

        var error_name = false;
	    var error_password = false;

	$('#uname').blur(function() {
		check_user_name();
	});

	$('#upwd').blur(function() {
		check_pwd();
	});

	$('#uname').focus(function() {
		$('#uname').next().html('');
	    $('#uname').next().hide();
	});

	$('#upwd').focus(function() {
		$('#upwd').next().html('');
	    $('#upwd').next().hide();
	});

	function check_user_name() {
        var len = $('#uname').val().length;

        if (len < 5 || len > 20)
        {
            $('#uname').next().html('请输入5-20个字符的用户名');
            $('#uname').next().show();
            error_name = true;
        }
        else
        {
            $('#uname').next().hide();
            error_name = false;
            $.post('/user/login_check2/', {'uname': $('#uname').val(),'upwd':$('#upwd').val()}, function (data) {
                if (data.check == '0')
                {
                    $('#uname').next().html('用户名不存在');
                    $('#uname').next().show();
                    error_name = true;
                }
            });
        }
    }

	function check_pwd() {
	    if (error_name != true){
            var len = $('#upwd').val().length;

            if (len < 8 || len > 20) {
                $('#upwd').next().html('密码最少8位，最长20位')
                $('#upwd').next().show();
                error_password = true;
            }
            else {
                $('#upwd').next().hide();
                error_password = false;
                $.post('/user/login_check2/', {'upwd': $('#upwd').val(), 'uname': $('#uname').val()}, function (data) {
                    if (data.check == '1')
                    {
                        $('#upwd').next().html('密码错误，请重新输入');
                        $('#upwd').next().show();
                         error_password = true;
                    }
                });
            }
            }
        else
        {
            error_password=true;
        }
    }

	$('form').submit(function() {
		check_user_name();
		check_pwd();

		if(error_name == false && error_password == false)
		{
            if($('#checkbox').attr('checked'))
            {
                document.cookie="uname="+$('#uname').val();
            }
			return true;
		}
		else
		{
			return false;
		}
	});

    });

