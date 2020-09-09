#
# spec file for package python-patsy
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
# Tests have dependency loop with pandas
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define test 1
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
Name:           python-patsy%{pkg_suffix}
Version:        0.5.1
Release:        0
Summary:        A Python package for statistical models and design matrices
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/patsy
Source:         https://files.pythonhosted.org/packages/source/p/patsy/patsy-%{version}.tar.gz
# patsy is EOL https://github.com/pydata/patsy/pull/162#issuecomment-688831172
# https://github.com/pydata/patsy/pull/163
Patch0:         python-patsy-remove-nose.patch
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-six
Recommends:     python-scipy
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module patsy = %{version}}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A Python package for describing statistical models and for
building design matrices.
It is closely inspired by and compatible with the 'formula'
mini-language used in `R <http://www.r-project.org/>`_ and
`S <https://secure.wikimedia.org/wikipedia/en/wiki/S_programming_language>`_.

%prep
%setup -q -n patsy-%{version}
%patch0 -p1

%if !%{with test}
%build
%python_build
%endif

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/patsy/
%{python_sitelib}/patsy-%{version}-py*.egg-info
%endif

%changelog
