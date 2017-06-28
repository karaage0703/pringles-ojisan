# pringles-ojisan
raspberry pi assistant


# Preparation

## Hardware
- Raspberry Pi 3(Raspbian Jessie)
- Touch Sensor(Analog)
- MCP3008(SPI ADC)
- Wireless Speaker(Bluetooth)

## ADC(Analog Digital Convert)
### Install spidev(SPI Library)
Execute following commands:
```sh
$ sudo apt-get update
$ sudo apt-get install python-dev
$ cd
$ git clone https://github.com/doceme/py-spidev
$ cd py-spidev
$ sudo python setup.py install
```

　Check spidev
```sh
$ python
Python 2.7.9 (default, Sep 17 2016, 20:26:04) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import spidev
```
 Confirm, no error.

#### Run Test
 Execute following command:
```sh
$ python read_spi_adc.py
adc  :     1023 
volts:     3.30
adc  :      141 
volts:     0.45
adc  :     1023 
volts:     3.30
adc  :      121 
volts:     0.39
```

 If you touch sensor, value is changed.


### Install Julius(Voice Recognition)
Execute following commands for setup:
```sh
$ cp recog.dic ~/julius-kits/dictation-kit-v4.4/
$ cp recog.jconf ~/julius-kits/dictation-kit-v4.4/
```

　If you want to edit dictionary, edit `recog.yomi` and execute following command for convert:
```sh
$ iconv -f utf8 -t eucjp recog.yomi | yomi2voca.pl > recog.dic
```

### Install mecab for chat bot
Execute following commands:
```
$ sudo apt-get update
$ sudo apt-get install mecab
$ sudo apt-get install libmecab-dev
$ sudo apt-get install mecab-ipadic-utf8
$ sudo apt-get install python-mecab
```


# Usage
## Clone pringles-ojisan and TextGenerator
Execute following commands:
```sh
$ cd
$ git clone https://github.com/karaage0703/pringles-ojisan
$ cd pringles-ojisan
$ git clone https://github.com/karaage0703/TextGenerator.git
$ cd TextGenerator
$ python PrepareChain.py sample.txt
```

## Run program
Execute following command:
```sh
$ julius -C ~/julius-kits/dictation-kit-v4.4/recog.jconf
```

Run julius as module mode, then please run main program by executing following command.
```sh
$ python voice_recog.py
```

## Test
Please talk to pringles-ojisan.


# References
http://qiita.com/masato/items/f089a17b1c9329eb7d03
http://karaage.hatenadiary.jp/entry/2015/08/24/073000
http://karaage.hatenadiary.jp/entry/2016/01/27/073000
