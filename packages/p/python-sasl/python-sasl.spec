#
# spec file for package python-sasl
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


%bcond_without test
Name:           python-sasl
Version:        0.3.1
Release:        0
Summary:        SASL for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/cloudera/python-sasl
Source:         https://files.pythonhosted.org/packages/source/s/sasl/sasl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-311.patch gh#cloudera/python-sasl#31
Patch0:         python-311.patch
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
%autosetup -p1 -n sasl-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc PKG-INFO
%license LICENSE.txt
%{python_sitearch}/sasl
%{python_sitearch}/sasl-%{version}*-info

%changelog
