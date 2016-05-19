development environments:
ubuntu14.04:
1.ubuntu14.04 LTS 64bit.
2.sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev libgtk2.0-dev
3.install boa-constructor:
  3.1 download boa-constructor source code from http://boa-constructor.sourceforge.net, the latest version
      is boa-constructor-0.6.1.src.zip and unzip at /usr/lib/python2.7, if you want to run boa just #python Boa.py
      in this directory.

win7:
1.first you need to install python from www.python.org download latest python version,i download python-2.7.11.amd64.msi,
  after installing,you need to add python path to win7 system environment value of 'Path', after this you can type python in
  commandline to verify python is ok or not.

2.install wxpython
   i download wxpython from www.wxpython.org/download.php and because i have alreay install python2.7.11,
   so i select wxPython-win64-py27

3.install boa-constructor
   i do not download boa-constructor-0.6.1.src.zip from sourceforge,because this version is very old,has problem when running,which ask you
   'NO-3D' problem, instead i download a clone version from bitbucket.org ,it has been tested ok, the address is https://bitbucket.org/cwt/boa-constructor/downloads, and the downloaded package name is cwt-boa-constructor-fc7a7a661661.zip. after download this package you need to unzip it under c:/Python27/Lib/site-packages/  and then run Boa.py, it should be ok

4. install git for windows
    download Git-2.8.2-64-bit.exe from github and install it, it will create git bash app and git GUI app, then after install you need to use
	git bash to config, it is same with linux environment, #git config --global user.name your_name, #git config --global user.email your@email.com

5. install notepad++ edit tools