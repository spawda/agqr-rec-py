# agqr-rec-py
Python及びrtmpdumpを用いて[超A&G+](https://www.agqr.jp/)の番組録画を行い、録画完了後にLINEへ通知を送ります。  
利用は私的利用の範囲でお願いします。本プログラム利用に関する一切の責任を負いかねますのでご了承ください。

## 導入方法
1. [rtmpdump](https://rtmpdump.mplayerhq.hu/)をインストールします     
windowsの場合はexeファイルを[ダウンロード](http://rtmpdump.mplayerhq.hu/download/)、mac os (Linux)の場合はhomebrew (apt-get)などを用いてインストールしてください
2. Python3系及び以下のライブラリをインストールしてください  
    - requests 2.22.0
    - schedule 0.6.0
3. 本リポジトリをcloneして、[program_info.csv](program_info.csv)を録画したい番組の情報に書き換えてください

    |  曜日  |  録画開始時間  |  番組名  |  録画時間(秒)  |
    |:------------:|:------------:|:------------:|:------------:|
    |  monday  |  20:59  |  番組名1  |  1920  |
    |  sunday  |  19:29  |  番組名2  |  1920  |
4. [line_token.txt](line_token.txt)に[LINE Notify](https://notify-bot.line.me/ja/)用のアクセストークンを保存してください
## 使い方
- リポジトリ内で以下のコマンドにより実行可能です     
`--exe_path`オプションはwindows以外のosを使用する場合には必要ありません

    - windows : `python agqr_rec.py  --root_dava_dir [保存先ディレクトリ]  --exe_path [rtmpdump.exeのpath]`
    - mac os (Linux) : `python agqr_rec.py  --root_dava_dir [保存先ディレクトリ]`
    - mac osの場合の実行例 : `python agqr_rec.py  --root_dava_dir ./agqr`
- 録画された動画ファイルは `[保存先ディレクトリ]/[番組名]/YYYYMMDD.flv` の形式で保存されます

## tips
- [program_info.csv](program_info.csv)に格納した番組名がそのままディレクトリ名になるため、特殊文字("〜"など)や空白を用いるとエラーが発生する場合があります
- 録画開始時間を番組開始時間より1分余裕を持たせると不足なく録画できます(時間があれば修正するかもしれません)
