#
# spec file for package python-python-json-logger
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
Name:           python-python-json-logger
Version:        0.1.11
Release:        0
Summary:        A python library adding a json log formatter
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://github.com/madzak/python-json-logger
Source:         https://files.pythonhosted.org/packages/source/p/python-json-logger/python-json-logger-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
A python library adding a json log formatter.

%prep
%setup -q -n python-json-logger-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
