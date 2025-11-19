#
# spec file for package python-protobuf
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define baseversion 33.1
%{?sle15_python_module_pythons}
Name:           python-protobuf
Version:        6.%{baseversion}
Release:        0
Summary:        Python Bindings for Google Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://files.pythonhosted.org/packages/source/p/protobuf/protobuf-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
%python_subpackages

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

This package contains the Python bindings for Google Protocol Buffers.

%prep
%autosetup -p2 -n protobuf-%{version}

# The previous blank line is crucial for older system being able
# to use the autosetup macro

grep -qF "'%{version}'" google/protobuf/__init__.py

# kill shebang that we do not really want
sed -i -e '/env python/d' google/protobuf/internal/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%fdupes %{buildroot}%{_prefix}

%files %{python_files}
%license LICENSE
%{python_sitearch}/google
%{python_sitearch}/protobuf-%{version}.dist-info

%changelog
