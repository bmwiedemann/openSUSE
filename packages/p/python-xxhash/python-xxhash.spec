#
# spec file for package python-xxhash
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


%{?sle15_python_module_pythons}
Name:           python-xxhash
Version:        3.5.0
Release:        0
Summary:        Python binding for xxHash
License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
Source:         https://files.pythonhosted.org/packages/source/x/xxhash/xxhash-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xxhash-devel
%python_subpackages

%description
xxhash is a Python binding for the xxHash library.

%prep
%setup -q -n xxhash-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export LANG=en_US.UTF-8
export XXHASH_LINK_SO=1
%pyproject_wheel

%install
export LANG=en_US.UTF-8
export XXHASH_LINK_SO=1
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF-8
export XXHASH_LINK_SO=1
mv xxhash{,.hide}
%pyunittest_arch discover -v
mv xxhash{.hide,}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/xxhash
%{python_sitearch}/xxhash-%{version}.dist-info

%changelog
