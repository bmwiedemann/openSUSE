#
# spec file for package python-wirerope
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
%bcond_without python2
Name:           python-wirerope
Version:        0.4.2
Release:        0
Summary:        The Way to Handle Bound Methods
License:        BSD-2-Clause
URL:            https://github.com/youknowone/wirerope
Source0:        https://github.com/youknowone/wirerope/archive/%{version}.tar.gz#/wirerope-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.11.0
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-inspect2 >= 0.1.0
BuildRequires:  python-singledispatch >= 3.4.0.3
%endif
%ifpython2
Requires:       python-inspect2 >= 0.1.0
Requires:       python-singledispatch >= 3.4.0.3
%endif
%python_subpackages

%description
wirerope.rope.WireRope is the wrapper for callables. By wrapping a function
with WireRope with a custom subclass of the wirerope.wire.Wire class, the
wire object will be created by each function or bound method.

%prep
%setup -q -n wirerope-%{version}
sed -i -e '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
