#
# spec file for package python-pyxattr
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


%global mod_name pyxattr
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{mod_name}
Version:        0.6.1
Release:        0
Summary:        Filesystem extended attributes for python
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://pyxattr.k1024.org/
Source:         https://files.pythonhosted.org/packages/source/p/pyxattr/pyxattr-%{version}.tar.gz
BuildRequires:  %{python_module devel}
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
%setup -q -n pyxattr-%{version}

%build
%python_build

%check
%python_exec setup.py test

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/xattr*
%{python_sitearch}/*egg-info
%license COPYING
%doc NEWS README.rst

%changelog
