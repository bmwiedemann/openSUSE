#
# spec file for package python-cbor
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


Name:           python-cbor
Version:        1.0.0
Release:        0
Summary:        RFC 7049 - Concise Binary Object Representation
License:        Apache-2.0
URL:            https://github.com/brianolson/cbor_py
Source:         https://files.pythonhosted.org/packages/source/c/cbor/cbor-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/brianolson/cbor_py/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
RFC 7049 - Concise Binary Object Representation

%prep
%setup -q -n cbor-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="-fno-strict-aliasing %{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%{python_sitearch}/cbor
%{python_sitearch}/cbor-%{version}.dist-info

%changelog
