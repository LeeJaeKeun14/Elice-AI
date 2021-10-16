var str = "abcdef";

function myUpperCase(str){
    var capitalStr = "";

    for(var i = 0; i < str.length; i++){
        var asciValue = str[i].charCodeAt();
        var asci_num = asciValue - 32;
        capitalStr += String.fromCharCode(asci_num);
    }
    return capitalStr;
}

document.getElementsByClassName

console.log(myUpperCase(str));