#
# spec file for package python-Bottleneck
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
%define skip_python36 1
Name:           python-Bottleneck
Version:        1.3.2
Release:        0
Summary:        A collection of fast NumPy array functions
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/pydata/bottleneck
Source0:        https://files.pythonhosted.org/packages/source/B/Bottleneck/Bottleneck-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.16.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.16.0
%python_subpackages

%description
Bottleneck is a collection of fast NumPy array functions written in C.

%prep
%setup -q -n Bottleneck-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch %{buildroot}%{$python_sitearch}/bottleneck/tests/

%files %{python_files}
%license LICENSE
%doc README.rst RELEASE.rst
%{python_sitearch}/bottleneck/
%{python_sitearch}/Bottleneck-%{version}-py*.egg-info

%changelog
