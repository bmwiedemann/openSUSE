#
# spec file for package libjreen-qt5
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 1
Name:           libjreen-qt5
Version:        1.3.0
Release:        0
Summary:        Qt Jabber/XMPP library
License:        LGPL-3.0-or-later
Group:          System/Libraries
URL:            http://github.com/euroelessar/jreen
Source:         v%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- fix-build-with-Qt-5_11.patch
Patch0:         fix-build-with-Qt-5_11.patch
BuildRequires:  cmake
BuildRequires:  libgsasl-devel
BuildRequires:  pkgconfig
BuildRequires:  speex-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Xml)

%description
Qt Jabber/XMPP extensible library.

%package -n libjreen-qt5-%{soname}
Summary:        Qt Jabber/XMPP library
Group:          System/Libraries

%description -n libjreen-qt5-%{soname}
Qt Jabber/XMPP extensible library.

%package -n libjreen-qt5-devel
Summary:        Qt Jabber/XMPP library
Group:          Development/Libraries/C and C++
Requires:       libjreen-qt5-%{soname} = %{version}

%description -n libjreen-qt5-devel
Qt Jabber/XMPP extensible library.

%prep
%autosetup -p1 -n jreen-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=None

%make_jobs

%install
%cmake_install

%post   -n libjreen-qt5-%{soname} -p /sbin/ldconfig
%postun -n libjreen-qt5-%{soname} -p /sbin/ldconfig

%files -n libjreen-qt5-%{soname}
%license COPYING*
%doc AUTHORS ChangeLog README.md
%{_libdir}/libjreen-qt5.so.%{soname}
%{_libdir}/libjreen-qt5.so.%{soname}.*

%files -n libjreen-qt5-devel
%license COPYING*
%{_includedir}/jreen-qt5/
%{_libdir}/libjreen-qt5.so
%{_libdir}/pkgconfig/libjreen-qt5.pc

%changelog
