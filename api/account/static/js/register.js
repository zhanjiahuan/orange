$(function () {
    let URL=' http://127.0.0.1:8000/account/register/';
    var email=$('#email').val()
    var password=$('#password').val()
    var password_again=$('#passwordRepeat').val()
    data={
        email:email,
        password:password,
        password_again:password_again,

    }
    $('#register').click(function () {
        $.post(URL,data,function (result) {

            //邮箱账号已存在
            user_error=result.content.user_error
            if(user_error){
                $('#email').val(user_error)
            }
            //前后密码不一致
            password_error=result.content.password_error
            if(password_error){
                $('#email').val(password_error)
            }
            //获取去验证邮箱的界面
            mail_url=result.content.mail_url
            window.location.href=mail_url
        })
    })

})