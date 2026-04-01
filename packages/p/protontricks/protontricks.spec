#
# spec file for package protontricks
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           protontricks
Version:        1.14.1
Release:        0
Summary:        Winetricks for Proton-enabled Games
License:        GPL-3.0-only
URL:            https://github.com/Matoking/protontricks
Source0:        %{name}-%{version}.tar.xz
Patch1:         0001-Fix-using-local-vdf-module.patch
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools_scm
Requires:       python3-Pillow
Requires:       winetricks
Requires:       (yad or zenity)
BuildArch:      noarch

%description
A simple wrapper that does winetricks things for Proton enabled games.

%prep
%autosetup -p1

# Fix non-executable-script check
chmod +x src/protontricks/data/scripts/*.sh

%build
%python3_build

%install
%python3_install
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_bindir}/%{name}-desktop-install
%{_bindir}/%{name}-launch
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-launch.desktop
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info

%changelog
