#
# spec file for package python-dukpy-kovidgoyal
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


%{?sle15_python_module_pythons}
Name:           python-dukpy-kovidgoyal
Version:        0.3
Release:        0
Summary:        JavaScript in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kovidgoyal/dukpy
Source:         https://github.com/kovidgoyal/dukpy/archive/v%{version}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-dukpy

%python_subpackages

%description
DukPy is a JavaScript runtime environment for Python using the duktape
embeddable JavaScript engine. With dukpy, you can run JavaScript in
Python.

%prep
%autosetup -p1 -n dukpy-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
