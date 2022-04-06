var res_array = [];
var offset;

for (offset = 0; offset < 1000; offset+=100) {    
    $.ajax({
        type: "GET",
        url: "/api/v2/products",
        data: {"offset": offset, "limit":100},
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-Cafe24-Client-Id","6z3enNnBUKBeufZzZA9SYI");
            xhr.setRequestHeader("Content-Type","application/json");
        },
        success: function (res) {
            if (res.code === 200) {
                res_array.append(res.products);
            }
        },
        error: function (request, status, error) {
            console.log(request);
        }
    });    
}
console.log(res_array);