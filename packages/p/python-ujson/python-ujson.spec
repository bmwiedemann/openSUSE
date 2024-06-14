#
# spec file for package python-ujson
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
Name:           python-ujson
Version:        5.10.0
Release:        0
Summary:        JSON encoder and decoder for Python
License:        BSD-3-Clause
URL:            https://github.com/esnme/ultrajson
Source:         https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros

%python_subpackages

%description
An ultrafast JSON encoder and decoder written in pure C with
bindings for Python 2.7 and 3.8+

%prep
%setup -q -n ujson-%{version}
%autopatch -p1

%build
rm -r deps
export CFLAGS="%{optflags} -fno-strict-aliasing"
export UJSON_BUILD_DC_INCLUDES='%{_includedir}/double-conversion'
export UJSON_BUILD_DC_LIBS='-ldouble-conversion'
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%{python_sitearch}/ujson.*
%{python_sitearch}/ujson-%{version}*-info

%changelog
