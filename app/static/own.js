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


$(document).ready(function(){
	$("#addProduct").click(function(){
		$("#popup").dialog({
			resizable: false,
			modal: true,
			buttons: {
				"Add Product": function(){
					if (checkInputs()){

					// var data = { "data": {
					// 		"name":  $("#name").val(),
					// 		"descripton": $("#descripton").val(),
					// 		"ratíng": $('input[name="optradio"]:checked').val(),
					// 		"price": $("#price").val()
					// 	}
					// };
					$.ajax({
						url: "/addProduct",
						data: $("#data").serialize(),
						type: "POST",
						success: function(response) {
							location.reload();
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