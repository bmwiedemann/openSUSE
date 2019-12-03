#
# spec file for package libmodulemd1
#
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global majorversion 1
%global minorversion 8
%global patchversion 16
%global majorminorversion %{majorversion}.%{minorversion}
%global nsversion %{majorversion}.0

%global libmodulemd_version %{majorminorversion}%{?patchversion:.%{patchversion}}

%global origname libmodulemd
%global libname %{name}
%global devname %{name}-devel
%global girname typelib-1_0-Modulemd-%{majorversion}_0


Name:           libmodulemd1
Version:        %{libmodulemd_version}
Release:        0
Summary:        Module metadata manipulation library (legacy version)
Group:          System/Libraries
License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        %{url}/releases/download/%{origname}-%{libmodulemd_version}/modulemd-%{libmodulemd_version}.tar.xz

BuildRequires:  meson >= 0.46.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(gtk-doc)
# For tests
BuildRequires:  gcc-c++

%description
Legacy version of the C Library for manipulating module
metadata files.

This package provides the main library for applications
that use %{name}.


%package -n modulemd-validator-v1
Summary:        Tool for validating modulemd data
Group:          System/Packages
Requires:       %{libname}%{?_isa} = %{libmodulemd_version}-%{release}
# Conflicts with versions of modulemd-validator that included the v1 binary too...
Conflicts:      modulemd-validator < 2.7.0

%description -n modulemd-validator-v1
The modulemd-validator tool provides the facility for verifying
constructed modulemd data is correct and usable.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname}%{?_isa} = %{libmodulemd_version}-%{release}

%description -n %{girname}
This package provides the GObject Introspection typelib interface
for applications to use %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{libmodulemd_version}-%{release}
Requires:       %{girname}%{?_isa} = %{libmodulemd_version}-%{release}
# This conflicts with the modern libmodulemd-devel package
Conflicts:      %{origname}-devel

%description -n %{devname}
This package provides files for developing applications to use %{name}.

%prep
%autosetup -p1 -n modulemd-%{libmodulemd_version}

%if 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150100
# SLE 15 SP1 / openSUSE Leap 15.1 higher have a patched meson that works
sed -e "s/meson_version : '>=0.47.0'/meson_version : '>=0.46.0'/" -i meson.build
%endif

%build
%meson -Ddeveloper_build=false

%meson_build

%check
export LC_CTYPE=C.utf8
# Don't run tests on ARM and RISC-V for now. There are problems
# with performance on the builders and often these time out.
%ifnarch %{arm} aarch64 riscv64
%meson_test
%endif

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
# Hardcode the soname, this library isn't changing anytime soon
%{_libdir}/%{origname}.so.1*

%files -n modulemd-validator-v1
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator-v1

%files -n %{girname}
%{_libdir}/girepository-1.0/Modulemd-%{nsversion}.typelib

%files -n %{devname}
%{_libdir}/%{origname}.so
%{_libdir}/pkgconfig/modulemd.pc
%{_includedir}/modulemd/
%{_datadir}/gir-1.0/Modulemd-%{nsversion}.gir
%{_datadir}/gtk-doc/html/modulemd-%{nsversion}/

%changelog
