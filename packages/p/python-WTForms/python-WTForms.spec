#
# spec file for package python-WTForms
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-WTForms
Version:        2.3.3
Release:        0
Summary:        A flexible forms validation and rendering library for Python web development
License:        BSD-3-Clause
URL:            http://wtforms.simplecodes.com/
Source:         https://files.pythonhosted.org/packages/source/W/WTForms/WTForms-%{version}.tar.gz
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module email_validator}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-MarkupSafe
Requires:       python-email_validator
Recommends:     python-Babel
Recommends:     python-Django
Recommends:     python-SQLAlchemy
Recommends:     python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
Provides:       python-WTForms-lang
Obsoletes:      python-WTForms-lang
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

%prep
%setup -q -n WTForms-%{version}

%build
%python_build
# Fix wrong EOL-encoding
sed -i "s/\r//" CHANGES.rst 
# remove reference to ../CHANGES.rst
rm docs/changes.rst

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
%python_expand $python runtests.py
popd

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%files -n %{name}-doc
%doc docs/*.rst

%changelog
