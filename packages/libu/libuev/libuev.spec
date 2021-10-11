#
# spec file for package libuev
#
# Copyright (c) 2021 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 3
Name:           libuev
Version:        2.4.0
Release:        0
Summary:        Event loop library
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/troglobit/libuev/
Source:         https://github.com/troglobit/libuev/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
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
%autosetup -p1

%build
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -r %{buildroot}%{_datadir}/doc

%check
%make_build check

%post   -n libuev%{sover} -p /sbin/ldconfig
%postun -n libuev%{sover} -p /sbin/ldconfig

%files -n libuev%{sover}
%doc AUTHORS ChangeLog.md README.md
%license LICENSE
%{_libdir}/libuev.so.%{sover}*

%files devel
%license LICENSE doc/API.md
%{_includedir}/uev
%{_libdir}/libuev.so
%{_libdir}/pkgconfig/libuev.pc

%changelog
