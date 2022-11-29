#
# spec file for package DirectX-Headers
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


Name:           DirectX-Headers
Version:        1.608.0
Release:        0
Summary:        DirectX Headers for Mesa
License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
# osc service runall download_files
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
ExclusiveArch:  %{ix86} x86_64

%description
This package contains the official Direct3D 12 headers.
These headers are made available under the MIT license rather than the traditional Windows SDK license.
Additionally, this package hosts several helpers for using these headers.
Make sure that you visit the DirectX Landing Page for more resources for DirectX developers.

%prep
%autosetup

%build
%global _lto_cflags %{nil}
%meson -Dbuild-test=false
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}

%files
%{_includedir}/directx
%{_includedir}/dxguids
%{_includedir}/wsl
%{_libdir}/pkgconfig/DirectX-Headers.pc
%{_libdir}/libDirectX-Guids.a

%changelog
