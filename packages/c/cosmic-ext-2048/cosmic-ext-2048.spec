#
# spec file for package cosmic-ext-2048
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


%define         appname io.github.Kartonrealista.cosmic-ext-2048
Name:           cosmic-ext-2048
Version:        0.1.0+git20240802.b8c9457
Release:        0
Summary:        2048 application for the Cosmic desktop
License:        GPL-3.0-only
URL:            https://github.com/Kartonrealista/cosmic-ext-2048
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xkbcommon)

%description
A 2048 game written in libcosmic and Rust.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
