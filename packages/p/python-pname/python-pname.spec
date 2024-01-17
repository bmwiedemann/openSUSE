#
# spec file for package python-pname
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pname
Version:        1.0.2
Release:        0
Summary:        Check whether a package name is available on PyPI
License:        MIT
URL:            https://gitlab.com/yo/pname
Source:         https://files.pythonhosted.org/packages/source/p/pname/pname-%{version}.tar.gz
Source99:       https://gitlab.com/yo/pname/-/raw/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Check whether a package name is available on PyPI

%prep
%setup -q -n pname-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the tests are online as they poll pypi.org

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
