#
# spec file for package python-fpylll
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-fpylll
Version:        0.6.4
Release:        0
Summary:        A Python interface for https://githubcom/fplll/fplll
License:        GPL-3.0-or-later
URL:            https://github.com/fplll/fpylll
Source:         https://files.pythonhosted.org/packages/source/f/fpylll/fpylll-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module cysignals}
BuildRequires:  %{python_module cysignals-devel}
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fplll
BuildRequires:  fplll-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  binutils
Requires:       fplll
%python_subpackages

%description
A Python interface for https://github.com/fplll/fplll

%prep
%autosetup -p1 -n fpylll-%{version}

%build
# Disable _FORTIFY_SOURCE to prevent crashes in cysignals stack switching during signal handling
export CFLAGS="%{optflags} -U_FORTIFY_SOURCE"
export CXXFLAGS="%{optflags} -U_FORTIFY_SOURCE"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
find %{buildroot} -name "*.so" | xargs strip

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE
%{python_sitearch}/fpylll
%{python_sitearch}/fpylll-%{version}.dist-info

%changelog
