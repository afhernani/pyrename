#!/bin/bash
shopt -s nullglob #ignora las coincidencias fallidas.
echo "{ Archivos: ["
for file in *.* #`ls` #old_names/*
do
  if [ -f "$file" ];then
    str="exe sh dll cmd txt json"
    echo "{"
    echo "    Archivo: '$file'"
    name=${file%.*}
    echo "    Name: '$name'"
    ext=${file##*.}
    echo "    Extension: '$ext'"
    if [[ "$str" == *"$ext"* ]]; then
      echo "    New_name: 'Not remane file type .$ext'"
      echo "},"
      continue
    else
      newfile=$(openssl md5 "$file" | awk '{print $NF}')
      echo "    New_name: '$newfile.$ext'"
      echo "},"
      mv "$file" "$newfile.$ext"
    fi
  fi
done
echo "] }"

