#
# spec file for package python-Mathics
#
# Copyright (c) 2021 SUSE LLC
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
# Upstream no longer supports python2
%define skip_python2 1
%define skip_python36 1
%define pyname Mathics3
Name:           python-Mathics
Version:        1.1.1
Release:        0
Summary:        A general-purpose computer algebra system
# Mathics itself is licensed as GPL-3.0 but it includes third-party software with MIT, BSD-3-Clause, and Apache-2.0 Licensing; also includes data from wikipedia licensed under CC-BY-SA-3.0 and GFDL-1.3
License:        Apache-2.0 AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            https://mathics.github.io/
Source:         https://github.com/mathics/Mathics/archive/%{version}/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mpmath >= 0.19}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module sympy >= 1.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.8
Requires:       python-mpmath >= 0.19
Requires:       python-python-dateutil
Requires:       python-six >= 1.10
Requires:       python-sympy >= 1.7.1
# SECTION For tests
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module palettable}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Mathics is a general-purpose computer algebra system (CAS). It is meant to be a free, lightweight alternative to Mathematica.

%prep
%setup -q -n Mathics-%{version}
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
%python_clone -a %{buildroot}%{_bindir}/dmathicsserver
%python_clone -a %{buildroot}%{_bindir}/dmathicsscript
%python_clone -a %{buildroot}%{_bindir}/mathics
%python_clone -a %{buildroot}%{_bindir}/mathicsserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Home page tests require django server up and running
%pytest -k 'not test_home_page'

%post
%python_install_alternative dmathicsserver
%python_install_alternative dmathicsscript
%python_install_alternative mathics
%python_install_alternative mathicsserver

%postun
%python_install_alternative dmathicsserver
%python_install_alternative dmathicsscript
%python_install_alternative mathics
%python_install_alternative mathicsserver

%files %{python_files}
%license COPYING.txt
%doc README.rst AUTHORS.txt
%{python_sitelib}/mathics/
%{python_sitelib}/%{pyname}-%{version}-py%{python_version}.egg-info/
%python_alternative %{_bindir}/dmathicsscript
%python_alternative %{_bindir}/dmathicsserver
%python_alternative %{_bindir}/mathics
%python_alternative %{_bindir}/mathicsserver

%changelog
