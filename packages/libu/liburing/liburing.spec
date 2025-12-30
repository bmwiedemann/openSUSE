#
# spec file for package liburing
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname   liburing2
Name:           liburing
Version:        2.13
Release:        0
Summary:        Linux-native io_uring I/O access library
License:        (GPL-2.0-only AND LGPL-2.1-or-later) OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/axboe/liburing
Source0:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
Source1:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz.asc
Source2:        https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/F7D358FB2971E0A6.asc#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  procps
# Kernel part has landed in 5.1
Conflicts:      kernel < 5.1

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %{lname}
Summary:        Linux-native io_uring I/O access library
Group:          Development/Libraries/C and C++

%description -n %{lname}
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n liburing-ffi2
Summary:        io_uring I/O access library for non-C/C++ languages
Group:          Development/Libraries/C and C++

%description -n liburing-ffi2
Foreign function interface for liburing, offering non-C/C++ language
integration.

%package devel
Summary:        Development files for Linux-native io_uring I/O access library
Group:          Development/Libraries/C and C++
# SLE/Leap 15.4+ retain liburing-devel for the inherited 0.6 API. The v2 API is:
Provides:       %{lname}-devel = %{version}
Requires:       %{lname} = %{version}
Requires:       pkgconfig

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup -p1

%build
# not autotools, so configure macro doesn't work
%set_build_flags
%ifarch %{ix86}
# Otherwise 32-bit x86 fails with: undefined reference to `__stack_chk_fail_local'
export CFLAGS="%{optflags} -fno-stack-protector"
export CPPFLAGS="%{optflags} -fno-stack-protector"
%endif
./configure --prefix=%{_prefix} \
            --includedir=%{_includedir} \
            --libdir=%{_libdir} \
            --libdevdir=%{_libdir} \
            --mandir=%{_mandir} \
            --datadir=%{_datadir}
%make_build -C src

%check
# the tests terribly (and randomly!) fail on non-x86
%ifarch x86_64
# io_uring syscalls not supported as of qemu 7.0.0 and would test the host
# kernel anyway not the target kernel..
%if !0%{?qemu_user_space_build}
declare -a TEST_EXCLUDE=( resize-rings.t conn-unreach.t min-timeout-wait.t )

%if 0%{?sle_version} == 150500
TEST_EXCLUDE+=( fallocate.t fd-pass.t fixed-buf-merge.t msg-ring-overflow.t nop.t poll-race-mshot.t reg-hint.t sqwait.t wq-aff.t )
%endif
%if 0%{?sle_version} == 150600
TEST_EXCLUDE+=( register-restrictions.t sqpoll-sleep.t )
%endif
%if 0%{?sle_version} == 150600 || 0%{?sle_version} == 150700
TEST_EXCLUDE+=( accept-non-empty.t bind-listen.t fallocate.t nop.t recvsend_bundle.t recvsend_bundle-inc.t sqwait.t timeout.t )
%endif
%if 0%{?sle_version} == 150700
TEST_EXCLUDE+=( fifo-futex-poll.t )
%endif
%if 0%{?suse_version} == 1600
TEST_EXCLUDE+=( read-inc-file.t sqwait.t timeout.t )
%endif

echo "TEST_EXCLUDE=\"${TEST_EXCLUDE[@]}\"" > test/config.local
%make_build runtests
%endif
%endif

%install
%make_install
rm -v %{buildroot}%{_libdir}/%{name}*.a

%fdupes %{buildroot}/%{_mandir}/

%ldconfig_scriptlets -n %{lname}
%ldconfig_scriptlets -n liburing-ffi2

%files -n %{lname}
%{_libdir}/liburing.so.*
%license COPYING COPYING.GPL LICENSE

%files -n liburing-ffi2
%license COPYING COPYING.GPL LICENSE
%{_libdir}/liburing-ffi.so.*

%files devel
%license COPYING COPYING.GPL LICENSE
%doc README
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%{_libdir}/liburing-ffi.so
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*2%{?ext_man}
%{_mandir}/man3/*3%{?ext_man}
%{_mandir}/man7/*7%{?ext_man}

%changelog
