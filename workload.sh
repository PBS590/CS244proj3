#! /bin/bash

echo "Starting";

while read key; do
    mongo benchmarks --eval "db.smallkv.findOne({"a":$key})" > /dev/null;
done < "output.txt"

echo "Done";
