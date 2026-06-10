#
# spec file for package pcg-c
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define sover   0
%define libname lib%{name}%{sover}
%define devname %{libname}-devel

Name:           pcg-c
Version:        0.94.2
Release:        0
Summary:        Library implementing the PCG random number generation scheme
License:        Apache-2.0 OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/andy5995/pcg-c
Source:         https://github.com/andy5995/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.58.0

%description
PCG-C implements the PCG random number generation scheme. PCG
generators are statistically well-distributed, but trade
cryptographical strength for faster turnaround, and small state.
PCG-C supports multiple output sizes (8 through 128-bit) and multiple
independent streams.

%package -n %{libname}
Summary:        Library implementing the PCG random number generation scheme
Group:          System/Libraries

%description -n %{libname}
PCG-C implements the PCG random number generation scheme. PCG
generators are statistically well-distributed, but trade
cryptographical strength for faster turnaround, and small state.
PCG-C supports multiple output sizes (8 through 128-bit) and multiple
independent streams.

This package contains the shared library for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%meson \
    -Ddocdir=%{_docdir}/%{name}
%meson_build

%install
%meson_install
rm -r %{buildroot}%{_docdir}/%{name}/

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE-APACHE.txt LICENSE-MIT.txt
%doc README.md
%{_libdir}/libpcg-c.so.%{sover}*

%files -n %{devname}
%{_libdir}/libpcg-c.so
%{_libdir}/pkgconfig/pcg-c.pc
%{_includedir}/pcg_variants.h

%changelog
