#
# spec file for package niri-settings
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>
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


Name:           niri-settings
Version:        0~git.20251225.d20e9f5
Release:        0
Summary:        GUI in PyQt for configuring niri
License:        GPL-2.0
URL:            https://github.com/stefonarch/niri-settings
Source:         %{name}-%{version}.tar.zst

# PATCH-FIX-OPENSUSE 0001-adjust-paths.patch <sfalken@opensuse.org>
Patch0:         0001-adjust-paths.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  zstd

Requires:       python3-PyQt6
Requires:       qt6-wayland
Requires:       niri >= 25.11

%description
GUI application for configuring the Niri Wayland Compositor

%prep
%autosetup -p1 -S git_am

%build

%install
install -Dm755 niri-settings %{buildroot}%{_bindir}/niri-settings
install -Dm644 niri-settings.desktop %{buildroot}%{_datadir}/applications/niri-settings.desktop
install -d %{buildroot}%{_libexecdir}/%{name}/ui
install -Dm755 niri_settings.py %{buildroot}%{_libexecdir}/%{name}/niri_settings.py
install -Dm644 ui/*.py %{buildroot}%{_libexecdir}/%{name}/ui
install -d %{buildroot}%{_datadir}/%{name}/translations
install -Dm644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
install -Dm644 niri-settings.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/niri-settings.svg

%find_lang %{name} --all-name --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/ui
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_libexecdir}/%{name}/niri_settings.py
%{_libexecdir}/%{name}/ui/*.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog

