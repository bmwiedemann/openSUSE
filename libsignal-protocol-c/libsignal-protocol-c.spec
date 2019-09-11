#
# spec file for package libsignal-protocol-c
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


%define c_lib libsignal-protocol-c2
Name:           libsignal-protocol-c
Version:        2.3.2
Release:        0
Summary:        Signal Protocol C Library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            https://github.com/signalapp/libsignal-protocol-c/
Source:         https://github.com/signalapp/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix_bigendian.patch
BuildRequires:  check-devel >= 0.9.10
BuildRequires:  cmake >= 2.8.4
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl) >= 1.0

%description
The Signal Protocol is a ratcheting forward secrecy protocol that works in synchronous and asynchronous messaging environments.

%package -n libsignal-protocol-c-devel
Summary:        Development files for libsignal-protocol-c
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description -n libsignal-protocol-c-devel
Development files and headers for libsignal-protocol-c

%package -n %{c_lib}
Summary:        Signal Protocol C Library
Group:          System/Libraries

%description -n %{c_lib}
The libsignal-protocol-c library is a forward secrecy protocol library written in C.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DBUILD_TESTING=ON
%if %suse_version > 1500
%cmake_build
%else
%make_jobs
%endif

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files -n %{c_lib}
%license LICENSE
%doc README.md
%{_libdir}/libsignal-protocol-c.so.2
%{_libdir}/libsignal-protocol-c.so.2.3.2

%files devel
%dir %{_includedir}/signal
%{_includedir}/signal/*.h
%{_libdir}/libsignal-protocol-c.so
%{_libdir}/pkgconfig/libsignal-protocol-c.pc

%changelog
