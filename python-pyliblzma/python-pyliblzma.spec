#
# spec file for package python-pyliblzma
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


%define oname   pyliblzma
%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyliblzma
Version:        0.5.3
Release:        0
Summary:        Python bindings for liblzma
License:        LGPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://launchpad.net/pyliblzma
Source:         https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.bz2
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(liblzma)
Obsoletes:      %{name}-doc
%python_subpackages

%description
PylibLZMA provides a python interface for the liblzma library
to read and write data that has been compressed or can be
decompressed by Lasse Collin's xz / lzma utils.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc ChangeLog NEWS README THANKS
%{python_sitearch}/*

%changelog
