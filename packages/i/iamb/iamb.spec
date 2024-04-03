#
# spec file for package iamb
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

%bcond_without system_openssl
%if %{with system_openssl}
%define features native-tls
%else
%define features bundled
%endif

Name:           iamb
Version:        0.0.9
Release:        0
Summary:        A Matrix client for Vim addicts
License:        Apache-2.0
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/ulyssa/iamb
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  update-desktop-files
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
%if %{with system_openssl}
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
%endif

%description
iamb is a Matrix client for the terminal that uses Vim keybindings.

This project is a work-in-progress, and there's still a lot to be
implemented, but much of the basic client functionality is already
present.

%prep
%autosetup -a1

%build
%{cargo_build} --no-default-features --features=%{features}

%install
%{cargo_install} --no-default-features --features=%{features}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

mkdir -p %{buildroot}%{_mandir}/man{1,5}
install -Dm 644 docs/%{name}.1 "%{buildroot}%{_mandir}/man1/"
install -Dm 644 docs/%{name}.5 "%{buildroot}%{_mandir}/man5/"
install -Dm 644 docs/%{name}.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg"
install -Dm 644 docs/%{name}-256x256.png "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png"
install -Dm 644 docs/%{name}-512x512.png "%{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png"

%check
%{cargo_test} --no-default-features --features=%{features}

%files
%doc README.md config.example.toml
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.*

%changelog
