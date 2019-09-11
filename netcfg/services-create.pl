#!/usr/bin/perl -w

use strict;
use utf8;
use XML::LibXML::Reader;

binmode( STDOUT, 'utf8:' );

my $portsurl = 'http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml';
my $servicesfile = 'services.new';
my $reader = XML::LibXML::Reader->new(location => $portsurl)
         or die "cannot read $portsurl\n";
open(SERVICESNEW, ">$servicesfile") or die "cannot write $servicesfile\n";
binmode(SERVICESNEW, 'utf8:');

while ($reader->read) {
  processNode($reader);
}

sub processNode 
{
  my $reader = shift;

  if ($reader->name eq 'title' and $reader->nodeType == 1) 
  { 
    $reader->read; 
    my $title = $reader->value;
    $title =~ tr/a-z/A-Z/;
    print SERVICESNEW "#\n",
                      "# ", $title, "\n",
                      "#\n"; 
  }
  elsif ($reader->name eq 'updated' and $reader->nodeType == 1 and $reader->depth == 1) 
  { 
    $reader->read; 
    print SERVICESNEW "# (last updated on ", $reader->value, ")\n",
                      "#\n",
                      "# "; 
  }
  elsif ($reader->name eq 'note' and $reader->nodeType == 1) 
  { 
    $reader->read; 
    while ($reader->depth != 1)
    { 
      if ($reader->name eq '#text')
      { 
        my $text = $reader->value; 
        $text =~ s/\n/\n# /g;
        print SERVICESNEW $text; 
      }
      elsif ($reader->name eq 'xref')
      { 
        my $xref = $reader->getAttribute('data'); 
        $xref =~ tr/a-z/A-Z/;
        printf SERVICESNEW "[%s]", $xref;
      }
      $reader->read;
    }
    print  SERVICESNEW "\n";
    print  SERVICESNEW "#\n";
    printf SERVICESNEW "# %-18s %-12s %s\n", ('Service Name', 'Port/Proto', 'Description, Update Date, References');
    printf SERVICESNEW "# %-18s %-12s %s\n", ('------------', '----------', '------------------------------------');
    print  SERVICESNEW "#\n";
  }
  elsif ($reader->name eq 'record')
  {
    my $name = "";
    my $number = "";
    my $protocol = "";
    my $description = "";
    my $updated = $reader->getAttribute('updated');
    my $xrefs = "";
    $reader->read;

    if (defined $updated)
    { $updated = "(updated $updated)"; }
    else
    { $updated = ""; }
    

    while ($reader->depth != 1)
    {
      my $property = $reader->name;
      if ($property eq 'name' and $reader->nodeType == 1) # not take ending tag into account <name> </name>
      { $reader->read; $name = $reader->value; }
      elsif ($property eq 'number' and $reader->nodeType == 1)
      { $reader->read; $number = $reader->value; }
      elsif ($property eq 'protocol' and $reader->nodeType == 1)
      { $reader->read; $protocol = $reader->value; }
      elsif ($property eq 'description' and $reader->nodeType == 1)
      { 
        if (not $reader->isEmptyElement) # sometimes happen <description /> 
        { 
          $reader->read;
          while ($reader->depth == 3)  # sometimes happen <description>.* <br/><br/> .*</description>; <br/> --> ';'
          {
            if ($reader->name eq '#text')
            {  $description = $description.$reader->value." "; }
            elsif ($reader->name eq 'br')
            { $description = $description.";"; }
            $reader->read;
          }
        }
      }
      elsif ($property eq 'xref' and $reader->nodeType == 1)
      {
        my $xref = $reader->getAttribute('data');
        if (defined $xref)
        {
          my $xreftype = $reader->getAttribute('type');
          if ($xreftype eq 'rfc')
          { $xref =~ tr/a-z/A-Z/; }

          $xrefs = "$xrefs [$xref]";
        }
      }
      $reader->read
    }

    my $comment = $description.$updated.$xrefs;
    if ($name eq "")
    { $name = "#"; }
    elsif ($comment)
    { 
      $comment =~ s/\n/ /g;
      $comment = "# $comment"; 
    }
    
    my $numproto;
    if ($number and $protocol)
    {
      my ($from, $to) = split('-', $number); # handle intervals
      if (not $to)
      { $to = $from; }
      for (my $i = $from; $i <= $to; $i++)
      {
        $numproto  = "$i/$protocol";  # to print with %-12s
        printf SERVICESNEW "%-18s %-12s %s\n", ($name, $numproto, $comment);
      }
    }
  }
  elsif ($reader->name eq 'people' and $reader->nodeType == 1)
  {
    #print  SERVICESNEW "#\n";
    #print  SERVICESNEW "# PEOPLE\n";
    #print  SERVICESNEW "#\n";
    #printf SERVICESNEW "# %-25s%-25s%-25s%s\n", ('ID', 'Name', 'Organization', 'Contact');
    #printf SERVICESNEW "# %-25s%-25s%-25s%s\n", ('--', '----', '------------', '-------');
    #print  SERVICESNEW "#\n";
  }
  elsif ($reader->name eq 'person')
  {
    my $xref = $reader->getAttribute('id');
    my $name = "";
    my $org = "";
    my $uri = "";

    $reader->read;    
    while ($reader->depth != 2)
    {
      if ($reader->name eq 'name' and $reader->nodeType == 1)
      { $reader->read; $name = $reader->value; }
      if ($reader->name eq 'org' and $reader->nodeType == 1)
      { $reader->read; $org = $reader->value; }
      if ($reader->name eq 'uri' and $reader->nodeType == 1)
      { $reader->read; $uri = $reader->value; }
 
      $reader->read;
    }

    #printf SERVICESNEW "# %-25s%-25s%-25s%s\n", ($xref, $name, $org, $uri);
  }
}

close(SERVICESNEW);

