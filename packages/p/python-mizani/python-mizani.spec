#
# spec file for package python-mizani
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


Name:           python-mizani
Version:        0.11.4
Release:        0
Summary:        Scales for Python
License:        BSD-3-Clause
URL:            https://github.com/has2k1/mizani
Source:         https://files.pythonhosted.org/packages/source/m/mizani/mizani-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.1.1
Requires:       python-numpy
Requires:       python-palettable
Requires:       python-pandas >= 1.1.0
Requires:       python-scipy >= 1.5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module backports.zoneinfo if %python-base < 3.9}
BuildRequires:  %{python_module matplotlib >= 3.1.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module palettable}
BuildRequires:  %{python_module pandas >= 1.1.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.5.0}
# /SECTION
%python_subpackages

%description
Mizani is a scales package for graphics.

%prep
%setup -q -n mizani-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken test in i586
donttest="mizani.breaks.log_breaks"
# test_breaks needs https://github.com/matplotlib/matplotlib/issues/22305 fixed in next mpl
%pytest --ignore mizani/tests/test_breaks.py -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mizani
%{python_sitelib}/mizani-%{version}*-info

%changelog
