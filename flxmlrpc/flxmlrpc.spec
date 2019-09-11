#
# spec file for package flxmlrpc
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


%define sover 1
Name:           flxmlrpc
Version:        0.1.4
Release:        0
Summary:        An implementation of the XMLRPC protocol
License:        LGPL-3.0+
Group:          Productivity/Hamradio/Other
Url:            https://sourceforge.net/projects/fldigi/
#Git-Clone:     https://git.code.sf.net/p/fldigi/flxmlrpc
Source:         http://downloads.sourceforge.net/project/fldigi/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
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
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libflxmlrpc%{sover} -p /sbin/ldconfig
%postun -n libflxmlrpc%{sover} -p /sbin/ldconfig

%files -n libflxmlrpc%{sover}
%defattr(-,root,root)
%doc README COPYING AUTHORS NEWS
%{_libdir}/libflxmlrpc.so.%{sover}*

%files devel
%defattr(-,root,root)
%{_includedir}/flxmlrpc
%{_libdir}/libflxmlrpc.so
%{_libdir}/pkgconfig/flxmlrpc.pc

%changelog
