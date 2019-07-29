# NyanTimer
DIY Stackmat Timer for cubing



## 概要

このタイマーはキューバー目線をコンセプトに製作しました。そのため、普通のスタックタイマーにはない2つの大きな追加機能、インスペクションタイム計測とラップタイム計測があります。これらの機能はわたしがTwitterでキューバーの皆さんに向けて取ったアンケートの結果に基づいてつけた機能です。

最終的に販売も目指してプロジェクトを進めていますが、このGitHubには個人で同じものを製作するのに十分な情報が載っています。ぜひご活用ください。

ご質問等ございましたら、どのような形でしていただいても結構ですが、下記Twitterからの連絡が一番タイムラグが少ないと思います。

https://twitter.com/nyanyan_cube

最後に、NyanTimerの紹介動画のURLを載せておきます。

https://www.youtube.com/watch?v=Nj-br9DjQB4&t=30s

## 機能

標準のスタックタイマーの機能(信号出力を含む)

インスペクションタイム計測(秒数を知らせる機能を含む)

ラップタイム計測(99個まで計測可能)



## 使い方

### 基本的な使い方

#### 電池

左右にある写真の蓋を取って、CR2540を入れます。

<img src="https://github.com/Nyanyan/NyanTimer/blob/images/image/battery.jpeg" width="7cm">

ちょっと蓋が取りにくいです。裏側に出ているネジを押しつつ表側でネジの上を押さえると取りやすいです。

### 電源

タイマーにあるスライドスイッチで電源が入ります。これも少し扱いにくいです(ごめんなさい)

![power](https://github.com/Nyanyan/NyanTimer/blob/images/image/power.jpeg)

秋月にいい感じのスイッチが見当たらなくて…

#### ボタン

![power](https://github.com/Nyanyan/NyanTimer/blob/images/image/switch.jpeg)

* 左上: インスペクションタイム計測モード切り替え

* 左下: タイムリセット

* 右上: ラップ計測回数調整(アップ)

* 右下: ラップ計測回数調整(ダウン)

### インスペクションタイム計測

インスペクションタイム計測モード切り替えボタンを押すと、画面左上に‘I’や‘Is’が表示されたり消えたりします。これらの表示について、示す機能は以下です。

* ‘ ’: インスペクションタイムを計測しない
* ‘I’: インスペクションタイム計測(8秒、12秒のコールなし)
* ‘Is’: インスペクションタイム計測(8秒、12秒で音が鳴る)



### ラップタイム計測



## 開発環境

Visual Studio Code

Arduino IDE

Autodesk Eagle

Autodesk Fusion 360

## 解説

### ハードウェア

詳しいことはboard-vXの中のEagleのデータをご覧ください。簡単に説明すると、Arduinoから各部品に接続しているだけです。

タッチセンサについてのみ、少し細く説明をします。その後、その他の部品の概要を少し書きます。

#### タッチセンサ

スタックタイマーのタッチセンサは静電容量方式のセンサです。これについて、今回は自作しました。

![touchpad](https://github.com/Nyanyan/NyanTimer/blob/images/image/touchsensor.PNG)

少々図が汚いですが勘弁してください。

この図でP$1となっているところがタッチパッドの部分です。PADLINから5Vを定期的に入れて、PADLにかかる電圧を調べます。この時、タッチパッドに手を置いているとタッチパッドと手とがそれぞれ極板となって擬似的なコンデンサが成立し、このコンデンサを充電することになります。そのためにPADLがHIGHになるまでの時間が延び、タッチパッドに手が置かれたことを判定できます。

詳しい静電容量方式のセンサについては以下を参照してください。

https://www.fujiele.co.jp/semiconductor/ti/tecinfo/news201707210000/

http://nn-hokuson.hatenablog.com/entry/2017/03/22/200454

余談ですが、キューブの大会ではタイマーで1/1000秒まで計測可能であるにも関わらず、公式タイムには1/100秒までしか書きません。この理由を私は詳しく知りませんが、このセンサの「時間を計測することで近接を感知する」特性によるところもあるのではないかと個人的に思っています。

#### その他の入出力部品

ブザー

タクトスイッチ

液晶(16文字x2行)





### ソフトウェア

#### 全体的な処理

フローチャートをそのうち書きます。

#### 信号

信号はこちらなどを参考にしました。

https://github.com/fw42/atmel/tree/master/stackmat

かんたんに日本語で書きます。私は信号に詳しくないので、正確には上を参照してください。

* 信号はRS232
* 1200bps
* データビットは8つ
* パリティビットなし
* 終了ビットは一つ(LF)

送るデータ

* 1: ステータスのデータ('I', 'A', 'S', 'L', 'R', 'C', ' ')
* 2-6: 時刻のデータ(1:23.45なら‘12345’)
* 7: チェックサム(ASCIIコードで64+タイムの各数字の和, 上の例ならASCIIで79=O)
* 8: CR(ASCIIコード0x0D)
* 9: LF(ASCIIコード0x0A)

1番目、ステータスのデータは、

* ‘I’: タイマー初期化(リセットされた状態)
* ‘A’: タイマースタート直前(パッドを手で押さえて、話したらスタートできる状態)
* ‘ ’: 計測中
* ‘S’: タイム計測完了
* ‘L’: 左パッドが覆われている状態
* ‘R’: 右パッドが覆われている状態
* ‘C’: 両方のパッドが覆われている状態

ただし、NyanTimerでは‘L’, ‘R’, ‘C’は特に必要ないために実装していません。



## ファイル

### board-v4

旧ボード

Eagleのファイルとガーバーデータ

### board-v5

最新版(2019/07/17現在)のボード

Eagleのファイルとガーバーデータ

### board-v6

board-v5から穴の大きさなどを少し変えたボードです。2019/07/21現在製作していませんので動作保証はありません。

### body

外装

Fusion360のファイルとobjとstlファイル

### nyantimer-program

プログラム

inoファイル

### README

これ

## 参考資料

信号関係: https://github.com/fw42/atmel/tree/master/stackmat