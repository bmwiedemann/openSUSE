#
# spec file for package perl-Crypt-UnixCrypt_XS
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Crypt-UnixCrypt_XS
Name:           perl-Crypt-UnixCrypt_XS
Version:        0.110.0
Release:        0
# 0.11 -> normalize -> 0.110.0
%define cpan_version 0.11
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl xs interface for a portable traditional  F<crypt> function.
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BORISZ/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Crypt::UnixCrypt_XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements the DES-based Unix _crypt_ function. For those who
need to construct non-standard variants of _crypt_, the various building
blocks used in _crypt_ are also supplied separately.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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

%changelog
