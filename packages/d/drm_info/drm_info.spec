#
# spec file for package drm_info
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


Name:           drm_info
Version:        2.5.0
Release:        0
Summary:        Small utility to dump info about DRM devices
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/drm_info
Source0:        https://gitlab.freedesktop.org/emersion/drm_info/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libdrm-devel
BuildRequires:  libjson-c-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pciutils-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  scdoc

%description
Small utility to dump info about DRM devices.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/drm_info
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
