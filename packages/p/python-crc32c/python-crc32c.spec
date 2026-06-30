#
# spec file for package python-crc32c
#
# Copyright (c) 2026 SUSE LLC
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

%bcond_without libalternatives

%{?sle15_python_module_pythons}
Name:           python-crc32c
Version:        2.8
Release:        0
Summary:        A python package implementing the crc32c algorithm in hardware and software
License:        LGPL-2.1-or-later
URL:            https://github.com/ICRAR/crc32c
Source:         https://files.pythonhosted.org/packages/source/c/crc32c/crc32c-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
%python_subpackages

%description
This package implements the crc32c checksum algorithm. It automatically chooses
between a hardware-based implementation (using the CRC32C SSE 4.2 instruction
of Intel CPUs, and the crc32* instructions on ARMv8 CPUs), or a software-based
one when no hardware support can be found.

%prep
%autosetup -p1 -n crc32c-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm -rf %{buildroot}%{$python_sitearch}/crc32c/ext
%python_clone -a %{buildroot}%{_bindir}/crc32c

%check
%pytest_arch

%post
%python_install_alternative crc32c

%postun
%python_uninstall_alternative crc32c

%files %{python_files}
%doc AUTHORS.google-crc32c README.rst
%license LICENSE LICENSE.google-crc32c LICENSE.slice-by-8
%python_alternative %{_bindir}/crc32c
%{python_sitearch}/crc32c
%{python_sitearch}/crc32c-%{version}.dist-info

%changelog
