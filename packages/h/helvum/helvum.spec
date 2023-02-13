#
# spec file for package helvum
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%define app_id org.pipewire.Helvum
Name:           helvum
Version:        0.4.0
Release:        0
Summary:        A GTK patchbay for pipewire
License:        (Apache-2.0 OR BSL-1.0) AND GPL-3.0-only AND (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            https://gitlab.freedesktop.org/pipewire/helvum
Source:         https://gitlab.freedesktop.org/pipewire/helvum/uploads/2b68fb86bf4b988c3183de123dfd1065/%{name}-%{version}.tar.xz
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  gtk4-devel
BuildRequires:  pipewire-devel
ExcludeArch:    s390 s390x ppc ppc64 ppc64le %{ix86}

%description
Helvum is a GTK-based patchbay for pipewire, inspired by the JACK tool catia.

%prep
%setup -q

%build
RUSTFLAGS=%{rustflags} cargo build --release

%install
RUSTFLAGS=%{rustflags} cargo install --no-track --root=%{buildroot}%{_prefix} --path .
sed 's/@icon@/%{app_id}/g' data/%{app_id}.desktop.in > data/%{app_id}.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/applications/ data/%{app_id}.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps data/icons/%{app_id}.svg
install -D -m0644 -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps data/icons/%{app_id}-symbolic.svg

%files
%{_bindir}/helvum
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/

%changelog
