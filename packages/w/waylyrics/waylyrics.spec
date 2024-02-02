#
# spec file for package waylyrics
#
# Copyright (c) 2024 SUSE LLC
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


Name:           waylyrics
Version:        0~git475
Release:        0
Summary:        The furry way to show desktop lyrics
License:        MIT
URL:            https://github.com/waylyrics/waylyrics
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.73.0
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-devel
BuildRequires:  gtk4-devel
BuildRequires:  libgraphene-devel
BuildRequires:  mimalloc-devel
BuildRequires:  openssl-devel

# Override "-C debuginfo=2" from cargo-packaging, to solve rustc SIGSEGV exception:
#   error: rustc interrupted by SIGSEGV, printing backtrace
#   /usr/lib/librustc_driver-16d66626a1fefc07.so(+0x7aafa6)[0x7fbd6ffaafa6]
# Tested with rustc 1.75.0 (82e1608df 2023-12-21) by xtexChooser
%global build_rustflags %build_rustflags -C debuginfo=0

%description
The furry way to show desktop lyrics, and simple universal desktop lyrics made with GTK4 and love.

%prep
%autosetup -a1 -p0

%build
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
%{cargo_build} --locked

%install
export WAYLYRICS_THEME_PRESETS_DIR=%{_datadir}/waylyrics/themes
# locked is required as waylyrics includes some git dependencies
%{cargo_install} --locked

install -d %{buildroot}%{_datadir}/waylyrics
cp -r themes %{buildroot}%{_datadir}/waylyrics/

install -Dm644 "io.poly000.waylyrics.desktop" -t %{buildroot}%{_datadir}/applications/
install -Dm644 "io.poly000.waylyrics.gschema.xml" -t %{buildroot}%{_datadir}/glib-2.0/schemas/

%check
# waylyrics does not have any tests

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/waylyrics/
%{_datadir}/applications/io.poly000.waylyrics.desktop
%{_datadir}/glib-2.0/schemas/io.poly000.waylyrics.gschema.xml

%changelog
