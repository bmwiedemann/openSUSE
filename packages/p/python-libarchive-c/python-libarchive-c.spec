#
# spec file for package python-libarchive-c
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


%define requires_file() %( readlink -f '%*' | LC_ALL=C xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' -f | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

Name:           python-libarchive-c
Version:        5.1
Release:        0
Summary:        Python interface to libarchive
License:        CC0-1.0
Group:          Development/Languages/Python
URL:            https://github.com/Changaco/python-libarchive-c
Source:         https://files.pythonhosted.org/packages/source/l/libarchive-c/libarchive-c-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/Changaco/python-libarchive-c/pull/131 Handle new libarchive versions
Patch0:         libarchive.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libarchive_dynamically}
%requires_file  %{_libdir}/libarchive.so
%else
Requires:       libarchive13
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  libarchive-devel
# /SECTION
%python_subpackages

%description
A Python interface to libarchive. It uses the standard ctypes_ module to
dynamically load and access the C library.

%prep
%autosetup -p1 -n libarchive-c-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF-8"
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.md
%{python_sitelib}/libarchive
%{python_sitelib}/libarchive_c-%{version}*info

%changelog
