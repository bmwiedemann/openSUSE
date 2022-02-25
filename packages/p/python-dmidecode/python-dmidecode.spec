#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define python_subpackage_only 1
%define oldpython python

Name:           %{oldpython}-dmidecode
Version:        3.12.2+git.1625035095.f0a089a
Release:        0
Summary:        Python module to access DMI data
Group:          System/Management
License:        GPL-2.0-only
URL:            https://github.com/nima/python-dmidecode
# Source0:        https://github.com/nima/python-dmidecode/archive/refs/tags/v%%{version}.tar.gz#/python-dmidecode-%%{version}.tar.gz
Source0:        python-dmidecode-%{version}.tar.gz
Patch0:         huge-memory.patch
Patch1:         gcc7-inline.patch
Patch2:         detect-lib-with-py3.patch
# PATCH-FIX-UPSTREAM 31-version_info-v-version.patch gh#nima/python-dmidecode#31 mcepl@suse.com
# use sys.version_info instead of sys.version
Patch3:         31-version_info-v-version.patch
BuildRequires:  %{python_module devel}
%if 0%{?sle_version} && 0%{?sle_version} < 150400
BuildRequires:  %{oldpython}-libxml2-python
BuildRequires:  %{oldpython}3-libxml2-python
%else
BuildRequires:  %{python_module libxml2}
%endif
BuildRequires:  fdupes
BuildRequires:  libxml2-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
python-dmidecode is a python extension module that uses the code-base
of the 'dmidecode' utility, and presents the data as python data
structures or as XML data using libxml2.

%package -n python-python-dmidecode
Summary:        Python module to access DMI data
Requires:       %{oldpython}-dmidecode = %{version}-%{release}

%description -n python-python-dmidecode
A Python extension module that uses the code-base of the
'dmidecode' utility, and presents the data as Python data
structures or as XML data using libxml2.

%prep
%autosetup -p1

sed -i 's/python2/python3/g' Makefile unit-tests/Makefile

%build
%{python_expand export LDFLAGS="-Wl,-rpath=%{$python_sitearch}"
%make_build PY_BIN=$python build
}

%install
%{python_expand $python src/setup.py install --root %{buildroot} --prefix=%{_prefix}
%fdupes %{buildroot}%{$python_sitearch}
}

%check
pushd unit-tests
%{python_expand export PYTHON=$python
%make_build
}
popd

%clean

%files
%license doc/LICENSE
%doc README doc/README.upstream doc/AUTHORS doc/AUTHORS.upstream
%dir %{_datadir}/python-dmidecode/
%{_datadir}/python-dmidecode/

%files %{python_files python-dmidecode}
%{python_sitearch}/dmidecode*
%{python_sitearch}/*.egg-info
%pycache_only %{python_sitearch}/__pycache__/*

%changelog
