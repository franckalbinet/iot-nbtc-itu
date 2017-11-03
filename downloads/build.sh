#/bin/bash

folder_name=iot-uaa-isoc-material

mkdir $folder_name

# Copy files
cp ../agenda.md $folder_name

# Copy folders
cp -R ../labs $folder_name
cp -R ../python-fundamentals $folder_name 
cp -R ../softs/pycom $folder_name
echo "Files copied successfully!"

# Create archive
now=`date +"%Y%m%d"`
zip -r $folder_name-$now.zip $folder_name
echo "Material zipped successfully!"

rm -r $folder_name
