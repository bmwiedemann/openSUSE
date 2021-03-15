#
# spec file for package python-yg.lockfile
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-yg.lockfile
Version:        2.3
Release:        0
Summary:        Lockfile object with timeouts and context manager
License:        MIT
URL:            https://github.com/yougov/yg.lockfile
Source0:        https://files.pythonhosted.org/packages/source/y/yg.lockfile/yg.lockfile-%{version}.tar.gz
# PyPI tarball does not contain a LICENSE file
Source1:        https://raw.githubusercontent.com/yougov/yg.lockfile/master/LICENSE
BuildRequires:  %{python_module jaraco.functools >= 1.16}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tempora}
BuildRequires:  %{python_module zc.lockfile}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.functools >= 1.16
Requires:       python-tempora
Requires:       python-zc.lockfile
BuildArch:      noarch
%python_subpackages

%description
A FileLock class that implements a context manager with timeouts on top
of zc.lockfile, an excellent, cross-platorm implementation of file locking.

%prep
%setup -q -n yg.lockfile-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/yg/
%{python_sitelib}/yg.lockfile-*.egg-info
%{python_sitelib}/yg.lockfile-*nspkg.pth

%changelog
