#
# spec file for package oboete
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


%define         appname dev.mariinkys.Oboete
Name:           oboete
Version:        0.1.4+git20240709.0e05eb4
Release:        0
Summary:        A simple flashcards application for the COSMIC desktop
License:        GPL-3.0-only
URL:            https://github.com/mariinkys/oboete
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  just
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(xkbcommon)

%description
A simple flashcards application for the COSMIC desktop. Written in Rust.

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
%{_iconsdir}/hicolor/??x??/apps/%{appname}.svg
%{_iconsdir}/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
