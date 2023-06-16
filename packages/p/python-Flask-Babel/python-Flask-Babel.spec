#
# spec file for package python-Flask-Babel
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-Flask-Babel
Version:        3.1.0
Release:        0
Summary:        i18n and l10n support for Flask
License:        BSD-3-Clause
URL:            https://github.com/python-babel/flask-babel
Source:         https://github.com/python-babel/flask-babel/archive/refs/tags/v%{version}.tar.gz#/Flask-Babel-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 2.12}
BuildRequires:  %{python_module Flask >= 2.0}
BuildRequires:  %{python_module Jinja2 >= 3.1}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2022.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 2.12
Requires:       python-Flask >= 2.0
Requires:       python-Jinja2 >= 3.1
Requires:       python-pytz >= 2022.7
BuildArch:      noarch
%python_subpackages

%description
This module implements i18n and l10n support for Flask. It is based on
the Python babel module as well as pytz.

%prep
%autosetup -p1 -n flask-babel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_babel
%{python_sitelib}/flask_babel-%{version}.dist-info

%changelog
