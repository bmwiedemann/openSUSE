#
# spec file for package espanso
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


%define         __rustflags -Clink-arg=-I/usr/include/libxkbcommon
Name:           espanso
Version:        2.4.1
Release:        0
Summary:        A cross-platform Text Expander written in Rust
License:        GPL-3.0-only AND MPL-2.0
URL:            https://github.com/espanso/espanso
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  gcc-c++
BuildRequires:  libnotify4
BuildRequires:  pkgconfig
BuildRequires:  wxGTK3-devel >= 3.0
BuildRequires:  xdotool-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xtst)
Requires:       xclip
Requires:       xdotool
ExclusiveArch:  %{rust_tier1_arches}
%if 0%{?suse_version} < 1600
BuildRequires:  libstdc++6-devel-gcc13
%endif

%description
A cross-platform Text Expander written in Rust. espanso detects when you type a
keyword and replaces it while you're typing.

%prep
%autosetup -a 1 -p 1
rm -f rust-toolchain.toml

%build
export CFLAGS="${optflags} -I/usr/include/libxkbcommon"
export CXXFLAGS="${optflags} -I/usr/include/libxkbcommon"
%{cargo_build}

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 espanso/src/res/linux/espanso.desktop %{buildroot}%{_datadir}/applications/espanso.desktop
install -Dm0644 espanso/src/res/linux/espanso.png %{buildroot}%{_datadir}/pixmaps/espanso.png

%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/%{name}
%{_datadir}/applications/espanso.desktop
%{_datadir}/pixmaps/espanso.png

%changelog
