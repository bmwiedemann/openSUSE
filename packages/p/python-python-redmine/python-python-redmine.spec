#
# spec file for package python-python-redmine
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-redmine
Version:        2.2.1
Release:        0
Summary:        Python library for the Redmine RESTful API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://python-redmine.com
Source:         https://files.pythonhosted.org/packages/source/p/python-redmine/python-redmine-%{version}.tar.gz
Patch0:         python-python-redmine-use-system-requests.patch
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-requests
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python Redmine is a library for communicating with a Redmine
project management application. Redmine exposes some of it's data
via REST API for which Python Redmine provides a simple but
powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup -q -n python-redmine-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/redminelib/packages/

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
