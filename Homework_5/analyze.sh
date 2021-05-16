#!/usr/bin/env bash

outfile=analyzed

help(){
    cat <<EOF
usage: analyze.sh  a | t | f | c | s   <FILE>

  a     общее кол-во запросов (all)
  t     общее кол-во запросов по типу (type)
  f     топ 10 самых частых запросов (frequent)
  с     топ 5 самых больших запросов с кодом 4ХХ (client)
  s     топ 5 самыхбольших запросов с кодом 5ХХ (server)

  FILE  входной файл

  Имя выходного файла - $outfile.
EOF
}

err(){
    if [ $# -ne 0 ]; then exit "$1"; fi
    exit 1
}


if [ ! $# -eq 2 ]; then
    help
    err
fi

for last_arg in "$@"; do :; done
if [ -f "$last_arg" ]; then
    file="$last_arg"
else
    echo 'No such file or directory' >&2
    err 2
fi

if [ -f analyzed ]; then
    echo "File '$outfile' exists, overwrite? (yes/no): " >&2
    read answer
    if [ ! "$answer" = "y" ] && [ ! "$answer" = "yes" ]; then
        err 17
    fi
fi

exec 1>$outfile

case "$1" in
    a)
      wc -l "$file" | awk '{print $1}'
      ;;
    t)
      awk -F '[ "]' '{print $7}' "$file" | sort | uniq -c | sort -rg | awk '{print $2,$1}'
      ;;
    f)
      awk -F '[ "]' '{print $8}' "$file" | sort | uniq -c | sort -k 1,1rn | head -10 | awk '{print $2,$1}'
      ;;
    c)
      awk -F '[ "]' '$11>=400 && $11<500 {print $1,$11,$12,$8}' "$file" | sort -k 3,3rn | head -5 | awk '{print $4,$2,$3, $1}'
      ;;
    s)
      awk -F '[ "]' '$11>=500 && $11<600 {print $1}' "$file" | sort -rn | uniq -c | sort -rnk 1,1 | head -5 | awk '{print $2, $1}'
      ;;
    *)
      rm $outfile
        print_help >&2
        err
        ;;
esac