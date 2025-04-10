#
# spec file for package python-WTForms
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-WTForms
Version:        3.2.1
Release:        0
Summary:        A flexible forms validation and rendering library for Python web development
License:        BSD-3-Clause
URL:            https://github.com/wtforms/wtforms
Source:         https://files.pythonhosted.org/packages/source/W/WTForms/wtforms-%{version}.tar.gz
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module email-validator}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-MarkupSafe
Requires:       python-email-validator
Recommends:     python-Babel
Recommends:     python-Django
Recommends:     python-SQLAlchemy
Recommends:     python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Babel >= 2.6.0}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
WTForms is a forms validation and rendering library for Python web development.
With WTForms, form field HTML can be generated and be customized with templates.
This allows to maintain separation of code and presentation, and keep those parameters out of Python code.
Because of this loose coupling, any template engine may be used for this.

%package -n %{name}-doc
Summary:        Documentation for WTForms

%description -n %{name}-doc
Documentation for WTForms, which is a forms validation and rendering library for Python web development.

%package lang
Summary:        Translations for builtin WTForms messages
Requires:       %{name} = %{version}
Provides:       python-WTForms-lang = %{version}
Obsoletes:      python-WTForms-lang < %{version}

%description lang
Translations for builtin WTForms messages.

WTForms is a forms validation and rendering library for Python web development.

%prep
%autosetup -p1 -n wtforms-%{version}

%build
%pyproject_wheel
# Fix wrong EOL-encoding
sed -i "s/\r//" CHANGES.rst
# remove reference to ../CHANGES.rst
rm docs/changes.rst

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_find_lang wtforms

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%exclude %{python_sitelib}/wtforms/locale
%{python_sitelib}/wtforms
%{python_sitelib}/wtforms-%{version}.dist-info

%files -n %{name}-doc
%doc docs/*.rst

%files %{python_files lang} -f %{python_prefix}-wtforms.lang
%{python_sitelib}/wtforms/locale

%changelog
