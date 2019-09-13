#
# spec file for package python-iptables
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-iptables
Version:        0.13.0
Release:        0
Summary:        Python bindings for iptables
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ldx/python-iptables
Source:         https://github.com/ldx/python-iptables/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python-iptables is a Python project that provides bindings to the iptables C libraries in Linux.
Interoperability with iptables is achieved using the iptables C libraries (libiptc, libxtables,
and iptables extensions), not calling the iptables executable and parsing its output as most other
iptables wrapper libraries do; this makes python-iptables faster and not prone to parsing errors,
at the same time leveraging all available iptables match and target extensions without further work.

%prep
%setup -q
chmod -x README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py clean build test --help

%files %{python_files}
%license NOTICE
%doc doc README.md
%{python_sitearch}/*

%changelog
