#
# spec file for package python-pysol-cards
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python3
Name:           python-pysol-cards
Version:        0.16.0
Release:        0
Summary:        Python module for pysol-cards
License:        Apache-2.0
URL:            https://pypi.org/project/pysol-cards/
Source:         https://files.pythonhosted.org/packages/source/p/pysol_cards/pysol_cards-%{version}.tar.gz
# https://github.com/shlomif/pysol_cards/issues/6
Patch0:         python-pysol-cards-no-six.patch
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
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -name "*.py" -exec sed -i 's|#! %{_bindir}/env python|#!%{_bindir}/python3|' {} ";"

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
%{_bindir}/pysol_cards
%{python_sitelib}/pysol_cards
%{python_sitelib}/pysol_cards-%{version}.dist-info

%changelog
