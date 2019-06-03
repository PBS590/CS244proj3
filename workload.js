
use test4
var file = cat('./output.txt');
var words = file.split('\n');
for (var i = 0; i < words.length; i++) {
    db.smallkv.findOne({"a":words[i]});
}
