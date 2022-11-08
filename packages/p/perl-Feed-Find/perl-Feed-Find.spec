#
# spec file for package perl-Feed-Find
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Feed-Find
Name:           perl-Feed-Find
Version:        0.13
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Syndication feed auto-discovery
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(URI)
Requires:       perl(Class::ErrorHandler)
Requires:       perl(HTML::Parser)
Requires:       perl(LWP)
Requires:       perl(URI)
%{perl_requires}

%description
_Feed::Find_ implements feed auto-discovery for finding syndication feeds,
given a URI. It (currently) passes all of the auto-discovery tests at
_http://diveintomark.org/tests/client/autodiscovery/_.

_Feed::Find_ will discover the following feed formats:

* * RSS 0.91

* * RSS 1.0

* * RSS 2.0

* * Atom

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
