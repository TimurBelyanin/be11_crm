//// Обрабатываем редирект после успешной аутентификации
//document.body.addEventListener('htmx:afterRequest', function(event) {
//    var response = event.detail.xhr.response;
//
//    try {
//        var jsonResponse = JSON.parse(response);
//        if (jsonResponse.redirect) {
//        console.log("Hello!");
//            // Если есть ключ redirect, делаем редирект
//            window.location.href = jsonResponse.redirect;
//        }
//    } catch (e) {
//        // Если ошибка парсинга (не JSON), продолжаем обычную работу
//    }
//});