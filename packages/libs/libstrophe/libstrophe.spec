#
# spec file for package libstrophe
#
# Copyright (c) 2020 SUSE LLC
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


%define c_lib   libstrophe0
Name:           libstrophe
Version:        0.10.0
Release:        0
Summary:        A XMPP library for C
License:        GPL-3.0-or-later OR MIT
Group:          Development/Libraries/C and C++
URL:            http://strophe.im/libstrophe/
Source0:        https://github.com/strophe/%{name}/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Strophe is a collection of libraries for speaking the XMPP protocol.

While most XMPP libraries and implementations are focused on chat-based applications,
Strophe takes a grander view.

It has been used to implement real-time games, notification systems, search engines,
as well as traditional instant messaging.

The implementations are production ready, well documented,
easy to use, and easy to extend.

%package -n libstrophe-devel
Summary:        Development files for libstrophe
Group:          Development/Libraries/C and C++ 
Requires:       libstrophe0 = %{version}

%description -n libstrophe-devel
Development files and headers for libstrophe

%package -n %{c_lib}
Summary:        A XMPP library for C
Group:          System/Libraries

%description -n %{c_lib}
The libstrophe library is a XMPP library written in C.

%prep
%setup -q

%build
mkdir m4
./bootstrap.sh
%configure --disable-static --with-libxml2
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libstrophe.la

%post -n libstrophe0 -p /sbin/ldconfig
%postun -n libstrophe0 -p /sbin/ldconfig

%files -n libstrophe0
%license COPYING
%doc ChangeLog README
%{_libdir}/libstrophe.so.*

%files -n libstrophe-devel
%{_libdir}/libstrophe.so
%{_includedir}/strophe.h
%{_libdir}/pkgconfig/libstrophe.pc

%changelog
