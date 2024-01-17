#
# spec file for package python-ana
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


%define internal_version 0.6
Name:           python-ana
Version:        0.06
Release:        0
Summary:        The Python "ana" module
License:        BSD-2-Clause
URL:            https://github.com/zardus/ana
Source:         https://files.pythonhosted.org/packages/source/a/ana/ana-%{version}.tar.gz
# https://github.com/zardus/ana/issues/13
Source2:        test.py
Source3:        https://raw.githubusercontent.com/zardus/ana/master/test_pickle.p
# https://github.com/zardus/ana/commit/7f3c0dd8bd9ed89e3e146f934212516831147c51
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python module that provides an undocumented data layer for Python objects.

%prep
%autosetup -p1 -n ana-%{version}
cp %{SOURCE2} test.py
cp %{SOURCE3} test_pickle.p

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ana
%if %python_version_nodots < 38
%{python_sitelib}/ana-%{version}*-info
%else
%{python_sitelib}/ana-%{internal_version}*-info
%endif

%changelog
