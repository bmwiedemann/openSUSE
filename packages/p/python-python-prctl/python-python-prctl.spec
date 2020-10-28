#
# spec file for package python-python-prctl
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-prctl
Version:        1.7
Release:        0
Summary:        Python(ic) interface to the linux prctl syscall
License:        GPL-3.0-or-later
URL:            https://github.com/seveas/python-prctl
Source:         https://files.pythonhosted.org/packages/source/p/python-prctl/python-prctl-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/seveas/python-prctl/master/COPYING
Patch0:         disable-sandboxed-test.patch
Patch1:         memory_failure_early_kill.patch
Patch2:         bigendian.patch
Patch3:         powerpc.patch
Patch4:         disable_no_new_privs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  iputils
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcap)
%python_subpackages

%description
The linux prctl function allows you to control specific characteristics of a
process' behaviour. Usage of the function is fairly messy though, due to
limitations in C and linux. This module provides a nice non-messy python(ic)
interface.

Besides prctl, this library also wraps libcap for complete capability handling
and allows you to set the process name as seen in ps and top.

%prep
%setup -q -n python-prctl-%{version}
%autopatch -p1
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest discover -v

%files %{python_files}
%license COPYING
%doc README
%{python_sitearch}/*

%changelog
