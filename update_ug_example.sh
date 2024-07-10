#!/bin/bash

url_base="https://raw.githubusercontent.com/cronologic-de/ndigo6g_babel/main/ug_example/src"
target_dir="./source/_ug_example"
file_names=(
    "delay.h"
    "ndigo6g12_adc_averager.cpp"
    "ndigo6g12_adc_dual.cpp"
    "ndigo6g12_adc_quad.cpp"
    "ndigo6g12_adc_single.cpp"
    "ndigo6g12_app.h"
    "ndigo6g12_example.cpp"
    "ndigo6g12_tdc.cpp"
)

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