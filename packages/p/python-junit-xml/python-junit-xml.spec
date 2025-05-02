#
# spec file for package python-junit-xml
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
Name:           python-junit-xml
Version:        1.9
Release:        0
Summary:        Module that creates JUnit XML test result documents
License:        MIT
URL:            https://github.com/kyrus/python-junit-xml
# 1.9 source not published on pypi
#Source:         https://files.pythonhosted.org/packages/source/j/junit-xml/junit-xml-%{version}.tar.gz
Source:         junit-xml-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Creates JUnit XML test result documents
that can be read by tools such as Jenkins.

%prep
%setup -q -n junit-xml-%{version}
sed -i '1{/^#!/d}' junit_xml/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/junit_xml
%{python_sitelib}/junit_xml-%{version}.dist-info

%changelog
