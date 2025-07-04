#
# spec file for package python-tri.struct
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


Name:           python-tri.struct
Version:        4.1.0
Release:        0
Summary:        Python dictionaries with attribute access
License:        BSD-3-Clause
URL:            https://github.com/TriOptima/tri.struct
Source:         https://github.com/TriOptima/tri.struct/archive/%{version}.tar.gz#/tri.struct-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
tri.struct supplies classes that can be used like dictionaries and as
objects with attribute access at the same time.

%prep
%setup -q -n tri.struct-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitearch}/tri_struct
%{python_sitearch}/tri[._]struct-%{version}.dist-info

%changelog
