#
# spec file for package cosmic-ext-calculator
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


%define         lic_crate_ver 3.5.1
%define         lic_data_ver 3.25.0
%define         appid dev.edfloreshz.Calculator
Name:           cosmic-ext-calculator
Version:        0.1.1+23
Release:        0
Summary:        A simple calculator for the COSMIC desktop
License:        GPL-3.0-only
URL:            https://github.com/edfloreshz/cosmic-ext-calculator
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# https://github.com/evenorog/license/issues/6
Source2:        https://github.com/spdx/license-list-data/archive/refs/tags/v%{lic_data_ver}.tar.gz#/license-list-data-%{version}.tar.gz
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -a1 -b2
mkdir -p vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data
cp -r ../license-list-data-%{lic_data_ver}/* vendor/license-%{lic_crate_ver}+%{lic_data_ver}/license-list-data/

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg

%changelog
