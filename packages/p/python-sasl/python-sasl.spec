#
# spec file for package python-sasl
#
# Copyright (c) 2024 SUSE LLC
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
URL:            https://github.com/cloudera/python-sasl
Source:         https://files.pythonhosted.org/packages/source/s/sasl/sasl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#cloudera/python-sasl#32
Patch0:         cythonize-during-build.patch
# PATCH-FIX-UPSTREAM https://github.com/cloudera/python-sasl/pull/33 Drop python-six dependency
Patch1:         remove-six.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsasl2)
%python_subpackages

%description
Cyrus-SASL bindings for Python.

%prep
%autosetup -p1 -n sasl-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# Don't ship generated sources
%python_expand rm %{buildroot}%{$python_sitearch}/sasl/saslwrapper.{cpp,h}

%files %{python_files}
%doc PKG-INFO
%license LICENSE.txt
%{python_sitearch}/sasl
%{python_sitearch}/sasl-%{version}.dist-info

%changelog
