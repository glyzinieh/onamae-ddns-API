# これなに？

お名前.com ダイナミックDNSクライアント API(非公式)です。

## 実行環境

- Python 3.10.2

## 使い方

```console
pip install -r requirements.txt
uvicorn api:app
```

表示されたURLにアクセスしてください。

## 謝辞

内部処理に[Tomoya Tanjo](https://github.com/tom-tan)さんの[onamae-ddns-client](https://github.com/tom-tan/onamae-ddns-client)を利用しています。
ありがとうございます。

## 参考

- [LinuxやMacで お名前.com ダイナミックDNS の IPアドレスを更新する](https://qiita.com/ats124/items/59ec0f444d00bbcea27d)
