#
# spec file for package python-zc.lockfile
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-zc.lockfile
Version:        3.0.post1
Release:        0
Summary:        Basic inter-process locks
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zc.lockfile
Source:         https://files.pythonhosted.org/packages/source/z/zc.lockfile/zc.lockfile-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} <= 1500
BuildRequires:  python2-mock
%endif
Provides:       python-zc-lockfile = %{version}
Obsoletes:      python-zc-lockfile < %{version}
Requires:       python-setuptools
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
%pyproject_wheel

%install
%pyproject_install
# concatenate both README.txt
cat %{buildroot}%{python_sitelib}/zc/lockfile/README.txt >> README.txt
rm %{buildroot}%{python_sitelib}/zc/lockfile/README.txt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
touch %{buildroot}%{$python_sitelib}/zc/__init__.py
$python -B -m unittest -v zc.lockfile.tests
$python -B -m doctest -v src/zc/lockfile/README.txt
rm %{buildroot}%{$python_sitelib}/zc/__init__.py
}

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.txt
%dir %{python_sitelib}/zc
%{python_sitelib}/zc/lockfile
%{python_sitelib}/zc.lockfile-%{version}-py*-nspkg.pth
%{python_sitelib}/zc[._]lockfile-%{version}.dist-info

%changelog
