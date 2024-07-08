#
# spec file for package halloy
#
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


%define appid   org.squidowl.halloy
Name:           halloy
Version:        2024.8
Release:        0
Summary:        IRC application written in Rust
License:        GPL-3.0-or-later
URL:            https://github.com/squidowl/halloy
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  openssl-devel
BuildRequires:  rust >= 1.75.0

%description
Halloy is an open-source IRC client written in Rust, with the Iced GUI
library. It aims to provide a simple and fast client for Mac, Windows,
and Linux platforms.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}
install -Dm644 assets/linux/%{appid}.appdata.xml -t %{buildroot}%{_datadir}/metainfo
install -Dm644 assets/linux/%{appid}.desktop -t %{buildroot}%{_datadir}/applications
cp -r assets/linux/icons %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICEN*
%doc README* CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/metainfo
%{_datadir}/applications
%{_datadir}/icons/hicolor/*/apps/%{appid}.png

%changelog
