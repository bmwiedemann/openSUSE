#
# spec file for package python-wsaccel
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
Name:           python-wsaccel
Version:        0.6.2
Release:        0
Summary:        Accelerator for ws4py and AutobahnPython
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/methane/wsaccel
Source:         https://github.com/methane/wsaccel/archive/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/methane/wsaccel/master/LICENSE
Patch0:         fix-encoding.patch
BuildRequires:  %{python_module Cython >= 0.16}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
WSAccell is WebSocket accelerator for `AutobahnPython <http://autobahn.ws/python>`_,
`ws4py <https://github.com/Lawouach/WebSocket-for-Python>`_ and
`Tornado <http://www.tornadoweb.org/>`_.

%prep
%setup -q -n wsaccel-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Tests do work on py3 only
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest-%{python3_bin_suffix} tests

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
