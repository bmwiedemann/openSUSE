#
# spec file for package python-cx_Freeze
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
%define skip_python2 1
%define oldpython python
Name:           python-cx_Freeze
Version:        6.0
Release:        0
Summary:        Scripts to create standalone executables from Python scripts
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/anthony-tuininga/cx_Freeze
Source:         https://github.com/anthony-tuininga/cx_Freeze/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module devel}
# imports nose in one test
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
# we provide same binary like the deprecated py2 variant
Conflicts:      %{oldpython}-cx_Freeze
%python_subpackages

%description
CX_Freeze is a set of scripts and modules for turning Python scripts
into executables in much the same way that py2exe and py2app do.

It works by bundling Python executables and libraries from the local
Python installation. As such, the distribution produced by CX_Freeze
shares the very same dependencies. System libraries are not bundled
however, so additional dependencies may need to be manually installed
before being able to run "cx-frozen" executables that were created by
other systems.

%prep
%setup -q -n cx_Freeze-%{version}
sed -i -e '/^#!\//, 1d' cx_Freeze/samples/*/*.py
chmod a-x cx_Freeze/initscripts/*.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cxfreeze-quickstart
%python_clone -a %{buildroot}%{_bindir}/cxfreeze
%python_expand chrpath -d %{buildroot}%{$python_sitearch}/cx_Freeze/bases/Console*
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_FindModule_from_zip - needs testpkg1.egg which is not present
%pytest_arch -k 'not test_FindModule_from_zip'

%post
%python_install_alternative cxfreeze-quickstart
%python_install_alternative cxfreeze

%postun
%python_uninstall_alternative cxfreeze-quickstart
%python_uninstall_alternative cxfreeze

%files %{python_files}
%doc README.md
%license doc/src/license.rst
%python_alternative %{_bindir}/cxfreeze
%python_alternative %{_bindir}/cxfreeze-quickstart
%{python_sitearch}/*

%changelog
