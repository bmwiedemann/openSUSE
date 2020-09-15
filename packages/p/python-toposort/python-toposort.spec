#
# spec file for package python-toposort
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
Name:           python-toposort
Version:        1.5
Release:        0
Summary:        Implements a topological sort algorithm
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ericvsmith/toposort
Source:         https://files.pythonhosted.org/packages/source/t/toposort/toposort-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Implements a topological sort algorithm.

%prep
%setup -q -n toposort-%{version}
chmod a-x *.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{python_sitelib}/*

%changelog
