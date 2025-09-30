#
# spec file for package python-pysol-cards
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Name:           python-pysol-cards
Version:        0.24.0
Release:        0
Summary:        Python module for pysol-cards
License:        Apache-2.0
URL:            https://pypi.org/project/pysol-cards/
Source:         https://files.pythonhosted.org/packages/source/p/pysol_cards/pysol_cards-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module random2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-random2
BuildArch:      noarch
%python_subpackages

%description
This module allows the python developer to generate the initial deals of some
PySol FC games. It also supports PySol legacy deals and Microsoft FreeCell /
Freecell Pro deals.

%prep
%autosetup -p1 -n pysol_cards-%{version}
find . -name "*.py" -exec sed -i '/\#\!\ \/usr\/bin\/env\ python/d' {} \;

%build
export LC_ALL=en_US.utf8
%pyproject_wheel

%install
export LC_ALL=en_US.utf8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
sed -i '/^addopts/d' setup.cfg
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pysol_cards
%{python_sitelib}/pysol_cards-%{version}.dist-info

%changelog
