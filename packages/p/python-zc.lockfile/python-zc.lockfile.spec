#
# spec file for package python-zc.lockfile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-zc.lockfile
Version:        2.0
Release:        0
Summary:        Basic inter-process locks
License:        ZPL-2.1
Group:          Development/Libraries/Python
URL:            https://pypi.python.org/pypi/zc.lockfile
Source:         https://files.pythonhosted.org/packages/source/z/zc.lockfile/zc.lockfile-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-zc-lockfile = %{version}
Obsoletes:      python-zc-lockfile < %{version}
BuildArch:      noarch
%python_subpackages

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to lock
files, but to simply provide locks with an implementation based on file-locking
primitives. Of course, these locks could be used to mediate access to other
files. For example, the ZODB file storage implementation uses file locks to
mediate access to file-storage database files. The database files and lock file
files are separate files.

%prep
%setup -q -n zc.lockfile-%{version}
rm -rf src/zc.lockfile.egg-info
find -name *~ -delete

%build
%python_build

%install
%python_install
# concatenate both README.txt
cat %{buildroot}%{python_sitelib}/zc/lockfile/README.txt >> README.txt
rm %{buildroot}%{python_sitelib}/zc/lockfile/README.txt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.txt
%{python_sitelib}/*

%changelog
