#
# spec file for package python-managesieve
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2009 Guido Berhoerster.
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


%define oname  managesieve
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-managesieve
Version:        0.6
Release:        0
Summary:        Python Module Implementing the ManageSieve Protocol
License:        GPL-3.0-or-later AND Python-2.0
Group:          Development/Libraries/Python
URL:            https://managesieve.readthedocs.io/
Source:         https://gitlab.com/htgoebel/managesieve/-/archive/v%{version}/managesieve-v%{version}.tar.bz2
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
# provides same binary: /usr/bin/sieveshell
Conflicts:      perl-Cyrus-SIEVE-managesieve
BuildArch:      noarch
%python_subpackages

%description
python-managesieve is a Python module implementing the ManageSieve client
protocol. It also includes an user application (the interactive sieveshell).

%prep
%setup -q -n %{oname}-v%{version}
touch test/__init__.py

# Fix URL
sed -i 's|http://packages.python.org/managesieve|%{url}|' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sieveshell

%check
%python_exec setup.py test -v

%post
%python_install_alternative sieveshell

%postun
%python_uninstall_alternative sieveshell

%files %{python_files}
%doc README.txt
%{_bindir}/sieveshell-%{python_bin_suffix}
%python_alternative %{_bindir}/sieveshell
%{python_sitelib}/*

%changelog
