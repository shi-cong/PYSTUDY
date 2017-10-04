//登录、注册js
$(document).ready(function(){
    var input_arr = ['loginname','password','verifycode'];
    $.each(input_arr,function(i,item){
        $("#"+item).focus(function(){
            $("#"+item).parent().addClass("focus");
        });
        $("#"+item).blur(function(){
            $("#"+item).parent().removeClass("focus");
        });
    });

    var sLang = $("#language").val();

    //注册跳转
    $("#sign_btn").click(function(){
        window.location.href = (supporthttps==1 ? 'https://' : 'http://') + 'login.51job.com/register.php?lang='+sLang+'&from_domain=i&source=&url='+encodeURIComponent("http://www.51job.com/default.php");
    });

    $("#create_resume").click(function(){
        window.location.href = "http://i.51job.com/resume/tri_resume.php";
    });

    //首页导航浮层
    var showguide = $("#showguide").val();
    if(showguide == '1'){
        var html = '<style>.pop{width:100%;height:100%;background-color:#000;opacity:.5}.home_guide{position:relative;width:1002px;margin:0 auto;margin-top:45px}.home_guide .close{position:absolute;width:30px;height:30px;right:0;background:url(http://img01.51jobcdn.com/im/2016/temp/icon_close.png) center no-repeat;cursor:pointer}.home_guide .bg{width:1002px;height:400px;margin-bottom:30px;background:url(http://img01.51jobcdn.com/im/2016/temp/IMG_sxl.png) center no-repeat}.home_guide .btn{width:182px;float:none;height:60px;margin:0 auto;background:url(http://img01.51jobcdn.com/im/2016/temp/butte_ljty.png) center no-repeat;cursor:pointer}.home_guide.h2 .bg{width:1002px;height:384px;margin-bottom:0;background:url(http://img01.51jobcdn.com/im/2016/temp/IMG_dlh.png) center no-repeat}.home_guide.h2 .btn{position:absolute;width:101px;height:44px;left:505px;background:url(http://img01.51jobcdn.com/im/2016/temp/butten_zdl.png) center no-repeat;cursor:pointer}</style><div class="pop"></div><div class="home_guide"><div class="close"></div><div class="bg"></div><div class="btn" onclick="$(\'.close\').click();"></div></div>';
        var oLayerParams = {'layer_close_class': 'close'};
        oLayerSettings = jQuery.FLayer.init(oLayerParams);
        jQuery.FLayer.setContent(oLayerSettings,html);
        jQuery.FLayer.open(oLayerSettings);
    }

    var showguide = $("#showlayer").val();
    if(showguide == '1'){
        var html = '<style>.pop{width:100%;height:100%;background-color:#000;opacity:.5}.home_guide{position:relative;width:1002px;margin:0 auto;margin-top:45px}.home_guide .close{position:absolute;width:30px;height:30px;right:0;background:url(http://img01.51jobcdn.com/im/2016/temp/icon_close.png) center no-repeat;cursor:pointer}.home_guide .bg{width:1002px;height:400px;margin-bottom:30px;background:url(http://img01.51jobcdn.com/im/2016/temp/IMG_sxl.png) center no-repeat}.home_guide .btn{width:182px;height:60px;margin:0 auto;background:url(http://img01.51jobcdn.com/im/2016/temp/butte_ljty.png) center no-repeat;cursor:pointer}.home_guide.h2 .close{top:-160px}.home_guide.h2 .bg{width:1002px;height:384px;margin-bottom:0;background:url(http://img01.51jobcdn.com/im/2016/temp/IMG_dlh.png) center no-repeat}.home_guide.h2 .btn{position:absolute;width:101px;height:44px;top:40px;left:505px;background:url(http://img01.51jobcdn.com/im/2016/temp/butten_zdl.png) center no-repeat;cursor:pointer}</style><div class="pop"></div><div class="home_guide h2"><div class="close"></div><div class="bg"></div><div class="btn" onclick="$(\'.close\').click();"></div></div>';
        var oLayerParams = {'layer_close_class': 'close'};
        oLayerSettings = jQuery.FLayer.init(oLayerParams);
        jQuery.FLayer.setContent(oLayerSettings,html);
        jQuery.FLayer.open(oLayerSettings);
    }

    if(islogin==1){
        //首页个人名片信息
        var url = 'http://i.51job.com/userset/ajax/index_cv.php?jsoncallback=?';
        var lang = sLang;
        var flag = 0;
        $.ajaxSettings.async = false;
        $.getJSON(url,{lang:lang},function(data){
            if(data.resumeid != ""){
                $("#hasresume").show();
                $("#noresume").hide();
                $("#origin").hide();
                if(data.resumetype == '9'){
                    var resume_url = "http://i.51job.com/resume/paste_resume.php?lang="+lang+'&resumeid='+data.resumeid+"&"+(Math.round(Math.random()*10));
                }else{
                    var resume_url = "http://i.51job.com/resume/standard_resume.php?lang="+lang+'&resumeid='+data.resumeid+"&"+(Math.round(Math.random()*10));
                }
                $("#resumeurl").attr("href",resume_url);
                $("#avatal").attr("src",data.avatarurl).parent().attr("href", resume_url);
                $("#resumename").html(data.resumename).attr("href", resume_url);
                var index = (data.finishstar.toString()).indexOf('.');
                var star = "s"+(index == -1 ? parseInt(data.finishstar) : (data.finishstar.toString()).replace(".","_"));
                $("#finishstar").addClass(star).parent().attr("href", resume_url);
                $("#seeme").html(data.seenumber);
                $("#applynum").html(data.applynumber);
                $("#refreshresume").click(function(){
                    if(!$(this).hasClass("unclick")){
                        Refreshresume(data.resumeid,lang,'http://i.51job.com/resume');
                    }
                });
            }else{
                $("#hasresume").hide();
                $("#origin").hide();
                $("#noresume").show();
            }
        });
        $.ajaxSettings.async = true;
    }

});

function load(){
    var sLang = $("#language").val();
    var doc = $("#iframe1").contents().find("body").html();
    if(doc != ""){
        var data = eval('('+doc+')');
        var loginname = $("#loginname").val();
        var userpassword = $("#password").val();
        if(data.result=='0'){ //登录失败
            if(data.scode == '18'){
                var str = langs['name_pwd_error'];
                if(data.remainder == 1){
                    changeVerifyCode();
                    str = langs['seek_pwd'];
                }
                if($("#verifypic").is(":visible")){
                    changeVerifyCode();
                    $("#verifycode_ok").hide();
                }
                $("#p_err").html(str).show();
                $("#loginname").val("").focus().val(loginname);
            }
            if(data.scode == '3'){
                $("#p_err").html(langs['seek_pwd']).show();
                var objDate = new Date();
                var strTime = objDate.getTime();
                var code_url = (supporthttps==1 ? 'https://' : 'http://') + 'login.51job.com/ajax/verifycode.php?type=3&from_domain=my&t='+strTime;
                $("#verifyPic_img").attr('src',code_url);
                $("#verifypic").show();
                $("#verifycode_needed").val("1");
                $("#verifycode").val("");
                if(!('placeholder' in document.createElement('input'))){
                    $("#verifycode").focus().blur();
                }
                $("#loginname").val("").focus().val(loginname);
            }
            if(data.scode == '4' || data.scode == '27'){
                changeVerifyCode();
                $("#p_err").html(langs['piccode_error']).show();
                $("#verifycode").focus().parent().addClass("focus");
            }
            if(data.remainder == '0'){
                $("#p_err").html(langs['login_too_many']).show();
            }
        }else{
            if(data.url != ""){
                var url = (data.url).replace(/&amp;/g, '&');
                window.location.href = url;
            }else{   //静态页面替换
                $("#login_btn").html(langs['signIning']);
                //window.location.href = 'ht'+'tp://www.51job.com/default'+(sLang=='c' ? '.php' : '-e.php');
                //window.location.reload();
                window.location.href = 'ht'+'tp://my.51job.com/my/My_login_trace.php?url=ht'+'tp://www.51job.com'+(sLang == 'c' ? '' : '/default-e.php');
            }
        }
    }
}


function checkOK(){
    if(!checkaccount()){
        $("#loginname").focus();
        return false;
    }
    if(!checkpwd()){
        $("#password").focus();
        return false;
    }
    if($("#verifypic").is(":visible")){
        if(!checkVerifyCode()){
            $("#verifycode").focus();
            return false;
        }
    }
    document.domain = "51job.com";
    $("#login_form").attr("action",'ht'+'tp://login.51job.com/ajax/login.php');
    return true;
}


function checkaccount(){
    if($("#loginname").val() == ""){
        $("#p_err").html(langs['username_empty']);
        $("#p_err").show();
        return false;
    }
    $("#p_err").hide();
    return true;
}

function checkpwd(){
    if($("#password").val() == ""){
        $("#p_err").html(langs['pwd_empty']);
        $("#p_err").show();
        return false;
    }
    $("#p_err").hide();
    return true;
}

function checkVerifyCode(){
    var verifycode = $.trim($("#verifycode").val());
    if(verifycode == ''){
        $("#p_err").html(langs['piccode_empty']);
        $("#p_err").show();
        return false;
    }
    if(getlength(verifycode) != 4){
        $("#p_err").html(langs['piccode_error']).show();
        return false;
    }
    /*******************************************/
    var url = (supporthttps==1 ? 'https://' : 'http://') + 'login.51job.com/ajax/checkcode.php?jsoncallback=?';
    var type = $("#verifyPic_img").attr("type");
    var flag = 0;
    $.ajaxSettings.async = false;
    $.getJSON(url,{verifycode:verifycode,type:type,from_domain:'my'},function(data){
        if(data.result == '0'){
            flag = 1;
        }
    });
    $.ajaxSettings.async = true;
    if(flag == 1){
        $("#p_err").html(langs['piccode_error']).show();
        return false;
    }
    $("#p_err").hide();
    return true;
}

function changeVerifyCode(){
    var objDate = new Date();
    var strTime = objDate.getTime();
    url = $('#verifyPic_img').attr('src');
    var type = $('#verifyPic_img').attr('type');
    if(type == '' || type == undefined){
        type=3;
    }
    if(url.indexOf('?') > 0)
    {
        url = url.replace(/\?.*/g,'?');
    }else
    {
        url = url + '?';
    }
    url = url + 'type=' + type + '&from_domain=my&t=' + strTime;

    $('#verifyPic_img').attr('src',url);
    $("#verifycode").val("");
    if(!('placeholder' in document.createElement('input'))){
        $("#verifycode").focus().blur();
    }
    $("#verifycode_ok").hide();
}

//onkeyup 事件
function chkverifycode(){
    var verifycode = $("#verifycode").val();
    if(getlength(verifycode) == 4){
        var url = (supporthttps==1 ? 'https://' : 'http://') + 'login.51job.com/ajax/checkcode.php?jsoncallback=?';
        var type = $("#verifyPic_img").attr("type");
        var flag = 0;
        $.ajaxSettings.async = false;
        $.getJSON(url,{verifycode:verifycode,type:type,from_domain:'my'},function(data){
            if(data.result == '0'){
                $("#p_err").html(langs['piccode_error']).show();
                $("#verifycodechked").val("0");
                $("#verifycode_ok").hide();
                changeVerifyCode();
            }else{
                $("#verifycodechked").val("1");
                $("#verifycode_ok").show();
                $("#p_err").hide();
            }
        });
        $.ajaxSettings.async = true;
    }else{
        $("#verifycodechked").val("0");
        $("#verifycode_ok").hide();
    }
}

//密码明暗文
function showtext(){
    var str = $("#password").val();
    if($("#eye").hasClass("on")){
        var htm = '<input type="password" autocomplete="off" name="password" id="password" onfocus="getfocus(this.id)" onblur="removefocus(this.id)" value="'+str+'" placeholder="'+langs['password']+'"><em class="e_eye e_icon" onclick="showtext()" id="eye"></em>';
        $("#showpwd").html(htm);
    }else{
        var htm = '<input type="text" autocomplete="off" name="password" id="password" onfocus="getfocus(this.id)" onblur="removefocus(this.id)" value="'+str+'" placeholder="'+langs['password']+'"><em class="e_eye on e_icon" onclick="showtext()" id="eye"></em>';
        $("#showpwd").html(htm);
    }
}

//密码框获取焦点时加黄色框
function getfocus(obj_id){
    $("#"+obj_id).parent().addClass("focus");
}

//密码框失去焦点时去黄色框
function removefocus(obj_id){
    $("#"+obj_id).parent().removeClass("focus");
}

//刷新
function Refreshresume(ReSumeID,Lang,DOMAIN_MY)
{
	var request_url = DOMAIN_MY + '/ajax/refresh_resume.php?'+ Math.random() + '&jsoncallback=?';
	$.getJSON(request_url,{ReSumeID:ReSumeID,lang:$("#language").val()}, function(result) {
        var html = langs['refresh_success']+'<em class="angle"></em>';
		$("#refresh_re").html(html).show();
        timeoutButton(6, 'refreshresume');
        setTimeout(function(){$("#refresh_re").hide();},3000);
	});
}

function getlength(str){
	return str.replace(/[^\x00-\xff]/g,"**").length;
}

function timeoutButton(p_iExpireTime, p_sElementId)
{
    var oElement = $('#' + p_sElementId);

    if (!oElement.hasClass('unclick'))
    {
        oElement.toggleClass("unclick");
    }

    if (p_iExpireTime <= 1)
    {
        oElement.toggleClass("unclick");
        oElement.text(langs['refresh_resume']);
        $("#not_received").show();
    }
    else
    {
        p_iExpireTime -= 1;
        oElement.text(langs['refresh_timertext'] + ' ' + p_iExpireTime + 's');
        setTimeout('timeoutButton('+ p_iExpireTime +', "'+ p_sElementId +'")',"1000");
    }
}