#!/bin/bash

# Set the directory path where XML files are located
directory_path="./build/doxygen/xml"

echo "run replace_xsd_commands.sh"

# Loop through all XML files in the directory and its subdirectories
find "$directory_path" -type f -name "*.xml" | while read -r file; do
    echo "replacements in $file"
    output_file="${file%.xml}_temp.xml"
    while IFS= read -r line; do
        line="${line//<deg\/>/&#176;}"
        line="${line//<nonbreakablespace\/>/&#160;}"
        line="${line//<minus\/>/&#8722;}"
        line="${line//<ldquo\/>/&#8220;}"
        line="${line//<rdquo\/>/&#8221;}"
        line="${line//<le\/>/&#8804;}"
        line="${line//<ge\/>/&#8805;}"
        echo "$line"
    done < "$file" > "$output_file"

    # Replace the original XML file with the modified one
    mv -f "$output_file" "$file"
done
