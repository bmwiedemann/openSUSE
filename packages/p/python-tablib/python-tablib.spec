#
# spec file for package python-tablib
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


%if 0%{?rhel}
# I get syntax errors in the brp-python-bytecompile step...
%define _python_bytecompile_errors_terminate_build 0
%endif
Name:           python-tablib
Version:        3.7.0
Release:        0
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)
License:        MIT
URL:            https://github.com/jazzband/tablib
Source:         https://files.pythonhosted.org/packages/source/t/tablib/tablib-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module odfpy}
BuildRequires:  %{python_module openpyxl >= 2.6.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xlrd}
BuildRequires:  %{python_module xlwt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-odfpy
Requires:       python-openpyxl >= 2.6.0
Requires:       python-tabulate
Requires:       python-xlrd
Requires:       python-xlwt
Suggests:       python-pandas
BuildArch:      noarch
%python_subpackages

%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

- Excel (Sets + Books)
- JSON (Sets + Books)
- YAML (Sets + Books)
- HTML (Sets)
- TSV (Sets)
- CSV (Sets)

%prep
%setup -q -n tablib-%{version}
# Remove shebang lines from non-executable scripts:
find src -name "*.py" | xargs sed -i '1 { /^#!/ d }'
sed -i '/addopts/ d' pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# v3.2.1: test_cli_export_github fails on Leap 15.3 & .4 due to minor differences in output
%pytest -k 'not test_cli_export_github'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md HISTORY.md
%{python_sitelib}/tablib
%{python_sitelib}/tablib-%{version}.dist-info

%changelog
