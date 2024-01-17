#
# spec file for package perl-Devel-CoreStack
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

# norootforbuild


Name:           perl-Devel-CoreStack
BuildRequires:  gdb perl
BuildRequires:  perl-macros
Version:        1.3
Release:        289
Provides:       Devel-CoreStack
AutoReqProv:    on
Group:          Development/Languages/Perl
License:        Artistic-1.0
Url:            http://cpan.org/modules/by-module/Devel/
Source:         Devel-CoreStack-%{version}.tar.gz 
Summary:        try to generate a stack dump from a core file
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This module attempts to generate a stack dump from a core file by
locating the best available debugger (if any) and running it with the
appropriate arguments and command script.



Authors:
--------
    Alligator Descartes <descarte@hermetica.com>
    Tim Bunce

%prep 
%setup -n Devel-CoreStack-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags} all
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/Devel
%{perl_vendorlib}/Devel

%changelog
