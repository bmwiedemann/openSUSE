#
# spec file for package cosmic-ext-tweaks
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


%define         lic_crate_ver 3.6.0
%define         lic_data_ver 3.26.0
%define         appname dev.edfloreshz.CosmicTweaks
Name:           cosmic-ext-tweaks
Version:        0.1.3+42
Release:        0
Summary:        A tweaking tool for the COSMIC DE
License:        GPL-3.0-only
URL:            https://github.com/edfloreshz/cosmic-tweaks
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# https://github.com/evenorog/license/issues/6
Source2:        https://github.com/spdx/license-list-data/archive/refs/tags/v%{lic_data_ver}.tar.gz#/license-list-data-%{version}.tar.gz
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)

%description
This is a tool which gives you advanced tweaking options for the Cosmic Desktop

%prep
%autosetup -a1 -b2
mkdir -p vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data
cp -r ../license-list-data-%{lic_data_ver}/* vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data/

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%fdupes %{buildroot}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg

%changelog
