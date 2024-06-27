#
# spec file for package python-dukpy
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


Name:           python-dukpy
Version:        0.4.0
Release:        0
Summary:        JavaScript interpreter for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/amol-/dukpy
Source:         https://github.com/amol-/dukpy/archive/%{version}.tar.gz#/dukpy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mutf8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module webassets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mutf8
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
chmod a-x dukpy/jsmodules/react/react-dom-server.js
# remove test that relies on bunch of node binaries
rm tests/test_webassets_filter.py
# remove downloading tests
rm tests/test_installer.py
# https://github.com/amol-/dukpy/issues/60
sed -i 's:import mock:from unittest import mock:' tests/test_evaljs.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/dukpy
%python_clone -a %{buildroot}%{_bindir}/dukpy-install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -v

%post
%python_install_alternative dukpy
%python_install_alternative dukpy-install

%postun
%python_uninstall_alternative dukpy
%python_uninstall_alternative dukpy-install

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/dukpy-install
%python_alternative %{_bindir}/dukpy
%{python_sitearch}/dukpy
%{python_sitearch}/dukpy-%{version}*-info

%changelog
