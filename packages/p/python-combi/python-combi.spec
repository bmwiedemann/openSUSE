#
# spec file for package python-combi
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-combi
Version:        1.1.4
Release:        0
Summary:        A Pythonic package for combinatorics
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/combi/
Source:         https://files.pythonhosted.org/packages/source/c/combi/combi-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Recommends:     python-pytest
BuildArch:      noarch
%python_subpackages

%description
Combi lets you explore spaces of permutations and combinations as if they
were Python sequences, but without generating all the permutations/combinations
in advance. It lets you specify a lot of special conditions on these spaces. It
also provides a few more classes that might be useful in combinatorics
programming.

%prep
%autosetup -p1 -n combi-%{version}

# Fix CRLF -> LF
sed -i -e 's/\r//g' docs/changelog.txt

# Remove unnecessary nosetests.xml
rm source_py*/test_combi/nosetests.xml

%build
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitelib}/combi/MIT_license.txt
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest source_py3/test_combi

%files %{python_files}
%license source_py3/combi/MIT_license.txt
%doc docs/changelog.txt
%{python_sitelib}/combi-%{version}-py*.egg-info
%{python_sitelib}/combi/
%{python_sitelib}/test_combi/

%changelog
