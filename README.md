# 臉部辨識的專案<br>
使用環境：python<br><br>

database裡存有50個人的照片各15張<br>
先設置兩個陣列:images,face_encodigs方便學習過程間的存取<br>

![Alt text](https://i.imgur.com/zNBc5gD.jpg)<br><br>

在prepare_data中，先利用第一個for迴圈抓取每一個人的照片<br>
再將每人的照片存取至images陣列中準備進行學習<br><br>
將要學習的照片進行特徵點分析，並加入face_encoding中<br>
然後print該編號學習完成的訊息<br>
其他狀況則視為error<br><br><br>
在recognize的函式中<br>
將欲辨識的照片存入unknow_person的陣列中<br>
透過face_recognition將照片進行處理存進unknown_person_encoding<br>
![Alt text](https://i.imgur.com/oEKe33I.jpg)<br><br>
將過的照片和要辨識的照片進行比對<br>
把比較的特徵點存進result裡<br>
在這裡設置一個計數器count以便之後計算辨識率<br>
若result裡的比較結果正確<br>
則將count加上一<br>
最後將比較完後的count結果除上result的長度存入sucess_rate中<br>
即為辨識率<br>
![Alt text](https://i.imgur.com/XHNwDNT.jpg)<br><br>
若sucess_rate與以學習過的照片i中有超過五成以上的辨識率<br>
則將此欲辨識的照片判定為和照片i為同一個人<br>
並print出準確度<br>
若沒有則print出沒有學習過的提示訊息<br>
[Alt text](https://i.imgur.com/CbynqIn.jpg)<br><br>