#
# spec file for package python-Flask-WTF
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-Flask-WTF
Version:        0.14.2
Release:        0
Summary:        WTForms support for Flask
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/lepture/flask-wtf
Source:         https://files.pythonhosted.org/packages/source/F/Flask-WTF/Flask-WTF-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-WTForms
Requires:       python-Werkzeug
Requires:       python-itsdangerous
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask-Babel}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module nose}
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
%python_expand nosetests-%{$python_bin_suffix} tests
%endif

%files %{python_files}
%doc AUTHORS LICENSE README.rst
%{python_sitelib}/*

%changelog
