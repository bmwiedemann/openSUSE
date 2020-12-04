#
# spec file for package python-pyxattr
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
%global mod_name pyxattr
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define github_url https://github.com/iustin/%{mod_name}/releases/download
Name:           python-%{mod_name}
Version:        0.7.2
Release:        0
Summary:        Filesystem extended attributes for python
License:        LGPL-2.1-or-later
URL:            https://pyxattr.k1024.org/
Source0:        %{github_url}/v%{version}/%{mod_name}-%{version}.tar.gz
Source1:        %{github_url}/v%{version}/%{mod_name}-%{version}.tar.gz.asc
Source2:        https://k1024.org/files/key.asc#/%{name}.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a C extension module for Python which
implements extended attributes manipulation. It is a wrapper on top
of the attr C library - see attr(5).

%prep
%autosetup -n pyxattr-%{version}

%build
%python_build

%check
%pytest_arch tests

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/xattr*
%{python_sitearch}/pyxattr-%{version}*-info
%license COPYING
%doc NEWS README.md

%changelog
