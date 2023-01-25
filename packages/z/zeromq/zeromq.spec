#
# spec file for package zeromq
#
# Copyright (c) 2023 SUSE LLC
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


%define lib_name libzmq5
%ifarch %ix86 x86_64
%bcond_without pgm
%else
%bcond_with pgm
%endif
Name:           zeromq
Version:        4.3.4
Release:        0
Summary:        Lightweight messaging kernel
License:        LGPL-3.0-or-later
Group:          Productivity/Networking/Web/Servers
URL:            http://www.zeromq.org/
Source:         https://github.com/zeromq/libzmq/releases/download/v%{version}/zeromq-%{version}.tar.gz
Source99:       baselibs.conf
Patch1:         qemu-user.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libunwind-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
BuildRequires:  libsodium-devel
BuildRequires:  libuuid-devel
%else
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(uuid)
%endif
%if %{with pgm}
BuildRequires:  openpgm-devel >= 5.1
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
BuildRequires:  glib2-devel >= 2.8
%else
BuildRequires:  pkgconfig(glib-2.0) >= 2.8
%endif
%endif  # with pgm

%description
The ZeroMQ messaging kernel is a library extending the standard
socket interfaces with an abstraction of asynchronous message queues,
multiple messaging patterns, message filtering (subscriptions) and
seamless access to multiple transport protocols.

%package -n %{lib_name}
Summary:        Shared Library for ZeroMQ
Group:          Productivity/Networking/Web/Servers
Recommends:     %{name}-tools = %{version}

%description -n %{lib_name}
The ZeroMQ messaging kernel is a library extending the standard
socket interfaces with an abstraction of asynchronous message queues,
multiple messaging patterns, message filtering (subscriptions) and
seamless access to multiple transport protocols.

This package holds the shared library part of the ZeroMQ package.

%package tools
Summary:        Tools to work with ZeroMQ
# Conflict old libraries as we collide with them
Group:          Productivity/Networking/Web/Servers
Conflicts:      libzmq1
Conflicts:      libzmq2
Conflicts:      libzmq3

%description tools
The ZeroMQ messaging kernel is a library extending the standard
socket interfaces with an abstraction of asynchronous message queues,
multiple messaging patterns, message filtering (subscriptions) and
seamless access to multiple transport protocols.

This package contains the utilities to work with ZeroMQ library.

%package devel
Summary:        Development files for ZeroMQ
Group:          Development/Languages/C and C++
Requires:       %{lib_name} = %{version}
Provides:       libzmq-devel = %{version}

%description devel
The ZeroMQ messaging kernel is a library extending the standard
socket interfaces with an abstraction of asynchronous message queues,
multiple messaging patterns, message filtering (subscriptions) and
seamless access to multiple transport protocols.

This package holds the development files for ZeroMQ.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fi
export LIBS=-ldl
%configure \
  --with-libsodium \
  --enable-curve \
%if %{with pgm}
  --with-pgm \
%endif
  --disable-static \
  --disable-dependency-tracking \
  --disable-silent-rules \
  --disable-Werror
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if ! 0%{?qemu_user_space_build}
# Tests don't run well concurrently and some are flaky, hence 3x before fail
make check %{?_smp_mflags} || make check || make check || make check || (cat ./test-suite.log && false)
%endif

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%license COPYING COPYING.LESSER
%{_libdir}/libzmq.so.*

%files tools
%defattr(-,root,root)
%license COPYING COPYING.LESSER
%defattr(-,root,root,-)
%{_bindir}/curve_keygen

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS
%license COPYING COPYING.LESSER
%{_includedir}/zmq*
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_mandir}/man3/zmq*.3*
%{_mandir}/man7/zmq*.7*

%changelog
