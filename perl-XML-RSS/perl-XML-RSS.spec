#
# spec file for package perl-XML-RSS
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-XML-RSS
Version:        1.60
Release:        0
%define cpan_name XML-RSS
Summary:        Creates and Updates Rss Files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-RSS/
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
that allow you to generate HTML from an RSS, convert between 0.9, 0.91, and
1.0 version, and other nifty things. This might be helpful if you want to
include news feeds on your Web site from sources like Slashdot and
Freshmeat or if you want to syndicate your own content.

XML::RSS currently supports 0.9, 0.91, and 1.0 versions of RSS. See
http://backend.userland.com/rss091 for information on RSS 0.91. See
http://www.purplepages.ie/RSS/netscape/rss0.90.html for RSS 0.9. See
http://web.resource.org/rss/1.0/ for RSS 1.0.

RSS was originally developed by Netscape as the format for Netscape
Netcenter channels, however, many Web sites have since adopted it as a
simple syndication format. With the advent of RSS 1.0, users are now able
to syndication many different kinds of content including news headlines,
threaded messages, products catalogs, etc.

*Note:* In order to parse and generate dates (such as 'pubDate' and
'dc:date') it is recommended to use DateTime::Format::Mail and
DateTime::Format::W3CDTF , which is what XML::RSS uses internally and
requires.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
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
