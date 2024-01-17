#
# spec file for package python-ftputil
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ftputil
Version:        3.4
Release:        0
Summary:        High-level FTP client library (virtual file system and more) for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://ftputil.sschwarzer.net/
Source:         https://files.pythonhosted.org/packages/source/f/ftputil/ftputil-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
FTPutil is a high-level FTP client library for the Python programming
language. ftputil implements a virtual file system for accessing FTP
servers, that is, it can generate file-like objects for remote files.
The library supports many functions similar to those in the os,
os.path and shutil modules. ftputil has convenience functions for
conditional uploads and downloads, and handles FTP clients and
servers in different timezones.

%prep
%setup -q -n ftputil-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mkdir -p %{buildroot}%{_docdir}
%python_expand cp -r %{buildroot}%{_prefix}/doc/ftputil %{buildroot}%{_docdir}/%{$python_prefix}-ftputil
rm -rf %{buildroot}%{_prefix}/doc/ftputil

%files %{python_files}
%{_docdir}/%{python_prefix}-ftputil
%license LICENSE
%{python_sitelib}/*

%changelog
