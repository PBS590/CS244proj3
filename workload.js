
use test4
var file = cat('./output.txt');
var words = file.split('\n');
for (var i = 0; i < words.length; i++) {
    db.smallkv.findOne({"a":words[i]});
    //db.smallkv.findOne({"b":words[i]});
    //db.smallkv.findOne({"c":words[i]});
    //db.smallkv.findOne({"d":words[i]});
    //db.smallkv.findOne({"e":words[i]});
    //db.smallkv.findOne({"f":words[i]});
    //db.smallkv.findOne({"g":words[i]});
    //db.smallkv.findOne({"h":words[i]});
    //db.smallkv.findOne({"i":words[i]});
    //db.smallkv.findOne({"j":words[i]});
    //db.smallkv.findOne({"k":words[i]});
    //db.smallkv.findOne({"l":words[i]});
    //db.smallkv.findOne({"m":words[i]});
    //db.smallkv.findOne({"n":words[i]});
    //db.smallkv.findOne({"o":words[i]});
    //db.smallkv.findOne({"p":words[i]});
}
