#
# spec file for package libXNVCtrl
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

Name:           libXNVCtrl
Version:        510.47.03
Release:        0
Summary:        NV-CONTROL X library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/NVIDIA/nvidia-settings
Source0:        %{name}-%{version}.tar.xz
Patch0:         shared-library.patch
Patch1:         persistent-nvidia-id-string.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xv)

%description
The NV-CONTROL X extension provides a mechanism for X clients to query
and set configuration parameters of the NVIDIA X driver.
State set by the NV-CONTROL X extension is assumed to be persistent
only for the current server generation.

%package -n libXNVCtrl0
Summary:        NV-CONTROL X extension library
Group:          System/Libraries

%description -n libXNVCtrl0
The NV-CONTROL X extension provides a mechanism for X clients to query
and set configuration parameters of the NVIDIA X driver.
State set by the NV-CONTROL X extension is assumed to be persistent
only for the current server generation.

%package devel
Summary:        Development files for the NV-CONTROL X extension library
Group:          Development/Libraries/C and C++
Requires:       libXNVCtrl0 = %{version}

%description devel
This package contains the development files for the
NV-CONTROL X extension library

%prep
%autosetup -p0

%build
%make_build

%install
mkdir -p %{buildroot}%{_includedir}/NVCtrl
mkdir -p %{buildroot}%{_libdir}
install -m0644 ./*.h %{buildroot}%{_includedir}/NVCtrl
cp -a ./libXNVCtrl.so* %{buildroot}%{_libdir}

%ldconfig_scriptlets -n libXNVCtrl0

%files -n libXNVCtrl0
%{_libdir}/libXNVCtrl.so.*

%files -n libXNVCtrl-devel
%{_libdir}/libXNVCtrl.so
%{_includedir}/NVCtrl

%changelog
