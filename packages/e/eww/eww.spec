#
# spec file for package eww
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 mantarimay
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


%bcond_without test
Name:           eww
Version:        0.6.0+git86.g98c220126d912b935987766f56650b55f3e226eb
Release:        0
Summary:        ElKowars wacky widgets
License:        MIT
URL:            https://github.com/elkowar/eww
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  zstd

%description
Elkowars Wacky Widgets is a standalone widget system made in Rust that
allows you to implement your own, custom widgets in any window manager.

%prep
%autosetup -a1 -p1
sed -i '1s|#!/bin/sh|#!/usr/bin/sh|' examples/eww-bar/scripts/getvol

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%check
%if %{with test}
%{cargo_test}
%endif

%files
%license LICEN*
%doc README* docs examples CHANGELOG.md
%{_bindir}/%{name}

%changelog
