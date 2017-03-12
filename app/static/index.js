function checkInputs(){
	var check = true;
	if ($("#name").val() == ""){
		alert("ERROR: Name is missing");
		check = false;
	}
	if($("#price").val() == 0){
		alert("ERROR: Price is missing");
		check = false;
	}
	if(typeof $('input[name="optradio"]:checked').val() == "undefined"){
		alert("ERROR: Rating is missing");
		check = false;
	}
	return check;
}

function sendDelete(value){
	$.ajax({
		url: "/deleteProduct",
		data: {"value" : value},
		type: "POST",
		success: function(response) {
			location.reload();
		    console.log(response);
		},
		error: function(error) {
		    console.log(error);
		}
	});
}

function showFadingImage(){
	$("tr").click(function(e){
		$("#preview").attr("src", $(this).attr("url"));
		$("#overlay").css("top", e.screenY-125);
		$("#overlay").css("left", e.screenX);
		$("#overlay").show();
		setTimeout(function(){
			$("#overlay").fadeOut("slow", function(){});
		}, 1500);
	});
}

function dateFormat(date){
	var month = parseInt(date.getMonth())+1;
	month = month < 10 ? '0'+month : month;
	return date.getDate() + "." + month + "." + date.getFullYear();
}

$(document).ready(function(){

	showFadingImage();

	$("#addProduct").click(function(){
		$("#popup").dialog({
			resizable: false,
			modal: true,
			buttons: {
				"Add Product": function(){
					if (checkInputs()){
						$.ajax({
							url: "/addProduct",
							data: $("#data").serialize(),
							type: "POST",
							success: function(response) {
								response = JSON.parse(response);
								text = "<tr url=" + response["url"] + "> " + 
									"<td>" + $("#name").val() + "</td> " +
									"<td>" + ($("#description").val() == undefined ? "None" : $("#description").val()) + "</td> " +
									"<td>" + $("input[name=optradio]:checked").val() + "</td>" +
									"<td>" + $("#price").val() + "</td>" +
									"<td>" + dateFormat(new Date()) + "</td>" +
									"<td>\
										<input type='image' name='delete' src='/static/trash.jpg' height=32px width=32px \
										value= {{row[0]}} onclick='sendDelete(this.value)'>\
									</td>" +
								 "</tr>";
								$("#table > tbody").append(text);
								showFadingImage();
			               	 	console.log(response);
			            	},
			            	error: function(error) {
			                	console.log(error);
			            	}
						});
						$(this).dialog("close");	
					}	
				}
			}
		});
		$("#popup").css("display", "block");
	});
});