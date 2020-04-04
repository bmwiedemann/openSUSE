#
# spec file for package python-versiontag
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
Name:           python-versiontag
Version:        1.2.0
Release:        0
Summary:        Python git tag based version numbers
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/thelabnyc/python-versiontag
Source:         https://files.pythonhosted.org/packages/source/v/versiontag/versiontag-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
BuildArch:      noarch
%python_subpackages

%description
Simple git tag based version numbers.

%prep
%setup -q -n versiontag-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/versiontag/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE.md
%{python_sitelib}/*

%changelog
