#
# spec file for package winetricks
#
# Copyright (c) 2025 SUSE LLC
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
Version:        20250102
Release:        0
Summary:        A way to work around problems in WINE
License:        LGPL-2.1-or-later
URL:            https://github.com/Winetricks/winetricks
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       cabextract
Requires:       unzip
Requires:       wine
Recommends:     (zenity or kdialog)
BuildArch:      noarch

%description
Winetricks is a way to work around problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also allows the installation of missing
DLLs and tweaking of various WINE settings.

%package bash-completion
Summary:        Bash Completions for %{name}
BuildArch:      noarch

%description bash-completion
%{summary}.

%prep
%autosetup -p1

%build
#nothing to do

%install
%make_install
%suse_update_desktop_file %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
#{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/metainfo/io.github.winetricks.Winetricks.metainfo.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
