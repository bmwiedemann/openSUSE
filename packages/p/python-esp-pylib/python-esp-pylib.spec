#
# spec file for package python-esp-pylib
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-esp-pylib
Version:        1.2.1
Release:        0
Summary:        Logging, utils and constants for Espressif Systems' Python projects
License:        Apache-2.0
URL:            https://github.com/espressif/esp-pylib
Source:         https://files.pythonhosted.org/packages/source/e/esp-pylib/esp_pylib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  %{python_module rich}
# tests/test_cli.py and tests/test_cli_options.py import rich_click and click at module level
BuildRequires:  %{python_module rich-click}
BuildRequires:  %{python_module click}
# tests/test_ports.py imports esp_pylib.serial_ports, which imports serial at module level
BuildRequires:  %{python_module pyserial}
BuildArch:      noarch
Requires:       python-rich
%python_subpackages

%description
esp-pylib provides the logging, serial port and reset helpers, configuration handling
and constants shared by Espressif Systems' Python projects.

%prep
%autosetup -p1 -n esp_pylib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/

%files %{python_files}
%license LICENSE
%{python_sitelib}/esp_pylib/
%{python_sitelib}/esp_pylib-%{version}.dist-info/

%changelog
