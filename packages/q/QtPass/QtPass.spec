#
# spec file for package QtPass
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         _name qtpass
Name:           QtPass
Version:        1.7.0
Release:        0
Summary:        A multi-platform gui for pass
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://qtpass.org
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Platform)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
Requires:       password-store
Recommends:     git-core
Recommends:     gpg2
Recommends:     pwgen
Provides:       qtpass

%description
QtPass is a multi-platform GUI for pass, the standard unix password manager.

%prep
%autosetup

%build
%qmake6 PREFIX=%{_prefix}
%cmake_build

%install
%qmake6_install
install -Dpm0644 %{_name}.desktop %{buildroot}%{_datadir}/applications/%{_name}.desktop
install -Dpm0644 %{_name}.appdata.xml %{buildroot}%{_datadir}/metainfo/%{_name}.appdata.xml
install -Dpm0644 artwork/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{_name}-icon.svg
install -Dpm0644 %{_name}.1 %{buildroot}%{_mandir}/man1/%{_name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{_name}-icon.svg
%{_datadir}/metainfo/%{_name}.appdata.xml
%{_mandir}/man?/%{_name}.?%{ext_man}

%changelog
