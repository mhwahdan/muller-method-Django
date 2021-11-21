    	$("#calc").submit(function (event) {
		event.preventDefault();
        $('#calculate').html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>evaluate numerically');
		let post_url = $(this).attr("action"); //get form action url
		let request_method = $(this).attr("method"); //get form GET/POST method
		let form_data = $(this).serialize(); //Encode form elements for submission
		$.ajax({
			url: post_url,
			type: request_method,
			data: form_data
		}).done(function (response) {
            $('#Answer').html(response);
            $('#calculate').html('evaluate numerically');
		}).fail(function (error){
            $('#calculate').html('evaluate numerically');
            alert('error');
            console.log(error);
        });
	});

        /* Creating function in HTML for backspace operation */
        function backspace(calc) {
            size = calc.display.value.length;
            calc.display.value = calc.display.value.substring(0, size - 1);
        }