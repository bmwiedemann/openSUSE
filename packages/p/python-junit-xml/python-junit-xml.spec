#
# spec file for package python-junit-xml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-junit-xml
Version:        1.8
Release:        0
Summary:        Module that creates JUnit XML test result documents
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/kyrus/python-junit-xml
Source:         https://files.pythonhosted.org/packages/source/j/junit-xml/junit-xml-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
