# Chat-GPT
Ai-Chat

Update the key on line 54 of the index.html file

eg:

<img width="2297" alt="image" src="https://user-images.githubusercontent.com/54488712/222626605-614a5de6-16c6-44b3-ab78-7eb5a7282edb.png">

api直连，目前国内给API墙了，我写了一个python脚本，callGPT.py
```shell
pip install flask
pip install requests
```

把key放入，使用post请求
http://localhost:8080/chatgpt
{
    "message": "要发送的消息"
}
。
