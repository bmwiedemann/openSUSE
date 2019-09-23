#
# spec file for package libmodulemd
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


%global majorversion 2
%global minorversion 5
%global patchversion 0
%global majorminorversion %{majorversion}.%{minorversion}
%global nsversion %{majorversion}.0

%global libmodulemd_version %{majorminorversion}%{?patchversion:.%{patchversion}}

%global libname %{name}%{majorversion}
%global devname %{name}-devel
%global girname typelib-1_0-Modulemd-%{majorversion}_0

# Legacy modulemd API
%global oldmajorver 1
%global oldminorver 8
%global oldpatchver 11
%global oldmajorminorver %{oldmajorver}.%{oldminorver}
%global oldnsver %{oldmajorver}.0

%global libmodulemd_v1_version %{oldmajorminorver}%{?oldpatchver:.%{oldpatchver}}

%global oldlibname %{name}%{oldmajorver}
%global olddevname %{name}%{oldmajorver}-devel
%global oldgirname typelib-1_0-Modulemd-%{oldmajorver}_0

Name:           libmodulemd
Version:        %{libmodulemd_version}
Release:        0
Summary:        Module metadata manipulation library
Group:          System/Packages
License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
Source0:        %{url}/releases/download/%{name}-%{libmodulemd_version}/modulemd-%{libmodulemd_version}.tar.xz

BuildRequires:  meson >= 0.46.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  python3-gobject
# For tests
BuildRequires:  gcc-c++

%description
C Library for manipulating module metadata files.


%package -n modulemd-validator
Summary:        Tool for validating modulemd data
Group:          System/Packages
Requires:       %{libname}%{?_isa} = %{libmodulemd_version}-%{release}
Requires:       %{oldlibname}%{?_isa} = %{libmodulemd_v1_version}-%{release}

%description -n modulemd-validator
The modulemd-validator tool provides the facility for verifying
constructed modulemd data is correct and usable.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Group:          Development/Libraries/Python
Requires:       %{girname}%{?_isa} = %{libmodulemd_version}-%{release}
Requires:       python3-gobject
Requires:       python3-six

%description -n python3-%{name}
This package provides the Python 3 bindings for %{name}.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries

%description -n %{libname}
This package provides the main library for applications
that use %{name}.

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

%description -n %{devname}
This package provides files for developing applications to use %{name}.

%package -n %{oldlibname}
Summary:        Main library for %{name} 1.x
Version:        %{libmodulemd_v1_version}
Group:          System/Libraries

%description -n %{oldlibname}
This package provides the main library for applications
that use %{name} 1.x.

%package -n %{oldgirname}
Summary:        GObject Introspection interface description for %{name} 1.x
Version:        %{libmodulemd_v1_version}
Group:          System/Libraries
Requires:       %{oldlibname}%{?_isa} = %{libmodulemd_v1_version}-%{release}

%description -n %{oldgirname}
This package provides the GObject Introspection typelib interface
for applications to use %{name} 1.x.

%package -n %{olddevname}
Summary:        Development files for %{name} 1.x
Version:        %{libmodulemd_v1_version}
Group:          Development/Libraries/C and C++
Conflicts:      %{devname}
Requires:       %{oldlibname}%{?_isa} = %{libmodulemd_v1_version}-%{release}
Requires:       %{oldgirname}%{?_isa} = %{libmodulemd_v1_version}-%{release}
RemovePathPostfixes: .compat

%description -n %{olddevname}
This package provides files for developing applications to use %{name} 1.x.

%prep
%autosetup -p1 -n modulemd-%{libmodulemd_version}

%if 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150100
# SLE 15 SP1 / openSUSE Leap 15.1 higher have a patched meson that works
sed -e "s/meson_version : '>=0.47.0'/meson_version : '>=0.46.0'/" -i meson.build
%endif

%build
%meson -Ddeveloper_build=false -Dbuild_api_v1=true -Dbuild_api_v2=true \
       -Dwith_py3_overrides=true -Dwith_py2_overrides=false

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

ln -s libmodulemd.so.%{libmodulemd_v1_version} \
      %{buildroot}%{_libdir}/%{name}.so.compat

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{oldlibname} -p /sbin/ldconfig
%postun -n %{oldlibname} -p /sbin/ldconfig

%files -n modulemd-validator
%license COPYING
%doc README.md
%{_bindir}/modulemd-validator
%{_bindir}/modulemd-validator-v1

%files -n python3-%{name}
%{python3_sitearch}/gi/overrides/Modulemd.py

%files -n %{libname}
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{majorversion}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Modulemd-%{nsversion}.typelib

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/modulemd-%{nsversion}.pc
%{_includedir}/modulemd-%{nsversion}/
%{_datadir}/gir-1.0/Modulemd-%{nsversion}.gir
%{_datadir}/gtk-doc/html/modulemd-%{nsversion}/

%files -n %{oldlibname}
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{oldmajorver}*

%files -n %{oldgirname}
%{_libdir}/girepository-1.0/Modulemd-%{oldnsver}.typelib

%files -n %{olddevname}
%{_libdir}/%{name}.so.compat
%{_libdir}/pkgconfig/modulemd.pc
%{_includedir}/modulemd/
%{_datadir}/gir-1.0/Modulemd-%{oldnsver}.gir
%{_datadir}/gtk-doc/html/modulemd-%{oldnsver}/

%changelog
