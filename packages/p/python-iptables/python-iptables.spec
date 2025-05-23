#
# spec file for package python-iptables
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


Name:           python-iptables
Version:        1.0.1
Release:        0
Summary:        Python bindings for iptables
License:        Apache-2.0
URL:            https://github.com/ldx/python-iptables
Source:         https://github.com/ldx/python-iptables/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libiptc-devel
BuildRequires:  libxtables-devel
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  xtables-plugins
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export XTABLES_LIBDIR=$(pkg-config xtables --variable=xtlibdir)
# Most of the tests require root
%pytest_arch -k 'TestChain and not (test_chain or test_create_chain)'

%files %{python_files}
%license NOTICE
%doc doc README.md
%{python_sitearch}/iptc
%{python_sitearch}/libxtwrapper.cpython*-linux-gnu.so
%{python_sitearch}/python_iptables-%{version}.dist-info

%changelog
