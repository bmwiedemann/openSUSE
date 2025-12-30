#
# spec file for package libnvidia-egl-gbm
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define so_ver 1
%define lname libnvidia-egl-gbm%{so_ver}
%define rname egl-gbm
Name:           libnvidia-egl-gbm
Version:        1.1.2.1
Release:        0
Summary:        The GBM EGL external platform library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/NVIDIA/egl-gbm
Source0:        https://github.com/NVIDIA/egl-gbm/archive/%{version}/%{rname}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0001-egl-gbm-add-FP16-DRM-format.patch
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.2
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)

%description
The GBM EGL external platform library.

%package -n %{lname}
Summary:        The GBM EGL external platform library
Group:          System/Libraries

%description -n %{lname}
The GBM EGL external platform library.

%package -n libnvidia-egl-gbm-devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}-%{release}

%description -n libnvidia-egl-gbm-devel
The GBM EGL external platform library.

This package provides headers and libraries required to build software
using %{name}.

%prep
%autosetup -n %{rname}-%{version} -p1

%build
export LDFLAGS="-Wl,-z,noexecstack -Wl,-z,now -Wl,-z,relro %{?_lto_cflags}"
%meson
%meson_build

%install
%meson_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libnvidia-egl-gbm.so.%{so_ver}*
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%files -n libnvidia-egl-gbm-devel
%license COPYING
%{_libdir}/libnvidia-egl-gbm.so

%changelog
