#
# spec file for package python-libsass
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


%define _name   libsass
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-libsass
Version:        0.19.2
Release:        0
Summary:        Python binding for libsass
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sass/libsass-python
Source:         https://files.pythonhosted.org/packages/source/l/libsass/libsass-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-six
# Both are providing sassc binary with different parameters
Conflicts:      sassc
%python_subpackages

%description
A straightforward binding of libsass for Python. Compile Sass/SCSS in Python
with no Ruby stack at all!

%prep
%setup -q -n %{_name}-%{version}

%build
export SYSTEM_SASS=true
%python_build

%install
export SYSTEM_SASS=true
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%python3_only %{_bindir}/pysassc
%python3_only %{_bindir}/sassc
%{python_sitearch}/*

%changelog
