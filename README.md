# Project-Data-Engineering
Project Unigap

Thực hiện các dự án của Unigap.

Project 1: thực hiện việc sử dụng linux để lấy dữ liệu từ server xuống và làm sạch dữ liệu sau đó là phân tích một số câu hỏi về chuyên môn như:
Dữ liệu trên đang được đặt trên Linux server, cần team Data Engineer sử dụng command line Linux hỗ trợ các tác vụ sau để có các thông tin cơ bản về dữ liệu.

1. Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới.
2. Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới.
3. Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất.
4. Tính tổng doanh thu tất cả các bộ phim.
5. Top 10 bộ phim đem về lợi nhuận cao nhất.
6. Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất.
7. Thống kê số lượng phim theo các thể loại. Ví dụ có bao nhiêu phim thuộc thể loại Action, bao nhiêu thuộc thể loại Family, ….
8. Idea của bạn để có thêm những phân tích cho dữ liệu?

Project 2: thực hiện crawling data tiki 200.000 sản phẩm, và chuẩn hóa lại data trường description về đúng định dạng text.
- sử dụng request để crawl data tiki.
- sử dụng tqdm để hiển thị tiến trình crawl.
- sử dụng pandas để đọc file_id.csv từng sản phẩm của tiki.
- sử dụng ThreadPoolExecutor để có thể thu thập dữ liệu đa luông thay vì dùng for duyệt từng data.
- viết thêm hàm chunks sử dụng package math, ceil để thực hiện chia file, hay nói cách khác là lặp vòng loop theo từng đợt.
- ghi các kết quả ra file json.
- tổng hợp file lỗi và file đúng rồi tính tổng có bao nhiêu % data đúng => có 99.4% data sạch trong project này.
