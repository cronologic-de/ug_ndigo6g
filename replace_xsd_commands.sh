#!/bin/bash

# Set the directory path where XML files are located
directory_path="./build/doxygen/xml"

echo "Running replace_xsd_commands.sh"

# Loop through all XML files in the directory and its subdirectories
find "$directory_path" -type f -name "*.xml" | while read -r file; do
    echo "Processing $file"
    output_file="${file%.xml}_temp.xml"
    # Use sed to handle the replacements, escaping the & character properly
    sed -e 's|<deg/>|\&#176;|g' \
        -e 's|<nonbreakablespace/>|\&#160;|g' \
        -e 's|<minus/>|\&#8722;|g' \
        -e 's|<ldquo/>|\&#8220;|g' \
        -e 's|<rdquo/>|\&#8221;|g' \
        -e 's|<le/>|\&#8804;|g' \
        -e 's|<ge/>|\&#8805;|g' \
        "$file" > "$output_file"

    # Replace the original XML file with the modified one
    mv -f "$output_file" "$file"
done