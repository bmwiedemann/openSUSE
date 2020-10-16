#
# spec file for package perl-XML-RSS
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-XML-RSS
Version:        1.62
Release:        0
%define cpan_name XML-RSS
Summary:        Creates and updates RSS files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::Parser)
Requires:       perl(DateTime::Format::Mail)
Requires:       perl(DateTime::Format::W3CDTF)
Requires:       perl(HTML::Entities)
Requires:       perl(XML::Parser)
%{perl_requires}

%description
This module provides a basic framework for creating and maintaining RDF
Site Summary (RSS) files. This distribution also contains many examples
that allow you to generate HTML from an RSS, convert between 0.9, 0.91,
1.0, and 2.0 version, and other nifty things. This might be helpful if you
want to include news feeds on your Web site from sources like Slashdot and
Freshmeat or if you want to syndicate your own content.

XML::RSS currently supports versions at http://www.rssboard.org/rss-0-9-0,
at http://www.rssboard.org/rss-0-9-1, at http://web.resource.org/rss/1.0/,
and at http://www.rssboard.org/rss-2-0 of RSS.

RSS was originally developed by Netscape as the format for Netscape
Netcenter channels, however, many Web sites have since adopted it as a
simple syndication format. With the advent of RSS 1.0, users are now able
to syndication many different kinds of content including news headlines,
threaded messages, products catalogs, etc.

*Note:* In order to parse and generate dates (such as 'pubDate' and
'dc:date') it is recommended to use DateTime::Format::Mail and
DateTime::Format::W3CDTF , which is what XML::RSS uses internally and
requires. It should also be possible to pass DateTime objects which will be
formatted accordingly. E.g:

    use DateTime ();

    my $dt = DateTime->from_epoch(epoch => 1_500_000_000);

    $rss->channel(
        pubDate => $dt,
        .
        .
        .
    );

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README TODO
%license LICENSE

%changelog
