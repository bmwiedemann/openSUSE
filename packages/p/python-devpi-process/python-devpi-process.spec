#
# spec file for package python-devpi-process
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-devpi-process
Version:        0.3.0
Release:        0
Summary:        Programmatic API to create and use a devpi server process
License:        MIT
URL:            https://github.com/tox-dev/devpi-process
Source:         https://files.pythonhosted.org/packages/source/d/devpi_process/devpi_process-0.3.0.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-devpi-client >= 6.0.2
Requires:       python-devpi-server >= 6.7
Suggests:       python-httpx >= 0.23.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module devpi-client >= 6.0.2}
BuildRequires:  %{python_module devpi-server >= 6.7}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest >= 7.2}
# /SECTION
%python_subpackages

%description
This package provides a programmatic API to create and use a
devpi server process.

%prep
%autosetup -p1 -n devpi_process-%{version}

# Both of these issues are resolved in the upstream master
sed -i -e '/^license_file =/s/ =/s =/' \
    -e '/^name/aversion = %{version}' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/devpi_process
%{python_sitelib}/devpi_process-%{version}*-info

%changelog
