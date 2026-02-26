#
# spec file for package python-PyAVM
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


Name:           python-pyavm
Version:        0.9.8
Release:        0
Summary:        Simple pure-python AVM meta-data handling
License:        MIT
URL:            http://astrofrog.github.io/pyavm/
Source:         https://files.pythonhosted.org/packages/source/p/pyavm/pyavm-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
Suggests:       python-astropy
Suggests:       python-numpy
Suggests:       python-Pillow
BuildArch:      noarch
%python_subpackages

%description
Simple pure-python AVM meta-data handling

%prep
%autosetup -p1 -n pyavm-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/pyavm
%{python_sitelib}/[Pp]y[Aa][Vv][Mm]-%{version}.dist-info

%changelog
