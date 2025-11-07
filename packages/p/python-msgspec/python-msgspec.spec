#
# spec file for package python-msgspec
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-msgspec
Version:        0.19.0
Release:        0
Summary:        A fast serialization and validation library
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
Source:         https://github.com/jcrist/msgspec/archive/refs/tags/%{version}.tar.gz#/msgspec-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#jcrist/msgspec#852 & gh#jcrist/msgspec#854
Patch0:         support-python314.patch
BuildRequires:  %{python_module devel >= 3.9}
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
# Requires to import the module, but other tests require the path
# Can be dropped next release
donttest="test_raw_copy_doesnt_leak"
if [ $(getconf LONG_BIT) = 32 ]; then
    # Overflow errors on 32 bit arches
    donttest="$donttest or test_hashtable or test_decoding_large_arrays or test_timestamp"
fi
%pytest_arch -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/msgspec
%{python_sitearch}/msgspec-%{version}.dist-info

%changelog
