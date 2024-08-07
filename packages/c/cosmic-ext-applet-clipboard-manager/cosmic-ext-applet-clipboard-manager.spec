#
# spec file for package cosmic-ext-applet-clipboard-manager
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


%define         appname io.github.wiiznokes.cosmic-ext-applet-clipboard-manager
Name:           cosmic-ext-applet-clipboard-manager
Version:        0.1.0+git20240724.1893132
Release:        0
Summary:        Clipboard manager for COSMIC
License:        MIT
URL:            https://github.com/wiiznokes/clipboard-manager
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xkbcommon)

%description
The goal is to make a simple yet fast clipboard history, with a focus on UX,
rapidity and security.

Currently support storing the history on disk, search, delete

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
%{_iconsdir}/hicolor/scalable/apps/%{appname}-symbolic.svg
%{_prefix}/lib/environment.d/%{name}.conf
%{_datadir}/%{name}

%changelog
