#! /usr/bin/perl

my $name = $ARGV[0];
$name =~ s,.*/,,;
$name =~ s,\.spec.*,,;

my %attributes = ();
open(FILE, $ARGV[1]) || die 'no attributes';
my $pack = undef;
my $text = undef;
while ( <FILE> ) {
	if (/^\+(.*)$/) { $pack = $1; $text = ''; next }
	if (/^-(.*)$/) {
	    if ($pack ne $1) {
		die "$pack and $1 do not match";
	    }
	    $text =~ s,^\s*,,;
	    $text =~ s,\s*$,,;
	    $attributes{$pack} = $text;
	    $text = undef;
	    $pack = undef;
	    next;
	}
	if (defined $text) {
	    $text .= $_;
	} elsif (/^(\S*)\s*(.*)$/) {
	    my $attr = $1;
	    my $string = $2;
	    $string =~ s,^\s*,,;
	    $string =~ s,\s*$,,;
	    $attributes{$attr} = $string;
	}
}
close(FILE);

open(FILE, $ARGV[0]);

sub description()
{
  if (/^%description\s*(.*)\s*/) {
        my $suffix = $1;
        my $pname = $name;

	if ($suffix =~ m/-n\s*(.*)/) {
		$pname = $1;
        } else {
	        $pname = "$name-$suffix" if ($suffix);
	}

        if (defined $attributes{"description.$pname"}) {
           print $_;
           my $descr = $attributes{"description.$pname"};
           print "$descr\n";
           $_ = '';
           do {
	       $_ = <FILE>;
           } while ( $_ !~ /^%/ && $_ !~ /^@/ );
           print "\n";
           description();
        }
  }

}

# current subpackage
my $pname = $name;

while ( <FILE> )
{
  if (/^Name:\s*(.*)/) {
	$name = $1;
	$pname = $1;
  }
  description();

  if (/^%package\s*(.*)/) {
      my $suffix = $1;
      if ($suffix =~ m/-n\s*(.*)/) {
	  $pname = $1;
      } else {
	  $pname = "$name-$1";
      }
  }

  if (/^(Summary:\s*)(.*)$/) {
      if (defined $attributes{"summary.$pname"}) {
	  print $1 . $attributes{"summary.$pname"} ."\n";
	  next;
      }
  }
  if (/^(License:\s*)(.*)$/) {
      if (defined $attributes{"license.$pname"}) {
	  print $1 . $attributes{"license.$pname"} ."\n";
	  next;
      }
  }
  if (/^(Group:\s*)(.*)$/) {
      if (defined $attributes{"group.$pname"}) {
	  print $1 . $attributes{"group.$pname"} ."\n";
	  next;
      }
  }
  print $_;
}

close(FILE);
