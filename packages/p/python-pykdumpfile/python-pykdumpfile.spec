#
# spec file for package python-pykdumpfile
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


%define skip_python2 1

Name:           python-pykdumpfile
Version:        0.5.5.1
Release:        0
Summary:        Python bindings to libkdumpfile
License:        GPL-2.0-or-later
URL:            https://github.com/ptesarik/pykdumpfile
Source:         https://files.pythonhosted.org/packages/source/p/pykdumpfile/pykdumpfile-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.8}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libkdumpfile-devel
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.8
Obsoletes:      python-libkdumpfile < %{version}
Provides:       python-libkdumpfile = %{version}
%python_subpackages

%description
Python bindings to libkdumpfile

%prep
%autosetup -p1 -n pykdumpfile-%{version}
rm addrxlat/defs_py2.py
rm kdumpfile/defs_py2.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install --ignore-installed
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/_addrxlat.*.so
%{python_sitearch}/addrxlat/
%{python_sitearch}/_kdumpfile.*.so
%{python_sitearch}/kdumpfile/
%{python_sitearch}/pykdumpfile-%{version}.dist-info

%changelog
