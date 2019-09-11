#
# spec file for package perl-pcsc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name pcsc-perl
Name:           perl-pcsc
Version:        1.4.14
Release:        0
Summary:        Perl interface to Smart Card Reader
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source:         http://ludovic.rousseau.free.fr/softwares/pcsc-perl/%{cpan_name}-%{version}.tar.bz2
Source1:        http://ludovic.rousseau.free.fr/softwares/pcsc-perl/%{cpan_name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpcsclite)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1130
BuildRequires:  perl-macros
Requires:       perl-base = %{perl_version}
%{perl_requires}
%else
Requires:       perl = %{perl_version}
%endif

%description
PC/SC represents an abstraction layer to smart card readers. It
provides a communication layer with a wide variety of smart card
readers through a standardized API.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
# No daemon and no card in the sysroot => no test.
#make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%if 0%{?suse_version} > 1130
%perl_gen_filelist
%else
touch %{name}.files
%endif

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changelog LICENCE README
%if 0%{?suse_version} <= 1130
%{perl_vendorarch}/Chipcard
%{perl_vendorarch}/auto/Chipcard
%doc %{_mandir}/man3/*
%{_localstatedir}/adm/perl-modules/%{name}
%endif

%changelog
