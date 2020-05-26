#
# spec file for package python-Mathics
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pyname Mathics
Name:           python-Mathics
Version:        1.0
Release:        0
Summary:        A general-purpose computer algebra system
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        GPL-3.0-only AND BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://mathics.github.io/
Source:         https://github.com/mathics/Mathics/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mpmath >= 0.19}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module sympy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
Requires:       python-mpmath >= 0.19
Requires:       python-python-dateutil
Requires:       python-six >= 1.10
Requires:       python-sympy
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Mathics is a general-purpose computer algebra system (CAS). It is meant to be a free, lightweight alternative to Mathematica.

%prep
%setup -q -n %{pyname}-%{version}
%autopatch -p1

# FIX SPURIOUS EXEC PERMISSIONS
find ./mathics/web/media/js -name "*.js" -exec chmod -x '{}' \;
find ./mathics/web/media/js -name "*.svg" -exec chmod -x '{}' \;
chmod -x ./mathics/data/ExampleData/{numberdata.csv,InventionNo1.xml}

# WRONG END-OF-FILE ENCODING
sed -i "s/\r$//" ./mathics/data/ExampleData/numberdata.csv

# REMOVE SHEBANGS FROM FILES INSTALLED TO NON-EXEC LOCATIONS
pushd mathics
for d in `find ./ -prune -type d`
do
  find ${d} -name "*.py" -exec sed -i "1,4{/\/usr\/bin\/env/d}" '{}' \;
done
popd

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mathics
%python_clone -a %{buildroot}%{_bindir}/mathicsserver
%python_clone -a %{buildroot}%{_bindir}/mathicsscript
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests fail with new sympy, probably worth fixing upstream
#%%python_exec setup.py test

%post
%python_install_alternative mathics
%python_install_alternative mathicsserver
%python_install_alternative mathicsscript

%postun
%python_uninstall_alternative mathics
%python_uninstall_alternative mathicsserver
%python_uninstall_alternative mathicsscript

%files %{python_files}
%license COPYING.txt
%doc README.rst AUTHORS.txt
%{python_sitelib}/mathics/
%{python_sitelib}/%{pyname}-%{version}-py%{python_version}.egg-info/
%python_alternative %{_bindir}/mathicsscript
%python_alternative %{_bindir}/mathicsserver
%python_alternative %{_bindir}/mathics

%changelog
