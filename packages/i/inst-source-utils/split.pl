#!/usr/bin/perl -w
#
use strict;

my $file="";
my $newfile="";
my $newdata="";
my $starttag="# <!--internal-->";
my $endtag="# <!--/internal-->";
my $loglevel=0;

sub usage {
	print <<EOF
Usage: $0 [-s <start-tag>] [-e <end-tag>] <filename> <newfile>
       
       splits out textblocks marked with start and endtag. 
	   Default:
       $starttag
       $endtag

       -s <starttag> : define new start-tag
       -e <endtag>   : define new end-tag

EOF
;
	exit 1;
}

sub LOG {
  my $message = shift;
  my $level   = shift || 0;
#  my $time = localtime(time);
  if ( $level <= $loglevel ) {
#      print LOGFILE "[$time] [$$] $message\n";
	print "$message\n";
  }
}

sub splitInternal {
	my $file=shift;
    my $data;
    open (FILE,"$file") || die ("Can not open $file: $! $?!\n");
    while (<FILE>) {
      chomp;
      if ( $_ =~ /^$starttag/){
		while (<FILE>) {
			chomp;
			last if $_ eq "$endtag";
		}
	  } else {
		  $data .= "$_\n";
	  }
	}
  return $data;			
}

while  (my $param = shift (@ARGV)) {
	if (( $param eq "-h" ) || ( $param eq "--help" )){
        usage();
    }

	if (($param eq "-s" ) || ($param eq "--start-tag")){
		$starttag=shift(@ARGV);
		next;
	}

	if (($param eq "-e" ) || ($param eq "--end-tag")){
		$endtag=shift(@ARGV);
        next;
    }

	if (($param eq "-v" ) || ($param eq "--verbose")){
		$loglevel=2;
		next;
	}

	if ($file eq ""){
		$file=$param;	
		next;
	} 

	$newfile=$param;
}

if ($newfile eq ""){
	die("newfile not defined!\n");
	usage();
}

if ($file eq ""){
    die("filename not defined!\n");
    usage();
}

if (-f $file) {
	$newdata=splitInternal($file);
	LOG ("File $newfile exists - overwriting!\n",1) if (-f $newfile);
	open(NEWFILE, "> $newfile");
		print NEWFILE $newdata;
	close(NEWFILE);
	LOG("New file $newfile written",2);
} else {
	print "File $file not found.\n";
	usage();
}

