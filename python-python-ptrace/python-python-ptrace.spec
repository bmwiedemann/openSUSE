#
# spec file for package python-python-ptrace
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pkg_name python-ptrace
Name:           python-%{pkg_name}
Version:        0.9.3
Release:        0
Summary:        Python binding for ptrace
License:        GPL-2.0
Group:          Development/Languages/Python
Url:            http://python-ptrace.readthedocs.io/
Source:         https://github.com/haypo/%{pkg_name}/archive/%{version}.tar.gz#!./%{pkg_name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
python-ptrace is a debugger using ptrace written in Python.

%prep
%setup -q -n %{pkg_name}-%{version}
sed -i 's/\x0D$//' doc/*.rst
chmod 0644 examples/*.py

%build
%python_build
%python_exec setup_cptrace.py build

%install
%python_install
%python_exec setup_cptrace.py install -O1 --skip-build --root %{buildroot}
%python_clone -a %{buildroot}%{_bindir}/gdb.py
%python_clone -a %{buildroot}%{_bindir}/strace.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%post
%python_install_alternative strace.py
%python_install_alternative gdb.py

%postun
%python_uninstall_alternative strace.py
%python_uninstall_alternative gdb.py

%files %{python_files}
%doc COPYING
%doc README.rst
%doc doc/* examples
%python_alternative %{_bindir}/gdb.py
%python_alternative %{_bindir}/strace.py
%{python_sitelib}/ptrace/
%{python_sitelib}/python_ptrace-*-py*.egg-info
%{python_sitearch}/cptrace*.so
%{python_sitearch}/cptrace-*-py*.egg-info

%changelog
