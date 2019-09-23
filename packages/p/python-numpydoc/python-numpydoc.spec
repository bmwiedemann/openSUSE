#
# spec file for package python-numpydoc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-numpydoc
Version:        0.9.1
Release:        0
Summary:        Sphinx extension to support docstrings in Numpy format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/numpy/numpydoc
Source:         https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.6.}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-Jinja2 >= 2.3
Requires:       python-Sphinx >= 1.6.5
BuildArch:      noarch
%python_subpackages

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this numpydoc package, in case you want to make use
of them in third-party projects.

%prep
%setup -q -n numpydoc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/numpydoc/
%{python_sitelib}/numpydoc-%{version}-py*.egg-info

%changelog
