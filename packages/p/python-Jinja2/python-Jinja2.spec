#
# spec file for package python-Jinja2
#
# Copyright (c) 2021 SUSE LLC
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


%ifarch %{ix86} armv7l
%bcond_with test
%else
%bcond_without test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-Jinja2
Version:        3.0.1
Release:        0
Summary:        A template engine written in pure Python
License:        BSD-3-Clause
URL:            https://jinja.palletsprojects.com
Source:         https://files.pythonhosted.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
BuildRequires:  %{python_module MarkupSafe >= 0.23}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 0.8
Requires:       python-MarkupSafe >= 0.23
# Do not declare buildarch as the tests are arch specific
#BuildArch:      noarch
Provides:       python-jinja2 = %{version}-%{release}
Obsoletes:      python-jinja2 < %{version}-%{release}
%python_subpackages

%description
Jinja2 is a template engine written in pure Python.  It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%prep
%setup -q -n Jinja2-%{version}
dos2unix LICENSE.rst # Fix wrong EOL encoding

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
%pytest
%endif

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst artwork examples
%{python_sitelib}/jinja2
%{python_sitelib}/Jinja2-%{version}-py%{python_version}.egg-info

%changelog
