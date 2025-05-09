#
# spec file for package python-defusedxml
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


%bcond_without tests
%{?sle15_python_module_pythons}
Name:           python-defusedxml
Version:        0.7.1
Release:        0
Summary:        XML bomb protection for Python stdlib modules
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/defusedxml
Source:         https://files.pythonhosted.org/packages/source/d/defusedxml/defusedxml-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xml}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
BuildArch:      noarch
%python_subpackages

%description
The results of an attack on a vulnerable XML library can be fairly dramatic.
With just a few hundred bytes of XML data an attacker can occupy several
gigabytes of memory within seconds. An attacker can also keep
CPUs busy for a long time with a small to medium size request.

This library allows for XML to be parsed in a manner that avoids these
pitfalls.

%prep
%setup -q -n defusedxml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
# see test_main() in tests.py; test_html_arg: deprecation warning is not raised, perhaps capturing wrongly setup?
usable_tests=$(grep addTests tests.py | sed 's:.*makeSuite(\([a-zA-Z]*\)).*:\1:' | tr '\n' ' ' | sed -e 's: $::' -e 's: : or :g')
%pytest -s -k "($usable_tests) and not test_html_arg"
%endif

%files %{python_files}
%license LICENSE
%doc README.txt CHANGES.txt
%{python_sitelib}/defusedxml
%{python_sitelib}/defusedxml-%{version}.dist-info

%changelog
