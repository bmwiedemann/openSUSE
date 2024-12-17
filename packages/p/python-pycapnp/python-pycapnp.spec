#
# spec file for package python-pycapnp
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
Name:           python-pycapnp
Version:        2.0.0
Release:        0
Summary:        Cython wrapping of the C++ Cap'n Proto library
License:        BSD-2-Clause
URL:            https://github.com/capnproto/pycapnp
Source:         https://github.com/capnproto/pycapnp/archive/refs/tags/v%{version}.tar.gz#/pycapnp-%{version}.tar.gz
BuildRequires:  %{python_module Cython with %python-Cython < 3}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(capnp)
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A cython wrapping of the C++ Cap'n Proto library.

%prep
%setup -q -n pycapnp-%{version}
sed -i '1{/^#!/d}' capnp/templates/setup.py.tmpl

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/capnpc-cython
%{python_expand rm %{buildroot}%{$python_sitearch}/capnp/helpers/*.h
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mv capnp/ /tmp
# Attempts to resolve names
%pytest_arch -k 'not (test_ssl_async_example or test_ssl_reconnecting_async_example or test_async_ssl_calculator_example)'
mv /tmp/capnp/ .

%post
%python_install_alternative capnpc-cython

%postun
%python_uninstall_alternative capnpc-cython

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/capnpc-cython
%{python_sitearch}/capnp
%{python_sitearch}/pycapnp-%{version}.dist-info

%changelog
