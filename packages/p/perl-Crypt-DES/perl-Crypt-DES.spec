#
# spec file for package perl-Crypt-DES
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Crypt-DES
Name:           perl-Crypt-DES
Version:        2.90.0
Release:        0
# 2.09 -> normalize -> 2.90.0
%define cpan_version 2.09
#Upstream:  of, Eric Young (eay@mincom.oz.au). Other parts of the perl extension and Cross-platform work and packaging for single algorithm distribution is
License:        BSD-3-Clause
Summary:        Perl DES encryption module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Crypt::DES) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The module implements the Crypt::CBC interface, which has the following
methods

* blocksize

* keysize

* encrypt

* decrypt

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes COPYRIGHT README SECURITY.md

%changelog
