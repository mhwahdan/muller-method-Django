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
        draw(parseFloat($('#answer_number').html()),$('#display').val())
    }).fail(function (error) {
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

function draw(axis, equation) {
            try {
                // compile the expression once
                const expr = math.compile(equation.toLowerCase());
                // evaluate the expression repeatedly for different values of x
                const xValues = math.range(axis - 50, axis + 50, 0.0001).toArray()
                const yValues = xValues.map(function (x) {
                    return expr.evaluate({x: x})
                })
                $('#plot').html('');
                // render the plot using plotly
                const trace1 = {
                    x: xValues,
                    y: yValues,
                    type: 'scatter'
                }
                const data = [trace1];
                Plotly.newPlot('plot', data, {
                    title: 'function graph',
                    font: {size: 18}
                }, {responsive: true})
            } catch (err) {
                console.error(err)
                alert(err)
            }
        }