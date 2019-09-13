#
# spec file for package crossc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libcrossc1
Name:           crossc
Version:        1.6.0
Release:        0
Summary:        Portable C wrapper for SPIRV-Cross
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/rossy/crossc
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig

%description
This package contains crossc, a portable C wrapper for SPIRV-Cross.

%package -n %{libname}
Summary:        Portable C wrapper for SPIRV-Cross
Group:          System/Libraries

%description -n %{libname}
This package contains crossc, a portable C wrapper for SPIRV-Cross.

%package devel
Summary:        Portable C wrapper for SPIRV-Cross
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains development files for crossc, a portable C
wrapper for SPIRV-Cross.

%prep
%setup -q -n crossc-%{version}

%build
make %{?_smp_mflags} shared

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} \
    install-shared

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/crossc.pc
%{_includedir}/crossc.h

%changelog
