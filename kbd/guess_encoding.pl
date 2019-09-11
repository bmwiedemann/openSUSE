#! /usr/bin/perl -w
#
# encoding.pl -- guess charset encoding
#
# (C) 2007, jw@suse.de, Novell Inc.
# Distribute under GPLv2
# 
# 2006-12-05, jw, V0.1 -- only framework.
# 2007-01-23, jw, V0.2 -- utf8 and latin1 for ttys.
# 2007-02-08, jw, V0.3 -- utf8 and latin1 for files.

use Data::Dumper;
use POSIX;
use IO::Handle;

my $version = '0.3';
my $verbose = 0;
my $stdin = 0;

while (defined (my $arg = shift))
  {
    if    ($arg !~ m{^-.})		{ unshift @ARGV, $arg; last }
    elsif ($arg =~ m{^(-h|--help|-\?)})	{ exit usage(); }
    elsif ($arg =~ m{^--?v})		{ $verbose++; }
    elsif ($arg =~ m{^--?q})		{ $verbose = 0; }
    else { exit usage("unknown option $arg"); }
  }

if (!@ARGV and -t STDIN and -t STDERR)
  {
    my $r = probe_tty();
    print "$r\n";
    exit 0;
  }

for my $file (@ARGV)
  {
    my $fd;
    open $fd, ($file eq '-') ? '<&=STDIN' : "<$file" or die "open($file) failed: $!";
    probe_file($fd, $file);
    close $fd;
  }

exit 0;
########################################################################

sub usage
{
  my ($msg) = @_;
  print STDERR qq{$0 V$version usage:

encoding [options] [file]

valid options are:
 -h                         Print this online help
 -v                         Be more verbose. Default $verbose
 -q                         Be quiet
 -                          Read from stdin.

Without any parameters, the terminal (if any) is probed, 
using stdin and stderr.

Files are searched for characters outside the ascii range.
Those characters are tested for their likeliness in 
various encodings.
Thus an illegal mix of encodings can be detected.

If not verbose, only one single word is printed to stdout:
The name of the most likely encoding.

};

  print STDERR "\nERROR: $msg\n" if $msg;
  return 0;
}

sub sysread_tout
{
  my ($FILE, $len, $tout) = @_;
  my $r = '';
  while ($len > 0)
    {
      my $rout;
      my $rin = '';
      vec($rin,fileno($FILE), 1) = 1;
      my ($n, $t) = select($rout = $rin, undef, undef, $tout);
      $tout = $t if defined $t;
      last unless $n;
      my $buf = '';
      last if sysread($FILE, $buf, 1) <= 0;
      $r .= $buf;
      $len--;
    }
  return $r;
}

sub tty_raw
{
  my ($FILE) = @_;

  my $t = POSIX::Termios->new;
  my $o = POSIX::Termios->new;
  $t->getattr(fileno $FILE);
  $o->getattr(fileno $FILE);

  $t->setlflag(0);	# -echo, -icanon
  $t->setcc(POSIX::VMIN, 1);
  $t->setcc(POSIX::VTIME, 0);
  tty_set($FILE, $t);
  return $o;
}

sub tty_set
{
  my ($FILE, $t) = @_;
  $t->setattr(fileno $FILE, POSIX::TCSANOW) or die "TCSANOW failed: $!\n";
}

sub get_cursor_pos
{
  my ($hint) = @_;
  # 1 may be an ansi term?
  # testing device status report 6, as seen in vttest.
  my $t = tty_raw(STDIN);

  while (length(sysread_tout(STDIN, 1, 0.1))) { }

  syswrite(STDOUT, "\33[6n", 4);
  my $r = sysread_tout(STDIN, 10, 0.1);
  tty_set(STDIN, $t);
  return { x => $2 - 1, y => $1 - 1, hint => 'DC6' } if $r =~ m{^\33\[(\d+);(\d+)R};
  return undef;
}

sub probe_tty
{
  #
  # we can use STDIN and STDERR.
  # 0) first, see, if the terminal can report cursor positions.
  syswrite(STDOUT, "\r", 1);
  my $o = get_cursor_pos();
  print ", x=$o->{x}\n" if $verbose > 1;

  # - if not, abort.
  die "get_cursor_pos failed.\n" unless defined $o;

  # - if it can, store the current position 
  if ($o->{x} != 0)
    {
      warn "strace (or other) output interferes or\n" if $o->{x} >= 20;
      die "carriage return does not work.\n";
    }

  # 1) write a single byte ascii character, 'X' and check, 
  # if it advances by one. 
  syswrite(STDOUT, "\rX", 2);
  my $p = get_cursor_pos($o->{hint});
  print ", x=$p->{x}\n" if $verbose;
  

  # - If not, it is probably in microsoft-multibyte encoding, 
  #   and requires '\0' prefixing. check this, report and abort.
  die "multi-byte mode" if $p->{x} != 1;

  # 2)Then try non-ascii characters, e.g. a-umlaut.
  # 2a) send its latin1 code, and see what happens,
  syswrite(STDOUT, "\r1\34434", 5);	# 1, a-umlaut-latin1, 3, 4
  $p = get_cursor_pos($o->{hint});
  print ", x=$p->{x}\n" if $verbose;
  die "no report" unless defined $p;

  # - no advance indicates that the terminal is not in latin1 mode 
  #   or a lousy font is used.
  # - advance by 2 indicates a defect in the tty-emulator.
  die "latin1 a-umlaut caused confusion." if $p->{x} > 4 or $p->{x} < 2;

  # in utf8, our \344 consumes another char, thus the '3' is not printed.
  # we don't know what the font does then.
  my $maybe = 'utf8' if $p->{x} == 2 or $p->{x} == 3;
  $maybe = 'latin1'  if $p->{x} == 4;
  print "maybe $maybe\n" if $verbose;
  # - advance by 1 says nothing, may be latin1.
  # 2b) send its utf8 code.

  syswrite(STDOUT, "\r1\303\24434", 6);	 # 1, a-umlaut-utf8, 3, 4
  $p = get_cursor_pos($o->{hint});
  print ", x=$p->{x}\n" if $verbose;

  die "no report" unless defined $p;
  # - no advance indicates that a lousy font is used.
  # - advance by one indicates that the terminal is in utf8 mode.
  # - advance by two indicates that the terminal is in latin1 mode.

  syswrite(STDOUT, "\r      \r", 8) unless $verbose;	 # clear scratch area
  
  if ($p->{x} == 4)
    {
      return 'utf8' if $maybe eq 'utf8';
      return 'possibly utf8';
    }
  
  return 'latin1' if $maybe eq 'latin1';
  return 'possibly latin1';
}

##
## if utf8_valid is positive, then it can only be utf-8.
##   (if also utf8_invalid and/or latin1_typ are positive, then it is a mixture)
## if only utf8_invalid or latin1_typ are positive, then it is latin1.
## if all 3 are zero, it is plain ascii.
##
## FIXME: should take an optional length parameter to limit runtime.
##
sub probe_file
{
  my ($fd, $name) = @_;
  print "probing $name\n" if $verbose;

  my %typ_latin = map { $_ => 1 } qw(169 171  174 176 177 178 179 181
  185 187 191 192 193 194 195 196 197 199 200 201 202 203 204 205 206 207 208 209
  210 211 212 213 214 215 216 217 218 219 220 
  223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245
  246 249 250 251 252 253 189 164);


  # when running incremental, $fd is probably not seekable.
  # so we need to buffer characters to be re-read after a lookahead.

  # http://de.wikipedia.org/wiki/UTF-8#Kodierung

  my $utf8_valid   = 0;		# parser happy.
  my $utf8_invalid = 0;		# something wrong.
  my $latin1_typ   = 0;		# valid chars in 128..255 range followed by a ascii byte
  my $ascii        = 0;		# char in 10..127 range
  my $utf8_size    = 0;		# how many bytes belong to this utf-8 char.
  my $utf8_len     = 0;		# how many more bytes belong to this utf-8 char.
  my $utf8_start   = 0;		# ord of utf_8 start char.

  while (defined(my $c = getc($fd)))
    {
      my $v = ord($c);
      if ($utf8_len)
        {
	  if (($v & 0xc0) == 0x80)	# 10xx xxxx
	    {
#	      printf "0 %02x\n", $v;
	      unless (--$utf8_len)
	        {
	          $utf8_valid++;
		  $utf8_size = 0;
		}
	    }
	  else
	    {
#	      printf "0x %02x %02x '$c' $utf8_size-$utf8_len\n", $utf8_start, $v;
              if (($utf8_size - $utf8_len) == 1 and $typ_latin{$utf8_start})
		{
		  if ($v > 7 && $v < 128)
		    {
		      $latin1_typ++;
		      $ascii++;
		    }
		  elsif ($typ_latin{$v})
		    {
		      $latin1_typ += 2;
		    }
		  else
		    {
		      $utf8_invalid++;
		    }
		}
	      else
		{
		  $utf8_invalid++;
		}
	      $utf8_len = $utf8_size = $utf8_start = 0;
	    }
	}
      elsif ($v > 7 && $v < 128)
        {
	  $ascii++;
	  next;
	}
      elsif (($v & 0xe0) == 0xc0)	 	# 110x xxxx
        {
	  $utf8_start = $v;
	  $utf8_size = 2;
	  $utf8_len = 1;
#	  printf "1 %02x\n", $v;
	}
      elsif (($v & 0xf0) == 0xe0)		# 1110 xxxx
        {
	  $utf8_start = $v;
	  $utf8_size = 3;
	  $utf8_len = 2;
#	  printf "2 %02x\n", $v;
	}
      elsif (($v & 0xf8) == 0xf0)		# 1111 0xxx
        {
	  $utf8_start = $v;
	  $utf8_size = 4;
	  $utf8_len = 3;
#	  printf "3 %02x\n", $v;
	}
      elsif ($typ_latin{$v})
        {
	  $latin1_typ++;
	}
      else
        {
	  $utf8_invalid++;
#	  printf "x %02x\n", $v;
	}
    }
  print "$name: utf8_valid=$utf8_valid utf8_invalid=$utf8_invalid latin1_typ=$latin1_typ ascii=$ascii\n";
}
