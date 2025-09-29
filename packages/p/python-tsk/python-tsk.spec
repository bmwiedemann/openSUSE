#
# spec file for package python-tsk
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           python-tsk
Version:        20250729
Release:        0
Summary:        Python bindings for tsk (The SleuthKit)
# the included talloc library is LGPL 3
License:        Apache-2.0 AND LGPL-3.0-or-later
URL:            https://github.com/py4n6/pytsk/
Source:         https://files.pythonhosted.org/packages/source/p/pytsk3/pytsk3-%{version}.tar.gz
Source2:        https://github.com/py4n6/pytsk/releases/download/%{version}/pytsk3-%{version}.tar.gz.asc
Source3:        python-tsk.keyring
#PATCH-FIX-UPSTREAM fix-rename-bool-variable.patch taken from https://github.com/py4n6/pytsk/pull/111/
Patch0:         fix-rename-bool-variable.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtalloc-devel
BuildRequires:  postgresql-devel
BuildRequires:  python-rpm-macros
BuildRequires:  sleuthkit-devel >= 4.10.2
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libvhdi)
BuildRequires:  pkgconfig(libvmdk)

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%python_subpackages

%description
The Sleuthkit is a forensic filesystem analysis framework (http://www.sleuthkit.org/). This project is a python 3 binding for the sleuthkit.

%prep
%autosetup -p1 -n pytsk3-%{version}
# remove unused libraries with incompatible license, use libtalloc from main repositories
# rm -rf pytsk talloc
# rm -rf pytsk talloc.new

%build
CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# pytest is NOT suppoerted (see gh#py4n6/pytsk#48)
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python ./run_tests.py
}

%files %{python_files}
%doc README
%license LICENSE
%{python_sitearch}/pytsk3-%{version}.dist-info
%{python_sitearch}/pytsk3.*.so

%changelog
