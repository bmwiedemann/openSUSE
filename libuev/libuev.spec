#
# spec file for package libuev
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


%define sover 2
Name:           libuev
Version:        2.3.0
Release:        0
Summary:        Event loop library
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/troglobit/libuev/
Source:         https://github.com/troglobit/libuev/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libuEv is an event loop in the style of libevent, libev and the Xt(3)
event loop. It has a small feature set.

libuEv is built on top of the Linux APIs epoll, timerfd and signalfd.
Note however, a certain amount of care is needed when dealing with
APIs that employ signalfd.

%package -n libuev%{sover}
Summary:        Event loop library
Group:          System/Libraries

%description -n libuev%{sover}
libuEv is an event loop in the style of libevent, libev and the Xt(3)
event loop. It has a small feature set.

libuEv is built on top of the Linux APIs epoll, timerfd and signalfd.
Note however, a certain amount of care is needed when dealing with
APIs that employ signalfd.

%package devel
Summary:        Header files for libuEv
Group:          Development/Libraries/C and C++
Requires:       libuev%{sover} = %{version}

%description devel
Development and header files for libuEv.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}/%{_datadir}/doc

%post   -n libuev%{sover} -p /sbin/ldconfig
%postun -n libuev%{sover} -p /sbin/ldconfig

%files -n libuev%{sover}
%doc API.md AUTHORS ChangeLog.md README.md
%license LICENSE
%{_libdir}/libuev.so.%{sover}*

%files devel
%{_includedir}/uev
%{_libdir}/libuev.so
%{_libdir}/pkgconfig/libuev.pc

%changelog
