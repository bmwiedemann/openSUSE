#
# spec file for package python-frozenlist
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-frozenlist
Version:        1.3.3
Release:        0
Summary:        Python list-like structure which implements MutableSequence
License:        Apache-2.0
URL:            https://github.com/aio-libs/frozenlist
Source:         https://files.pythonhosted.org/packages/source/f/frozenlist/frozenlist-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.24}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python list-like structure which implements collections.abc.MutableSequence.

%prep
%setup -q -n frozenlist-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/frozenlist
%{python_sitearch}/frozenlist-%{version}*-info

%changelog
