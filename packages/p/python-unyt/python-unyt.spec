#
# spec file for package python-unyt
#
# Copyright (c) 2023 SUSE LLC
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-unyt
Version:        2.9.4
Release:        0
Summary:        A package for handling numpy arrays with units
License:        BSD-3-Clause
URL:            https://github.com/yt-project/unyt
Source:         https://files.pythonhosted.org/packages/source/u/unyt/unyt-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.17.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy >= 1.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.17.5
Requires:       python-packaging > 20.9
Requires:       python-sympy >= 1.5
BuildArch:      noarch
%python_subpackages

%description
A package for handling numpy arrays with units.

Often writing code that deals with data that has units can be confusing. A
function might return an array but at least with plain NumPy arrays, there is no
way to easily tell what the units of the data are without somehow knowing *a
priori*.

%prep
%setup -q -n unyt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Two old registry tests requires fixture data not provided in tarball
%pytest unyt/tests -k 'not (test_old_registry_json or test_old_registry_multiple_load)'

%files %{python_files}
%doc *.rst
%license LICENSE
%{python_sitelib}/unyt
%{python_sitelib}/unyt-%{version}*-info

%changelog
