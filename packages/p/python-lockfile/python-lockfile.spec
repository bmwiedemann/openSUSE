#
# spec file for package python-lockfile
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lockfile
Version:        0.12.2
Release:        0
Summary:        Platform-independent file locking module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/openstack/pylockfile
Source:         https://files.pythonhosted.org/packages/source/l/lockfile/lockfile-%{version}.tar.gz
Patch0:         %{name}-empty_ident.patch
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The lockfile package exports a LockFile class which provides a simple API for
locking files.  Unlike the Windows msvcrt.locking function, the fcntl.lockf
and flock functions, and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms.
The lock mechanism relies on the atomic nature of the link (on Unix) and
mkdir (on Windows) system calls.  An implementation based on SQLite is also
provided, more as a demonstration of the possibilities it provides than as
production-quality code.

%prep
%setup -q -n lockfile-%{version}
# current thread has ident = None, which causes a TypeError
# http://code.google.com/p/pylockfile/issues/detail?id=8
%patch0 -p1 -b .empty_ident

%build
%python_build

%install
%python_install

%check
%python_exec -m nose

%files %{python_files}
%license LICENSE
%doc README.rst AUTHORS ACKS RELEASE-NOTES ChangeLog
%{python_sitelib}/lockfile*

%changelog
