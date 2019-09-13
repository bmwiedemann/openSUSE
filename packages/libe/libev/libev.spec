#
# spec file for package libev
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define library_name libev4
Name:           libev
Version:        4.27
Release:        0
Summary:        An event loop library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            http://software.schmorp.de/pkg/libev.html
Source:         http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
# Upstream has received patches to add pkg-config support for years but it always ignored them (yes, no answer at all). But since every distribution creates it we just follow.
Source1:        libev.pc
Source99:       baselibs.conf
Patch0:         libev-4.15_compiler_warnings.patch
BuildRequires:  pkgconfig

%description
An event loop that is loosely modeled after libevent.

%package -n %{library_name}
Summary:        An event loop library
Group:          System/Libraries

%description -n %{library_name}
An event loop that is loosely modeled after libevent. Features
include child/PID watchers, periodic timers based on wallclock
(absolute) time (in addition to timers using relative timeouts), as
well as epoll/kqueue/event ports/inotify/eventfd/signalfd support,
timer management, time jump detection and correction.

This package holds the shared libraries of libev.

%package devel
Summary:        Development files for libev
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}

%description devel
An event loop that is loosely modeled after libevent. Features
include child/PID watchers, periodic timers based on wallclock
(absolute) time (in addition to timers using relative timeouts), as
well as epoll/kqueue/event ports/inotify/eventfd/signalfd support,
timer management, time jump detection and correction.

It can be used as a libevent replacement using its emulation API, or
directly embedded into programs. An optional Perl interface is
available.

This package holds the development files for libev.

%prep
%setup -q
%patch0

%build
CFLAGS="%{optflags} -fno-strict-aliasing -Wno-unused"
%configure \
	--docdir=%{_docdir} \
	--disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

rm -v %{buildroot}%{_libdir}/libev.la
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -i 's;@prefix@;%{_prefix};' %{SOURCE1}
sed -i 's;@lib_suffix@;%{_lib};' %{SOURCE1}
sed -i 's;@VERSION@;%{version};' %{SOURCE1}
cp %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/libev.pc

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files devel
%doc LICENSE README ev.pod Changes
%{_includedir}/ev++.h
%{_includedir}/ev.h
%{_includedir}/event.h
%{_libdir}/libev.so
%{_mandir}/man3/ev.3*
%{_libdir}/pkgconfig/libev.pc

%files -n %{library_name}
%{_libdir}/libev.so.4*

%changelog
