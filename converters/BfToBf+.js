function convert(string, list) {
    let start = 0;
    let len = string.length;
    let result = "";
    string = string.split("");
    for(let i = 0; i < len - 1; ++i) {
        if(string[i] != string[i + 1]) {
            if(i - start + 1 <= 2 || !list.includes(string[i])) {
                result += string.join("").substring(start, i + 1);
                start = i + 1;
                continue;
            }
            result += string[i];
            result += i - start + 1;
            start = i + 1;
        }
    }
    if(len - start <= 2 || !list.includes(string[len - 1])) {
        result += string.join("").substring(start, len);
        return result;
    }
    result += string[len - 1];
    result += len - start;
    return result;
}