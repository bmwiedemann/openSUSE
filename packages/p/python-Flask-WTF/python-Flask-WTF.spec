#
# spec file for package python-Flask-WTF
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
%define skip_python2 1
%bcond_without     test
Name:           python-Flask-WTF
Version:        1.0.1
Release:        0
Summary:        WTForms support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lepture/flask-wtf
Source:         https://files.pythonhosted.org/packages/source/F/Flask-WTF/Flask-WTF-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-WTForms
Requires:       python-Werkzeug
Requires:       python-itsdangerous
Recommends:     python-email_validator
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask-BabelEx}
BuildRequires:  %{python_module Flask-Babel}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Adds WTForms support to your Flask application

%prep
%setup -q -n Flask-WTF-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{_prefix}

%if %{with test}
%check
export LANG=en_US.UTF-8
# Excluded tests because of gh#wtforms/wtforms#697
%pytest -k 'not (test_set_default_message_language or test_i18n)' tests
%endif

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/flask_wtf
%{python_sitelib}/Flask_WTF-%{version}-py*.egg-info

%changelog
