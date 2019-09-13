#
# spec file for package python-dfVFS
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


%define timestamp 20171230
Name:           python-dfVFS
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Virtual File System
License:        Apache-2.0
Group:          Productivity/File utilities
Url:            https://github.com/log2timeline/dfvfs/wiki
Source:         https://github.com/log2timeline/dfvfs/releases/download/%timestamp/dfvfs-%timestamp.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
Requires:       python-construct
Requires:       python-pycrypto
# Use the python- variant of the libyal python bindings.  This allows python singlespec to tweak the Requires for python2 and python3
Requires:       python-six
Requires:       python2-dfdatetime >= 0~20180110
Requires:       python2-libbde
Requires:       python2-libewf
Requires:       python2-libfsntfs >= 0~20160418
Requires:       python2-libfvde
Requires:       python2-libfwnt
Requires:       python2-libqcow
Requires:       python2-libsigscan
Requires:       python2-libsmdev
Requires:       python2-libsmraw
Requires:       python2-libvhdi
Requires:       python2-libvmdk
Requires:       python2-libvshadow >= 0~20170902
Requires:       python2-libvslvm
Requires:       python2-tsk >= 0~20160721
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
dfVFS, or Digital Forensics Virtual File System, provides read-only access to file-system objects from various storage media types and file formats. The goal of dfVFS is to provide a generic interface for accessing file-system objects, for which it uses several back-ends that provide the actual implementation of the various storage media types, volume systems and file systems.

dfVFS originates from the Plaso project and is also based on ideas from the GRR project. It was largely rewritten and made into a stand-alone project to provide more flexibility and allow other projects to make use of the VFS functionality. dfVFS originally was named PyVFS, but that name conflicted with another project.

dfVFS is currently implemented as a Python module.

%prep
%setup -q -n dfvfs-%{timestamp}
find dfvfs -name \*.py | xargs sed -i "/#!\/usr\/bin\/python/d"
chmod -x utils/check_dependencies.py
chmod -x run_tests.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}
# force complie to resolve an rpmlint complaint
pushd %{buildroot}%{python_sitelib}/dfvfs/
%py_compile .
%py_compile serializer
popd
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS AUTHORS LICENSE README
%doc utils/check_dependencies.py utils/dependencies.py
%doc examples
%{python_sitelib}/dfvfs-%{timestamp}-py2.7.egg-info
%{python_sitelib}/dfvfs
# these are installed into the wrong place
%exclude %{_datadir}/doc/dfvfs/

%changelog
