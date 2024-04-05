example = 1
example += 6 

function variable_1 () {
    example -= 2
}

const variable_2 = () => {
    var example = 2
}

variable_1()
variable_2()
console.log(example);


// for (var i = 0; i < 10; i ++) {
//     console.log(i)
// }


const get = () => {
    var date = new Date();
    var data = 'Ngày: ' + date.getDate() + '<br>';
    data += 'Ngày trong tuần: ' + date.getDay() + '<br>';
    data += 'Tháng: ' + String(date.getMonth() + 1) + '<br>';
    data += 'Năm đầy đủ: ' + date.getFullYear() + '<br>';
    data += 'Giờ: ' + date.getHours() + '<br>';
    data += 'Phút: ' + date.getMinutes() + '<br>';
    data += 'Giây: ' + date.getSeconds() + '<br>';
    document.write(data)
}
get()


// const num = 12;
// for(var i = 1; i <= num; i++) {
//     if (num % i == 0) {
//         console.log(i)
//     }
// }