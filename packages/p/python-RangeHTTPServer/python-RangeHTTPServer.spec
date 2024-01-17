#
# spec file for package python-rangehttpserver
#
# Copyright (c) 2023 SUSE LLC
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


%define modname RangeHTTPServer
Name:           python-%{modname}
Version:        1.3.3
Release:        0
Summary:        SimpleHTTPServer with support for Range requests
License:        Apache-2.0
URL:            https://github.com/danvk/RangeHTTPServer/
# PyPI tarball does not contain tests
Source:         https://github.com/danvk/RangeHTTPServer/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# Section test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /Section
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
SimpleHTTPServer with support for Range requests

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/rangehttpserver-%{version}.dist-info

%changelog
