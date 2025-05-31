#
# spec file for package python-jsonslicer
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


Name:           python-jsonslicer
Version:        0.1.8
Release:        0
Summary:        Streaming JSON parser with iterator interface
License:        MIT
URL:            https://github.com/AMDmi3/jsonslicer
Source:         https://files.pythonhosted.org/packages/source/j/jsonslicer/jsonslicer-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(yajl)
%python_subpackages

%description
JsonSlicer performs a stream or iterative, pull JSON parsing, which
means it does not load whole JSON into memory and is able to parse
very large JSON files or streams. The module is written in C and uses
YAJL JSON parsing library.

JsonSlicer takes a path of JSON map keys or array indexes, and
provides iterator interface which yields JSON data matching
given path as complete Python objects.

%prep
%setup -q -n jsonslicer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitearch}/jsonslicer
%{python_sitearch}/jsonslicer-%{version}*-info
%{python_sitearch}/jsonslicer.cpython*

%changelog
