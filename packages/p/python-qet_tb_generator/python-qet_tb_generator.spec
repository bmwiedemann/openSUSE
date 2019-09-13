#
# spec file for package python-qet_tb_generator
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname qet_tb_generator
%define skip_python2 1
Name:           python-%{modname}
Version:        1.0.16
Release:        0
Summary:        Generates terminal blocks & connectors for QElectroTech
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/qet-tb-generator
Source0:        https://files.pythonhosted.org/packages/source/q/qet_tb_generator/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-qt5
Requires:       qelectrotech
BuildArch:      noarch
%python_subpackages

%description
Allows to generate terminal blocks and connectors for QElectroTech
electrical diagram software.

%prep
%setup -q -n %{modname}-%{version}
rm -rf *.egg-info
sed -i '/^#!\/usr\/bin\/env python3/d' -i src/main.py

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license LICENSE.txt
%python3_only %{_bindir}/%{modname}
%{python_sitelib}/*

%changelog
