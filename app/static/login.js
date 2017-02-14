$(document).ready(function(){

	$("#submit").click(function(){
		$.ajax({
			url: "/checkLogin",
			data: $("#login").serialize(),
			type: "POST",
			success: function(response){
				response = JSON.parse(response);
				if (response["status"] == "OK"){
					window.open("/index", "_self");
				}else{
					alert("Wrong Username or password!");
				}
			},
			error: function(){
			}
		});
	});
});