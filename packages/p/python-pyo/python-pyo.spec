#
# spec file for package python-pyo
#
# Copyright (c) 2024 SUSE LLC
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
%define         skip_python2 1
Name:           python-pyo
Version:        1.0.5
Release:        0
Summary:        Python digital signal processing module
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://ajaxsoundstudio.com/software/pyo/
Source:         https://files.pythonhosted.org/packages/source/p/pyo/pyo-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/belangeo/pyo/master/LICENSE
# PATCH-FIX-UPSTREAM - Fix multiple incorrect declarations and signatures of callback functions
Patch:          https://github.com/belangeo/pyo/pull/277.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
%python_subpackages

%description
PYO is a Python module written in C to help digital signal processing
script creation.

%prep
%setup -q -n pyo-%{version}
%autopatch -p1
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build --use-jack --use-double

%install
%python_install --use-jack --use-double
%python_clone -a %{buildroot}%{_bindir}/epyo
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# testsuite is broken and can not be run even from github tarball

%post
%python_install_alternative epyo

%postun
%python_uninstall_alternative epyo

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/epyo
%{python_sitearch}/*

%changelog
