#
# spec file for package gophie
#
# Copyright (c) 2022-2026, Martin Hauke <mardnh@gmx.de>
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

Name:           gophie
Version:        2.3.1
Release:        0
Summary:        A modern Gopher client
License:        GPL-3.0-or-later
URL:            https://gophie.org/
#Git-Clone:     https://github.com/jankammerath/gophie.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme

%description
A modern, graphical, cross-platform Gopher browser.
Browse Gopherspace (RFC 1436 & RFC 4266) with menus, text files,
inline images, full-text search, and an integrated download manager.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}
# Icons
for i in 48 128 512; do
  install -Dpm 0644 packaging/linux/gophie-${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
# Desktop file
install -Dpm 0644 packaging/linux/gophie.desktop %{buildroot}%{_datadir}/applications/gophie.desktop

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md config/config.ini
%{_bindir}/gophie
%{_datadir}/icons/hicolor/*/apps/gophie.png
%{_datadir}/applications/%{name}.desktop

%changelog
