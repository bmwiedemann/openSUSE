#
# spec file for package python-atom
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-atom
Version:        0.8.2
Release:        0
Summary:        Memory efficient Python objects
License:        BSD-3-Clause
URL:            https://github.com/nucleic/atom
Source:         https://files.pythonhosted.org/packages/source/a/atom/atom-%{version}.tar.gz
BuildRequires:  %{python_module cppy >= 1.2.0}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/atom
%{python_sitearch}/atom-%{version}*-info

%changelog
