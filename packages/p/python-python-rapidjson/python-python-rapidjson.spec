#
# spec file for package python-python-rapidjson
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
# check git submodule and update devel:libraries:c_c++/rapidjson
%define rjversion 1.1.0+git20211015.4d6cb081
Name:           python-python-rapidjson
Version:        1.9
Release:        0
Summary:        Python wrapper around rapidjson
License:        MIT
URL:            https://github.com/python-rapidjson/python-rapidjson
Source:         https://github.com/python-rapidjson/python-rapidjson/archive/v%{version}.tar.gz#/python-rapidjson-%{version}.tar.gz
Patch0:         rapidjson-system.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  rapidjson-devel = %{rjversion}
%python_subpackages

%description
RapidJSON is a C++ JSON parser and serialization library. This
module wraps it into a Python 3 extension, exposing its
serialization/deserialization (to/from either bytes, str or file-like
instances) and JSON Schema validation capabilities.

%prep
%setup -q -n python-rapidjson-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF-8
%pytest_arch tests -s

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/rapidjson.*.so
%{python_sitearch}/python_rapidjson-%{version}*-info

%changelog
