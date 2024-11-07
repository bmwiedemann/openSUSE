#
# spec file for package python-Durus
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
Name:           python-Durus
Version:        4.3
Release:        0
Summary:        A Python Object Database
License:        CNRI-Python
URL:            https://www.mems-exchange.org/software/durus/
Source:         https://files.pythonhosted.org/packages/source/d/durus/durus-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Serves and manages changes to persistent objects being used in
multiple client processes.

%prep
%setup -q -n durus-%{version}
# Fix non-executable scripts
sed -i "1d" bin/db_renumber.py
sed -i "1d" durus/__main__.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/durus
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative durus

%postun
%python_uninstall_alternative durus

%check
# TODO, uses sancho's utest format from 2005 on
# see CHANGES.txt

%files %{python_files}
%license LICENSE.txt
%doc ACKS.txt CHANGES.txt README.md doc/FAQ.txt
%python_alternative %{_bindir}/durus
%{python_sitearch}/durus
%{python_sitearch}/Durus-%{version}.dist-info

%changelog
