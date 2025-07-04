#
# spec file for package python-qet_tb_generator
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


%define modname qet_tb_generator
%bcond_without libalternatives
Name:           python-%{modname}
Version:        1.3.1
Release:        0
Summary:        Generates terminal blocks & connectors for QElectroTech
License:        GPL-2.0-only
URL:            https://pypi.python.org/pypi/qet-tb-generator
Source0:        https://files.pythonhosted.org/packages/source/q/qet_tb_generator/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-qt5
Requires:       qelectrotech
BuildArch:      noarch
%python_subpackages

%description
Allows to generate terminal blocks and connectors for QElectroTech
electrical diagram software.

%prep
%setup -q -n %{modname}-%{version}
chmod a-x README LICENSE.txt
rm -rf *.egg-info
sed -i '/^#!\/usr\/bin\/env python3/d' -i src/main.py
# Rename package and adjust console script
mv src qet_tb_generator
sed -i 's/qet_tb_generator=src.main:main/qet_tb_generator=qet_tb_generator.main:main/' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{modname}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative %{modname}

%files %{python_files}
%doc README
%license LICENSE.txt
%python_alternative %{_bindir}/%{modname}
%{python_sitelib}/qet_tb_generator*

%changelog
