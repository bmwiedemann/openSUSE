#
# spec file for package perl-Cpanel-JSON-XS
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Cpanel-JSON-XS
Name:           perl-Cpanel-JSON-XS
Version:        4.380.0
Release:        0
# 4.38 -> normalize -> 4.380.0
%define cpan_version 4.38
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        CPanel fork of JSON::XS, fast and correct serializing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Time::Piece)
Provides:       perl(Cpanel::JSON::XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be _correct_ and its secondary goal is to be _fast_. To
reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason to
write yet another JSON module? While it seems there are many JSON modules,
none of them correctly handle all corner cases, and in most cases their
maintainers are unresponsive, gone missing, or not listening to bug reports
for other reasons.

See below for the cPanel fork.

See MAPPING, below, on how Cpanel::JSON::XS maps perl values to JSON values
and vice versa.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license COPYING

%changelog
