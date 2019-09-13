#
# spec file for package perl-Device-SerialPort
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Device-SerialPort
%define cpan_name Device-SerialPort
Version:        1.04
Release:        8
Provides:       %cpan_name
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://search.cpan.org/dist/Device-SerialPort/
Summary:        Linux/POSIX emulation of Win32::SerialPort functions
Source:         %cpan_name-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
This module provides an object-based user interface essentially identical
to the one provided by the Win32::SerialPort module.

%prep
%setup -q -n %cpan_name-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
make

%check
make test

%install
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
# clean up the hard disc after build
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/modemtest
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Device
%{perl_vendorarch}/auto/Device
%doc Changes MANIFEST README TODO

%changelog
