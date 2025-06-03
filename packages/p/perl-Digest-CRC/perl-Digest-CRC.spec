#
# spec file for package perl-Digest-CRC
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


%define cpan_name Digest-CRC
Name:           perl-Digest-CRC
Version:        0.240.0
Release:        0
# 0.24 -> normalize -> 0.240.0
%define cpan_version 0.24
#Upstream:  CRC algorithm code taken from "A PAINLESS GUIDE TO CRC ERROR DETECTION ALGORITHMS". the public domain.
License:        SUSE-Public-Domain
Summary:        Generic CRC functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Digest::CRC) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The *Digest::CRC* module calculates CRC sums of all sorts. It contains
wrapper functions with the correct parameters for CRC-CCITT, CRC-16, CRC-32
and CRC-64, as well as the CRC used in OpenPGP's ASCII-armored checksum.

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
