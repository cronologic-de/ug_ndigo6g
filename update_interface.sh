#!/bin/bash

url_base="https://raw.githubusercontent.com/cronologic-de/ndigo6g_babel/main/include"
target_dir="./source"
file_names=("ndigo6g12_interface.h" "crono_interface.h")

for file_name in "${file_names[@]}"; do
    url="$url_base/$file_name"
    local_file="$target_dir/$file_name"

    curl -o "$local_file" "$url"

    if [ $? -eq 0 ]; then
        echo "Updated $file_name"
    else
        echo "Failed to download $file_name"
    fi
done