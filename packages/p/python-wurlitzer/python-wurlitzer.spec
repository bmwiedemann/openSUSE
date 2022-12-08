#
# spec file for package python-wurlitzer
#
# Copyright (c) 2022 SUSE LLC
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
%bcond_without python2
Name:           python-wurlitzer
Version:        3.0.3
Release:        0
Summary:        Python package to capture C-level output in context managers
License:        MIT
URL:            https://github.com/minrk/wurlitzer
Source:         https://files.pythonhosted.org/packages/source/w/wurlitzer/wurlitzer-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-selectors2
%endif
%ifpython2
Requires:       python-selectors2
%endif
%python_subpackages

%description
Wurlitzer is a python package to capture C-level
output in context managers.

%prep
%setup -q -n wurlitzer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
