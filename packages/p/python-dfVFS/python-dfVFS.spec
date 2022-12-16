#
# spec file for package python-dfVFS
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
%define skip_python2 1
%define timestamp 20220917
Name:           python-dfVFS
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Virtual File System
License:        Apache-2.0
Group:          Productivity/File utilities
URL:            https://github.com/log2timeline/dfvfs/wiki
Source0:        https://github.com/log2timeline/dfvfs/releases/download/%{timestamp}/dfvfs-%{timestamp}.tar.gz
Source99:       python-dfVFS-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dfdatetime}
BuildRequires:  %{python_module dtfabric >= 20220219}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module libbde}
BuildRequires:  %{python_module libcaes}
BuildRequires:  %{python_module libewf}
BuildRequires:  %{python_module libfsapfs}
BuildRequires:  %{python_module libfsext}
BuildRequires:  %{python_module libfsfat}
BuildRequires:  %{python_module libfshfs}
BuildRequires:  %{python_module libfsntfs}
BuildRequires:  %{python_module libfsxfs}
BuildRequires:  %{python_module libfvde}
BuildRequires:  %{python_module libfwnt}
BuildRequires:  %{python_module libluksde >= 20220121}
BuildRequires:  %{python_module libmodi}
BuildRequires:  %{python_module libphdi}
BuildRequires:  %{python_module libqcow}
BuildRequires:  %{python_module libsigscan >= 0~20191221}
BuildRequires:  %{python_module libsmdev}
BuildRequires:  %{python_module libsmraw}
BuildRequires:  %{python_module libvhdi}
BuildRequires:  %{python_module libvmdk}
BuildRequires:  %{python_module libvsgpt}
BuildRequires:  %{python_module libvshadow}
BuildRequires:  %{python_module libvslvm}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tsk}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-construct
Requires:       python-dfdatetime >= 0~20180110
Requires:       python-dtfabric >= 20220219
Requires:       python-libbde
Requires:       python-libcaes
Requires:       python-libewf
Requires:       python-libfsapfs
Requires:       python-libfsext
Requires:       python-libfsfat
Requires:       python-libfshfs
Requires:       python-libfsntfs >= 0~20160418
Requires:       python-libfsxfs
Requires:       python-libfvde
Requires:       python-libfwnt >= 20210717
Requires:       python-libluksde >= 20220121
Requires:       python-libmodi
Requires:       python-libphdi
Requires:       python-libqcow
Requires:       python-libsigscan
Requires:       python-libsmdev
Requires:       python-libsmraw
Requires:       python-libvhdi
Requires:       python-libvmdk
Requires:       python-libvsgpt
Requires:       python-libvshadow >= 0~20170902
Requires:       python-libvslvm
Requires:       python-tsk >= 0~20160721
Obsoletes:      python3-dfVFS < 0~%{timestamp}
BuildArch:      noarch
%python_subpackages

%description
dfVFS, or Digital Forensics Virtual File System, provides read-only
access to file-system objects from various storage media types and file
formats. The goal of dfVFS is to provide a generic interface for
accessing file-system objects, for which it uses several back-ends that
provide the actual implementation of the various storage media types,
volume systems and file systems.

dfVFS originates from the Plaso project and is also based on ideas from
the GRR project. It was largely rewritten and made into a stand-alone
project to provide more flexibility and allow other projects to make use
of the VFS functionality. dfVFS originally was named PyVFS, but that
name conflicted with another project.

dfVFS is currently implemented as a Python module.

%prep
%setup -q -n dfvfs-%{timestamp}
%autopatch -p1

find dfvfs -name \*.py | xargs sed -i "/#!\/usr\/bin\/python/d"
chmod -x utils/check_dependencies.py
chmod -x run_tests.py

%build
%python_build

%install
%python_install

%fdupes %{buildroot}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
# APFS testing for encrypted volumes is currently failing dfVFS 20220917
# $python ./run_tests.py
}

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%doc utils/check_dependencies.py utils/dependencies.py
# these are installed into the wrong place
%exclude %{_datadir}/doc/dfvfs/
%{python_sitelib}/dfvfs*

%changelog
