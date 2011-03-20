user-revire-notifier-for-android-market
=======================================
This is a set of scripts that periodically check user reviews
on your android app in Android Market, and email you if there
is new reviews you get.

What You Need
-------------

- Unix Server
- sendmail (command)
- lxml (python)
- cron

How To Setup
------------
* 1. Replace upper-case strings in user-review-notifier.sh with your own. ::

   #!/bin/sh
   dir="PATH_TO_THIS_DIR"
   package="PACKAGE_NAME"
   mail="YOUR_ADDR@example.com"

   python ${dir}user-review-getter.py ${package} > ${dir}latest.data
   diff ${dir}latest.data ${dir}last.data > ${dir}diff.data
   mv ${dir}latest.data ${dir}last.data
   python ${dir}sendmail.py ${dir}diff.data ${mail}

Example:

   #!/bin/sh
   dir="/home/yasulab/user-review-notifier/"
   package="org.sorarier.whistle"
   mail="yasulab@gmail.com"

   python ${dir}user-review-getter.py ${package} > ${dir}latest.data
   diff ${dir}latest.data ${dir}last.data > ${dir}diff.data
   mv ${dir}latest.data ${dir}last.data
   python ${dir}sendmail.py ${dir}diff.data ${mail}

* 2. Make sure that your server can type the following commands. ::

- $ sendmail
- $ python
    >  import lxml

* 3. Check if python scripts run. ::

- $ python user-review-getter.py PACKAGE_NAME
- $ python sendmail.py FILENAME TO_ADDR

* 4. Test to run initial shell script. ::

- $ sh user-review-notifier.sh

* 5. Check your e-mail box if you got an e-mail. ::

* 6. Setup your cron to run the shell script periodically. ::

- $ sudo crontab -e

Example:
# m h  dom mon dow   command
0,10,20,30,40,50 * * * * /bin/sh /PATH_TO_DIR/user-review-notifier.sh >/dev/null 2>&1

* 7. Done! ::

   You will be able to get an e-mail if there is new reviews.


user-review-getter.py
---------------------
* Usage ::

     $ python user-review-getter.py PACKAGE_NAME

* Example ::

     $ python user-review-getter.py org.sorarier.whistle

* Result ::

非常に素晴らしいアプリだと思います。 そして迅速な改善に頭が下がります。 製作者樣、ありがとうございます。by あっきー–2011/03/19
こまめな更新に、感謝感激by Gaz–2011/03/19
音量自動最大はいいんですが、元々の音量設定に戻りません。 これだと困ります。改善おねがいします。 Xperia 2.1by 陸–2011/03/19
強制終了問題解決！対応の早さに感謝！by 環境IS04–2011/03/18
ちゃんと意見を汲み上げ判断したのち反映する誠実さと、その迅速な行動力に感服しました…。 災害時のみならず、防犯上でも役に立つ。 ...by aki–2011/03/18ちゃんと意見を汲み上げ判断したのち反映する誠実さと、その迅速な行動力に感服しました…。 災害時のみならず、防犯上でも役に立つ。 できうるなら、音声（例えば自分で録音しておいたものとか）の方がより分かりやすいのだろうが。
速やかな改良、対応に頭が下がります。by Gen–2011/03/17
使用時に端末の音量設定を最大まで上げるようには出来ないのですか？by まーさん–2011/03/16
音が小さいby 沙弥香–2011/03/15
音が小さいよねby 綾子–2011/03/15
シンプルで良いと思うけど、もっと音が大きくないと…by 五月女–2011/03/14
Works on droidx. No permissions needed.by Leonard–March 13, 2011


sendmail.py
-----------
* Usage ::

   $ python sendmail.py FILENAME TO_ADDR

* Description :: 

   The command above read a given file and
   send e-mail its content to a given mail address.


Copyright
---------

Copyright (c) 2011 Taku Fukushima. All rights reserved.

License
-------

user-review-notifier-for-android-market is `MIT Lisense <http://www.opensource.org/licenses/mit-license.php>`_

If you'd like to know more detail, check ``COPYING`` in source.
