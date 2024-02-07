#
# spec file for package vorta
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


Name:           vorta
Version:        0.9.1
Release:        0
Summary:        Desktop Backup Client based on BorgBackup
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://github.com/borgbase/vorta
Source:         https://github.com/borgbase/%{name}/archive/v%{version}.tar.gz
Source1:        vorta.desktop
# PATCH-FIX-OPENSUSE vorta-fix-dependencies.patch malcolmlewis@opensuse.org -- Remove dependencies that are named differently.
Patch0:         vorta-fix-dependencies.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-APScheduler < 4.0
BuildRequires:  python3-QDarkStyle
BuildRequires:  python3-keyring
BuildRequires:  python3-peewee
BuildRequires:  python3-platformdirs
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-qt6
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-git
BuildRequires:  update-desktop-files
## MANUAL BEGIN
Requires:       borgbackup
Requires:       python3-APScheduler < 4.0
Requires:       python3-QDarkStyle
Requires:       python3-keyring
Requires:       python3-peewee
Requires:       python3-platformdirs
Requires:       python3-psutil
Requires:       python3-python-dateutil
Requires:       python3-qt6
## MANUAL END
BuildArch:      noarch

%description
Vorta is a backup client for Linux desktops. It integrates BorgBackup with
the desktop environment to protect data from disk failure,
ransomware and theft.

%prep
%autosetup -p1

%build
export LANG=en_US.UTF-8
%python3_build

%install
export LANG=en_US.UTF-8
%python3_install
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dm644 "src/vorta/assets/icons/icon.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/vorta.svg"
install -Dm644 -t %{buildroot}%{_datadir}/metainfo "src/vorta/assets/metadata/com.borgbase.Vorta.appdata.xml"
%suse_update_desktop_file -i vorta
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/vorta
%{_datadir}/applications/vorta.desktop
%{_datadir}/metainfo/com.borgbase.Vorta.appdata.xml
%{_datadir}/icons/hicolor/256x256/apps/vorta.svg
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info

%changelog
