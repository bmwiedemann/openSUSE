#
# spec file for package python-ujson
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
Name:           python-ujson
Version:        2.0.1
Release:        0
Summary:        JSON encoder and decoder for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/esnme/ultrajson
Source:         https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
# unbundle double-conversion (https://github.com/ultrajson/ultrajson/issues/375)
Patch0:         python-ujson-system-double-conversion.patch
BuildRequires:  %{python_module blist}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
UltraJSON is a JSON encoder and decoder written in pure C with
bindings for Python 2.5+ and 3. For a different C/C++ JSON
decoder experience please checkout ujson4c_, based on UltraJSON.

%prep
%setup -q -n ujson-%{version}
%autopatch -p1

%build
rm -r deps
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%{python_sitearch}/ujson.*
%{python_sitearch}/ujson-%{version}-py*.egg-info

%changelog
