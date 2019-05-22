#!/usr/bin/env bash


for shard_size in "2.5GB" "5GB" "6.25GB" "7.5GB" "10GB" "12.5GB"; do
  # echo item: $shard_size
  out_dir="smallkv/$shard_size"
  mkdir -p ${out_dir}
  echo "Downloading smallkv $shard_size x 8 shards to $out_dir ..."
  for part in 0 1 2 3 4 5 6 7; do
    url="https://s3.amazonaws.com/succinct-datasets/smallkv/${shard_size}/data_${part}"
    wget --quiet $url -O ${out_dir}/data_${part}&
  done
  wait
  echo "Finished downloading smallkv $shard_size x 8 shards"
done
