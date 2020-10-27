#
# spec file for package winetricks
#
# Copyright (c) 2020 SUSE LLC
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


Name:           winetricks
Version:        20200412
Release:        0
Summary:        A way to work around problems in WINE
License:        LGPL-2.1-or-later
Group:          System/Emulators/PC
URL:            https://github.com/Winetricks/winetricks
Source0:        https://github.com/Winetricks/%{name}/archive/%{version}.tar.gz##/%{name}-%{version}.tar.gz
BuildRequires:  update-desktop-files
Requires:       cabextract
Requires:       unzip
Requires:       wine

%description
Winetricks is a way to work around problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also allows the installation of missing
DLLs and tweaking of various WINE settings.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%suse_update_desktop_file -G Winetricks -r %{name} System Emulator

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
