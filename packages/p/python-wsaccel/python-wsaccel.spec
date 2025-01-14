#
# spec file for package python-wsaccel
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


%{?sle15_python_module_pythons}
Name:           python-wsaccel
Version:        0.6.7
Release:        0
Summary:        Accelerator for ws4py and AutobahnPython
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/methane/wsaccel
Source:         https://github.com/methane/wsaccel/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
WSAccell is WebSocket accelerator for `AutobahnPython <http://autobahn.ws/python>`_,
`ws4py <https://github.com/Lawouach/WebSocket-for-Python>`_ and
`Tornado <http://www.tornadoweb.org/>`_.

%prep
%setup -q -n wsaccel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Tests do work on py3 only
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest-%{python3_bin_suffix} tests

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitearch}/wsaccel
%{python_sitearch}/wsaccel-%{version}.dist-info

%changelog
