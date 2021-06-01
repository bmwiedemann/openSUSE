#
# spec file for package python-BTrees
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-BTrees
Version:        4.8.0
Release:        0
Summary:        Persistent B-tree object containers for Python
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/BTrees
Source:         https://files.pythonhosted.org/packages/source/B/BTrees/BTrees-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module persistent-devel >= 4.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module transaction}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-persistent >= 4.1.0
Requires:       python-zope.interface
Obsoletes:      %{name}-doc
%python_subpackages

%description
This package contains a generic BTrees implementation for Python. It is
mainly used by the ZODB, though.

Note that the data manager API, BTrees.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not easy to
express in the interface. This could probably use more work. The semantics are
presented in detail through examples of a sample data manager in
BTrees.tests.test_SampleDataManager.

%package        devel
Summary:        Development files for the python-BTrees module
Requires:       %{name} = %{version}

%description    devel
This package contains the files needed for binding the %{name} C module.

%prep
%setup -q -n BTrees-%{version}
rm -rf BTrees.egg-info

%build
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/BTrees/*.c
  %fdupes %{buildroot}%{$python_sitearch}
}

%check
# testPurePython tests would require this step which setup.py test did:
#%%{python_expand cp build/lib.linux-*/BTrees/*.so src/BTrees/}
# it can be overcome with --import-mode=append
%pytest_arch -k 'not testPurePython'

%files %{python_files}
%doc CHANGES.rst README.rst PKG-INFO
%license COPYRIGHT.txt LICENSE.txt
%exclude %{python_sitearch}/BTrees/*.h
%{python_sitearch}/*

%files %{python_files devel}
%{python_sitearch}/BTrees/*.h

%changelog
