#
# spec file for package xplr
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xplr
Version:        0.20.0
Release:        0
Summary:        TUI file explorer
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/sayanarijit/xplr
Source0:        https://github.com/sayanarijit/xplr/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
Source3:        https://github.com/sayanarijit/xplr/releases/download/v%{version}/source.tar.gz.asc#/v%{version}.tar.gz.asc
Source4:        https://arijitbasu.in/gpg.txt#/%{name}.keyring
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  rust+cargo

%description
xplr is a terminal UI based file explorer for command-line utilities
that work with the file-system.

xplr integrates shell commands and GUI file managers and exposes a
scriptable, keyboard-controlled, real-time visual interface.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
sed -i 's/-- version = "0.0.0"/version = "%{version}"/' src/init.lua

%build
%{cargo_build}

%install
%{cargo_install}

install -Dm644 -T \
    %{_builddir}/%{name}-%{version}/assets/desktop/%{name}.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 -T \
    %{_builddir}/%{name}-%{version}/src/init.lua \
    %{buildroot}%{_sysconfdir}/%{name}/init.lua

for i in 128 16 32 64; do
    install -Dm644 "%{_builddir}/%{name}-%{version}/assets/icon/%{name}${i}.png" "%{buildroot}/%{_datadir}/icons/hicolor/${i}-${i}/apps/%{name}.png"
done

install -Dm644 "%{_builddir}/%{name}-%{version}/assets/icon/%{name}.svg" -t "%{buildroot}/%{_datadir}/icons/hicolor/scalable/apps"

%files
%license LICENSE
%doc CONTRIBUTING.md README.md RELEASE.md

%{_bindir}/%{name}
%{_datadir}/icons/*
%{_datadir}/applications/*

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/init.lua

%changelog
