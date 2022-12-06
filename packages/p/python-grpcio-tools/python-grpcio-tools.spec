#
# spec file for package python-grpcio-tools
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


# PYTHON2 NOT SUPPORTED BY UPSTREAM
%define         skip_python2 1

Name:           python-grpcio-tools
Version:        1.51.1
Release:        0
Summary:        Protobuf code generator for gRPC
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://grpc.io
Source:         https://files.pythonhosted.org/packages/source/g/grpcio-tools/grpcio-tools-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-grpcio >= %{version}
Requires:       python-protobuf >= 3.5.0.post1
# SECTION test requirements
BuildRequires:  %{python_module grpcio >= %{version}}
BuildRequires:  %{python_module protobuf >= 3.5.0.post1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package provides a python-based Protobuf code generator for gRPC.

%prep
%setup -q -n grpcio-tools-%{version}
# Drop a hashbang from anon-exec script
sed -i "1{/\/usr\/bin\/env python/d}" grpc_tools/protoc.py

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%{python_sitearch}/*

%changelog
