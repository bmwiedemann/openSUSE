#
# spec file for package python-vegas
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-vegas
Version:        6.3
Release:        0
Summary:        Tools for adaptive multidimensional Monte Carlo integration
License:        GPL-3.0-only
URL:            https://github.com/gplepage/vegas
Source:         https://files.pythonhosted.org/packages/source/v/vegas/vegas-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module numpy >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module gvar >= 13.1.5}
BuildRequires:  %{python_module numpy >= 2.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-gvar >= 13.1.5
Requires:       python-numpy >= 2.0
%python_subpackages

%description
Tools for adaptive multidimensional Monte Carlo integration.

%prep
%autosetup -p1 -n vegas-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt LICENSE.txt
%{python_sitearch}/vegas
%{python_sitearch}/vegas-%{version}.dist-info

%changelog
