function convert(string) {
    string = string.split('');
    const len = string.length;
    for(let i = 0; i < len; ++i) {
        string[i] = string[i].charCodeAt();
        if(string[i] > 127)
            string[i] -= 256;
    }
    let res = (string[0] > 0 ? '+' : '') + (string[0] ? string[0] : '') + '.';
    for(let i = 1; i < len; ++i) {
        const diff = (string[i] + (string[i] < 0) * 256) - (string[i - 1] + (string[i - 1] < 0) * 256);
        res += (diff > 0 ? '+' : '') + (diff ? diff : '') + '.';
    }
    return res;
}
