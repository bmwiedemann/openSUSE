#
# spec file for package python-sane
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sane
Version:        2.8.3
Release:        0
Summary:        A Python interface to the SANE scanner and frame grabber interface
License:        NTP
Group:          Development/Languages/Python
URL:            https://github.com/python-pillow/Sane
Source:         https://github.com/python-pillow/Sane/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sane-backends-devel
%python_subpackages

%description
The SANE module provides an interface to the SANE scanner and frame grabber interface for Linux.  This module has been split out from Pillow since version 2.7.0.

%prep
%setup -q -n Sane-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%files %{python_files}
%doc README.rst CHANGES.rst
%license COPYING
%{python_sitearch}/*

%changelog
