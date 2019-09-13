#
# spec file for package python-ana
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
Name:           python-ana
Version:        0.06
Release:        0
Summary:        The Python "ana" module
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/zardus/ana
Source:         https://files.pythonhosted.org/packages/source/a/ana/ana-%{version}.tar.gz
# https://github.com/zardus/ana/issues/13
Source2:        https://raw.githubusercontent.com/zardus/ana/master/test.py
Source3:        https://raw.githubusercontent.com/zardus/ana/master/test_pickle.p
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
A Python module that provides an undocumented data layer for Python objects.

%prep
%setup -q -n ana-%{version}
[ -e test.py ] || cp %{SOURCE2} test.py
[ -e test_pickle.p ] || cp %{SOURCE3} test_pickle.p

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
