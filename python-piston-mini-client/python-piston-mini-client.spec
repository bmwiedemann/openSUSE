#
# spec file for package python-piston-mini-client
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
%define oldpython python
Name:           python-piston-mini-client
Version:        0.7.5
Release:        0
Summary:        A small package to consume Django-Piston web services
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://launchpad.net/piston-mini-client
Source:         https://files.pythonhosted.org/packages/source/p/piston-mini-client/piston-mini-client-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-oauthlib
BuildArch:      noarch
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module oauthlib}
%ifpython2
Provides:       %{oldpython}-piston-mini = %{version}
Obsoletes:      %{oldpython}-piston-mini < %{version}
%endif
%python_subpackages

%description
A small generic library for writing clients for Django's Piston REST APIs.

%prep
%setup -q -n piston-mini-client-%{version}
rm piston_mini_client/tests/test_pep8.py

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README doc/*.rst
%{python_sitelib}/*

%changelog
