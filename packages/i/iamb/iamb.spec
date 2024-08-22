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
Version:        0.0.10
Release:        0
Summary:        A Matrix client for Vim addicts
License:        Apache-2.0
URL:            https://github.com/ulyssa/iamb
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}-rpmlintrc

%if "%{_vendor}" == "debbuild"
# Needed to set Maintainer in output debs
%endif

%if 0%{?suse_version} > 1500
BuildRequires:  cargo-packaging
BuildRequires:  update-desktop-files
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  cargo
BuildRequires:  rustc >= 1.8.0
%else
BuildRequires:  cargo >= 1.8.0
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  zstd
%if %{with system_openssl}
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  libsqlite3-dev
BuildRequires:  libssl-dev
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig(openssl) > 3.0.0
BuildRequires:  pkgconfig(sqlite3)
%endif
%endif

%description
iamb is a terminal-based client for Matrix for the Vim addict. You
can edit messages, navigate windows and manage tabs in the same
ways that your fingers are used to.

%prep
%autosetup -a1
%define build_args --no-default-features --features=%{features}

%build
%if 0%{?suse_version} > 1500
%{cargo_build} %{build_args}
%else
cargo build --release %{build_args}
%endif

%install
%if 0%{?suse_version} > 1500
%{cargo_install} %{build_args}
%else
install -Dm 755 -t "%{buildroot}%{_bindir}" target/release/iamb
%endif

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%if 0%{?suse_version} > 1500
%suse_update_desktop_file %{name}
%endif

mkdir -p %{buildroot}%{_mandir}/man{1,5}
install -Dm 644 docs/%{name}.1 -t "%{buildroot}%{_mandir}/man1/"
install -Dm 644 docs/%{name}.5 -t "%{buildroot}%{_mandir}/man5/"
install -Dm 644 docs/%{name}.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg"
install -Dm 644 docs/%{name}-256x256.png "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png"
install -Dm 644 docs/%{name}-512x512.png "%{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png"

%files
%doc README.md config.example.toml
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.*

%changelog
