#
# spec file for package python-duckduckgo2
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-duckduckgo2
Version:        0.242
Release:        0
Summary:        Library for querying the DuckDuckGo API
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/crazedpsyc/python-duckduckgo/
Source:         https://files.pythonhosted.org/packages/source/d/duckduckgo2/duckduckgo2-%{version}.tar.gz
Patch0:         add-python3-support.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python library for querying the DuckDuckGo API.

%prep
%setup -q -n duckduckgo2-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/ddg
%{python_sitelib}/*

%changelog
