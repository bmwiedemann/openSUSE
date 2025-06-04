#
# spec file for package python-tox-no-internet
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


Name:           python-tox-no-internet
Version:        0.1.0
Release:        0
Summary:        Tox plugin to workaround no internet connection
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lulupac/tox-no-internet
Source:         https://files.pythonhosted.org/packages/source/t/tox-no-internet/tox-no-internet-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/lulupac/tox-no-internet/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tox >= 2.7
BuildArch:      noarch
%python_subpackages

%description
Workarounds for using tox with no internet connection.

%prep
%setup -q -n tox-no-internet-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tox_no_internet.py
%pycache_only %{python_sitelib}/__pycache__/tox_no_internet*.pyc
%{python_sitelib}/tox_no_internet-%{version}.dist-info

%changelog
