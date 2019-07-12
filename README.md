# myapp

DjangoでHelloWorldを出力するだけのアプリケーション

herokuにアップするため、色々ファイルを追加中

* app.jsonでデプロイ時の設定
* Procfileはdynoによって実行されるコマンドを指定
* requirements.txtはルートディレクトリに設置する必要あり
* runtime.txtは実行環境を指定

heroku[router]: at=error code=H10 desc="App crashed
上記エラーが発生中

```
heroku config:set DISABLE_COLLECTSTATIC=1
```

上記コマンドでデプロイすることができた

Procfileのパスは変更必須

myapp/settings.pyのALLOWED_HOSTSを設定する必要あり

