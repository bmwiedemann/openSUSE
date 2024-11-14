#
# spec file for package python-Flask-WTF
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


%bcond_without     test
%{?sle15_python_module_pythons}
Name:           python-Flask-WTF
Version:        1.2.2
Release:        0
Summary:        WTForms support for Flask
License:        BSD-3-Clause
URL:            https://github.com/lepture/flask-wtf
Source:         https://files.pythonhosted.org/packages/source/F/Flask-WTF/flask_wtf-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-WTForms
Requires:       python-Werkzeug
Requires:       python-itsdangerous
Recommends:     python-email_validator
BuildArch:      noarch
%if %{with test}
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
%autosetup -p1 -n flask_wtf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/flask_wtf-%{version}.dist-info

%changelog
