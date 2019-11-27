# NyanTimer
DIY Stackmat Timer for cubing

**日本語は下部にあります。**

![GitHub language count](https://img.shields.io/github/languages/count/Nyanyan/NyanTimer)![GitHub repo size](https://img.shields.io/github/repo-size/Nyanyan/NyanTimer)![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Nyanyan/NyanTimer)![GitHub last commit](https://img.shields.io/github/last-commit/Nyanyan/NyanTimer)![GitHub followers](https://img.shields.io/github/followers/Nyanyan?style=social)![Twitter Follow](https://img.shields.io/twitter/follow/Nyanyan_Cube?style=social)





<!-- TOC -->

- [NyanTimer](#nyantimer)
    - [Abstract](#abstract)
    - [Functions](#functions)
    - [概要](#概要)
    - [機能](#機能)
    - [使い方](#使い方)
        - [電池](#電池)
        - [電源](#電源)
        - [ボタン](#ボタン)
        - [タイマースタート・ストップ](#タイマースタート・ストップ)
        - [インスペクションタイム計測](#インスペクションタイム計測)
        - [ラップタイム計測](#ラップタイム計測)
        - [ハック](#ハック)
            - [board-v7でのハック](#board-v7でのハック)
        - [NyanTimerライブラリ](#nyantimerライブラリ)
            - [入手](#入手)
            - [必要なライブラリ](#必要なライブラリ)
            - [関数で使用する定数と変数](#関数で使用する定数と変数)
                - [NyanTimerの各ピン](#nyantimerの各ピン)
                - [基礎的な変数](#基礎的な変数)
            - [関数の紹介](#関数の紹介)
    - [開発環境](#開発環境)
    - [技術的な解説](#技術的な解説)
        - [ハードウェア](#ハードウェア)
            - [ボディ](#ボディ)
            - [タッチセンサ](#タッチセンサ)
            - [その他の入出力部品](#その他の入出力部品)
        - [ソフトウェア](#ソフトウェア)
            - [全体的な処理](#全体的な処理)
            - [信号](#信号)
    - [ファイル](#ファイル)
        - [board](#board)
        - [body](#body)
        - [program](#program)
        - [README](#readme)
    - [参考資料](#参考資料)

<!-- /TOC -->

## Abstract

This timer is made by a cuber for cubers, so it has some functions that ordinal timers don’t have: Measuring the inspection time and lap time. These functions are developped with asking cubers on Twitter.

I aim to sell this timer in the future, but on this page, there is enough information you to make one yourself.

This is an instruction manual for NyanTimer.

If you have any questions, ask me through any medium (Twitter is better).

https://twitter.com/nyanyan_cube

The movie of NyanTimer below:

https://youtu.be/ierR8ZPBncU

## Caution

If you break these promises, you might be in an accident.

* Use the timer after reading this manual.
* Do not shock the timer.

If you disassemble or hack the timer, we won’t take the responsibility.

## Functions

*  Functions of ordinal stack mat timers (including signal out)
* Inspection time measurement (including 8, 12, 15, and 17s call)
* Lap time measurement (Max 99 laps)

## Name of each part

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/nameEN.png" width="500">

### Name of each button

* Upper left: Mode button
* Bottom left: Reset button
* Upper right: Lap time button (up)
* Bottom right: Lap time button (down)

## Powering the timer

### Batteries

Remove the battery covers, then put two CR2450s.

### Powering

Slide the power switch.

## Measure the time

### Start & Stop the timer

Covering both pads, and the red LED lights. Then wait, and both red and green LEDs lights. If you release your hand, then timer starts.

When you cover the both pads during timing, the timer stops.

If you measure the lap times (when the LCD shows a number of lap except ‘1’), We strongly recommend not to cover one pad when timing.

### Sounding when timer stops

If you want the timer to sound when you stop the timer, press mode button a second. Then the LCD shows ‘S’ or nothing on the upper left.

* ‘ ’: No sound when timer stops
* ‘S’: Sounds when timer stops

### Measuring the inspection time

If you press mode button, the LCD shows ‘i’, ‘I’, or nothing on the upper left. These messages tells you:

* ‘ ’: Not measure the inspection time
* ‘i’: Measure the inspection time (no 8s, 12s, +2, DNF calls)
* ‘I’: Measure the inspection time (with 8s, 12s, +2, DNF calls)

On ‘i’ or ‘I’ mode, when you cover the both pads and wait about 1 second, the red LED lights. Then when you release, the inspection time starts.

### Measuring lap times

Press lap time button (up and down) and adjust the count of lap. If you press this button for long, the number will change quickly.

If you cover one or two pad during timing, lap time will be shown on the bottom right of the LCD.

After finishing timing, you can check each lap time with lap time buttons.

Max lap is 99.

### Auto power saving mode

If you leave this timer for about 5 minutes, it will be in power saving mode. To cancel this, slide the power switch and repower it.

## Hack

In this timer, ATMEGA328P (Arduino Uno) is used. So you can easily hack it.

### How to hack

Only people who are familiar to embedded technology should do this. And we will have no responsibility to this.

NyanTimer’s program is easy to edit, because of the hardware. You can update the firmware and edit the program with this repository.

First, take all the screws and see the board. On the upper left of the board, there is pins of USB-Serial conversion.

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/USB-Serial.jpeg" width="500">

1. Put 0.1uF condenser
2. Put a 6P pin header
3. Connect your USB-Serial conversion

We recommend you to use this one:

https://www.switch-science.com/catalog/1032/

pins are: from pin 1 (left), 

GND-CTS-VCC-TX-RX-DTR

### NyanTimer library

We published a library in order you to hack it.

#### How to get

program/libraries/NyanTimer on this GitHub is it. Download this and unzip it on your libraries folder.

#### Libraries used in NyanTimer library

NyanTimer uses some other libraries. Before hacking it, you must install these libraries below: 

* TimerOne
  https://www.arduinolibraries.info/libraries/timer-one
* MsTimer2
  https://playground.arduino.cc/Main/MsTimer2/
* SoftI2CMaster
  https://github.com/felias-fogg/SoftI2CMaster
* ST7032_SoftI2CMaster
  I modified this(https://ore-kb.net/archives/195). program/libraries/ST7032_SoftI2CMaster on this GitHub is it.

#### Constants and variables

All constants and variables must be used like this:

```c++
NyanTimer::constantsOrVariables
```

Constants and variables used in this library are below:

##### Constants (Pins of NyanTimer)

* **BUTTON1**
  Reset button
* **BUTTON2**
  Mode button
* **BUTTON3**
  Lap time button (up)
* **BUTTON4**
  Lap time button (down)
* **BUZZER**
  Buzzer (Sound when the pin is HIGH)
* **LEDR**
  Red LED
* **LEDG**
  Green LED
* **PAD1OUT**
  Output pin of right pad
* **PAD1IN**
  Input pin of right pad
* **PAD2OUT**
  Output pin of left pad
* **PAD2IN**
  Input pin of left pad

Users might not use PAD1OUT, PAD1IN, PAD2OUT, PAD2IN

##### Variables

* **int output[7]**
  An array, the information of time will be in it to output the signal and output on the LCD.
* **char stat**
  Status
* **int minute, second, msecond**
  Time, minute, second, milli second

#### Functions

All functions must be used like this:

```c++
NyanTimer::function(argments);
```

* **void begin(bool signal)**

Setting of NyanTimer. Must be done in void setup(). Argment is about signal output; true: output, false: no signal output.

**void timing()**

This function do timing. Must be done in void loop or something else.

* **void lightLED(int LED, bool HL)**

A function to light a LED. In ‘LED’, there will be LEDG or LEDR, in ‘HL’, true (on) or false (off).

* **void printLCD(int row, int col, String / char str)**

A function to show something on the LCD. In ‘row’, select the row (0 or 1), in ‘col’, select the column(0-15). On the LCD, ‘str’ will be written. ‘str’ must be char or String.

* **void startTimer(int msec, void function())**

Start the timer. This function is made of MsTimer2.

Input interval (milli second) on ‘msec’, and put the function to execute on ‘function’.

* **void stopTimer()**

Stop the timer.

* **int touch()**

Returns the status of touchpad. Returning number means:

0: Neither pad is covered

1: Both pads are covered

2: Only right pad is covered

3: Only left pad is covered

* **void calcTime(int minute, int second, int msecond, int output)**

From minute, second, msecond, make an array that enable you to output the signal or output on the LCD. This function changes ‘output’ aarray.

* **String strTime(int input[])**

From ‘input’ array, make a string. this string will be used to output on the LCD.

* **bool inputButton(int button)**

If ‘button’ is pressed, returns true. 

* **void setLCDclear(int mode)**

Clear the LCD. mode == 0: upper row, mode == 1: lower row, mode ==  2: both row, are cleared.

* **void powersave()**

Power saving function.

---

---



## 概要

このタイマーはキューバー目線をコンセプトに製作したものです。そのため、普通のスタックタイマーにはない2つの大きな追加機能、インスペクションタイム計測とラップタイム計測があります。これらの機能は私がTwitterでキューバーの皆さんに向けて取ったアンケートの結果に基づいてつけた機能です。

本書は製品版NyanTimerの取扱説明書です。

もしご質問等ございましたら(可能な限り)Twitter経由でご連絡ください。

https://twitter.com/nyanyan_cube

NyanTimerのPVのURLを載せておきます。

https://youtu.be/ierR8ZPBncU

## 注意

以下の注意を疎かにした場合、重大な事故につながる虞があります。

* 必ず本取扱説明書を読んでから使用すること。
* 製品に衝撃を与えないこと

製品の分解・改造について製造者は責任を負いません。

## 大きな機能

* 標準のスタックタイマーの機能(信号出力を含む)
* インスペクションタイム計測(秒数を知らせる機能を含む)
* ラップタイム計測(99個まで計測可能)

## 各部名称

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/nameJP.png" width="500">

### ボタン名称

* 左上: モード切り替えボタン
* 左下: タイムリセットボタン
* 右上: ラップ計測回数調整(アップ)ボタン
* 右下: ラップ計測回数調整(ダウン)ボタン

## 電源を入れる

### 電池

左右の電池蓋のネジを外して蓋を取って、CR2450を入れます。

### 電源

タイマーにあるスライドスイッチで電源が入ります。

## 時間を計測する

### タイマースタート・ストップ

両方のパッドを覆うと赤いLEDが点灯します。そのまま覆い続けると緑色のLEDが点き、パッドから手を話すと計測が開始します。

計測中に両方のパッドに手を置くとタイマーはストップします。

ラップタイム計測をする場合(ラップタイム表示が1以外の場合)はタイマーから両手を離すことを強く勧めます。

### 計測終了時の音声出力

モード切替ボタンを長押しすると画面に‘S’の文字が出現したり消えたりします。これらの表示について、示す機能は以下です。

* ‘ ‘:計測終了時に音が鳴らない
* ’S’: 計測終了時に音が鳴る

### インスペクションタイム計測

モード切り替えボタンを押すと、画面左上に‘i’や‘I’が表示されたり消えたりします。これらの表示について、示す機能は以下です。

* ‘ ’: インスペクションタイムを計測しない
* ‘i’: インスペクションタイム計測(8秒、12秒、+2、DNFのコールなし)
* ‘I’: インスペクションタイム計測(8秒、12秒、+2、DNFで音が鳴る)

両方のパッドを覆って1秒弱すると赤いLEDが点灯します。この状態で手を離すとインスペクションタイムの計測が開始します。

### ラップタイム計測

ラップタイム計測回数調整ボタンを押して目的のラップタイムに設定してください。

このボタンは押し続けると高速で数字が変わります。

タイム計測中に片方または両方のパッドを覆うと区間タイムが画面右下に表示されます。

タイム計測終了後にラップ計測回数調整ボタンを押すと各区間タイムが確認できます。

ラップタイムは99個まで設定可能です。

### オートパワーセーブ

計測をしていない状態で5分程度放置すると自動的に画面が消え、パワーセーブモードに入ります。解除するには電源を入れ直します。

## ハック

このタイマーはCPUにATMEGA328P(Arduino Uno)を使用しています。そのため、簡単にハックすることができます。

### やり方

これはある程度組み込み技術に精通した人が行ってください。なお、ハックによる不具合について製造元は保証しません。

NyanTimerはプログラムを簡単に変更できるようになっています。これを使ってソフトウェアアップデートを実行したり、このGitHubを見つつ自分好みにプログラムを変更できたりします。

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

このGitHub内のNyanTimer/program/libraries/内の“NyanTimer”がライブラリです。このままダウンロードしてご自身のライブラリフォルダに入れて使ってください。

#### 必要なライブラリ

NyanTimerには前提として必要なライブラリがあります。以下のライブラリをインストールしておいてください。最近のArduinoライブラリではメニューバーの“スケッチ->ライブラリをインクルード->ライブラリを管理“から大抵のライブラリはインストールできますが、ST7032_SoftI2CMasterのみ私が改変したライブラリのため、NyanTimerライブラリと同じフォルダにあるライブラリをインストールしてください。

* TimerOne
  https://www.arduinolibraries.info/libraries/timer-one
* MsTimer2
  https://playground.arduino.cc/Main/MsTimer2/
* SoftI2CMaster
  https://github.com/felias-fogg/SoftI2CMaster
* ST7032_SoftI2CMaster
  https://ore-kb.net/archives/195 のものを私が改変しました。本GitHub内のprogram/librariesフォルダにあります。

#### 関数で使用する定数と変数

全ての定数と変数は以下のように使ってください。

```c++
NyanTimer::constantsOrVariables
```

関数として使っている定数と変数についての解説です。関数内でstaticになっているものは解説しません。

##### NyanTimerの各ピン

以下のものです

* **BUTTON1**
  リセットボタン
* **BUTTON2**
  モード切替ボタン
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
  左パッドの出力ピン
* **PAD2IN**
  左パッドの入力ピン

なお、PAD1OUT, PAD1IN, PAD2OUT, PAD2INについて、ユーザが直接触ることはないと思います。

##### 基礎的な変数

以下のものです。

* **int output[7]**
  シリアル出力やLCD出力をする際に時間情報を格納しておく配列。長さは7
* **char stat**
  ステータス情報。
* **int minute, second, msecond**
  時間。分秒ミリ秒

#### 関数の紹介

全ての関数は必ず

```c++
NyanTimer::function(argments);
```

の形で使ってください。

* **void begin(bool signal)**

NyanTimerの初期処理関数です。必ずvoid setup()の中で実行してください。引数は信号出力の有無(true: あり false: なし)

* **void timing()**

NyanTimerのタイマー処理の中枢です。必ずvoid loop等の定期的なループ内で実行してください。

* **void lightLED(int LED, bool HL)**

LEDを光らせる関数です。LEDにLEDGまたはLEDR、HLにtrue(点灯)またはfalse(消灯)を入力します。

* **void printLCD(int row, int col, String / char str)**

LCDになにか文字を表示する関数です。rowで表示する段(0か1)、colで表示開始列(0-15)を選択し、strを表示します。strはchar型でもString型でも動きます。

* **void startTimer(int msec, void function())**

タイマーをスタートさせる関数です。内部はMsTimer2の関数で構成されています。

msecにインターバルをミリ秒で入力し、functionに実行する関数を入力します。この関数を実行すると即座にタイマーがスタートします。

* **void stopTimer()**

タイマーをストップします。

* **int touch()**

タッチパッドの情報を得る関数です。

0: どちらのパッドもタッチされていない場合

1: 両方のパッドがタッチされている場合

2: 右パッドがタッチされている場合

3: 左パッドがタッチされている場合

* **void calcTime(int minute, int second, int msecond, int output)**

minute(分), second(秒), msecond(ミリ秒)の情報から、LCDへの出力に使いやすい時間配列を作ります。なお、output配列(長さ7)の内容を破壊的に変更します。

* **String strTime(int input[])**

input配列(長さ7)の情報から、LCDに出力する時に使うString文字列を作成します。

* **bool inputButton(int button)**

ボタンが押されればtrue、押されていなければfalseを返す関数です。

‘button’にBUTTON1などを入力します。

* **void setLCDclear(int mode)**

LCDを消去する関数です。mode == 0で上の行、1で下の行、2ですべての行がクリアされます。

* **void powersave()**

主電源を入れたままでパワーセーブモードに入る関数です。



---

---



## オープンソースバージョンの使い方

### 電池

左右にある写真の蓋を取って、CR2450を入れます。

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/battery.jpeg" width="500">

ちょっと蓋が取りにくいです。裏側に出ているネジを押しつつ表側でネジの上を押さえると取りやすいです。

### 電源

タイマーにあるスライドスイッチで電源が入ります。これも少し扱いにくいです(ごめんなさい)

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/power.jpeg" width="500">

秋月にいい感じのスイッチが見当たらなくて…

### ボタン

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/switch.jpeg" width="500">

* 左上: インスペクションタイム計測モード切り替え

* 左下: タイムリセット

* 右上: ラップ計測回数調整(アップ)

* 右下: ラップ計測回数調整(ダウン)

### タイマースタート・ストップ

販売版をご覧ください。

### インスペクションタイム計測

販売版をご覧ください。

### ラップタイム計測

販売版をご覧ください。

### ハック

販売版をご覧ください。

### NyanTimerライブラリ

販売版をご覧ください。

## 開発環境

Visual Studio Code

Arduino IDE

Autodesk Eagle

Autodesk Fusion 360

## 技術的な解説

### ハードウェア

基板について詳しいことはboard-vXの中のEagleのデータをご覧ください(回路図描くのが下手でごめんなさい)。簡単に説明すると、Arduinoから各部品に接続しているだけです。

ボディとタッチセンサについてのみ、少し細かく説明をします。その後、その他の部品の概要を少し書きます。

####  ボディ

ボディはAutodesk Fusion 360で設計し、CNCフライス盤で切り出しました ~~(今後レーザーカッターでの出力に方針転換する予定)~~  今後は3Dプリンタで試作した後、金型作って大量生産する予定です。

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/nyantimer-fusion.PNG" width="500">

#### タッチセンサ

スタックタイマーのタッチセンサは静電容量方式のセンサです。これについて、今回は自作しました。

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/touchsensor.PNG" width="500">

少々図が汚いですが勘弁してください。

この図でP$1となっているところがタッチパッドの部分です。PADLINから5Vを定期的に入れて、PADLにかかる電圧を調べます。この時、タッチパッドに手を置いているとタッチパッドと手とがそれぞれ極板となって擬似的なコンデンサが成立し、このコンデンサを充電することになります。そのためにPADLがHIGHになるまでの時間が延び、タッチパッドに手が置かれたことを判定できます。

詳しい静電容量方式のセンサについては以下を参照してください。

https://www.fujiele.co.jp/semiconductor/ti/tecinfo/news201707210000/

http://nn-hokuson.hatenablog.com/entry/2017/03/22/200454

なお、電池が多少減ってきても正確にタッチセンサが動くよう、電源投入時にPADLにかかる電圧を測定し、それに1未満の係数を掛けた値をPADLがHIGHであると判定する閾値にしました。

余談ですが、キューブの大会ではタイマーで1/1000秒まで計測可能であるにも関わらず、公式タイムには1/100秒までしか書きません。この理由を私は詳しく知りませんが、このセンサの「時間を計測することで近接を感知する」特性によるところもあるのではないかと個人的に思っています。

#### その他の入出力部品

ブザー

タクトスイッチ

液晶(16文字x2行)

### ソフトウェア

#### 全体的な処理

<img src="https://github.com/Nyanyan/NyanTimer/blob/master/images/flow.png" width="1000">

なぜか繰り返し記号が使えなかったので適当に六角形で代用です。

プログラム中では左側がbutton()で、右側がtimer()です。

これ以外にも色々複雑に処理はしていますが、まあ大体はこんな感じです。

マイコンは要するにArduinoなので、使えるタイマーはTimer1とTimer2の２つのみです。そのため、Timer2は信号の割り込み処理にずっと使うとして、時間計測とインスペクションタイム計測をTimer1でやっています。

#### 信号

信号はこちらなどを参考にしました。

https://github.com/fw42/atmel/tree/master/stackmat

簡単に日本語で書きます。私は通信には詳しくないので、正確には上を参照してください。

* 信号はRS232
* 1200bps
* データビットは8つ(ステータス、時刻、チェックサム)
* パリティビットなし
* 終了ビットは一つ(LF)

送るデータ

* 1: ステータスのデータ('I', 'A', 'S', 'L', 'R', 'C', ' ')
* 2-7: 時刻のデータ(1:23.45なら‘12345’)
* 8: チェックサム(ASCIIコードで64+タイムの各数字の和, 上の例ならASCIIで79=O)
* 9: CR(ASCIIコード0x0D)
* 10: LF(ASCIIコード0x0A)

1番目、ステータスのデータは、

* ‘I’: タイマー初期化(リセットされた状態)
* ‘A’: タイマースタート直前(パッドを手で押さえて、話したらスタートできる状態)
* ‘ ’: 計測中
* ‘S’: タイム計測完了
* ‘L’: 左パッドが覆われている状態
* ‘R’: 右パッドが覆われている状態
* ‘C’: 両方のパッドが覆われている状態

ただし、NyanTimerでは‘C’は特に必要ないために実装していません(以前は‘R’,‘L’も実装していませんでしたが、CS Timerのインスペクションタイム計測機能であると便利とわかり実装しました)。

## ファイル

### board

基板です。2019/09/05現在、v4-v7までのボードの動作確認がとれています。

### body

外装

Fusion360のファイルとobjとstlファイル

body-v2内のncファイルはPartsTogether内のが最新版です

### program

プログラムとライブラリ

~~中に“calibration”とついたものがありますが、これはタッチセンサで電源投入時に自動でキャリブレーションを行うプログラムです。2019/09/24現在キャリブレーションは試用の機能なので分けて開発しています(Gitを使いこなせていない)~~

2019/10/11追記: キャリブレーション機能はデフォルトの機能になりました。古いプログラムは“archive”内に移動しました。

~~“withfunc”のついたプログラムは、NyanTimer専用関数郡を別に書いたもので、2019/10/11現在試用のプログラムです。~~ 2019/10/14現在、デフォルトのプログラムになりました。

### README

これ

## 参考資料

信号関係(私がまとめた日本語記事): https://qiita.com/Nyanyan_Cube/items/e517e71cf5c4e2aaf1e5

信号関係(英語記事): https://github.com/fw42/atmel/tree/master/stackmat