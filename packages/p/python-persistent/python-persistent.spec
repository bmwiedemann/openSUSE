#
# spec file for package python-persistent
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2019 LISA GmbH, Bingen, Germany.
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
Name:           python-persistent
Version:        4.5.0
Release:        0
Summary:        Translucent persistent objects
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/persistent
Source:         https://files.pythonhosted.org/packages/source/p/persistent/persistent-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
Requires:       python-cffi
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface
%python_subpackages

%description
This package contains a generic persistence implementation for Python. It forms
the core protocol for making objects interact "transparently" with a database
such as the ZODB.

%package        devel
Summary:        Translucent persistent objects
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-devel

%description    devel
This package contains the files needed for binding the %{name} C module.

%prep
%setup -q -n persistent-%{version}
rm -rf persistent.egg-info

%build
%python_build

%install
%python_install
# don't bother with development files
%{python_expand rm %{buildroot}%{$python_sitearch}/persistent/*.c
  %fdupes %{buildroot}%{$python_sitearch}
}

%check
find . -name \*.pyc -delete
%python_exec setup.py test -v

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%exclude %{python_sitearch}/persistent/*.h
%{python_sitearch}/*

%files %{python_files devel}
%dir %{python_sysconfig_path include}/persistent
%{python_sysconfig_path include}/persistent/*.h
%{python_sitearch}/persistent/*.h

%changelog
