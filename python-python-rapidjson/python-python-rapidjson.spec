#
# spec file for package python-python-rapidjson
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-rapidjson
Version:        0.7.2
Release:        0
Summary:        Python wrapper around rapidjson
License:        MIT
Group:          Development/Languages/Python
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
BuildRequires:  rapidjson-devel
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

%check
export LANG=en_US.UTF-8
%pytest_arch tests

%files %{python_files}
%doc CHANGE* README*
%license LICENSE*
%{python_sitearch}/*

%changelog
