#
# spec file for package python-munch
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-munch
Version:        2.5.0
Release:        0
Summary:        A dot-accessible dictionary
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/Infinidat/munch
Source:         https://files.pythonhosted.org/packages/source/m/munch/munch-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A dot-accessible dictionary (a la JavaScript objects).

%prep
%setup -q -n munch-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
