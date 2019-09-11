#
# spec file for package python-pycups
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define oldpython python
Name:           python-pycups
Version:        1.9.74
Release:        0
Summary:        Python Bindings for CUPS
License:        GPL-2.0+
Group:          Development/Libraries/Python
Url:            http://cyberelk.net/tim/software/pycups/
Source:         https://files.pythonhosted.org/packages/source/p/pycups/pycups-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE revert-postscriptdriver.prov-py3.patch switch back to python2
Patch0:         revert-postscriptdriver.prov-py3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%ifpython2
Obsoletes:      %{oldpython}-cups < %{version}
Provides:       %{oldpython}-cups = %{version}
%endif
%ifpython3
Obsoletes:      python3-cups < %{version}
Provides:       python3-cups = %{version}
%endif
%python_subpackages

%description
Python Bindings for CUPS, the Common Unix Printing System

%prep
%setup -q -n pycups-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%defattr(-,root,root)
%doc NEWS README TODO
%license COPYING
%{python_sitearch}/cups*.so
%{python_sitearch}/pycups-%{version}-py*.egg-info

%changelog
