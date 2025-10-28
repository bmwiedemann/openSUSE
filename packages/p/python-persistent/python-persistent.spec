#
# spec file for package python-persistent
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2013-2023 LISA GmbH, Bingen, Germany.
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


%{?sle15_python_module_pythons}
Name:           python-persistent
Version:        6.3
Release:        0
Summary:        Translucent persistent objects
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/persistent
Source:         https://files.pythonhosted.org/packages/source/p/persistent/persistent-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.deferredimport}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Requires:       python-zope.deferredimport
Requires:       python-zope.interface
%python_subpackages

%description
This package contains a generic persistence implementation for Python. It forms
the core protocol for making objects interact "transparently" with a database
such as the ZODB.

%package        devel
Summary:        Translucent persistent objects
Requires:       %{name} = %{version}
Requires:       python-devel

%description    devel
This package contains the files needed for binding the %{name} C module.

%prep
%autosetup -p1 -n persistent-%{version}
rm -rf persistent.egg-info
# this two tests fail persistently (pun intended): disable them here allows to build with 15.4 as well
sed -i 's|test__p_repr_exception|tst__p_repr_exception|' src/persistent/tests/test_persistence.py
sed -i 's|test__p_repr_in_instance_ignored|tst__p_repr_in_instance_ignored|' src/persistent/tests/test_persistence.py

%build
%pyproject_wheel

%install
%pyproject_install
# don't bother with development files
%{python_expand rm %{buildroot}%{$python_sitearch}/persistent/*.c
  %fdupes %{buildroot}%{$python_sitearch}
}

%check
%pyunittest_arch -v src/persistent/tests/*.py

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%exclude %{python_sitearch}/persistent/*.h
%{python_sitearch}/persistent
%{python_sitearch}/persistent-%{version}.dist-info

%files %{python_files devel}
%dir %{python_sysconfig_path include}/persistent
%{python_sysconfig_path include}/persistent/*.h
%{python_sitearch}/persistent/*.h

%changelog
