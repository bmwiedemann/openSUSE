#
# spec file for package lutgen-studio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lutgen-studio
Version:        0.4.0
Release:        0
Summary:        Blazingly fast interpolated LUT generator and applicator for arbitrary and popular color palettes.
License:        MIT
URL:            https://github.com/ozwaldorf/lutgen-rs
Source0:        lutgen-rs-%{version}.tar.xz
Source1:        vendor.tar.zst
Source2:        lutgen-studio.desktop

BuildRequires:  rust
BuildRequires:  cargo-packaging
BuildRequires:  libxcb-render0
BuildRequires:  libxcb-shape0
BuildRequires:  libxcb-xfixes0
BuildRequires:  libxkbcommon-devel
BuildRequires:  wayland-devel
BuildRequires:  desktop-file-utils
buildrequires:  hicolor-icon-theme

ExcludeArch:    i586

%description
A blazingly fast interpolated LUT utility for arbitrary and popular color palettes. Theme any image to your desktop colorscheme!

%prep
%autosetup -a1 -n lutgen-rs-%{version}

%build
%{cargo_build} --package lutgen-studio

%install
install -Dm755 target/release/lutgen-studio %{buildroot}%{_bindir}/lutgen-studio
install -Dm644 crates/studio/assets/lutgen.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/lutgen.png
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/lutgen-studio.desktop

%check
%{cargo_test}
desktop-file-validate %{buildroot}%{_datadir}/applications/lutgen-studio.desktop

%files
%license LICENSE*
%doc README.md docs/pages/*.md
%{_bindir}/lutgen-studio
%{_datadir}/applications/lutgen-studio.desktop
%{_datadir}/icons/hicolor/*/apps/lutgen.png

%changelog

