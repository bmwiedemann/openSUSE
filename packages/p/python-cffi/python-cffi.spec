#
# spec file for package python-cffi
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-cffi
Version:        1.16.0
Release:        0
Summary:        Foreign Function Interface for Python calling C code
License:        MIT
URL:            https://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/c/cffi/cffi-%{version}.tar.gz
Source1:        python-cffi-rpmlintrc
Patch1:         https://github.com/python-cffi/cffi/commit/49127c6929bfc7186fbfd3819dd5e058ad888de4.patch#/py313-use-format-unraisable.patch
Patch2:         https://github.com/python-cffi/cffi/commit/14723b0bbd127790c450945099db31018d80fa83.patch#/py313-compat.patch
Patch3:         https://github.com/python-cffi/cffi/commit/c27335f0f8e1e4436082236e92ddabe1b8324d22.patch#/py313-use-hashpointer.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libffi)
Requires:       python-pycparser
%python_subpackages

%description
Foreign Function Interface for Python calling C code. The aim of this project
is to provide a convenient and reliable way of calling C code from Python.

%prep
%autosetup -p1 -n cffi-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -W ignore::UserWarning src/c/ testing/

%files %{python_files}
%license LICENSE
%doc README.md doc/source/*.rst doc/misc/*.rst
%{python_sitearch}/cffi
%{python_sitearch}/_cffi_backend.*.so
%{python_sitearch}/cffi-%{version}*-info

%changelog
