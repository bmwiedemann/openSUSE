#
# spec file for package python-cbor
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cbor
Version:        1.0.0
Release:        0
Summary:        RFC 7049 - Concise Binary Object Representation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/brianolson/cbor_py
Source:         https://files.pythonhosted.org/packages/source/c/cbor/cbor-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/brianolson/cbor_py/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
%python_subpackages

%description
RFC 7049 - Concise Binary Object Representation

%prep
%setup -q -n cbor-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="-fno-strict-aliasing %{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%{python_sitearch}/*

%changelog
