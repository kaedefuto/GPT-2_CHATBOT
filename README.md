# GPT-2_Chatbot

## chatbot_v1

## 概要<br>
GPT-2で作成したChatbot

今後はレンタルサーバで動かす予定です

<img src="https://github.com/kaedefuto/GPT-2_Chatbot/blob/main/images/IMG_5630.jpg" alt="sample" width="40%" height="40%">

## 環境

### モデル作成環境

- 環境:Ubuntu18.04
- GPU:Quadro RTX 8000
- ドライバー:NVIDIA-SMI 460.32.03, Driver Version: 460.32.03, CUDA Version: 11.2
- pytorch環境:https://kaedefuto.github.io/kaede_blog/posts/1/conda/
- 事前学習済みモデル:https://huggingface.co/rinna
- ファインチューニング:ツイートデータ(リプライ会話データ:2021/8/1-8/3)
- モデル作成プログラム:https://github.com/kaedefuto/gpt-2/tree/main/ubuntu(chatbot)

### 実行環境

- 実行デモ環境:Ubuntu18.04 or macOS
- フロント:Line Messaging API
- バック:Django
- ツール:ngrok

```
pip install torch torchvision torchaudio
pip install transformers==4.5.0
pip install datasets==1.2.1
pip install sentencepiece==0.1.91
pip install django==3.2.5
```

## 実行

```
ngrok http 8000
python manage.py runserver
```

## 作成したモデル

https://huggingface.co/kaedefuto/chat_bot

## 参考サイト

Line Messaging API<br>
https://qiita.com/njn0te/items/d717840dc2addeae6439

GPT-2<br>
https://qiita.com/m__k/items/36875fedf8ad1842b729

