#
# spec file for package python-Jinja2
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


%ifarch %{ix86} armv7l
%bcond_with test
%else
%bcond_without test
%endif
%{?sle15_python_module_pythons}
Name:           python-Jinja2
Version:        3.1.5
Release:        0
Summary:        A template engine written in pure Python
License:        BSD-3-Clause
URL:            https://jinja.palletsprojects.com
Source:         https://files.pythonhosted.org/packages/source/J/Jinja2/jinja2-%{version}.tar.gz
BuildRequires:  %{python_module MarkupSafe >= 0.23}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-MarkupSafe >= 0.23
Recommends:     python-Babel >= 0.8
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
%autosetup -p1 -n jinja2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}
find . -name '*.pyc' -exec rm -f '{}' ';'
python%python_bin_suffix -m compileall *.py ';'
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
# Test broken with latest version of MarkupSafe (2.1.4)
# gh#pallets/jinja#1930, gh#pallets/markupsafe#417
donttest="test_striptags"
%pytest -W ignore:'Support for nose tests is deprecated' -k "not ($donttest)"
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.md docs/changes.rst docs/examples
%{python_sitelib}/jinja2
%{python_sitelib}/jinja2-%{version}.dist-info

%changelog
