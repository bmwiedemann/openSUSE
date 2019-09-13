#
# spec file for package net6
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           net6
Version:        1.3.14
Release:        0
Summary:        Network access framework for IPv4/IPv6
License:        LGPL-2.1+
Group:          Development/Libraries/GNOME
Url:            http://gobby.0x539.de/
Source:         http://releases.0x539.de/net6/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM net6-gnutls30.patch zaitor@opensuse.org -- Fix build with gnutls30, patch taken from Arch linux.
Patch0:         net6-gnutls30.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{name}-lang = %{version}

%description
net6 is a library which eases the development of network-based
applications as it provides a TCP protocol abstraction for C++. It is
portable to both the Windows and Unix-like platforms.

%package devel
Summary:        Network access framework for IPv4/IPv6
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       gnutls-devel
Requires:       libsigc++2-devel

%description devel
net6 is a library which eases the development of network-based
applications as it provides a TCP protocol abstraction for C++. It is
portable to both the Windows and Unix-like platforms.

%lang_package
%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static --with-pic
make %{?jobs:-j%jobs}

%install
%makeinstall
%find_lang %{name}
%fdupes $RPM_BUILD_ROOT
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files lang -f %{name}.lang

%files devel
%defattr (-, root, root)
%{_includedir}/net6
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
