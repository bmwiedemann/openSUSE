#
# spec file for package python-patsy
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Tests have dependency loop with pandas
%bcond_with tests
Name:           python-patsy
Version:        0.5.1
Release:        0
Summary:        A Python package for statistical models and design matrices
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/patsy
Source:         https://files.pythonhosted.org/packages/source/p/patsy/patsy-%{version}.tar.gz
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
%if %{with tests}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pandas}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%python_expand nosetests-%{$python_bin_suffix} --all-modules patsy
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/patsy/
%{python_sitelib}/patsy-%{version}-py*.egg-info

%changelog
