#
# spec file for package python-patsy
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


%{?sle15allpythons}
Name:           python-patsy
Version:        1.0.1
Release:        0
Summary:        A Python package for statistical models and design matrices
License:        BSD-2-Clause
URL:            https://github.com/pydata/patsy
Source:         https://files.pythonhosted.org/packages/source/p/patsy/patsy-%{version}.tar.gz
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Recommends:     python-scipy
BuildArch:      noarch
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
A Python package for describing statistical models and for
building design matrices.
It is closely inspired by and compatible with the 'formula'
mini-language used in `R <http://www.r-project.org/>`_ and
`S <https://secure.wikimedia.org/wikipedia/en/wiki/S_programming_language>`_.

%prep
%autosetup -p1 -n patsy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/patsy/
%{python_sitelib}/patsy-%{version}.dist-info

%changelog
