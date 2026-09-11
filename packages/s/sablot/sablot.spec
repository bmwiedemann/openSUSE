#
# spec file for package sablot
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


Name:           sablot
Version:        1.0.3
Release:        0
Summary:        XSL Processor
License:        GPL-2.0-or-later
URL:            http://www.gingerall.com/charlie/ga/xml/p_sab.xml
Source:         http://sourceforge.net/projects/sablotron/files/sablotron-%{version}/Sablot-%{version}.tar.gz
Patch0:         %{name}-%{version}-newautoconf.diff
Patch1:         %{name}-%{version}-gcc3.diff
Patch2:         %{name}-%{version}-delete.diff
Patch3:         %{name}-%{version}-cxx20.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
Provides:       sablotron

%description
Sablotron is an XSL processor fully implemented in C++. The excellent
Expat parser is used as the associated XML parser.

%package devel
Summary:        Header Files and Libraries for Sablot Development
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel

%description devel
Header files and libraries needed for sablot development.

%prep
%autosetup -p0 -n Sablot-%{version}

%build
chmod 644 README
touch COPYING NEWS AUTHORS ChangeLog
autoreconf -fiv
%configure --disable-static --with-pic
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets

%files
%doc README
%{_bindir}/sabcmd
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/sabcfg.h
%{_includedir}/sabdbg.h
%{_includedir}/sablot.h
%{_includedir}/sdom.h
%{_includedir}/shandler.h
%{_includedir}/sxpath.h
%{_libdir}/*.so
%{_bindir}/sablot-config

%changelog
