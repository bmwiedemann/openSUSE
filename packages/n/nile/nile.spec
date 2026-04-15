#
# spec file for package nile
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

%define         pythons %{primary_python}
Name:           nile
Version:        1.1.2
Release:        0
Summary:        Unofficial Amazon Games client
License:        GPL-3.0-only
URL:            https://github.com/imLinguin/nile.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module zstandard}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
Requires:       python3-protobuf
Requires:       python3-pycryptodome
Requires:       python3-requests
Requires:       python3-json5
Requires:       python3-zstandard
Requires:       python3-platformdirs
BuildArch:      noarch

%description
Nile aims to be CLI and GUI tool for managing and playing games from Amazon.

%prep
%setup -q
sed -i '1{/^#!/d}' nile/cli.py

cat > pyproject.toml <<EOF
[project]
name = "nile"
version = "%{version}"
description = "Unofficial Amazon Games client"
dependencies = [
    "protobuf", "pycryptodome", "requests", "json5", "zstandard", "platformdirs",
]
[project.scripts]
nile = "nile.cli:main"
[tool.setuptools.packages.find]
include = ["nile", "nile.*"]
[tool.setuptools.package-data]
"nile" = ["assets/**/*"]
EOF

%build
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-$(date +%%s)}
%pyproject_wheel

%install
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-$(date +%%s)}
export PYTHONHASHSEED=0
%pyproject_install

find %{buildroot} -name "*.py" -exec touch -d "@$SOURCE_DATE_EPOCH" {} +
%py3_compile %{buildroot}%{python_sitelib}/nile

%fdupes %{buildroot}%{python_sitelib}

%files
%license LICENSE*
%{_bindir}/nile
%{python_sitelib}/nile
%{python_sitelib}/nile-%{version}*.dist-info

%changelog
