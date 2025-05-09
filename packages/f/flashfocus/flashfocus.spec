#
# spec file for package flashfocus
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


Name:           flashfocus
Version:        2.4.1
Release:        0
Summary:        Focus animations for tiling window managers
License:        MIT
Group:          System/X11/Utilities
URL:            https://github.com/fennerm/flashfocus
Source:         https://github.com/fennerm/flashfocus/archive/v%{version}.tar.gz
Patch0:         flashfocus-2.4.0-no-i3ipc.patch
BuildRequires:  fdupes
BuildRequires:  libffi-devel
BuildRequires:  libxcb-devel
BuildRequires:  python3 >= 3.8
BuildRequires:  python3-pip
BuildRequires:  python3-pip-wheel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-PyYAML >= 5.1
Requires:       python3-cffi
Requires:       python3-click
Requires:       python3-marshmallow
Requires:       python3-xcffib
Requires:       python3-xpybutil
Recommends:     compton
BuildArch:      noarch

%description
Focus animations for tiling window managers. Compatible with all X based window managers.

%prep
%autosetup -p1
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" bin/nc_flash_window

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/flash_window
%{_bindir}/flashfocus
%{_bindir}/nc_flash_window
%{python3_sitelib}/flashfocus*

%changelog
