# machine_learning

##summary
Program for Chinease Restaurant Process.  


##functions

- crp(alpha, number_of_people) #出力(着席テーブルのリスト、テーブルごとの着席人数の辞書)    
- graph(table) #dictionary(key=table_number, value=number of people sit down the table)  crpの2つ目の返り値を受け取ってグラフにする。

- normal_gamma #ガウスガンマ分布に基づいたデータ点生成 PRML(2.154)式による
- gmm #複数のガウス分布からデータ点生成

##sample command
python  
import crp,graph  
(s,t) = crp.crp(3,1000)  
graph.graph(t)  

