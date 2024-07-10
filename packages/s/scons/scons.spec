#
# spec file for package scons
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define pythons python3
%{?sle15_python_module_pythons}
Name:           scons
Version:        4.8.0
Release:        0
Summary:        Replacement for Make
License:        MIT
Group:          Development/Tools/Building
URL:            https://www.scons.org/
Source:         http://prdownloads.sourceforge.net/scons/SCons-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
SCons is a make replacement that provides a range of enhanced features,
such as automated dependency generation and built-in compilation cache
support. SCons rule sets are Python scripts, which means that SCons
provides itself as well as the features. SCons allows you to use the
full power of Python to control compilation.

%prep
%autosetup -p1

sed -i -e '/QT3_LIBPATH = os.path.join.*QT3DIR/s/lib/%{_lib}/' \
    SCons/Tool/qt3.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files
%license LICENSE
%{_bindir}/*
%{python_sitelib}/SCons
%{python_sitelib}/SCons-%{version}-py*.egg-info

%changelog
