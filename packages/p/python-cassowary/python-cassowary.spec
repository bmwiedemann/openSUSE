#
# spec file for package python-cassowary
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-cassowary
Version:        0.5.2
Release:        0
Summary:        A pure Python implementation of the Cassowary constraint solving algorithm
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/brodderickrodriguez/cassowary
Source:         https://files.pythonhosted.org/packages/source/c/cassowary/cassowary-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A pure Python implementation of the Cassowary constraint-solving algorithm.
Cassowary is the algorithm that forms the core of the OS X and iOS visual
layout mechanism.

%prep
%setup -q -n cassowary-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/cassowary
%{python_sitelib}/cassowary-%{version}*-info

%changelog
