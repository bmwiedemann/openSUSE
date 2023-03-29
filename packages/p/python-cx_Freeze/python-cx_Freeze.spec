#
# spec file for package python-cx_Freeze
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


%define oldpython python
Name:           python-cx_Freeze
Version:        6.14.7
Release:        0
Summary:        Scripts to create standalone executables from Python scripts
License:        Python-2.0
URL:            https://github.com/anthony-tuininga/cx_Freeze
Source:         https://github.com/anthony-tuininga/cx_Freeze/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  patchelf
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%autosetup -p1 -n cx_Freeze-%{version}
sed -i -e '/^#!\//, 1d' samples/*/*.py
chmod a-x cx_Freeze/initscripts/*.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cxfreeze-quickstart
%python_clone -a %{buildroot}%{_bindir}/cxfreeze
%python_expand chrpath -d %{buildroot}%{$python_sitearch}/cx_Freeze/bases/console*
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# bdist_rpm is not long for this world, and it always execs the default Python
%pytest_arch -k 'not test_bdist_rpm'

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
%{python_sitearch}/cx_Freeze
%{python_sitearch}/cx_Freeze-%{version}*info

%changelog
