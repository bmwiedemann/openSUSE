#
# spec file for package python-deprecation
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
Name:           python-deprecation
Version:        2.0.7
Release:        0
Summary:        A library to handle automated deprecations
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/briancurtin/deprecation
Source:         https://files.pythonhosted.org/packages/source/d/deprecation/deprecation-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The `deprecation` library provides a `deprecated` decorator and a
`fail_if_not_removed` decorator for your tests. Together, the two
enable the automation of several things:

%prep
%setup -q -n deprecation-%{version}

%build

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
