#
# spec file for package flxmlrpc
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 1
Name:           flxmlrpc
Version:        1.0.1
Release:        0
Summary:        An implementation of the XMLRPC protocol
License:        LGPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://sourceforge.net/projects/fldigi/
#Git-Clone:     https://git.code.sf.net/p/fldigi/flxmlrpc
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
An implementation of the XMLRPC protocol written in C++, based upon XmlRpc++0.7
and modified to provide additional XMLRPC variable types. It is used in
fldigi, flrig, flnet, flmsg, flarq, flamp, fllog,
a suite of programs written for amateur radio emergency communications.
Both client and server objects can be used in applications for
peer-to-peer support.

%package -n libflxmlrpc%{sover}
Summary:        An implementation of the XMLRPC protocol
Group:          Development/Libraries/Other

%description -n libflxmlrpc%{sover}
An implementation of the XMLRPC protocol written in C++, based upon XmlRpc++0.7
and modified to provide additional XMLRPC variable types. It is used in
fldigi, flrig, flnet, flmsg, flarq, flamp, fllog,
a suite of programs written for amateur radio emergency communications.
Both client and server objects can be used in applications for
peer-to-peer support.

%package devel
Summary:        Flxmlrpc development libraries
Group:          Development/Libraries/Other
Requires:       libflxmlrpc%{sover} = %{version}

%description devel
An implementation of the XMLRPC protocol written in C++, based upon XmlRpc++0.7
and modified to provide additional XMLRPC variable types. It is used in
fldigi, flrig, flnet, flmsg, flarq, flamp, fllog,
a suite of programs written for amateur radio emergency communications.

%prep
%setup -q
sed -i 's/\r$//' COPYING

%build
sh autogen.sh
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libflxmlrpc%{sover} -p /sbin/ldconfig
%postun -n libflxmlrpc%{sover} -p /sbin/ldconfig

%files -n libflxmlrpc%{sover}
%license COPYING
%doc README AUTHORS NEWS
%{_libdir}/libflxmlrpc.so.%{sover}*

%files devel
%{_includedir}/flxmlrpc
%{_libdir}/libflxmlrpc.so
%{_libdir}/pkgconfig/flxmlrpc.pc

%changelog
