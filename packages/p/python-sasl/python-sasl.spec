#
# spec file for package python-sasl
#
# Copyright (c) 2021 SUSE LLC
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
%bcond_without test
Name:           python-sasl
Version:        0.2.1
Release:        0
Summary:        SASL for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/cloudera/python-sasl
Source:         https://files.pythonhosted.org/packages/source/s/sasl/sasl-%{version}.tar.gz
Patch0:         regenerate-cpp-wrappers.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsasl2)
Requires:       python-six
%python_subpackages

%description
Cyrus-SASL bindings for Python.

%prep
%setup -q -n sasl-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc PKG-INFO
%license LICENSE.txt
%{python_sitearch}/*

%changelog
