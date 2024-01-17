#
# spec file for package python-msgspec
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-msgspec
Version:        0.18.5
Release:        0
Summary:        A fast serialization and validation library
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
Source:         https://github.com/jcrist/msgspec/archive/refs/tags/%{version}.tar.gz#/msgspec-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-msgpack
Suggests:       python-attrs
Suggests:       python-furo
Suggests:       python-ipython
Suggests:       python-tomli_w
Suggests:       python-pyyaml
%python_subpackages

%description
A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.

%prep
%autosetup -p1 -n msgspec-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/msgspec
%{python_sitearch}/msgspec-%{version}.dist-info

%changelog
