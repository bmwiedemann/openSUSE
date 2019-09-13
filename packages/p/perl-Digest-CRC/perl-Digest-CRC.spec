#
# spec file for package perl-Digest-CRC
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Digest-CRC
Version:        0.21
Release:        0
#Upstream:  CRC algorithm code taken from "A PAINLESS GUIDE TO CRC ERROR DETECTION ALGORITHMS". the public domain.
%define cpan_name Digest-CRC
Summary:        Generic CRC functions
License:        SUSE-Public-Domain
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Digest-CRC/
Source0:        http://www.cpan.org/authors/id/O/OL/OLIMAUL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The *Digest::CRC* module calculates CRC sums of all sorts. It contains
wrapper functions with the correct parameters for CRC-CCITT, CRC-16, CRC-32
and CRC-64, as well as the CRC used in OpenPGP's ASCII-armored checksum.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
