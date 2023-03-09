#
# spec file for package libscrypt
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


%define soname 0
Name:           libscrypt
Version:        1.22
Release:        0
Summary:        SCrypt library
License:        BSD-1-Clause
Group:          System/Libraries
URL:            https://github.com/technion/%{name}
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
%{?suse_build_hwcaps_libs}

%description
This is a shared library that implements scrypt() functionality.

%package -n %{name}%{soname}
Summary:        SCrypt library
Group:          System/Libraries

%description -n %{name}%{soname}
This is a shared library that implements scrypt() functionality.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup

%build
%make_build CC="cc %{optflags}"

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%check
%make_build check

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%{_libdir}/*.so.*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
