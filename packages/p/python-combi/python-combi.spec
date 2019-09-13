#
# spec file for package python-combi
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
Name:           python-combi
Version:        1.1.2
Release:        0
Summary:        A Pythonic package for combinatorics
License:        MIT
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/combi/
Source:         https://files.pythonhosted.org/packages/source/c/combi/combi-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nose >= 1.0.0}
# /SECTION
Recommends:     python-nose >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Combi lets you explore spaces of permutations and combinations as if they
were Python sequences, but without generating all the permutations/combinations
in advance. It lets you specify a lot of special conditions on these spaces. It
also provides a few more classes that might be useful in combinatorics
programming.

%prep
%setup -q -n combi-%{version}
sed -i -e '/^#!\//, 1d' */test_combi/scripts/_test_combi.py
chmod a-x */test_combi/scripts/_test_combi.py

%build
%python_build

%install
%python_install
rm %{buildroot}%{_bindir}/_test_combi
%{python_expand rm %{buildroot}%{$python_sitelib}/combi/MIT_license.txt
%fdupes %{buildroot}%{$python_sitelib}
}

%check
pushd docs
%{python_expand export PYTHONPATH="%{buildroot}%{$python_sitelib}" 
$python %{buildroot}%{$python_sitelib}/test_combi/scripts/_test_combi.py
}
popd

%files %{python_files}
%license source_py2/combi/MIT_license.txt
%doc docs/changelog.txt
%{python_sitelib}/combi-%{version}-py*.egg-info
%{python_sitelib}/combi/
%{python_sitelib}/test_combi/

%changelog
