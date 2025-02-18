#
# spec file for package vorta
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


%if 0%{?suse_version} > 1500
# Build only one time
%define pythons %{primary_python}
%else
# Build only with python 3.11
%{?sle15_python_module_pythons}
%endif
Name:           vorta
Version:        0.10.3
Release:        0
Summary:        Desktop Backup Client based on BorgBackup
License:        Apache-2.0 AND GPL-3.0-only AND OFL-1.1
Group:          Productivity/Archiving/Backup
URL:            https://github.com/borgbase/vorta
Source:         https://github.com/borgbase/%{name}/archive/v%{version}.tar.gz
Source1:        vorta.desktop
# PATCH-FIX-OPENSUSE vorta-fix-dependencies.patch malcolmlewis@opensuse.org -- Remove dependencies that are named differently.
Patch0:         vorta-fix-dependencies.patch
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module peewee}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %{python_flavor}-PyQt6
Requires:       %{python_flavor}-SecretStorage
Requires:       %{python_flavor}-peewee
Requires:       %{python_flavor}-platformdirs
Requires:       %{python_flavor}-psutil
Requires:       borgbackup
BuildArch:      noarch

%description
Vorta is a backup client for Linux desktops. It integrates BorgBackup with
the desktop environment to protect data from disk failure,
ransomware and theft.

%prep
%autosetup -p1

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dm644 "src/vorta/assets/icons/icon.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/vorta.svg"
install -Dm644 -t %{buildroot}%{_datadir}/metainfo "src/vorta/assets/metadata/com.borgbase.Vorta.appdata.xml"
%suse_update_desktop_file -i vorta
%fdupes %{buildroot}%{python_sitelib}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/vorta
%{_datadir}/applications/vorta.desktop
%{_datadir}/metainfo/com.borgbase.Vorta.appdata.xml
%{_datadir}/icons/hicolor/256x256/apps/vorta.svg
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{python_bin_suffix}.egg-info

%changelog
