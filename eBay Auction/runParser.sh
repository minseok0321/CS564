python3 ebay_parser.py ebay_data/*.json

sort category_tmp.dat > category_sort.dat
uniq category_sort.dat > category.dat
rm category_tmp.dat category_sort.dat