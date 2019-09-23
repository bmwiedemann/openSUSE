#
# spec file for package python-atom
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-atom
Version:        0.4.3
Release:        0
Summary:        Memory efficient Python objects
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/nucleic/atom
Source:         https://github.com/nucleic/atom/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
Atom is a framework for creating memory efficient Python objects with
enhanced features such as dynamic initialization, validation, and
change notification for object attributes. It provides the default
model binding behaviour for the Enaml UI framework.

%prep
%setup -q -n atom-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
