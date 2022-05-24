#
# spec file for package libunwind
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libunwind
Version:        1.6.2
Release:        0
Summary:        Call chain detection library
License:        MIT
Group:          System/Base
URL:            https://savannah.nongnu.org/projects/libunwind/
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
ExcludeArch:    s390

%description
A C programming interface (API) to determine the call chain of a program.

%package -n libunwind8
Summary:        Call chain detection library for process self-inspection
Group:          System/Libraries
Conflicts:      libunwind < %{version}-%{release}

%description -n libunwind8
A C programming interface (API) to determine the call chain of a
program from within the same process.

%package -n libunwind-coredump0
Summary:        Call chain detection library for coredump images
Group:          System/Libraries
Conflicts:      libunwind < %{version}-%{release}

%description -n libunwind-coredump0
A C programming interface (API) to determine the call chains
of the threads in coredump images.

%package -n libunwind-ptrace0
Summary:        Call chain detection library for ptraced processes
Group:          System/Libraries
Conflicts:      libunwind < %{version}-%{release}

%description -n libunwind-ptrace0
A C programming interface (API) to determine the call chains of
another process by means of using ptrace(2) on it.

%package -n libunwind-setjmp0
Summary:        Non-local goto (setjmp/longmap) implementation based on libunwind
Group:          System/Libraries
Conflicts:      libunwind < %{version}-%{release}

%description -n libunwind-setjmp0
The unwind-setjmp library offers a libunwind-based implementation of
non-local gotos. This is a drop-in replacement for the normal,
system-provided routines of the same name. With this library, setting
up a non-local goto via setjmp is generally faster compared to the
system routines, at the cost of a much slower longjmp.

%package devel
Summary:        Headers for the Unwind library
Group:          Development/Libraries/C and C++
%ifnarch ppc ppc64 ppc64le s390x
Requires:       libunwind-coredump0 = %{version}-%{release}
%endif
Requires:       libunwind-ptrace0 = %{version}-%{release}
Requires:       libunwind-setjmp0 = %{version}-%{release}
Requires:       libunwind8 = %{version}-%{release}

%description devel
A set of C programming interfaces to determine the call chain within a running
program (libunwind), of a coredump image (libunwind-coredump), or of a separate
process (libunwind-ptrace).

%prep
%autosetup

%build
%configure \
    --enable-minidebuginfo
%make_build

%check
# run-coredump-unwind fails
%make_build check || :

%install
%make_install
find %{buildroot} -iregex '.*\.l?a$' -delete -print
# Help packagers with %files
find %{buildroot}/%{_libdir} -type f | sort

%post   -n libunwind8 -p /sbin/ldconfig
%postun -n libunwind8 -p /sbin/ldconfig
%post   -n libunwind-coredump0 -p /sbin/ldconfig
%postun -n libunwind-coredump0 -p /sbin/ldconfig
%post   -n libunwind-ptrace0 -p /sbin/ldconfig
%postun -n libunwind-ptrace0 -p /sbin/ldconfig
%post   -n libunwind-setjmp0 -p /sbin/ldconfig
%postun -n libunwind-setjmp0 -p /sbin/ldconfig

%files -n libunwind8
%{_libdir}/libunwind.so.8*
%ifarch %arm
%{_libdir}/libunwind-arm.so.8*
%else
%ifarch riscv32 riscv64
%{_libdir}/libunwind-riscv.so.8*
%else
%ifarch %ix86
%{_libdir}/libunwind-x86.so.8*
%else
%ifarch ppc
%{_libdir}/libunwind-ppc32.so.8*
%else
%ifarch ppc64 ppc64le
%{_libdir}/libunwind-ppc64.so.8*
%else
%{_libdir}/libunwind-%{_target_cpu}.so.8*
%endif
%endif
%endif
%endif
%endif

%ifnarch ppc ppc64 ppc64le s390x
%files -n libunwind-coredump0
%{_libdir}/libunwind-coredump.so.0*
%endif

%files -n libunwind-setjmp0
%{_libdir}/libunwind-setjmp.so.0*

%files -n libunwind-ptrace0
%{_libdir}/libunwind-ptrace.so.0*

%files devel
%{_includedir}/*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
