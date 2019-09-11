#
# spec file for package python-Pyrex
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Pyrex
Version:        0.9.9
Release:        0
Summary:        Compiles code that mixes Python and C data types into a C extension for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
Source0:        http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-%{version}.tar.gz
Patch0:         pyrex-no-buildtime.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  %{python_module base}
BuildRequires:  python-rpm-macros
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Provides:       pyrex = %{version}-%{release}
Obsoletes:      pyrex < %{version}-%{release}
%endif
%python_subpackages

%description
Pyrex is a language specially designed for writing Python extension
modules. It's designed to bridge the gap between the nice, high-level,
easy-to-use world of Python and the messy, low-level world of C/

%prep
%setup -q -n Pyrex-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyrexc

%post
%python_install_alternative pyrexc

%postun
%python_uninstall_alternative pyrexc

%files %{python_files}
%doc *.txt Doc/* Demos
%python_alternative %{_bindir}/pyrexc
%{python_sitelib}/*

%changelog
