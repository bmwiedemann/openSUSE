#
# spec file for package comet
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%global rustflags -C debuginfo=2 -C link-arg=-s
%if "x%{?rust_tier1_arches}" == "x"
%global rust_tier1_arches noarch
%endif

Name:           comet
Version:        0.3.1
Release:        0
Summary:        Communication service for Heroic Games Launcher
License:        GPL-3.0-only
URL:            https://github.com/imLinguin/comet.git
Source:         %{name}-%{version}.tar.xz
Source1:        vendor-comet.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  meson
BuildRequires:  mingw64-cross-cmake
BuildRequires:  mingw64-cross-gcc
BuildRequires:  rust
ExclusiveArch:  %{x86_64} %{aarch64} %{rust_tier1_arches}

%description
Open Source implementation of GOG Galaxy Communication Service.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}
pushd dummy-service
meson setup builddir --cross-file meson/x86_64-w64-mingw32.ini
meson compile -C builddir
popd

%install
install -Dm0755 target/release/comet %{buildroot}/%{_bindir}/comet
install -Dm0755 dummy-service/builddir/GalaxyCommunication.exe %{buildroot}/%{_libexecdir}/heroic/GalaxyCommunication.exe

%files
%license LICENSE
%{_bindir}/comet
%dir %{_libexecdir}/heroic
%{_libexecdir}/heroic/GalaxyCommunication.exe

%changelog
