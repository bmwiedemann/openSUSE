#
# spec file for package python-dukpy
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
Name:           python-dukpy
Version:        0.2.2
Release:        0
Summary:        JavaScript interpreter for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/amol-/dukpy
Source:         https://github.com/amol-/dukpy/archive/%{version}.tar.gz
Patch0:         pytest.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module webassets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-webassets

%python_subpackages

%description
DukPy is a javascript interpreter for Python built on top of
duktape engine.
It comes with a bunch of common transpilers built-in for convenience:

    - CoffeeScript
    - BabelJS
    - TypeScript
    - JSX
    - LESS

%prep
%setup -q -n dukpy-%{version}
%patch0 -p1
chmod a-x dukpy/jsmodules/react/react-dom-server.js
# remove test that relies on bunch of node binaries
rm tests/test_webassets_filter.py
# remove downloading tests
rm tests/test_installer.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH="%{buildroot}%{$python_sitearch}:%{buildroot}%{$python_sitearch}/dukpy" py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/dukpy-install
%python3_only %{_bindir}/dukpy
%{python_sitearch}/*

%changelog
