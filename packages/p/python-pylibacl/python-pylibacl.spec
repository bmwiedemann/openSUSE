#
# spec file for package python-pylibacl
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013-2020 LISA GmbH, Bingen, Germany
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
Name:           python-pylibacl
Version:        0.7.1
Release:        0
Summary:        POSIX1e ACLs for python
License:        LGPL-2.1-or-later
URL:            https://pylibacl.k1024.org/
Source:         https://files.pythonhosted.org/packages/source/p/pylibacl/pylibacl-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libacl)
%python_subpackages

%description
This is a C extension module for Python which
implements POSIX ACLs manipulation. It is a wrapper on top
of the systems's acl C library - see acl(5).

%prep
%setup -q -n pylibacl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license COPYING
%doc NEWS.md README.md
%{python_sitearch}/posix1e.*
%{python_sitearch}/pylibacl-%{version}.dist-info

%changelog
