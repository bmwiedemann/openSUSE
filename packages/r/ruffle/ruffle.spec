#
# spec file for package ruffle
#
# Copyright (c) 2026 mantarimay
# Copyright (c) 2020 SUSE LLC
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


%bcond_with test
%define appid rs.ruffle.Ruffle
Name:           ruffle
Version:        0.4.1
Release:        0
Summary:        Adobe Flash Player emulator written in Rust
License:        Apache-2.0 OR MIT
URL:            https://github.com/ruffle-rs/ruffle
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  fontconfig-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  java
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libudev)

%description
Ruffle is an Adobe Flash Player emulator written in the Rust programming
language. Ruffle targets both the desktop and the web using WebAssembly.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm0755 target/release/ruffle_desktop %{buildroot}%{_bindir}/%{name}

res="desktop/packages/linux"
install -Dm0644 $res/%{appid}.svg -t \
     %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -Dm0644 $res/%{appid}.metainfo.xml -t %{buildroot}%{_datadir}/metainfo
install -Dm0644 $res/%{appid}.desktop -t %{buildroot}%{_datadir}/applications

%check
%if %{with test}
%{cargo_test}
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
