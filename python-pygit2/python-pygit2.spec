#
# spec file for package python-pygit2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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
Name:           python-pygit2
Version:        0.28.1
Release:        0
Summary:        Python bindings for libgit2
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/libgit2/pygit2
Source:         https://files.pythonhosted.org/packages/source/p/pygit2/pygit2-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  libgit2-devel >= %{version}
BuildRequires:  libopenssl-devel
BuildRequires:  python-rpm-macros
Requires:       python-pycparser
Requires:       python-six
%requires_eq    python-cffi
%python_subpackages

%description
Bindings for libgit2, a linkable C library for the Git version-control system.

%prep
%setup -q -n pygit2-%{version}
# do not add options to pytest
rm pytest.ini

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitearch}/pygit2/decl/
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/*

%changelog
