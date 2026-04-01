#
# spec file for package python-soxr
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-soxr
Version:        1.0.0
Release:        0
Summary:        High quality, one-dimensional sample-rate conversion library
License:        LGPL-2.1-or-later
URL:            https://github.com/dofuuz/python-soxr
Source:         https://files.pythonhosted.org/packages/source/s/soxr/soxr-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nanobind-devel >= 2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build-core >= 0.10}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  soxr-devel >= 0.1.3
Requires:       python-numpy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
High quality, one-dimensional sample-rate conversion library

%prep
%setup -q -n soxr-%{version}
# make sure we use the library from the system
rm -r libsoxr

%build
export CFLAGS="%{optflags}"
export SKBUILD_CMAKE_ARGS="-DUSE_SYSTEM_LIBSOXR=ON"
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license COPYING.LGPL LICENSE.txt
%{python_sitearch}/soxr
%{python_sitearch}/soxr-%{version}.dist-info

%changelog
