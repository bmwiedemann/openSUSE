#
# spec file for package python-PyECLib
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-PyECLib
Version:        1.7.0
Release:        0
Summary:        Simple interface for implementing erasure codes
License:        BSD-3-Clause
URL:            https://opendev.org/openstack/pyeclib/
Source:         https://files.pythonhosted.org/packages/source/p/pyeclib/pyeclib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  liberasurecode-devel >= 1.4.0
BuildRequires:  python-rpm-macros
Requires:       alts
BuildRequires:  alts
%python_subpackages

%description
This library makes use of Jesasure for Reed-Solomon as implemented by the
liberasurecode library and provides its' own flat XOR-based erasure code
encoder and decoder.  Currently, it implements a specific class of HD
Combination Codes (see "Flat XOR-based erasure codes in storage systems:
Constructions, efficient recovery, and tradeoffs" in IEEE MSST 2010).  These
codes are well-suited to archival use-cases, have a simple construction and
require a minimum number of participating disks during single-disk
reconstruction (think XOR-based LRC code).

%prep
%setup -q -n pyeclib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyeclib-backend
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative pyeclib-backend

%postun
%python_uninstall_alternative pyeclib-backend

%check
%pyunittest_arch discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pyeclib-backend
%{python_sitearch}/pyeclib
%{python_sitearch}/pyeclib_c.abi3.so
%{python_sitearch}/[Pp]y[Ee][Cc][Ll]ib-%{version}.dist-info

%changelog
