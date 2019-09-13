#
# spec file for package sablot
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sablot
Version:        1.0.3
Release:        0
Summary:        XSL Processor
License:        GPL-2.0+
Group:          Productivity/Publishing/XML
Url:            http://www.gingerall.com/charlie/ga/xml/p_sab.xml
Source:         http://sourceforge.net/projects/sablotron/files/sablotron-%{version}/Sablot-%{version}.tar.gz
Patch0:         %{name}-%{version}-newautoconf.diff
Patch1:         %{name}-%{version}-gcc3.diff
Patch2:         %{name}-%{version}-delete.diff
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  libtool
Provides:       sablotron
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sablotron is an XSL processor fully implemented in C++. The excellent
Expat parser is used as the associated XML parser.

%package devel
Summary:        Header Files and Libraries for Sablot Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Provides:       sablotd
Obsoletes:      sablotd

%description devel
Header files and libraries needed for sablot development.

%prep
%setup -q -n Sablot-%{version}
%patch0
%patch1
%patch2

%build
chmod 644 README
touch COPYING NEWS AUTHORS ChangeLog
autoreconf -fiv
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%{_bindir}/sabcmd
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%attr(644,root,root) %{_includedir}/*
%{_libdir}/*.so
%{_bindir}/sablot-config

%changelog
