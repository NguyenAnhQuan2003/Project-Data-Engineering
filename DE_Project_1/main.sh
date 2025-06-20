#!/bin/bash
input_file="./tmdb-movies.csv"
gsed -E ':a;s/("[^"]*),([^"]*")/\1###\2/g;ta' "$input_file" > data.csv
gsed -E ':a;s/("[^"]*)\.([^"]*")/\1###\2/g;ta' data.csv > clean.csv
echo "Câu 1 và 2 được xuất riêng ra file question 1 và 2 ạ!"
awk -F, 'NR==1 || $18 > 7.5' data.csv > ./output/question2.csv
csvsort -d ',' -c release_date -r data.csv | sed 's/\r$//' > ./output/question1.csv
echo "3. Các bộ phim có doanh thu cao nhất là:"
awk -F, 'NR>1 && $5 ~ /^[0-9]+(\.[0-9]+)?$/ {if($5>max || max=="") max=$5} END {print max}' data.csv
echo "3.1 Các bộ phim có doanh thu thấp nhất là:"
awk -F, 'NR>1 && $5 ~ /^[0-9]+(\.[0-9]+)?$/ {if($5<min || min=="") min=$5}
END {print min}' data.csv
echo "4. Tổng doanh thu tất cả các bộ phim là:"
awk -F, 'NR>1 {sum += $5} END {print sum}' data.csv
echo "5. Top 10 phim có lợi nhuận cao nhất là:"
awk -F, 'NR>1 {printf "%-40s %15s\n", $6, $5}' data.csv | sort -k5,5nr | head -n 10
echo "6. Đạo diễn có nhiều bộ phim nhất là:"
awk -F, 'NR>1 && $9 != "" {count[$9]++} END {for (d in count) print count[d], d}' data.csv | sort -nr | head -n 10
echo "6.1 Diễn viên đóng nhiều bộ phim nhất là:"
awk -F, 'NR>1 && $7 != "" {
 n = split($7,actors,"|");
 for(i=1;i<=n;i++){
	 count[actors[i]]++;
 }
}
END {
 for (actor in count){
	 print count[actor], actor
 }
}
' data.csv | sort -nr | head -n 10
echo "7. Thống kê số lượng phim theo các thể loại như:"
awk -F, 'NR > 1 && $14 != "" {
    n = split($14, genres, "|");
    for (i = 1; i <= n; i++) {
        count[genres[i]]++;
    }
}
END {
    for (g in count) printf "%-20s %d\n", g, count[g];
}' clean.csv | sort -k2 -nr | head -n 18
rm -f data.csv clean.csv

