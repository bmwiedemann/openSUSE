#
# spec file for package python-cx_Freeze
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%bcond_without libalternatives
Name:           python-cx_Freeze
Version:        8.0.0
Release:        0
Summary:        Scripts to create standalone executables from Python scripts
License:        Python-2.0
URL:            https://github.com/anthony-tuininga/cx_Freeze
Source:         https://github.com/anthony-tuininga/cx_Freeze/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#marcelotduarte/cx_Freeze#2842
Patch0:         use-only-console-on-python-313.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module filelock >= 3.12.3}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging >= 24}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-datafiles}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 65}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  patchelf
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       patchelf
Requires:       python-filelock >= 3.12
Requires:       python-packaging >= 24
Requires:       python-setuptools >= 65
# we provide same binary like the deprecated py2 variant
Conflicts:      %{oldpython}-cx_Freeze
%if 0%{python_version_nodots} < 311
Requires:       python-tomli >= 2.0.1
%endif
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
sed -i -e 's/-nauto//' pyproject.toml
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
# test_bdist_deb_simple_pyproject runs the binary, which is currently complicated with libalternatives: https://github.com/openSUSE/python-rpm-macros/pull/196
%pytest_arch -k 'not (test_command_bdist_rpm or test_command_build_exe or test_command_build or test_bdist_appimage or test_bdist_deb_simple_pyproject)'

%pre
%python_libalternatives_reset_alternative cxfreeze-quickstart
%python_libalternatives_reset_alternative cxfreeze

%files %{python_files}
%doc README.md
%license doc/src/license.rst
%python_alternative %{_bindir}/cxfreeze
%python_alternative %{_bindir}/cxfreeze-quickstart
%{python_sitearch}/cx_Freeze
%{python_sitearch}/cx_[Ff]reeze-%{version}.dist-info

%changelog
