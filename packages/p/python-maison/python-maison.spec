#
# spec file for package python-maison
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


Name:           python-maison
Version:        2.0.2
Release:        0
Summary:        Read settings from config files
License:        MIT
URL:            https://github.com/dbatten5/maison
Source:         https://files.pythonhosted.org/packages/source/m/maison/maison-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module loguru >= 0.7.3}
BuildRequires:  %{python_module platformdirs >= 4.3.8}
BuildRequires:  %{python_module pydantic >= 2.11.9}
BuildRequires:  %{python_module pytest >= 8.3.5}
BuildRequires:  %{python_module tomli >= 2.2.1 if %python-base < 3.11}
BuildRequires:  %{python_module typer >= 0.15.4}
BuildRequires:  %{python_module typing-extensions >= 4.13.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-loguru >= 0.7.3
Requires:       python-platformdirs >= 4.3.8
Requires:       python-typer >= 0.15.4
Requires:       python-typing-extensions >= 4.13.2
%if %{python_version_nodots} < 311
Requires:       python-tomli >= 2.2.1
%endif
BuildArch:      noarch
%python_subpackages

%description
`maison` aims to provide a simple and flexible way to read and validate those
configuration options so that they may be used in the package.

%prep
%autosetup -p1 -n maison-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/maison
%{python_sitelib}/maison-%{version}.dist-info

%changelog
