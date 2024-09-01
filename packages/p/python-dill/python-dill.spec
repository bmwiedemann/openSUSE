#
# spec file for package python-dill
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
Name:           python-dill
Version:        0.3.8
Release:        0
Summary:        Module to serialize all of Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/uqfoundation/dill
Source:         https://github.com/uqfoundation/dill/archive/refs/tags/%{version}.tar.gz#/dill-%{version}.tar.gz
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module objgraph >= 1.7.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-objgraph >= 1.7.2
BuildArch:      noarch
%python_subpackages

%description
Dill extends python's `pickle` module for serializing and de-serializing
python objects to the majority of the built-in python types. Serialization
is the process of converting an object to a byte stream, and the inverse
of which is converting a byte stream back to on python object hierarchy.

Dill provides the user the same interface as the `pickle` module, and
also includes some additional features. In addition to pickling python
objects, `dill` provides the ability to save the state of an interpreter
session in a single command.

%prep
%autosetup -p1 -n dill-%{version}
find dill -name '*.py' -exec sed -i '1{\@^#!%{_bindir}/env python@d}' {} \;

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/dill/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/undill
%python_clone -a %{buildroot}%{_bindir}/get_gprof
%python_clone -a %{buildroot}%{_bindir}/get_objgraph

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{_builddir}/dill-%{version}
# Creative; copied from tox.ini
%python_exec dill/tests/__main__.py

%post
%{python_install_alternative undill get_objgraph get_gprof}

%postun
%python_uninstall_alternative undill

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/undill
%python_alternative %{_bindir}/get_gprof
%python_alternative %{_bindir}/get_objgraph
%{python_sitelib}/dill
%{python_sitelib}/dill-%{version}*-info

%changelog
