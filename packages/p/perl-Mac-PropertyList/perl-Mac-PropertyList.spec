#
# spec file for package perl-Mac-PropertyList
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Mac-PropertyList
Name:           perl-Mac-PropertyList
Version:        1.502
Release:        0
Summary:        Work with Mac plists at a low level
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(XML::Entities)
BuildRequires:  perl(parent)
Requires:       perl(XML::Entities)
Requires:       perl(parent)
%{perl_requires}

%description
This module is a low-level interface to the Mac OS X Property List (plist)
format in either XML or binary. You probably shouldn't use this in
applications–build interfaces on top of this so you don't have to put all
the heinous multi-level object stuff where people have to look at it.

You can parse a plist file and get back a data structure. You can take that
data structure and get back the plist as XML. If you want to change the
structure inbetween that's your business. :)

You don't need to be on Mac OS X to use this. It simply parses and
manipulates a text format that Mac OS X uses.

If you need to work with the old ASCII or newer JSON formet, you can use
the *plutil* tool that comes with MacOS X:

	% plutil -convert xml1 -o ExampleBinary.xml.plist ExampleBinary.plist

Or, you can extend this module to handle those formats (and send a pull
request).

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples
%license LICENSE

%changelog
