#
# spec file for package python-jsonpath-rw
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


%define modname jsonpath-rw
%bcond_without libalternatives
Name:           python-jsonpath-rw
Version:        1.4.0
Release:        0
Summary:        An extended implementation of JSONPath for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kennknowles/python-jsonpath-rw
Source:         https://files.pythonhosted.org/packages/source/j/jsonpath-rw/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-decorator
Requires:       python-ply >= 3.4
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This library provides a robust and significantly extended implementation
of JSONPath for Python. It is tested with Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a
full *language* implementation, meaning the JSONPath expressions are
first class objects, easy to analyze, transform, parse, print, and
extend. (You can also execute them :-)

%prep
%setup -q -n jsonpath-rw-%{version}
# remove unwanted shebang
sed -i '/^#!/ d' jsonpath_rw/bin/jsonpath.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jsonpath.py

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative jsonpath.py

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/jsonpath.py
%{python_sitelib}/jsonpath[-_]rw
%{python_sitelib}/jsonpath[-_]rw-%{version}*-info

%changelog
