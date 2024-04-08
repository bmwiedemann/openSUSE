#
# spec file for package python-python-redmine
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-redmine
Version:        2.5.0
Release:        0
Summary:        Python library for the Redmine RESTful API
License:        Apache-2.0
URL:            https://python-redmine.com
Source:         https://files.pythonhosted.org/packages/source/p/python-redmine/python-redmine-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.31.0
BuildArch:      noarch
%python_subpackages

%description
Python Redmine is a library for communicating with a Redmine
project management application. Redmine exposes some of it's data
via REST API for which Python Redmine provides a simple but
powerful Pythonic API inspired by a well-known Django ORM.

%prep
%autosetup -p1 -n python-redmine-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not (test_engine_init or test_session_key or test_session_requests)"

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/redminelib
%{python_sitelib}/python_redmine-%{version}.dist-info

%changelog
