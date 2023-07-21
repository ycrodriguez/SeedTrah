document.addEventListener("DOMContentLoaded", function (event) {
    var form = document.getElementById('form')

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        verificarInput();
    });

    function verificarInput() {
        let input_ci = document.getElementById('persona-natural-ci');
        var meses = {
            1: '31',
            2: '28',
            3: '31',
            4: '30',
            5: '31',
            6: '30',
            7: '31',
            8: '31',
            9: '30',
            10: '31',
            11: '30',
            12: '31',
        }
        if (input_ci.value.length === 11) {
            let mes = parseInt(input_ci.value.slice(2, 4));
            let dia = parseInt(input_ci.value.slice(4, 6));
            if ((mes <= 12 && mes > 0) && (dia <= meses[mes] && dia > 0)) {
                form.submit()
            } else {
                alert('Formato incorrecto del Carnet de Identidad')
            }
        } else {
            alert('El Carnet de Identidad debe tener 11 caracteres.')
        }
    }
});