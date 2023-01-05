#
# spec file for package python-fuse
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-fuse
Version:        1.0.5
Release:        0
Summary:        Python bindings for FUSE
License:        LGPL-2.1-only
Group:          Development/Libraries/Python
URL:            https://github.com/libfuse/python-fuse
Source:         https://github.com/libfuse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  fuse-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for FUSE (User space File System)

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Can not figured how to do it.

%files %{python_files}
%license COPYING
%doc README.* FAQ AUTHORS
%{python_sitearch}/fuse*
%pycache_only %{python_sitearch}/__pycache__

%changelog
