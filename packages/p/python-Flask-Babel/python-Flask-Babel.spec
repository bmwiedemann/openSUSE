#
# spec file for package python-Flask-Babel
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 Dr. Axel Braun
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
%define skip_python2 1
Name:           python-Flask-Babel
Version:        2.0.0
Release:        0
Summary:        i18n and l10n support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-babel/flask-babel
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Babel/Flask-Babel-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 2.3}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2 >= 2.5}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 2.3
Requires:       python-Flask
Requires:       python-Jinja2 >= 2.5
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
This module implements i18n and l10n support for Flask. It is based on
the Python babel module as well as pytz.

%prep
%setup -q -n Flask-Babel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/flask_babel
%{python_sitelib}/flask_babel/*
%{python_sitelib}/Flask_Babel-%{version}-py*.egg-info

%changelog
