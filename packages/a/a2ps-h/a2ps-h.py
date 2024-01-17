#! /usr/bin/env python

#
# (C) Mizi Research
# distributed under GPL
#
# Author: Hwang, ChiDeok (hwang@mizi.co.kr)
# 2000.03.14
#
# ChangeLog:
# -o option이 있을 경우나 argument로 주어진 파일이
# ps 파일이 아닌 경우 a2ps 를 부르도록 수정
# argument가 안 주어진 경우 stdin에서 읽어드림. (2000/03/16)
# string변환을 postscript language에서 하도록 변경. (2000/03/20)
# string변환을 하고 아직 비여있은 공간을 없앰 (2000/03/23)
# stdin으로부터 온 내용도 필요하면 a2ps로 보냄 (2000/12/28)
# mutt와 함께 쓸 수 있도록 -m옵션을 추가 (2000/01/03)

import string,sys,os

try: 
        from os import tmpnam # python2.0
except:
        def tmpnam():
                return "/tmp/a2ps-h-tmp"

hps = '/Gulim-Medium-KSC-EUC-H'
hbps = '/Gulim-Medium-KSC-EUC-H'
hbops = '/Gulim-Medium-KSC-EUC-H'
hops = '/Gulim-Medium-KSC-EUC-H'

hps = '/Gulim-Regular'
hbps = '/Gulim-Regular'
hbops = '/Gulim-Regular'
hops = '/Gulim-Regular'

def startswith(s, needle):
        if len(needle) > len(s): return 0
        return s[:len(needle)] == needle

def trans_file(filename):
        if type(filename) == type([]):
                lines = filename
        else:
                lines = open(filename).readlines()
        for i in range(len(lines)):
                if startswith(lines[i], '% Check PostScript language '):
                        print show_override
                        print lines[i],
                elif startswith(lines[i], '% Dictionary for ISO-8859-1'):
                        print lines[i],
                        print lines[i+1],
                        print hangul_font
                        lines = lines[i+10:]
                        break
                else:
                        print lines[i],
        for line in lines: print line,

hangul_font = """\
16 dict begin
  /FontName /fCourier def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Courier findfont %(hps)s findfont ] def
  FontName currentdict
  end
definefont /fCourier exch def

16 dict begin
  /FontName /fCourier-Bold def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Courier-Bold findfont %(hbps)s findfont ] def
  FontName currentdict
  end
definefont /fCourier-Bold exch def

16 dict begin
  /FontName /fCourier-BoldOblique def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Courier-BoldOblique findfont %(hbops)s findfont ] def
  FontName currentdict
  end
definefont /fCourier-BoldOblique exch def

16 dict begin
  /FontName /fCourier-Oblique def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Courier-Oblique findfont %(hops)s findfont ] def
  FontName currentdict
  end
definefont /fCourier-Oblique exch def

16 dict begin
  /FontName /fHelvetica def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Helvetica findfont %(hps)s findfont ] def
  FontName currentdict
  end
definefont /fHelvetica exch def

16 dict begin
  /FontName /fHelvetica-Bold def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Helvetica-Bold findfont %(hbps)s findfont ] def
  FontName currentdict
  end
definefont /fHelvetica-Bold exch def

16 dict begin
  /FontName /fTimes-Bold def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Times-Bold findfont %(hbps)s findfont ] def
  FontName currentdict
  end
definefont /fTimes-Bold exch def

16 dict begin
  /FontName /fTimes-Roman def /FontType 0 def
  /WMode 0 def /FMapType 3 def /FontMatrix matrix def
  /Encoding [0 1] def
  /FDepVector [ /Times-Roman findfont %(hps)s findfont ] def
  FontName currentdict
  end
definefont /fTimes-Roman exch def
""" % locals()

show_override = """\
%  
%%Copyright: (c) 2000, 2001 Chideok Hwang
/han-trans {
        dup length 3 mul string /mystr exch def
        /mylen 0 def
        /in-hangul false def
        { 
                dup 128 gt {
                        in-hangul {
                          % c
                           mystr exch mylen exch put
                           /mylen mylen 1 add def
                        } {
                          /in-hangul true def
                          % 255 1 c 
                          mystr mylen (\\377\\1) putinterval  
                          mystr exch mylen 2 add exch put
                           /mylen mylen 3 add def
                        } ifelse
                } {
                        in-hangul not {
                          % c
                          mystr exch mylen exch put
                           /mylen mylen 1 add def
                        } {
                          /in-hangul false def
                          % 255 0 c
                          mystr mylen (\\377\\0) putinterval  
                          mystr exch mylen 2 add exch put
                           /mylen mylen 3 add def
                        } ifelse
                } ifelse
        } forall
        mystr 0 mylen getinterval
} bind def

/origshow {show} bind def
/show {han-trans origshow} bind def
/origstringwidth {stringwidth} bind def
/stringwidth { han-trans origstringwidth } bind def

%\
"""

def run_a2ps(input_file):
        ps = os.popen('a2ps --output=- ' + input_file)
        return ps.readlines()

def run_a2ps_from_stdin(contents):
        infile_name = tmpnam()
        infile = open(infile_name, 'w')
        infile.write(contents)
        del infile # flush
        a2ps_args = ' --center-title="' + title + '" ' + \
                '--footer="편지 메시지" ' + \
                '--output=- '+ infile_name
        ps = os.popen('a2ps ' + a2ps_args, 'r')
        outlines = ps.readlines()
        os.remove(infile_name)
        return outlines

try:
        i = sys.argv.index('-o')
        sys.stdout = open(sys.argv[i+1], 'w')
        del sys.argv[i:i+2]
except: pass

if '-h' in sys.argv:
        sys.exit(0)

if '-m' in sys.argv:
        # called from mutt 
        i = sys.argv.index('-m')
        del sys.argv[i]
        assert len(sys.argv) == 1
        input_buf = sys.stdin.read()
        magic = input_buf[:5];
        import re
        title = re.search('^Subject:(.*)$', input_buf, re.M).group(1)
        input_file = None
elif len(sys.argv) == 1:
        input_buf = sys.stdin.read()
        magic = input_buf[:5]
        title = 'From Stdin'
        input_file = None
else:
        input_file = sys.argv[1]
        magic = open(input_file).read(5)

if magic != '%!PS-':
        if input_file:
                input_lines = run_a2ps(input_file)
        else:
                input_lines = run_a2ps_from_stdin(input_buf)

trans_file(input_lines)

