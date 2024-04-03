# VTuber_Unity

## 原文章:https://github.com/kwea123/VTuber_Unity?tab=readme-ov-file  
[![teaser](images/teaser.jpg)](https://www.youtube.com/playlist?list=PLDV2CyUo4q-JFGrpG595jMdWZLwYOnu4p)

--------------------------------------------------------------------------------
# Vtuber實作
主要流程
1.偵測臉部特徵點----Python  
2.將結果傳至Unity上----C#  
3.將結果反應到人物上和UI設計      
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1712161797340.jpg)  
## 偵測臉部特徵點  
臉部特徵偵測分為三步驟  
‧找到人臉  
‧偵測特徵點  
‧偵測姿勢   
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/assets/136084973/76155992-31e9-43db-918b-d8263ef80589)  
* ‧找到人臉: https://github.com/yinguobing/head-pose-estimation  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1671594929004.jpg)     
* ‧偵測特徵點: https://github.com/1adrianb/face-alignment  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1671596722858.jpg)  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/assets/136084973/8b434b8f-7682-416b-90ed-b1db78453936)
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/image2.png)  
* ‧偵測姿勢: https://github.com/jerryhouuu/Face-Yaw-Roll-Pitch-from-Pose-Estimation-using-OpenCV  
簡單來說就是將臉部特徵偵測到的68個點，由2D座標轉3D標，得到roll、pitch、yaw三個參數  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1671596051339.jpg)  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/image001.png)
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/assets/136084973/42539163-2b91-4691-9532-42c9a0b38505)  

## 2.將結果傳至Unity上  
*  利用TCP協定  
**  Python-客服端-rpy ⮕ Unity-伺服器-port  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1671598207847.jpg)
傳送參數後Unity會執行C#程式碼，來讓我們人物的皮動起來
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1671598599282.jpg )   
## 將結果反應到人物上和UI設計  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/assets/136084973/935d8c0c-2474-4491-9d4d-c135d2af1e8b)  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1712165867651.jpg)  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/1712165882029.jpg)  
![image](https://github.com/WANG-YI-CHEN-411034018/VTuber_Unity/blob/master/images/debug_gpu_connect.gif)  
