#
# spec file for package python-lxml_html_clean
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


%{?sle15_python_module_pythons}
Name:           python-lxml_html_clean
Version:        0.1.1
Release:        0
Summary:        HTML cleaner from lxml project
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/fedora-python/lxml_html_clean/
Source:         https://files.pythonhosted.org/packages/source/l/lxml-html-clean/lxml_html_clean-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module lxml}
# /SECTION
BuildRequires:  fdupes
Requires:       python-lxml
BuildArch:      noarch
%python_subpackages

%description
Separate project for HTML cleaning functionalities copied from lxml.html.clean.

%prep
%autosetup -p1 -n lxml_html_clean-%{version}

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
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/lxml_html_clean
%{python_sitelib}/lxml_html_clean-%{version}.dist-info

%changelog
