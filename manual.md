# NyanTimer
DIY Stackmat Timer for cubing

**日本語は下部にあります。**

## Abstract

This timer is made by a cuber for cubers, so it has some functions that ordinal timers don’t have: Measuring the inspection time and lap time. These functions are developped with asking cubers on Twitter.

I aim to sell this timer in the future, but on this page, there is enough information you to make one yourself.

This is an instruction manual for NyanTimer.

If you have any questions, ask me through any medium (Twitter is better).

https://twitter.com/nyanyan_cube

The movie of NyanTimer below:

https://www.youtube.com/watch?v=Nj-br9DjQB4&t=30s

## Caution

## Functions

## 概要

このタイマーはキューバー目線をコンセプトに製作したものです。そのため、普通のスタックタイマーにはない2つの大きな追加機能、インスペクションタイム計測とラップタイム計測があります。これらの機能は私がTwitterでキューバーの皆さんに向けて取ったアンケートの結果に基づいてつけた機能です。

本書は製品版NyanTimerの取扱説明書です。

もしご質問等ございましたら(可能な限り)Twitter経由でご連絡ください。

https://twitter.com/nyanyan_cube

NyanTimerの紹介動画のURLを載せておきます。

https://www.youtube.com/watch?v=Nj-br9DjQB4&t=30s

## 注意

以下の注意を疎かにした場合、重大な事故につながる虞があります。

* 

## 大きな機能

* 標準のスタックタイマーの機能(信号出力を含む)
* インスペクションタイム計測(秒数を知らせる機能を含む)
* ラップタイム計測(99個まで計測可能)

## 各部名称

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/nameJP.png" width="500">

### ボタン名称

* 左上: インスペクションタイム計測モード切り替え
* 左下: タイムリセット
* 右上: ラップ計測回数調整(アップ)
* 右下: ラップ計測回数調整(ダウン)

## 電源を入れる

### 電池

左右の電池蓋のネジを外して蓋を取って、CR2450を入れます。

### 電源

タイマーにあるスライドスイッチで電源が入ります。

## 時間を計測する

### タイマースタート・ストップ

両方のパッドを覆うと赤いLEDが点灯します。そのまま覆い続けると緑色のLEDが点き、パッドから手を話すと計測が開始します。

計測中に両方のパッドに手を置くとタイマーはストップします。

### インスペクションタイム計測

インスペクションタイム計測モード切り替えボタンを押すと、画面左上に‘I’や‘Is’が表示されたり消えたりします。これらの表示について、示す機能は以下です。

* ‘ ’: インスペクションタイムを計測しない
* ‘I’: インスペクションタイム計測(8秒、12秒のコールなし)
* ‘Is’: インスペクションタイム計測(8秒、12秒で音が鳴る)

両方のパッドを覆って1秒弱すると赤いLEDが点灯します。この状態で手を離すとインスペクションタイムの計測が開始します。‘Is’モードでは8秒と12秒で電子音が鳴ります。

### ラップタイム計測

ラップタイム計測回数調整ボタンを押して目的のラップタイムに設定してください。

このボタンは押し続けると高速で数字が変わります。

タイム計測中に両方のパッドを覆うと区間タイムが画面右下に表示されます。

タイム計測終了後にラップ計測回数調整ボタンを押すと各区間タイムが確認できます。

ラップタイムは99個まで設定可能です。

## ハック

### ハードウェアのハック

これはある程度組み込み技術に精通した人が行ってください。

NyanTimer board-v7以降のボードではNyanTimerのプログラムを簡単に変更できるようになっています。これを使ってソフトウェアアップデートを実行したり、このGitHubを見つつ自分好みにプログラムを変更できたりします。

なお、構想段階のboard-v8ではUSBシリアル変換を基板に載せることも考えているので、もっと簡単にハックできるかもしれません。

まず裏側のネジを全て取り外し、内部の基板を見ます。基板左上にUSBシリアル変換接続端子があります。

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/USB-Serial.jpeg" width="500">

1. コンデンサ取付部に0.1uFのコンデンサを取り付けます
2. ピンヘッダ取付部に6Pピンヘッダを取り付けます
3. USBシリアル変換を挿します

使うUSBシリアル変換にはこちらを推奨します(動作確認はこちらで行いました)。

https://www.switch-science.com/catalog/1032/

各ピンは上から見て左(1ピン)から、

GND-CTS-VCC-TX-RX-DTR

です。

### NyanTimerライブラリ

NyanTimerのハックにあたって必要となるであろう関数をまとめてライブラリとして提供しています。

#### 入手

このGitHub内のNyanTimer/program/library/内の“NyanTimer”がライブラリです。このままダウンロードしてご自身のライブラリフォルダに入れて使ってください。

#### 必要なライブラリ

NyanTimerには前提として必要なライブラリがあります。以下のライブラリをインストールしておいてください。最近のArduinoライブラリではメニューバーの“スケッチ->ライブラリをインクルード->ライブラリを管理“から大抵のライブラリはインストールできますが、2019/10/13現在ST7032ライブラリのみインターネットから自分で取ってくる必要があります。

* TimerOne
  https://www.arduinolibraries.info/libraries/timer-one
* MsTimer2
  https://playground.arduino.cc/Main/MsTimer2/
* Wire
  標準ライブラリです。
* ST7032
  https://ore-kb.net/archives/195

#### 関数で使用する定数と変数

関数として使っている定数と変数についての解説です。関数内でstaticになっているものは解説しません。

##### NyanTimerの各ピン

以下のものです

* **BUTTON1**
  リセットボタン
* **BUTTON2**
  インスペクションモードボタン
* **BUTTON3**
  ラップのカウントアップボタン
* **BUTTON4**
  ラップのカウントダウンボタン
* **BUZZER**
  ブザー(HIGHにするだけで勝手に鳴ります)
* **LEDR**
  赤色LED
* **LEDG**
  緑色LED
* **PAD1OUT**
  右パッドの出力ピン
* **PAD1IN**
  右パッドの入力ピン
* **PAD2OUT**
  左パッドのっ出力ピン
* **PAD2IN**
  左パッドの入力ピン

なお、PAD1OUT, PAD1IN, PAD2OUT, PAD2INについて、ユーザが直接触ることはないと思います。

##### 基礎的な変数

以下のものです。

* **int output[7]**
  シリアル出力をする際に時間情報を格納しておく配列。長さは7
* **char statout**
  シリアル出力をする際のステータス
* **char stat**
  ステータス情報。statoutと大体同じだが時々違う
* **int minute, second, msecond**
  時間。分秒ミリ秒

#### 関数の紹介

全ての関数は必ず

```Python
NyanTimer::function(argments);
```

の形で使ってください。

* **void begin()**

NyanTimerの初期処理関数です。必ずvoid setup()の中で実行してください。

* **void lightLED(int LED, bool HL)**

LEDを光らせる関数です。LEDにLEDGまたはLEDR、HLにtrue(点灯)またはfalse(消灯)を入力します。

* **void printLCD(int row, int col, String str)**

LCDになにか文字を表示する関数です。rowで表示する段(0か1)、colで表示開始列(0-15)を選択し、strを表示します。

* **void startTimer(int msec, void function())**

タイマーをスタートさせる関数です。内部はMsTimer2の関数で構成されています。

msecにインターバルをミリ秒で入力し、functionに実行する関数を入力します。この関数を実行すると即座にタイマーがスタートします。

* **void stopTimer()**

タイマーをストップします。

* **int touch(int mode)**

タッチパッドの情報を得る関数です。modeについて解説します。

**mode == 0**

返す数字が

0: どちらのパッドもタッチされていないまたはお片方のパッドがタッチされている場合

1: 両方のパッドがタッチされた場合

**mode == 1**

0: どちらのパッドもタッチされていない場合

1: 両方のパッドがタッチされている場合

2: 右パッドがタッチされている場合

3: 左パッドがタッチされている場合

* **void calcTime(int minute, int second, int msecond, int output)**

minute(分), second(秒), msecond(ミリ秒)の情報から、LCDへの出力に使いやすい時間配列を作ります。なお、output配列(長さ7)の内容を破壊的に変更します。

* **String strTime(int input[])**

input配列(長さ7)の情報から、LCDに出力する時に使うString文字列を作成します。

* **bool inputButton(int n)**

ボタンが押されればtrue、押されていなければfalseを返す関数です。

nにBUTTON1などを入力します。

* **void setLCDclear(int mode)**

LCDを消去する関数です。mode == 0で上の行、1で下の行、2ですべての行がクリアされます。