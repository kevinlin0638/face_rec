# 臉部辨識的專案<br>
使用環境：python<br><br>

database裡存有50個人的照片各15張<br>
先設置兩個陣列:images,face_encodigs方便學習過程間的存取<br>

![Alt text](https://i.imgur.com/zNBc5gD.jpg)<br><br>

在prepare_data中，先利用第一個for迴圈抓取每一個人的照片<br>
再將每人的照片存取至images陣列中準備進行學習<br><br>
將要學習的照片進行特徵點分析，並加入face_encoding中<br>
然後print該編號學習完成的訊息<br>
其他狀況則視為error<br><br>
