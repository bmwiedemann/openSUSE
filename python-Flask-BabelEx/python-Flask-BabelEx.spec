#
# spec file for package python-Flask-BabelEx
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

%bcond_without test
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-BabelEx
Version:        0.9.3
Release:        0
License:        BSD-3-Clause
Summary:        i18n/l10n support for Flask applications
Url:            http://github.com/mrjoes/flask-babelex
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/F/Flask-BabelEx/Flask-BabelEx-%{version}.tar.gz
Patch0:         remove-failing-tests.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
%if %{with test}
BuildRequires:  %{python_module Babel >= 1.0}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2 >= 2.5}
BuildRequires:  %{python_module speaklater >= 1.2}
%endif
BuildRequires:  fdupes
Requires:       python-Babel >= 1.0
Requires:       python-Flask
Requires:       python-Jinja2 >= 2.5
Requires:       python-speaklater >= 1.2
BuildArch:      noarch

%python_subpackages

%description
This package adds i18n/l10n support to Flask applications with the help of the Babel library.
This is a fork of the official Flask-Babel extension with some more features.

%prep
%setup -q -n Flask-BabelEx-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec tests/tests.py
%endif

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
