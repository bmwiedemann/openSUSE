#!/usr/bin/perl -w
# $Id: elilo.pl,v 0.94 2018/11/22 15:48:50 rw Exp $
use strict;

my $C = $0; $C =~ s{^.*/}{};

my $dbg = (exists( $ENV{"ELILO_DEBUG"})) ? $ENV{"ELILO_DEBUG"} : "";
my $Edition = q(@EDITION@);
my $Arch = q(@ARCH@);
my $LibD = q(@LIBDIR@);
my $MPold  = "$dbg/boot";
my $MPnew  = "$dbg/boot/efi";
my $Dlibold  = "$dbg$LibD/elilo";
my $Dlib     = "$dbg$LibD/efi";
my $Fconf = "elilo.conf";
my $Flist = "elilo.list";
my %Flist = ();
my $Sconf = "$dbg/etc/" . $Fconf;
my $Xconf = "xen.cfg";
my $Gconf = "grub.cfg";
my $GconfT = "$dbg/etc/default/elilo2grub.in";

my @eBinaries = ("elilo.efi", "xen.efi", "shim.efi");
my ($elilo, $xen, $shim) = @eBinaries;
my @sBinaries = ($shim, "grub.efi", "MokManager.efi"); # hardcoded for now!

my $Reserved = qr{(efi-mountpoint|vendor-directory|elilo-origin|precious|
		(?:y|e)bm-label|static-description|secure-boot|
		SB-(?:fallback|direct2xen|))}ox;
my %Sconf = ();
my %Econf = ();
my @Econf = ();
my %Xconf = ();
my %Xsonf = ();
my @Xconf = ();
my @Gconf = ();
my %Labels = ();
my @Labels = ();
my @Files = ();

my $keep = -1;
my $test = 0;
my $verbose = 0;
my $warn = 0;
my $optional = 1;
my $MP = "";		# Mount-Point for EFI/FAT partition
my $VD = "SuSE";	# vendor-specific directory in $MP/efi
my $D = "";		# will be $MP.$VD
my $EFIarch = "";

my $Disclaimer = <<EoD;
# This file has been transformed by /sbin/elilo.
# Please do NOT edit here -- edit /etc/elilo.conf instead!
# Otherwise your changes will be lost e.g. during kernel-update.
#
EoD

$| = 1;

sub Version() {
  my $v = q($Revision: 0.94 $ );
  $v =~ s/^\$ Rev.*:\ ([0-9.]+)\ \$\ /$1/x;
  $v .= " (part of elilo-$Edition)" if ( $Edition ne "\@EDITION\@" );
  print "$C version $v\n";
  exit( 0 );
}
sub Info ($$) {
  print STDERR $_[1] if ( $verbose >= $_[0] );
}
sub Warn ($) {
  print STDERR "$C: Warning: $_[0]";
  $warn ++;
}
sub Panic ($$) {
  print STDERR "$C: $_[1]";
  exit( $_[0]) if ( $_[0] );
  $warn ++;
  print STDERR "...trying to proceed anyway!\n";
}
sub System($@) {
  my( $fatal, @C) = @_;
  my $cmd = $C[0];

  foreach my $c ( @C[1..$#C] ) {
    if ( $c =~ /[\s\\]/ ) {
      $cmd .= " '$c'";
    } else {
      $cmd .= " $c";
    }
  }
  Info( 1, "> $cmd\n");
  return 0 if ( $test );

  system @C;
  if ($? == -1) {
    Panic( $fatal, "$C[0]: failed to execute: $!\n");
  } elsif ($? & 127) {
    Panic( $fatal, sprintf( "$C[0]: died with signal %d, %s coredump\n",
           ($? & 127),  ($? & 128) ? 'with' : 'without'));
  } elsif ( $? >> 8 != 0 ) {
    Panic( $fatal, "$C[0]: failed\n");
  }
}
sub Rename($$$) {
  my( $loglvl, $oldname, $newname) = @_;
  Info( $loglvl, "> mv $oldname $newname\n");
  if ( -e $newname ) {
    Info( $loglvl+1, ">> unlink( $newname)\n");
    unlink( "$newname") unless ($test);
  }
  Info( $loglvl+1, ">> rename( $oldname, $newname)\n");
  rename( $oldname, $newname) unless ($test);
  # fixme: add failure-detection and handling?
}
sub Write($$$$@) {
  my( $loglvl, $msg, $mode, $file, @lines) = @_;
  my $tmp = ($mode ne ">>");
  my $out = ($tmp) ? "$file.tmp" : "$file";
  my $mstr = ($tmp) ? "create" : "append";
  my $fh;

  Info( $loglvl, $msg);
  if ( $test && $verbose >= $loglvl + 1 ) {
    Info( $loglvl, " STDOUT\n");
    open( $fh, ">&STDOUT");
  } elsif ( $test ) {
    Info( $loglvl, " nowhere\n");
    open( $fh, ">> /dev/null");
  } elsif ( ! open( $fh, "$mode $out") ) {
    Warn( "$out: failed to $mstr: $!\n");
    return 1;
  } elsif ( $verbose > $loglvl ) {
    Info( $loglvl, " '$out'\n");
  } else {
    Info( $loglvl, " '$file'\n");
  }

  print( $fh @lines) || Panic( 1, "$out: failed to write: $!\n");
  close( $fh);

  if ( ! $test && $mode ne ">>" ) {
    Rename( $loglvl+1, $out, $file);
  }
}
sub Merge($$) {
  my( $target, $source) = @_;
  my $in;
  my @l = ();

  Info( 2, "### check file list of previous installs:");
  if ( ! open( $in, "<  $source") ) {
    Warn( "could not open < '$source': $!\n");
    return 1;
  }
  while ( <$in> ) {
    chomp;
    next if (m{/} || exists( $Flist{$_}));
    push @l, "$_\n";
  }
  close( $in);
  if ( $#l < 0) {
    Info( 2, " none!\n");
  } else {
    my $n = $#l + 1;
    Info( 2, " $n missing\n");
    Write( 2, "### appending to", ">>", $target, @l);
  }
}
sub Install($$$$) {
  my( $f, $o, $s, $d) = @_;
  my @C = ( "install", $o, $s, $d);

  if ( $o eq "-p" ) {
    @C = ( "cp", "--preserve=timestamps", $s, $d);
  }
  System( $f, @C);
}

my $labelc = 0;
sub mkLabel($$) {
  my( $label, $namespace) = @_;

  if (exists( $Labels{$namespace}{$label})) {
    my $t = 1;
    my $l = $label;
    while ( exists $Labels{$namespace}{$l} ) {
      $l = sprintf "%s.%d", $label, $t++;
    }
    Warn( "duplicate label '$label', replaced with '$l' in $namespace\n");
    $label = $l;
  }
  $Labels{$namespace}{$label} = ++$labelc;
  push @Labels, "$namespace $label";
  Info(4,"L($namespace)= ".join(", ",sort(keys(%{$Labels{$namespace}})))."\n");
  return $label;
}
my $sections = 0;
sub section2Econf($$%) {
  my( $in, $lnr, %current) = @_;

  if ( $current{xencfg} && ! $current{precious} ) {
    Info( 3, "===     Econf: skipping $current{label} for $Fconf.\n");
    return( 0 );
  }
  if ( exists( $current{label}) ) {
    my $l = mkLabel( $current{label}, "Econf");
    if ( $l ne $current{label} ) {
      $current{Econf}[$current{label_loc}] = $current{label_pre} . $l ."\n";
    }
    Info( 2, sprintf "=== %2d. Econf: $l\n", ++$sections);
    $Econf{$l}{options} = (exists( $current{append}) ? $current{append} :
        			(exists( $Sconf{append}) ? $Sconf{append} : ""));
    $Econf{$l}{kernel} = $current{image};
    $Econf{$l}{ramdisk} = (exists( $current{initrd}) ? $current{initrd} : "");
    $Econf{$l}{root} = (exists( $current{root}) ? $current{root} :
        			(exists( $Sconf{root}) ? $Sconf{root} : ""));
    $Econf{$l}{description} = (exists( $current{description}) ? $current{description} : $l);
    if ( exists($Sconf{default}) && $current{label} eq $Sconf{default} ) {
      $Sconf{grubdefault} = $Econf{$l}{description};
    }
  }
  foreach my $l ( @{$current{Econf}} ) {
    push @Econf, $l;
  }
  return( 0 );
}
my $Xsections = 0;
sub section2Xconf($$%) {
  my( $in, $lnr, %current) = @_;
  my( $label, $image, $initrd, $append, $root, $vmm, $vmmopts, $ucode, $desc);

  if ( ! $current{xencfg} ) {
    Info( 3, "===     Xconf: skipping ".
	(exists( $current{label}) ? $current{label} : "section")
	." for $Xconf.\n");
    return( 0 );
  }
  if ( ! exists( $current{image}) ) {
    Warn( "$in: $lnr: no image: incomplete section skipped\n");
    return( 1 );
  }
  if ( ! exists( $current{image}) || ! exists( $current{label}) ) {
    Warn( "$in: $lnr: incomplete section skipped\n");
    return( 1 );
  }

  $label = mkLabel( $current{label}, "Xconf");
  $image = $current{image};
  $initrd = (exists( $current{initrd}) ? $current{initrd} :
  	(exists( $Sconf{initrd}) ? $Sconf{initrd} : ""));
  $append = (exists( $current{append}) ? $current{append} :
  	(exists( $Sconf{append}) ? $Sconf{append} : ""));
  $vmmopts = (exists( $current{vmmopts}) ? $current{vmmopts} :
  	(exists( $Sconf{vmmopts}) ? $Sconf{vmmopts} : ""));
  $root = (exists( $current{root}) ? $current{root} :
  	(exists( $Sconf{root}) ? $Sconf{root} : ""));
  $root = ($root ? " root=$root " : " ");
  $vmm = (exists( $current{VMM}) ? $current{VMM} :
  	(exists( $Sconf{vmm}) ? $Sconf{vmm} : ""));
  $ucode = (exists( $current{ucode}) ? $current{ucode} :
  	(exists( $Sconf{ucode}) ? $Sconf{ucode} : ""));
  if ( exists( $current{description}) ) {
    $desc = $current{description};
  } else {
    my $vers = $image;
    $vers =~ s{^[^-]+-}{};
    $desc = "$label ($vers)";
  }

  if ( ! $vmm ) {
    Warn( "$in: $lnr: no vmm?!\n");
    return( 1 );
  }
  if ( exists( $current{vmm}) ) {
    Info( 1, "$in: $lnr: legacy vmm ($current{vmm}) skipped for $Xconf.\n");
    return( 0 );
  }
  Info( 2, sprintf "=== %2d. Xconf: $label\n", ++$sections);
  $Xconf{$label}{ucode} = $ucode if ($ucode);
  $Xconf{$label}{vmm} = $vmm;
  $Xconf{$label}{options} = $vmmopts;
  $Xconf{$label}{kernel} = $image;
  $Xconf{$label}{append} = $root . $append;
  $Xconf{$label}{ramdisk} = $initrd if ( $initrd);
  $Xconf{$label}{description} = $desc;
  if ( exists($Sconf{default}) && $current{label} eq $Sconf{default} ) {
    $Xconf{$label}{cfg} = $Xconf;
    $Sconf{grubdefault} = $desc;
  } elsif ( $Sconf{xencfg} != 2 && $Xsections == 0 ) {
    $Xconf{$label}{cfg} = $Xconf;
    ++$Xsections;
  } else {
    $Xconf{$label}{cfg} = "xen". ++$Xsections .".cfg";
  }

  return( 0 );
}

sub Parse($$) {
  my( $in, $verbosity) = @_;
  my $ov = $verbose;
  $verbose = ($verbosity < 0 ) ? $ov : $verbosity;

  $Sconf{xencfg} = 0;
  open( IN, "< $in") || Panic(1, "$in: failed to open: $!\n");
  Info( 1, "## parsing '$in'...\n");
  Info( 3, "### pick up global settings...\n");
  while ( <IN> ) {
    chomp;
    s{^##YaST - boot_efilabel =}{ybm-label=};
    if ( m/^$Reserved\s*(?:\=\s*(?|"([^"]+)"|([^"].*?)))?\s*$/xo ) {
      $Sconf{$1} = (defined($2)) ? $2 : "true";
    } elsif ( m/^(append|root|timeout)\s*=\s*(?|"([^"]+)"|([^"].*?))\s*$/xo ) {
      $Sconf{$1} = $2;
    } elsif ( m/^(default|prompt|relocatable)\s*(?:\=\s*(.+))?\s*$/xo ) {
      $Sconf{$1} = (defined($2)) ? $2 : "true";
    } elsif ( m/^(vmm)\s*\=\s*(?|"([^"]+)"|([^"].*?))\s*$/xo ) {
      my ($k, $v) = ($1, $2);
      next unless (defined( $v));
      $Sconf{$k} = $v;
      if ( $v =~ m/^(\S+.efi)(?:\s+(.*))?$/ ) {
	$Sconf{vmm} = $1;
	$Sconf{vmmopts} = (defined( $2) ? $2 : "");
	$Sconf{xencfg} = 1;
      } else {
	Info( 1, "$C: $in: $.: ignoring non-efi based VMM. ($Sconf{vmm})\n");
      }
    } elsif ( m/^image\s*=/ ) {
      last;
    } else {
      next;
    }
    Info( 3, ">>>  $1 = '$Sconf{$1}'\n");
  }
  my( $c, %f, $opt);
  my $default_label = "";
  my $default_loc;
  my $image = "";
  my %current = ();
  my %fp = ();
  Info( 3, "### start over...\n");
  seek( IN, 0, 0);
  $. = 0;
  while ( <IN> ) {
    $opt = $optional;
    if ( m/^\s*$Reserved\s*(?:\=\s*(.+))?\s*$/xo ) {
      $current{$1} = (defined($2)) ? $2 : "true";
      next;
    }
    if ( m{^\s*(?:image|initrd|vmm|ucode)\s*=\s*} ) {
      my $orig = $_;
      chomp;
      s{(vmm\s*=\s*)"([^"]+)"\s*(#.*)?$}{$1$2};
      s{^(\s*(image|initrd|vmm|ucode)\s*=\s*)(/\S+/)?([^/\s]+)\s*(.*?)\s*$}{$1$4};
      my( $k, $p, $f, $o) = ($2, $3, $4, $5);
      #Info( 8, ">>> $.: k=$k p=$p f=$f\n");
      $_ .= "\n";
      if ( $k eq "image" ) {
	# new "image=" => finish up the previous one...
	$c += section2Econf( $in, $., %current);
	$c += section2Xconf( $in, $., %current) if (exists( $current{image}));
	%current = ();
      }
      if ( $k eq "vmm" && $f =~ m/\.efi$/ ) {
        $k = "VMM";
	$p = $Dlib . "/" unless (defined( $p));
	$p =~ s{^$dbg}{}o if ($dbg);
	$current{vmmopts} = $o;
	$current{xencfg} = $Sconf{xencfg} = 1;
	$opt = 0; # 'xen.efi' is *never* optional!
      } elsif ( defined( $o) && $o ) {
	Warn( "$in: $.: ignoring trailing garbage...\n");
      }
      if ( $k eq "ucode" ) {
        $Sconf{$k} = $f if (!exists( $current{image}) && !exists( $Sconf{$k}));
        $_ = "# $_";  # hide 'ucode' from elilo.conf -- it's only for XEN!
	$opt = 0; # ucode is *never* optional!
      }
      if ( ! defined( $p) ) {
	$p = "/boot/";
      }
      if ( ! defined( $f) ) {
	Warn( "$in: $.: invalid file-specification\n" .
	      ">> $orig");
	$c++;
      } elsif ( exists( $f{$f}) ) {
	if ( "$p$f" eq $fp{$f} ) {
	  Info( 4, ">>> $.: copy only once (previous: line $f{$f})\n" .
	        ">> $orig");
	} else {
	  Warn( "$in: $.: ambigous target '$f' (previous: $f{$f}: $fp{$f})\n" .
	        ">> $orig" . "=> first wins\n");
	}
	$current{$k} = $f;
	$current{"path2$k"} = $fp{$f};
      } else {
	my $fp = "$dbg$p$f";
	if ( -r $fp ) {
	  $current{$k} = $f;
	  $current{"path2$k"} = $fp;
	  push @Files, $fp;
	  $fp{$f} = $p . $f;
	  $f{$f} = $.;
	} elsif ( $opt ) {
	  Info( 0, "$C: Info: $in: $.: missing optional '$p$f' skipped\n");
	} else {
	  Warn( "$in: $.: missing '$p$f'\n");
	}
      }
      next if ( $k eq "VMM" ); # omit efi-based "vmm" lines from elilo.conf!
    } elsif ( exists( $current{image}) &&
	      m{^(\s*description\s*=\s*)(?|"([^"]+)"|([^"].*?))\s*$}xo ) {
      my( $p, $d) = ($1, $2);
      my $image = $current{path2image};
      my $t = "";
      my $od = $d;
      $d .= " (%G)" if ( $d =~ m{^(Linux|Failsafe)$} );
      if ( $d =~ m{\%L} ) {
	if ( -l $image ) {
	  ($t = readlink( $image)) =~ s{^vmlinuz-}{};
	} else {
	  #($t = $image) =~ s{^.*vmlinux-}{};
	  $t = "no symlink";
	}
	Info( 3, ">>> $.: \%L => '$t'\n");
	$d =~ s{\%L}{$t};
      } elsif ( $d =~ m{\%G} ) {
	my $cmd = "/sbin/get_kernel_version";
	if ( -x $cmd ) {
	  chomp( $t = qx{$cmd $image});
	} else {
	  $t = "";
	}
	$d =~ s{\%G}{$t};
	Info( 3, ">>> $.: \%G => '$t'\n");
      }
      if ( $Sconf{'static-description'} ) {
        $d = $od;
      } else {
        $_ = $p . q{"} . $d . q{"} . "\n";
      }
      $current{description} = $d;
    } elsif (m{^\s*(append|root)\s*=\s*(?|"([^"]+)"|([^"].*?))\s*$}xo ) {
      my( $k, $v) = ($1, $2);
      Info( 0, "$C: $in: $.: duplicate option (last wins)\n")
         if (exists( $current{$k}));
      $current{$k} = $v;
    } elsif (m{^(\s*label\s*=\s*)(\S+)}) {
      my ($pre, $label) = ($1, $2);
      $current{label_pre} = $pre;
      $current{label} = $label;
      $current{label_loc} = $#{$current{Econf}} + 1;
    } elsif (m{^\s*default\s*=\s*(\S+)}) {
      $default_label = $1;
      $default_loc = $#{$current{Econf}} + 1;
    } elsif (m{^\s*read-only\s*$}) {
      $_ = "#read-only # Deprecated!" .
	"  (Add comment in '$Sconf' to overrule.)" .
	"\n";
      Info( 2, "  $in: $.: deprecated 'read-only' ignored.\n");
    } elsif (m{^\s*relocatable\s*$} && $Arch =~ m{86}) {
      $_ = "#relocatable # Unsupported on this architecture!\n" .
	"#  (May be forced by adding a comment in '$Sconf'.)\n";
      Info( 2, "  $in: $.: unsupported 'relocatable' ignored.\n");
    }
    push @{$current{Econf}}, $_;
  }
  if ( exists( $current{image})) {
    $c += section2Econf( $in, $., %current);
    $c += section2Xconf( $in, $., %current);
  }
  if ($default_label ne "" && exists( $Labels{Xconf}{$default_label})) {
    $Sconf{xencfg} = 2;
    $Econf[$default_loc] = "#" . $Econf[$default_loc];
    Info( 1, ">>> default label '$default_label' points to a XEN section\n");
  } elsif ($default_label ne "" && !exists $Labels{Econf}{$default_label}) {
    $Econf[$default_loc] = "#" . $Econf[$default_loc];
    Info( 1, ">>> default label '$default_label' undefined in $Fconf\n");
  } elsif ($default_label eq "" && $Labels[0] =~ m{^Xconf }) {
    $Sconf{xencfg} = 2;
    Info( 1, ">>> first section (implicit default) points to a XEN section\n");
  }
  close( IN);
  $Sconf{'__warn-count'} = $c;

  Info( 2, "## end of parsing $in\n") unless $test;
  $verbose = $ov;
}

sub addList($) {
  my( $f) = @_;
  $f =~ s{^.*/([^/]+)$}{$1};
  print( LIST "$f\n") if ( fileno( LIST) );
  $Flist{$f} = $_[0];
}
sub Output($$@) {
  my( $dir, $file, @lines) = @_;
  my $out = "$dir/$file";

  if ( (! $test || $verbose > 3) && $file ne $Gconf ) {
    unshift @lines, $Disclaimer;
  }
  Write( 1, "## writing '$file' to", ">", $out, @lines);
  addList( $out);
}
my %GconfFSuuid = ();
sub canonicalize($$) {
  my( $base, $rel) = @_;

  return( $rel ) unless( defined( $rel) );
  Info( 9, "canonicalize($base, $rel): ");
  $base = "" if ($rel =~ m{^/});
  $base =~ s{/[^/]+$}{};

  while ( $rel =~ s{^(\.\.?)/}{} ) {
    $base =~ s{/[^/]+$}{} if ( $1 eq ".." );
  }
  $rel =~ s{^/}{};
  Info( 9, "'$base/$rel'\n");
  return ( "$base/$rel" );
}
sub readLink($) {
  my( $lnk) = @_;

  my $tgt = readlink( $lnk);
  Info( 9, "readLink($lnk): ".(defined($tgt) ? $tgt : "(--undef--)")."\n");
  $tgt = canonicalize( $lnk, $tgt);
  Info( 8, "readLink($lnk): ".(defined($tgt) ? $tgt : "(--undef--)")."\n")
    unless ($verbose > 8);
  return( $tgt );
}
sub GconfProbeFSuuid($) {
  my( $dev) = @_;
  my $udir = "/dev/disk/by-uuid";
  my $ldir = "/dev/disk/by-label";
  my $uuid = "";
  my $tgt = "";

  Info( 5, "GconfProbeFSuuid($dev): \n");
  if ( ! -b $dev ) {
    if ( $dev =~ m{^UUID=([0-9A-Fa-f-]+)$} ) {
      return ( (-b "$udir/$1") ? $1 : "" );
    } elsif ( $dev =~ m{^LABEL=([0-9A-Fa-f-]+)$} ) {
      $dev = readLink( "$ldir/$1");
      return ( "" ) unless ( defined( $dev) );
    }
  }
  while ( -l $dev ) {
    $_ = readLink( $dev);
    return ( "" ) unless ( defined( $_) );
    Info( 5, "   $dev => $_\n");
    $dev = $_;
  }
  Info( 5, "  looking for: $dev\n");
  if ( opendir( my $fh, $udir) ) {
    while ( ($_ = readdir( $fh)) ) {
      $_ = "$udir/$_";
      next unless ( -l $_ );
      $tgt = readLink( $_);
      next unless (defined( $tgt) );
      Info( 5, "  looking at: $_ => $tgt\n");
      next unless ( $dev eq $tgt );
      s{^$udir/}{};
      $uuid = $_;
      Info( 5, "  found:  $uuid!\n");
      last;
    }
    closedir( $fh);
  }
  return ( $uuid );
}
sub GconfFSuuid($) {
  my( $spec) = @_;
  return ( "" ) unless ( $Sconf{SB} );
  $spec =~ s{^UUID=}{/dev/disk/by-uuid/};
  return ( $GconfFSuuid{$spec} ) if ( exists( $GconfFSuuid{$spec}) );

  my $uuid = "";
  my $cmd = "/usr/sbin/grub2-probe";
  if ( -x $cmd ) {
    my $dop = (-b $spec) ? "--device" : "";
    chomp( $uuid = qx{$cmd --target=fs_uuid $dop "$spec"});
  }
  if ( ! defined( $uuid) || ! $uuid ) {
    $uuid = GconfProbeFSuuid( $spec);
  }
  if ( ! defined( $uuid) || ! $uuid ) {
    Warn( "couldn't determine fs_uuid -- skip SecureBoot/grub2 config!\n");
    $Sconf{SB} = "";
    return ( "" );
  }
  $GconfFSuuid{$spec} = $uuid;
  return ( $uuid );
}
sub Gconf($) {
  my ($data) = @_;
  my @parts = ("pre", "Econf", "Xconf", "post");
  my @keys = ("label", "kernel", "ramdisk", "options", "description",
		"rootfsuuid", "bootfsuuid", "disknr", "partnr", "vmm", "cfg");
  my %S = ();
  my $re = join( '|', @parts);
  my $current = "";
  my $lines = "";
  my %Gconf;

  $re = qr{^\>\>grub\.($re|.*)\<\<}ox;

  while ( <$data> ) {
    if ( m{^__(END)__} || ($current && m{$re}o) ) {
      Info( 9, "<<$current\n$lines>>$current => $_");
      $S{$current} = $lines;
      $lines = "";
      last if ( $1 eq "END" );
    }
    if ( m{$re}o ) {
      $current = $1;
      next;
    }
    $lines .= $_;
  }

  $lines = $S{pre};
  foreach my $k ( "timeout" ) {
    my $val = (exists( $Sconf{$k})) ? $Sconf{$k} : "80";
    $val /= 10;
    $lines =~ s{\<$k\>}{$val}gm;
  }
  foreach my $k ( "grubdefault" ) {
    if (exists( $Sconf{$k})) {
      $lines =~ s{\<$k\>}{$Sconf{$k}}gm;
    } else {
      $lines =~ s{^set default='\<$k\>'$}{}gm;
    }
  }
  push @Gconf, $lines;
  Info( 8, "<<pre\n$lines>>pre\n");
  foreach my $l ( @Labels ) {
    my ($ns, $lbl) = ($l =~ m{^(\S+) (.+)$});
    %Gconf = ();
    Info( 8, "ns=$ns lbl=$lbl\n");
    if ( $ns eq "Econf" ) {
      foreach my $k ( "kernel", "ramdisk", "options", "description") {
        $Gconf{$k} = $Econf{$lbl}{$k} if (exists( $Econf{$lbl}{$k}));
      }
      $Gconf{rootfsuuid} = GconfFSuuid( $Econf{$lbl}{root});
      #TODO: $Gconf{bootfsuuid} = GconfFSuuid( "/boot");
    } elsif ( $ns eq "Xconf" ) {
      foreach my $k ( "vmm", "kernel", "cfg", "description") {
        $Gconf{$k} = $Xconf{$lbl}{$k} if (exists( $Xconf{$lbl}{$k}));
      }
      $Gconf{cfg} = $Xconf unless ( exists($Gconf{cfg}) );
    } else {
      next;
    }

    $lines = $S{$ns};
    $Gconf{label} = $lbl;
    foreach my $k ( @keys ) {
      my $val = (exists( $Gconf{$k})) ? $Gconf{$k} : "{{$k}}";
      $lines =~ s{\<$k\>}{$val}gm;
    }
    push @Gconf, $lines;
    Info( 8, "<<$lbl\n$lines>>$lbl\n");
  }
  $lines = $S{post};
  push @Gconf, $lines;
  Info( 8, "<<post\n$lines>>post\n");
}
sub Xconf() {
  my $l = "global";
  my $k = "default";
  my %Xlabels = %{$Labels{Xconf}};
  my @Xgc = ();

  push @Xgc, "[$l]\n";
  push @Xconf, "[$l]\n";
  push @Xconf, "#" if (exists( $Sconf{$k}) &&
		   ! exists( $Xconf{$Sconf{$k}}{kernel}));
  push @Xconf, "$k=$Sconf{$k}\n" if (exists( $Sconf{$k}));
  foreach my $k ( ("time-out", "gfx-mode") ) {
    push @Xgc,   "$k=$Sconf{$k}\n" if (exists( $Sconf{$k}));
    push @Xconf, "$k=$Sconf{$k}\n" if (exists( $Sconf{$k}));
  }
  push @Xgc, "\n";
  push @Xconf, "\n";
  foreach my $l ( sort { $Xlabels{$a} <=> $Xlabels{$b} } keys %Xlabels ) {
    next unless (exists( $Xconf{$l}{kernel}));
    my @Xlc = ();
    push @Xlc, "[$l]\n";
    if ( exists($Xconf{$l}{append}) ) {
      $Xconf{$l}{kernel} .= " " .  $Xconf{$l}{append};
    }
    foreach my $k ( sort( keys( %{ $Xconf{$l} })) ) {
      next if ( $k =~ m{^(?:append|description|vmm|cfg)$} );
      push @Xlc, "$k=$Xconf{$l}{$k}\n";
    }
    push @Xconf, @Xlc;
    push @Xconf, "\n";
    if ( $Xconf{$l}{cfg} ne $Xconf ) {
      my $cfg = $Xconf{$l}{cfg};
      unshift @Xlc, @Xgc;
      @{$Xsonf{$cfg}} = @Xlc;
    }
  }
}
sub Transfer ($$) {
  my( $in, $dir) = @_;
  my $c = $Sconf{'__warn-count'};

  if ( $Sconf{SB} ) {
    my $fh;
    if ( -r $GconfT ) {
      open( $fh, "< $GconfT") || Panic( 1, "$GconfT: failed to open: $!\n");
    } else {
      open( $fh, "<&DATA") || Panic( 1, "<DATA>: failed to dup: $!\n");
    }
    Gconf($fh) if ( $Sconf{SB} );
    close( $fh);
  }

  Warn( "no complete section for $Xconf!\n")
     if ( $Sconf{xencfg} && ! exists( $Labels{Xconf}) );
  Xconf() if ( exists( $Labels{Xconf}) );

  foreach ( @Files ) {
    if ( ! -r $_ ) {
      Warn( "$_: not found\n");
      $c++;
    }
  }
  if ( $c ) {
    Panic( 2, "$in: broken references\n");
  }

  Output( $dir, $Fconf, @Econf);

  # create xen.cfg
  if ( $Sconf{xencfg} ) {
    Output( $dir, $Xconf, @Xconf);
    foreach my $x ( keys( %Xsonf) ) {
      Output( $dir, $x, @{$Xsonf{$x}});
    }
  }

  # create grub.cfg
  Output( $dir, $Gconf, @Gconf) if ( $Sconf{SB} );

  $Sconf{'__warn-count'} = $c;
}

# remove old files (legacy!)
sub Purge($) {
  my( $d) = @_;

  if ( -r "$d/$Flist" ) {
    Info( 6, "## skip pattern-based removal of files from '$d'\n");
    return 0;
  }
  if ( $keep > 0) {
    Info( 1, "## skip pattern-based removal of old files from '$d'\n");
    return 0;
  }
  Info( 1, "## remove old files from '$d' by pattern\n");
  my @F = glob( "$d/*");
  foreach my $f ( @F ) {
    next if ( $f !~ m{.*/(((vm|)linu(x|z)|initrd)(|[-.]\S+)|xen.cfg)$} );
    Info( 1, "> rm $f\n");
    unlink( $f) unless ($test);
  }
}

# remove old files (list-based!)
sub Obsolete($$) {
  my( $d, $init) = @_;
  my $fh;
  my $F = "$d/$Flist";
  my $Fn = "$F.new";
  my $verb = "refresh";

  if ( $init ) {
    $verb = "establish new"; 
    # skip to end...
  } elsif ( $keep > 0 && -r $F ) {
    Info( 1, "## skip list-based removal of obsolete files from '$d'\n");
    Merge( $Fn, $F);
  } elsif ( ! -r $F ) {
    Info( 2, "## no list-based removal of obsolete files during migration\n");
  } else {
    my @obs = ();
    if ( ! open( $fh, "< $F") ) {
      Warn( "could not open '$F' for reading: $!\n");
    }
    while ( <$fh> ) {
      chomp;
      next if (m{/} || exists( $Flist{$_}));
      push @obs, $_;
    }
    close( $fh);
    Info( 1, "## remove obsolete files based on '$F'\n")
      if ( $#obs >= 0 );
    foreach ( @obs ) {
      Info( 1, "> rm $d/$_\n");
      unlink( "$d/$_") unless ($test);
    }
  }
  Info( 2, "## $verb file-list in '$d'\n");
  Rename( 2, $Fn, $F);
}

sub InstallFPSWA($) {
  my ( $d) = @_;
  my $Dfpswa = $Dlib;

  $d .= "/efi/Intel Firmware";
  $Dfpswa = $Dlibold unless ( -r "$Dfpswa/fpswa.efi" );

  return 0 unless ( -r "$Dfpswa/fpswa.efi" );

  my $head = "## fpswa: Floating Point Software Assist\n";
  if ( -d $d && -r "$d/fpswa.efi" ) {
    # check, if we need to update and failing that do nothing?!
    my $c = "$Dfpswa/fpswa-cmp-version";
    if ( -x $c ) {
      my $chk = qx{$c "$d/fpswa.efi" "$Dfpswa/fpswa.efi"};
      if ( $chk =~ /older/ ) {
	Info( 1, $head .
	      "##    Update '$d/fpswa.efi'.\n");
	Info( 2,
	      "##      $chk");
	Install( 0, "-p", "$Dfpswa/fpswa.efi", $d);
      } else {
	Info( 1, $head .
	      "##    Do NOT update '$d/fpswa.efi'.\n");
	Info( 2,
	      "##      $chk");
      }
    } else {
      use File::Compare;
      if ( compare( "$d/fpswa.efi", "$Dfpswa/fpswa.efi") == 0 ) {
	Info( 2, $head .
	      "##    Already installed.\n");
      } else {
	Info( 1, $head .
	      "##    Unable to compare versions.\n" .
	      "##      Installation skipped!\n");
      }
    }
  } else {
    Info( 1, $head . "##    Install 'fpswa.efi' to '$d'.\n");
    System( 0, "mkdir", $d) unless ( -d $d );
    Install( 0, "-p", "$Dfpswa/fpswa.efi", $d);
  }
}


sub isMounted($) {
  my ( $d) = @_;
  my @D  = stat( $d);
  my @P  = stat( $d . "/..");
  return( $D[0] != $P[0] );
}

sub MP($) {
  my ( $d) = @_;
  my @I = ("/etc/fstab", "/proc/mounts", "/etc/mtab");
  Info( 3, "### MP($d):");
  SOURCE: foreach my $f ( @I ) {
    open( IN, "< $f") || next;
    while ( <IN> ) {
      chomp;
      next if ( m{^#} );
      my @F = split;
      my $lno;
      if ( $F[1] eq $d ) {
	my $dev = $F[0];
	$dev =~ s{^UUID=}{/dev/disk/by-uuid/};
	$dev =~ s{^LABEL=}{/dev/disk/by-label/};
	$lno = $.;
	close( IN);
	while ( -l $dev ) {
	  my $t = `readlink -en "$dev"`;
	  if ( ! defined( $t) ) {
	    Info( 0, "readlink failed for line $lno in '$f'.\n");
	    next SOURCE;
	  }
	  if ( ! -b $dev ) {
	    Info( 0, "no block-device on line $lno in '$f': $dev.\n");
	    next SOURCE;
	  }
	  if ( $t =~ m{^(/dev/|(../)*)dm-[0-9a-f]+$}i ) {
	    last;
	  }
	  $dev = $t;
	}
	Info( 3, " found '$dev' in '$f' line $lno => true\n");
	return( $dev);
      }
    }
    close( IN);
  }
  Info( 3, " not found in [" . join( ", ", @I) . "] => false\n");
  return( 0);
}

sub backslash($) {
  my( $p) = @_;
  $p =~ s{\/}{\\}g;
  return ( $p );
}
sub ebc($$$$$) {
  my( $label, $dev, $part, $path, $extra) = @_;
  my @C = ("efibootmgr", "-v", "-cL", $label,
		"-d", "$dev", "-p", $part, "-l", backslash($path));
  my @out;

  if ( $extra ) {
    #push @C, "--unicode", $extra;
    push @C, "-u", $extra;
  }
  my $cmd = $C[0];
  foreach my $c ( @C[1..$#C] ) {
    if ( $c =~ /[\s\\]/ ) {
      $cmd .= " '$c'";
    } else {
      $cmd .= " $c";
    }
  }
  Info( 1, "> $cmd\n");
  return (undef()) if ( $test );

  open( EBM, "-|", @C) ;
  while (<EBM>) {
    print if ($verbose > 1);
    chomp;
    push @out, $_;
  }
  close( EBM);
  return( @out );
}
sub ebr($) {
  my( $num) = @_;
  my @C = ("efibootmgr", "-q", "-B", "-b" , sprintf( "%x", $num));

  $C[1] = "-v" if ( $verbose > 2 );
  System( 0, @C);
}
sub hwpEqual($$) {
  my( $s1, $s2) = @_;
  my $hex = qr{[0-9a-f]+}i;
  my $hexi = qr{[0-9a-f-]+}i;
  my @S1 = ($s1 =~ m{HD\(($hex),($hex),($hex),($hexi)\)}o);
  my @S2 = ($s2 =~ m{HD\(($hex),($hex),($hex),($hexi)\)}o);
  Info( 5, sprintf( "'%s' - '%s'\n", $S1[3],  $S2[3]));
  return( $s1 eq $s2 );
}
sub ebm($$$$$);
sub ebm($$$$$) {
  my( $label, $dev, $part, $path, $extra) = @_;
  my @out;
  my $entry;

  if ( ! -r "$MP$path" ) {
    #Warn( "refusing to create EBM for non-existent binary ($MP$path).\n");
    Warn( "refusing to create EBM for non-existent binary.\n");
    return unless ( $test );
    Info( 1, "#");
  }
  @out = ebc( $label, $dev, $part, $path, $extra);
  return if ( $test );

  $entry = pop @out;
  Panic( 2, "Unexpected failure of 'efibootmgr' (see elilo(8)).  Giving up!\n")
    unless (defined( $entry));
  Panic( 2, "Unexpected output from 'efibootmgr':\n  '$entry'\n")
    if ($entry !~ m{^Boot([0-9A-F]{4})[\* ] (.*?)\s+((?:HD|ACPI).+)File(.+)$}i);
  my ( $num, $lbl, $hwp, $file) = (hex($1), $2, $3, $4);
  Info( 1, sprintf( "# num=%d (0x%04X) hwp=%s\n", $num, $num, $hwp));

  foreach my $e ( @out) {
    $e =~ m{^Boot([0-9A-Fa-f]{4})[\* ] (.*?)\s+((?:HD|ACPI).+)File(.+)$} ||
	next;
    next unless ( hwpEqual( $hwp, $3) );
    if ( $file eq $4 ) {
      my $c = hex($1);
# This effort below to eliminate holes in the boot entry list voids
# the attempt to order EBM entries by simply calling '--refresh-EBM'.
# The full solution would require adding an interface to 'efibootmgr -o',
# which is unfortunately not feasible this late in the release cycle.
#     if ( $lbl eq $2 ) {
#	# delete label with higher number
#	my $n = ($num < $c) ? $c : $num;
#	ebr( $n);
#	$num = $c;
#     }  else {
#	# delete old/invalid label
#	ebr( $c);
#	if ( $num > $c ) {
#	  # now we have a hole!
#	  ebr( $num);
#	  ebm( $label, $dev, $part, $path, $extra);
#	  return;
#       }
#     }
      # delete old/invalid labels *irrespective* of holes
      ebr( $c);
    }
  }
}

sub Refresh($$) {
  my ( $device, $dir) = @_;
  my ($dev, $sep, $part, $path, $label, $ret);
  my $shim_opts = ""; #$sBinaries[1];

  # device & partition
  if ( $device =~ m{^(.*)([-_]part)(\d+)$} ) {
    $dev = $1;
    $sep = $2;
    $part = $3;
  } elsif ( $device =~ m{^(.*/[a-z0-9]+)(p)(\d+)$}i ) {
    # accept things like 'c0d0p1' or 'nvme0n0p1'
    $dev = $1;
    $sep = $2;
    $part = $3;
  } elsif ( $device =~ m{^(/dev/[a-z]+)(\d+)$}i ) {
    # accept '/dev/sda1', but refuse '/dev/dm-1'
    $dev = $1;
    $sep = "";
    $part = $2;
  } else {
    Panic( 2, "parse error on EFI partition $device.\n");
  }
  if ( ! -b $dev ) {
    Panic( 2, "EFI partition parent device $dev not found.\n");
  }
  if ( ! -b "$dev$sep$part" ) {
    Panic( 2, "EFI partition $part on device $dev not found.\n");
  }
  Info( 4, "#### dev=$dev, part=$part\n");
  # path
  $path = "/efi/$VD/";
  Info( 4, "#### path=$path\n");
  # label
  if ( exists( $Sconf{'ebm-label'}) ) {
    $label = $Sconf{'ebm-label'};
  } elsif ( exists( $Sconf{'ybm-label'}) ) {
    $label = $Sconf{'ybm-label'};
  } else {
    $label = "SUSE Linux Enterprise";
  }
  Info( 4, "#### label=$label\n");
  if ( $Sconf{SB} && ! exists($Sconf{'SB-fallback'}) &&
	! -r "$MP$path$shim" ) {
    # try to force "fallback" when primary target went missing!
    $Sconf{'SB-fallback'} = "true";
  }
  if ( ! $Sconf{SB} || exists($Sconf{'SB-fallback'}) ) {
    my $lbl = $label . ($Sconf{'SB'} ? " (fallback)" : "");
    $ret = ebm( "XEN ".$lbl, $dev, $part, $path . $xen, "")
       if ( $Sconf{xencfg} == 1 );

    $ret = ebm( $lbl, $dev, $part, $path . $elilo, "");

    $ret = ebm( "XEN ".$lbl, $dev, $part, $path . $xen, "")
       if ( $Sconf{xencfg} == 2 );
  }
  if ( $Sconf{SB} ) {
    $ret = ebm( "XEN ".$label, $dev, $part, $path . $shim, " $xen")
       if ( $Sconf{xencfg} == 1 && exists( $Sconf{'SB-direct2xen'}) );

    $ret = ebm( $label, $dev, $part, $path . $shim, $shim_opts);

    $ret = ebm( "XEN ".$label, $dev, $part, $path . $shim, " $xen")
       if ( $Sconf{xencfg} == 2 && exists( $Sconf{'SB-direct2xen'}) );
  }
}

sub CheckSB() {
  my $fh;
  my $sev = "/sys/firmware/efi/vars";
  my $sbd = "$sev/SecureBoot-8be4df61-93ca-11d2-aa0d-00e098032b8c/data";
  my $comment = "";
  $Sconf{SB} = "";
  $Sconf{'secure-boot'} = "auto" unless ( exists( $Sconf{'secure-boot'}) );
  if ( $Sconf{'secure-boot'} =~ m{^(off|false)$} ) {
    $comment = " (forced off)";
  } elsif ( $Sconf{'secure-boot'} =~ m{^(on|true|try)$} ) {
    $Sconf{SB} = "forced on";
  } elsif ( ! -r "$sbd" ) {
    $comment = " (not supported)";
  } elsif ( ! open( $fh, "< $sbd") ) {
    Warn( "$sbd: open: $!\n");
    $Sconf{SB} = "try";
    $comment = " (failed to open)";
  } else {
    my $val = <$fh>;
    if ( ! defined( $val) ) {
      Warn( "$sbd: read: $!\n");
      $Sconf{SB} = "try";
      $comment = " (failed to read)";
    } elsif ( unpack( "c", $val) == 0 ) {
      $comment = " (supported but inactive)"
    } else {
      $Sconf{SB} = "auto";
      $comment = sprintf( " (data=%d)", unpack( "c", $val)) if ($verbose > 2);
    }
  }
  Info( 2, "##  SecureBoot: '$Sconf{SB}'$comment\n");
}

my %Opt = ();
{
  use Getopt::Long;
  use Pod::Usage;
  $Getopt::Long::debug = 0;
  $Getopt::Long::ignorecase = 0;
  $Getopt::Long::bundling = 1;
  $Getopt::Long::passthrough = 0;

  pod2usage(2) unless ( GetOptions( \%Opt,
     'help|h', 'man|m', 'version|V', 'verbose|v+',
     'test|t', 'keep|k', 'purge|K', "refresh-EBM") &&
			( ! $Opt{'purge'} || ! $Opt{'keep'} ) &&
			! $Opt{'help'} );

  Version() if ( $Opt{'version'} );
  pod2usage(-exitstatus => 0, -verbose => 2) if ( $Opt{'man'} );
  pod2usage(1) if ( $Opt{'help'} );
  $test = 1 if ( $Opt{'test'} );
  $keep = 0 if ( $Opt{'purge'} );
  $keep = 1 if ( $Opt{'keep'} );
  $verbose += $Opt{'verbose'} if ( $Opt{'verbose'} );
}

# run-time init
if ( $Arch =~ m{ARCH} ) {
  chomp( $Arch = qx{uname -m});
  Info( 3, "### Arch: '$Arch'\n");
}
if ( ! $EFIarch ) {
  $EFIarch = ( $Arch eq "x86_64" ) ? "x64" : 
		( $Arch =~ m{86} ) ? "ia32" : $Arch;
  Info( 3, "### EFIarch: '$EFIarch'\n");
}
if ( $Dlib =~ m{LIBDIR} ) {
  $Dlib = "$dbg/usr/lib" . (($Arch eq "x86_64") ? "64/" : "/");
  $Dlibold = $Dlib . "elilo";
  $Dlib = $Dlib . "efi";
  $Dlib = $Dlibold if (! -r "$Dlib/elilo.efi" && -r "$Dlibold/elilo.efi");
  Info( 3, "### Dlib: '$Dlib'\n");
}

# try to read variables from $Sconf
Parse( $Sconf, ($Opt{'refresh-EBM'}&&!$Opt{test}) ? 0 : -1);

# check for Secure Boot
CheckSB();

# check environment
if ( exists( $Sconf{"efi-mountpoint"}) ) {
  $MP = $dbg . $Sconf{"efi-mountpoint"};
  Panic( 2, "EFI partition specification in $Sconf invalid.\n")
     unless ( -d $MP );  # or is it "$MP/efi"?
} elsif ( -d $MPnew . "/efi/" . $VD || MP($MPnew) ) {
  $MP = $MPnew;
} elsif ( -d $MPold . "/efi/" . $VD ) {
  $MP = $MPold;
} else {
  Info( 1, "## Neither new ($MPnew/efi/$VD) nor old ($MPold/efi/$VD)?\n");
  Panic( 2, "EFI partition not found.\n");
}
Info( 3, "### Mountpoint: '$MP'\n");

if ( exists( $Sconf{"vendor-directory"}) ) {
  $VD = $Sconf{"vendor-directory"};
  Info( 1, "## To apply changes of '$VD' run 'elilo --refresh-EBM'!\n")
     unless ( $VD =~ m{^(SuSE|boot)$}i || $Opt{'refresh-EBM'} );
}
if ( exists( $Sconf{"precious"}) && $keep < 0 ) {
  $keep = 1;
}
if ( ! isMounted( $MP) ) {
  Panic( 2, "EFI partition (". MP( $MP) .") not mounted at $MP.\n");
}


$D = $MP . "/efi/" . $VD;
Info( 2, "##  Output directory: '$D'\n");
System( 2, "mkdir", "-p", $D) unless ( -d $D );

if ( $Opt{'refresh-EBM'} ) {
  Refresh( MP( $MP), $D);
  exit 0;
}
if ( -r $Sconf ) {
  my $initializing = ( ! -r "$D/elilo.efi" && ! -r "$D/$Fconf" );
  if ( ! $test ) {
    open( LIST, "> $D/$Flist.new") ||
       Warn( "cannot open '$D/$Flist.new' for writing: $!\n");
  }
  # extract kernels, etc. and write fixed .conf
  Transfer( $Sconf, $D);
  # remove old files (legacy!)
  Purge( $D) unless ($initializing);
  # copy stuff
  Info( 1, "## copy files to '$D'\n");
  @sBinaries = () unless ( $Sconf{SB} );
  foreach ( reverse( $elilo, @sBinaries) ) {
    unshift @Files, "$Dlib/$_";
  }
  foreach ( @Files ) {
    Install( 0, "-p", $_, $D);
    addList( $_);
  }
  if ( $VD =~ m{^boot$}i ) {
    my $b = ( $Sconf{SB} ) ? $shim :  $elilo;
    $b = $xen if ($Sconf{xencfg} == 2 &&
		  (!$Sconf{SB} || exists( $Sconf{'SB-direct2xen'})));

    Install( 0, "-p", "$Dlib/$b", "$D/boot$EFIarch.efi");
    addList( "boot$EFIarch.efi");
  }
  close( LIST);
  # remove old files (list-based!)
  Obsolete( $D, $initializing);
  # take care of FPSWA
  InstallFPSWA( $MP);
} elsif ( $MP eq $MPold && -r "$D/$Fconf" ) {
  # assume old setup with only '/vmlinuz' and '/initrd'
  Install( 2, "-p", "$Dlib/elilo.efi", $D);
  InstallFPSWA( $MP);
} elsif ( $MP eq $MPold ) {
  Panic( 2, "$D/$Fconf: not found\n");
} elsif ( ! -e $Sconf ) {
  Panic( 2, "$Sconf: not found\n");
} else {
  Panic( 2, "$Sconf: not readable\n");
}

if ( $warn > 0 ) {
  Panic( 1, sprintf("%d warning%s encountered.\n", $warn, ($warn==1)?"":"s"));
}
exit( 0);

__DATA__
>>grub.pre<<
#
# DO NOT EDIT THIS FILE
#
# It is automatically generated by /sbin/elilo using
# settings from /etc/elilo.conf (and maybe /etc/default/grub)
#
### BEGIN 00 simplified header ###
if [ x"${feature_menuentry_id}" = xy ]; then
  menuentry_id_option="--id"
else
  menuentry_id_option=""
fi

if [ x${boot_once} = xtrue ]; then
  set timeout=0
elif sleep --interruptible 0 ; then
  set timeout=<timeout>
fi

set efibootdir=$prefix
set default='<grubdefault>'
### END 00 simplified header ###

### BEGIN 10 elilo ###
>>grub.Econf-full<<  # TODO: track down "disknr" and "partnr"
menuentry '<label>' --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-simple-<rootfsuuid>' {
  set root='hd<disknr>,gpt<partnr>'
  if [ x$feature_platform_search_hint = xy ]; then
    search --no-floppy --fs-uuid --set=root --hint-bios=hd<disknr>,gpt<partnr> --hint-efi=hd<disknr>,gpt<partnr> <bootfsuuid>
  else
    search --no-floppy --fs-uuid --set=root <bootfsuuid>
  fi
  set prefix=/usr/lib/grub2
  echo    'Loading <description> ...'
  linuxefi   /boot/<kernel> root=UUID=<rootfsuuid> <options>
  echo    'Loading initial ramdisk ...'
  initrdefi  /boot/<ramdisk>
}
>>grub.Econf<<
menuentry '<description>' --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-simple-<rootfsuuid>' {
  search --no-floppy --fs-uuid --set=root <rootfsuuid>
  set prefix=/usr/lib/grub2
  echo      'Loading <description> ...'
  linuxefi  $efibootdir/<kernel> root=UUID=<rootfsuuid> <options> 
  echo      'Loading initial ramdisk ...'
  initrdefi $efibootdir/<ramdisk>
}
>>grub.Xconf<<
menuentry '<description>' {
  echo        'Chainloading <vmm> (<kernel>)...'
  chainloader $efibootdir/<vmm> <vmm> -cfg=<cfg>
}
>>grub.post<<
### END 10 elilo ###
__END__

=head1 NAME

elilo - Installer for the EFI Linux Loader

=head1 SYNOPSIS

/sbin/elilo [options]

 Options:
      --refresh-EBM     refresh EFI boot menu
   -k --keep            don't purge old files
   -t --test            test only
   -v --verbose         increase verbosity
   -h --help            brief help message
      --man             full documentation
   -V --version         display version

=head1 OPTIONS

=over 8

=item B<--refresh-EBM>

Recreate EFI boot manager menu entries based on information in
C</etc/elilo.conf>.

=item B<--test>

Test only. Do not really write anything, no new boot configuration nor
kernel/initrd images.
Use together with B<-v> to find out what B<elilo> is about to do.

=item B<--verbose>

Increase level of verbosity.

=item B<--help>

Print a brief help message and exits.

=item B<--man>

Prints the manual page and exits.

=item B<--version>

Prints the version information and exits.

=back

=head1 DESCRIPTION

This program will perform all steps to transfer the
necessary parts to the appropriate locations...



=head1 LIMITATIONS

For now, I<all> image-entries are treated as "optional" in
order to more closely match the behavior of the real
loader (i.e. C<elilo.efi>), which silently ignores missing files
while reading the configuration.

This may be considered a bug by experienced B<LILO> users,
where only those specifically marked as such are treated that way.

It is planned to introduce keywords like C<mandatory> and C<optional>
in future releases though.

=head1 EFI Boot Manager Failure

Creation of EFI Boot Manager menu entries needs some space in non-volatile
memory.  This space is limited--even more so, since Linux dares using only
half of it.  Therefore C<--refresh-EBM> may fail with an C<unexpected error>.
If you encounter this, you basically have two options.  Either free up some
space (e.g. old C<dump-typeN> variables or outdated boot entries) and reboot.
(The tricky part here is to not remove vital system variables.)
Or, if you are really sure that your UEFI does sane garbage-collection and
fulfills the specification, you may use the C<efi_no_storage_paranoia> kernel
parameter.
B<But beware, using this parameter with faulty firmware may brick your board!>

Note: there are boards, which always use more than 50% of NVRAM.
Those factually leave no choice.

=head1 SEE ALSO

/usr/share/doc/packages/elilo

=cut
