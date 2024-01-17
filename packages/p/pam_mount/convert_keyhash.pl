#!/usr/bin/perl -w
#
#       convert tool for pam_mount.conf.xml
#
#       Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#       This file is under the same license as pam_mount itself.
#
#       Please submit bugfixes or comments via http://bugs.opensuse.org/
#
use Data::Dumper;
use Getopt::Long;
use IO::File;
use XML::Writer;
use XML::Parser;
use File::Temp qw/ tempfile /;
use File::Copy;
use strict;

my $OLD_CONF = "/etc/security/pam_mount.conf.xml";
my ($TMPFH, $TEMPNAME) = tempfile("pam_mount_conf.XXXXXXXX", DIR => "/tmp/", UNLINK => 1);
my $BAK = "";
my $debug = 0;
my $hasChanges = 0;
my $node = {};
$node->{element} = "";
$node->{attrs}   = {};
$node->{chars}   = "";
$node->{isEmpty} = 1;


Getopt::Long::Configure(qw(bundling));
GetOptions(
        "i=s" => \$OLD_CONF,
        "d"   => \$debug,
);

if( ! -e "$OLD_CONF" )
{
    print STDERR "$OLD_CONF: file not found.\n";
    exit 1;
}

$BAK = "$OLD_CONF";
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon  += 1;
$year += 1900;
$BAK .= ".$year-$mon-$mday";


sub handle_decl_tag
{
    my $wrt = shift;
    my( $expat, $version, $encoding, $standalone ) = @_;

    $wrt->xmlDecl($encoding, $standalone);
    $wrt->raw("\n\n");
    print "write xmlDecl with $encoding\n" if($debug);
}

sub handle_start_tag
{
    my $wrt = shift;
    my( $expat, $element, %attrs ) = @_;

    if($node->{element} ne "" && !$node->{drop})
    {
        # subnode write the old one first
        $wrt->startTag($node->{element}, %{$node->{attrs}});
        print "write starttag of $node->{element}\n" if($debug);
        if($node->{chars} ne "")
        {
            $wrt->characters($node->{chars});
            print "write characters\n" if($debug);
        }
        $wrt->raw("\n");
        $node->{element} = "";
        $node->{attrs}   = {};
        $node->{chars}   = "";
        $node->{isEmpty} = 1;
    }

    if(lc($element) eq "volume" && ! exists $attrs{fskeyhash})
    {
        print "!!! set fskeyhash to MD5\n" if($debug);
        $attrs{fskeyhash} = "md5";
        $hasChanges = 1;
    }
    
    if(lc($element) eq "volume" ||
       lc($element) eq "pam_mount" ||
       lc($element) eq "debug" ||
       lc($element) eq "luserconf" ||
       lc($element) eq "mntoptions" ||
       lc($element) eq "path" ||
       lc($element) eq "logout" ||
       lc($element) eq "mkmountpoint"
      )
    {
        $node->{drop} = 0;
    }
    else
    {
        $node->{drop} = 1;
    }
    
    $node->{element} = $element;
    $node->{attrs}   = \%attrs;
    $node->{chars}   = "";
    $node->{isEmpty} = 1;
}

sub handle_char_tag
{
    my $wrt = shift;
    my( $expat, $string ) = @_;
    
    $node->{chars} .= $string;
    $node->{isEmpty} = 0;
}

sub handle_end_tag
{
    my $wrt = shift;
    my( $expat, $element ) = @_;

    if(!$node->{drop} && $element eq $node->{element})
    {
        if($node->{isEmpty})
        {
            $wrt->emptyTag($node->{element}, %{$node->{attrs}});
            $wrt->raw("\n");
            print "write emptytag of $node->{element}\n" if($debug);
        }
        else
        {
            $wrt->startTag($node->{element}, %{$node->{attrs}});
            print "write starttag of $node->{element}\n" if($debug);
            if($node->{chars} ne "")
            {
                $wrt->characters($node->{chars});
                print "write characters\n" if($debug);
            }
            $wrt->endTag($node->{element});
            $wrt->raw("\n");
            print "write endtag of $node->{element}\n" if($debug);
        }
    }
    elsif($element ne $node->{element})
    {
        $wrt->endTag($element);
        print "write endtag of $element\n" if($debug);
    }
    $node->{element} = "";
    $node->{attrs}   = {};
    $node->{chars}   = "";
    $node->{isEmpty} = 1;
}


my $writer = new XML::Writer(OUTPUT => $TMPFH, UNSAFE => 1);
my $parser = XML::Parser->new( Handlers =>
                               { XMLDecl => sub { handle_decl_tag($writer, @_) }, 
                                 Start   => sub { handle_start_tag($writer, @_) },
                                 Char    => sub { handle_char_tag($writer, @_) },
                                 End     => sub { handle_end_tag($writer, @_) },
                               });
$parser->parsefile( $OLD_CONF );

$TMPFH->close();

if($hasChanges)
{
    print "Changes made. $OLD_CONF => $BAK\n" if($debug);
    copy( $OLD_CONF, $BAK );
    print "$TEMPNAME => $OLD_CONF \n" if($debug);
    copy( $TEMPNAME, $OLD_CONF );
}
else
{
    print "No changes made. Keeping $OLD_CONF.\n" if($debug);
}

exit 0;

