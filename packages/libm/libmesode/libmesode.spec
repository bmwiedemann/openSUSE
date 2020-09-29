#
# spec file for package libmesode
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


%define c_lib   libmesode0
Name:           libmesode
Version:        0.10.0
Release:        0
Summary:        An XMPP library for C
License:        GPL-3.0-or-later OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/profanity-im/libmesode
Source0:        https://github.com/profanity-im/%{name}/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libexpat-devel >= 2.0.0
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mesode is a collection of libraries for speaking the XMPP protocol.
It focus extends chat-based applications; it has has been used to
implement real-time games, notification systems, and search engines.

%package -n libmesode-devel
Summary:        Development files for libmesode, an XMPP library
Group:          Development/Libraries/C and C++
Requires:       libmesode0 = %{version}

%description -n libmesode-devel
Mesode is a collection of libraries for speaking the XMPP protocol.

This package contains the development files and headers for libmesode.

%package -n %{c_lib}
Summary:        An XMPP library for C
Group:          System/Libraries

%description -n %{c_lib}
Mesode is a collection of libraries for speaking the XMPP protocol.
It focus extends chat-based applications; it has has been used to
implement real-time games, notification systems, and search engines.

%prep
%setup -q

%build
mkdir m4
./bootstrap.sh
%configure --disable-static --with-libxml2
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/libmesode.la

%post -n libmesode0 -p /sbin/ldconfig

%postun -n libmesode0 -p /sbin/ldconfig

%files -n libmesode0
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_libdir}/libmesode.so.*

%files -n libmesode-devel
%defattr(-,root,root)
%{_libdir}/libmesode.so
%{_includedir}/mesode.h
%{_libdir}/pkgconfig/libmesode.pc

%changelog
