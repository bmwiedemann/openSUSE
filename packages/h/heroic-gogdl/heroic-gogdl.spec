#
# spec file for package heroic-gogdl
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

Name:             heroic-gogdl
Version:          1.2.1
Release:          0
Summary:          GOG download module for Heroic Games Launcher
License:          GPL-3.0-only
URL:              https://github.com/Heroic-Games-Launcher/heroic-gogdl
Source0:          %{name}-%{version}.tar.gz
Patch0:           use-system-xdelta3.patch
BuildRequires:    gcc
BuildRequires:    fdupes
BuildRequires:    xdelta3-devel
BuildRequires:    python3-devel
BuildRequires:    python3-pip
BuildRequires:    python3-setuptools
BuildRequires:    python3-wheel
BuildRequires:    python3-build
BuildRequires:    python3-installer
Requires:         python3
Requires:         python3-requests
Requires:         xdelta3
BuildArch:        noarch

%description
GOG Downloading module for Heroic Games Launcher

%prep
%autosetup -p1

rm -f gogdl/xdelta3.c

sed -i '/\[tool.setuptools.ext-modules\]/,/\]/d' pyproject.toml
sed -i '/xdelta3/d' pyproject.toml

find . -name "*.py" -exec sed -i '1{/^#!/d}' {} +

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir=%{buildroot} dist/*.whl

find %{buildroot} -name "*.pyc" -delete

%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE*
%{_bindir}/gogdl
%{python3_sitelib}/gogdl
%{python3_sitelib}/gogdl-%{version}*.dist-info

%changelog
