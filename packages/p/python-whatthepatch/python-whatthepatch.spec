#
# spec file for package python-whatthepatch
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
%define skip_python2 1
Name:           python-whatthepatch
Version:        1.0.0
Release:        0
Summary:        A patch parsing and application library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cscorley/whatthepatch
Source:         https://github.com/cscorley/whatthepatch/archive/%{version}.tar.gz#/whatthepatch-%{version}.tar.gz
Patch0:         no-nose.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  patch
BuildRequires:  python-rpm-macros
Requires:       ed
Requires:       patch
BuildArch:      noarch
%python_subpackages

%description
A patch parsing and application library.

%prep
%setup -q -n whatthepatch-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
