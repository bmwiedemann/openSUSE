#
# spec file for package perl-WWW-Shorten
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


%define cpan_name WWW-Shorten
Name:           perl-WWW-Shorten
Version:        3.094
Release:        0
Summary:        Interface to URL shortening sites
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.4
BuildRequires:  perl(LWP::UserAgent) >= 5.835
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny) >= 0.24
Requires:       perl(Getopt::Long) >= 2.4
Requires:       perl(LWP::UserAgent) >= 5.835
Requires:       perl(Try::Tiny) >= 0.24
%{perl_requires}

%description
A Perl interface to various services that shorten URLs. These sites
maintain databases of long URLs, each of which has a unique identifier.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# MANUAL no testing (needs network)
#make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
