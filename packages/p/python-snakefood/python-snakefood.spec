#
# spec file for package python-snakefood
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-snakefood
Version:        1.4
Release:        0
Summary:        Dependency Graphing for Python
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            http://furius.ca/snakefood
Source:         https://files.pythonhosted.org/packages/source/s/snakefood/snakefood-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Generate dependencies from Python code, filter, cluster and generate graphs
from the dependency list.

%prep
%setup -q -n snakefood-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc CHANGES README
%{_bindir}/sfood
%{_bindir}/sfood-checker
%{_bindir}/sfood-cluster
%{_bindir}/sfood-copy
%{_bindir}/sfood-filter-stdlib
%{_bindir}/sfood-flatten
%{_bindir}/sfood-graph
%{_bindir}/sfood-imports
%{_bindir}/sfood-target-files
%{python_sitelib}/*

%changelog
