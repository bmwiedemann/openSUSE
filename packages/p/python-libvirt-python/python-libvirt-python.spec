#
# spec file for package python-libvirt-python
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


# No longer build for python2. Support was dropped upstream in the 6.0.0 release
%define skip_python2  1

%{?!python_module:%define python_module() python3-%{**}}
%define srcname libvirt-python
Name:           python-libvirt-python
URL:            https://libvirt.org/
Version:        8.10.0
Release:        0
Summary:        Library providing a virtualization API
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Source0:        %{srcname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libvirt-devel = %{version}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
%ifpython2
Provides:       libvirt-python = %{version}
Obsoletes:      libvirt-python < %{version}
%endif

%python_subpackages

%description
The python-libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (v2.6.20+).

%prep
%setup -q -n %{srcname}-%{version}

# Unset execute bit for example scripts; it can introduce spurious
# RPM dependencies, like /usr/bin/python which can pull in python2
# for the -python3 package
find examples -type f -exec chmod 0644 \{\} \;

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README COPYING COPYING.LESSER examples/
%{python_sitearch}/libvirt*
%{python_sitearch}/libvirt_python-%{version}*info
%pycache_only %{python_sitearch}/__pycache__/libvirt*

%changelog
