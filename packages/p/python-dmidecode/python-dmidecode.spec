#
# spec file for package python-dmidecode
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
%define oldpython python
Name:           python-dmidecode
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
Obsoletes:      %{oldpython}-dmidecode <= 3.12.2+git.1625035095.f0a089a
Obsoletes:      python-python-dmidecode <= 3.12.2+git.1625035095.f0a089a
BuildRequires:  %{python_module devel}
%if 0%{?sle_version} && 0%{?sle_version} < 150400
BuildRequires:  python2-libxml2-python
BuildRequires:  python3-libxml2-python
%else
BuildRequires:  %{python_module libxml2}
%endif
BuildRequires:  fdupes
BuildRequires:  libxml2-devel
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
python-dmidecode is a python extension module that uses the code-base
of the 'dmidecode' utility, and presents the data as python data
structures or as XML data using libxml2.

%prep
%autosetup -p1

sed -i 's/python2/python3/g' Makefile unit-tests/Makefile

%build
%{python_expand export LDFLAGS="-Wl,-rpath=%{$python_sitearch}"
%make_build PY_BIN=$python build
}

%install
%{python_expand rm -f %{buildroot}%{_datadir}/python-dmidecode/pymap.xml
$python src/setup.py install --root %{buildroot} --prefix=%{_prefix}
ls -l %{buildroot}%{_datadir}/python-dmidecode/
mv %{buildroot}%{_datadir}/python-dmidecode/pymap{,-%{$python_bin_suffix}}.xml
touch %{buildroot}%{_datadir}/python-dmidecode/pymap.xml
%fdupes %{buildroot}%{$python_sitearch}
}

%check
pushd unit-tests
%python_expand PYTHON=$python %make_build
popd

%post
PRIO=$(echo %{python_version}|tr -d '.')
/usr/sbin/update-alternatives --install %{_datadir}/python-dmidecode/pymap.xml pymap.xml \
    %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml ${PRIO}

%postun
if [ ! -f %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml ] ; then
   MAJVER=$(ver=%{python_version}; echo ${ver:0:1})
   /usr/sbin/update-alternatives --remove pymap.xml \
        %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml
fi

%clean

%files %{python_files}
%license doc/LICENSE
%doc README doc/README.upstream doc/AUTHORS doc/AUTHORS.upstream
%dir %{_datadir}/python-dmidecode/
%ghost %{_sysconfdir}/alternatives/pymap.xml
%ghost %{_datadir}/python-dmidecode/pymap.xml
%{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml
%{python_sitearch}/dmidecode*
%{python_sitearch}/*.egg-info
%pycache_only %{python_sitearch}/__pycache__/*

%changelog
