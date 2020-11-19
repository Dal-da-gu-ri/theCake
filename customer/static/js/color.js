//보색 - 1
function complementaryColor1(r1, g1, b1) {
    var temp1 = Math.max(r1, g1, b1);
    var temp2 = Math.min(r1, g1, b1);
    if (temp1 == r1) {
        if (temp2 == g1)
            return [g1, r1, r1+g1-b1];
        else if (temp2 == b1)
            return [b1, r1+b1-g1, r1];
    }
    else if (temp1 == g1) {
        if (temp2 == r1)
            return [g1, r1, r1+g1-b1];
        else if (temp2 == b1)
            return [g1+b1-r1, b1, g1];
    }
    else if (temp1 == b1) {
        if (temp2 == r1)
            return [b1, r1+b1-g1, r1];
        else if (temp2 == g1)
            return [b1+g1-r1, b1, g1];
    }
}
//모노톤 - 2
function monoColor1(r1,g1,b1) {
    if (r1 > 220 && g1 > 220 && b1 > 220)
        return [(r1+250)/3, (g1+250)/3, (b1+250)/3, (r1+250)/4, (g1+250)/4, (b1+250)/4];
    else
        return [(r1+250)/2, (g1+250)/2, (b1+250)/2, (r1+500)/3, (g1+500)/3, (b1+500)/3];
}
//트리컬러 - 2
function triColor1(r1,g1,b1) {
    return [b1, r1, g1, g1, b1, r1];
}