#
# spec file for package libebur128
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   1
Name:           libebur128
Version:        1.2.6
Release:        0
Summary:        A library implementing the EBU R128 loudness standard
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/jiixyj/libebur128
Source0:        https://github.com/jiixyj/libebur128/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake >= 2.8.12
BuildRequires:  pkgconfig

%description
This library implements the EBU R 128 standard for loudness normalisation.

%package -n     %{name}-%{sover}
Summary:        A library implementing the EBU R128 loudness standard
Group:          System/Libraries

%description -n %{name}-%{sover}
This library implements the EBU R 128 standard for loudness normalisation.

This package contains the shared library.

%package -n     %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{sover} = %{version}

%description -n %{name}-devel
A library implementing the EBU R128 loudness standard.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install

%post -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%files -n %{name}-%{sover}
%doc README.md
%license COPYING
%{_libdir}/%{name}.so.%{sover}*

%files -n %{name}-devel
%{_includedir}/ebur128.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
