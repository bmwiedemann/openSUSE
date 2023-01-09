#
# spec file for package python-fastremap
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-fastremap
Version:        1.13.3
Release:        0
Summary:        Module to Remap, mask, renumber, and in-place transpose numpy arrays
License:        LGPL-3.0-only
URL:            https://github.com/seung-lab/fastremap/
Source:         https://files.pythonhosted.org/packages/source/f/fastremap/fastremap-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.16.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.16.0
%python_subpackages

%description
A module to remap, mask, renumber, and in-place transpose numpy arrays.

%prep
%setup -q -n fastremap-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{python_sitearch}/*

%changelog
