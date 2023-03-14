#
# spec file for package python-dmidecode
#
# Copyright (c) 2023 SUSE LLC
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


%define oldpython python
%define modname dmidecode
Name:           python-dmidecode
Version:        3.12.3
Release:        0
Summary:        Python module to access DMI data
License:        GPL-2.0-only
Group:          System/Libraries
URL:            https://github.com/nima/python-dmidecode
Source0:        https://github.com/nima/python-dmidecode/archive/refs/tags/v%{version}.tar.gz#/python-dmidecode-%{version}.tar.gz
Source99:       python-dmidecode.rpmlintrc
# PATCH-FIX-UPSTREAM gcc7-inline.patch gh#nima/python-dmidecode#35 mcepl@suse.com
# Don't use inline keyword.
Patch1:         gcc7-inline.patch
# PATCH-FIX-UPSTREAM 31-version_info-v-version.patch gh#nima/python-dmidecode#31 mcepl@suse.com
# use sys.version_info instead of sys.version
Patch2:         31-version_info-v-version.patch
# PATCH-FIX-UPSTREAM detect-lib-with-py3.patch gh#nima/python-dmidecode#36 mcepl@suse.com
#  Make the code future-proof against removal of distutils module.
Patch3:         detect-lib-with-py3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  libxml2-devel
BuildRequires:  python-rpm-macros
Requires:       python
Requires(post): update-alternatives
Requires(postun):update-alternatives
Obsoletes:      %{oldpython}-dmidecode <= %{version}
Obsoletes:      python-python-dmidecode <= %{version}
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
BuildRequires:  %{python_module libxml2}
%else
BuildRequires:  python2-libxml2-python
BuildRequires:  python3-libxml2-python
%endif
%python_subpackages

%description
python-dmidecode is a python extension module that uses the code-base
of the 'dmidecode' utility, and presents the data as python data
structures or as XML data using libxml2.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%{python_expand export LDFLAGS="-Wl,-rpath=%{$python_sitearch}"
%make_build PY_BIN=$python build
}

%install
%{python_expand rm -f %{buildroot}%{_datadir}/python-dmidecode/pymap.xml
$python src/setup.py install --root %{buildroot} --prefix=%{_prefix}

# prepare alternatives
install -d %{buildroot}%{_sysconfdir}/alternatives
mv %{buildroot}%{_datadir}/python-dmidecode/pymap{,-%{$python_bin_suffix}}.xml
touch %{buildroot}%{_sysconfdir}/alternatives/pymap.xml
ln -s %{_sysconfdir}/alternatives/pymap.xml \
      %{buildroot}%{_datadir}/python-dmidecode/pymap.xml
%fdupes %{buildroot}%{$python_sitearch}
}

%check
pushd unit-tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
%make_build PY_BIN=$python
}
popd

%post
PRIO=$(echo %{python_version}|tr -d '.')
%{_sbindir}/update-alternatives --install %{_datadir}/python-dmidecode/pymap.xml pymap.xml \
    %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml ${PRIO}

%postun
if [ ! -f %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml ] ; then
   MAJVER=$(ver=%{python_version}; echo ${ver:0:1})
   %{_sbindir}/update-alternatives --remove pymap.xml \
        %{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml
fi

%files %{python_files}
%license doc/LICENSE
%doc README doc/README.upstream doc/AUTHORS doc/AUTHORS.upstream
%dir %{_datadir}/python-dmidecode/
%ghost %{_sysconfdir}/alternatives/pymap.xml
%ghost %{_datadir}/python-dmidecode/pymap.xml
%{_datadir}/python-dmidecode/pymap-%{python_bin_suffix}.xml
# %%{python_sitearch}/python_dmidecode-%%{version}*-info
%{python_sitearch}/python_dmidecode-3.12.2*-info
%{python_sitearch}/dmidecode.py
%{python_sitearch}/dmidecodemod.*.so
%pycache_only %{python_sitearch}/__pycache__/dmidecode*.pyc

%changelog
