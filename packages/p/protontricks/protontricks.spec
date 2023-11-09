#
# spec file for package protontricks
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Name:           protontricks
Version:        1.10.5
Release:        0
Summary:        Winetricks for Proton-enabled Games
License:        GPL-3.0-only
Group:          System/Emulators/PC
URL:            https://github.com/Matoking/protontricks
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
# START TESTING SECTION
BuildRequires:  python3-Pillow
BuildRequires:  python3-pytest >= 3.6
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-vdf >= 2.4
BuildRequires:  update-desktop-files
# needed for the desktop file icon
BuildRequires:  wine
# END TESTING SECTION
Requires:       python3-Pillow
Requires:       python3-setuptools
Requires:       python3-vdf
Requires:       winetricks
Requires:       zenity
BuildArch:      noarch

%description
A simple wrapper that does winetricks things for Proton enabled games.

%prep
%setup -q
chmod -x src/protontricks/cli/main.py

# Fix non-executable-script check
chmod +x src/protontricks/data/scripts/*.sh

%build
%python3_build

%install
%python3_install
%suse_update_desktop_file -r protontricks Game Amusement
%fdupes -s %{buildroot}

%check
export LC_ALL='en_US.utf8'
PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitelib} py.test-%{python3_version}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_bindir}/%{name}-desktop-install
%{_bindir}/%{name}-launch
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-launch.desktop
%{python3_sitelib}/*

%changelog
