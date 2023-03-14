#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

# Dependency ligo-segments does not build for python2
%define         skip_python2 1

%define bins ligolw_add ligolw_cut ligolw_no_ilwdchar ligolw_print ligolw_segments ligolw_sqlite ligolw_run_sqlite
%define srcname python-ligo-lw

Name:           python-ligo-lw%{?psuffix}
Version:        1.8.3
Release:        0
Summary:        Python LIGO Light-Weight XML I/O Library
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://git.ligo.org/kipp.cannon/python-ligo-lw
Source:         http://software.ligo.org/lscsoft/source/%{srcname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ligo-lw-segments-test-fix.patch badshah400@gmail.com -- Fix a test that randomly fails due to dictionary ordering being undefined
Patch0:         ligo-lw-segments-test-fix.patch
# PATCH-FIX-UPSTREAM ligo-lw-disable-doctests.patch badshah400@gmail.com -- Disable doctests as these are not ready for py 3.10 yet
Patch1:         ligo-lw-disable-doctests.patch
# PATCH-FIX-OPENSUSE ligo-lw-disable-sqlite-test.patch badshah400@gmail.com -- Disable sqlite test that requires network resources
Patch3:         ligo-lw-disable-sqlite-test.patch
# https://git.ligo.org/kipp.cannon/python-ligo-lw/-/commit/693cfc4d4759c1984609effa1dde810a192fe94f
Patch4:         python-ligo-lw-no-python2.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-lal
Requires:       python-ligo-segments
Requires:       python-lscsoft-glue
Requires:       python-python-dateutil
Requires:       python-tqdm
Requires(post): update-alternatives
Requires(postun):update-alternatives
# lal no longer supported for 32bit, and is a hard dependency for ligo-lw
ExcludeArch:    %{ix86}
# SECTION Test requirements
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-lw = %{version}}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module lscsoft-glue}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module tqdm}
BuildRequires:  diffutils
BuildRequires:  libxml2-tools
BuildRequires:  python3
%endif
# /SECTION
%python_subpackages

%description
The LIGO Light-Weight XML format is used extensively by compact object
detection pipeline and associated tool sets.  This package provides a Python
I/O library for reading, writing, and interacting with documents in this
format.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Replace distutils.core by setuptools to fix namespace errors
# https://git.ligo.org/kipp.cannon/python-ligo-lw/-/issues/16
sed -i "1{s/distutils.core/setuptools/}" setup.py

%build
%python_build

%install
%if %{without test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%{lua: for c in string.gmatch(rpm.expand("%bins"), "%S+") do
  print(rpm.expand("%python_clone -a %{buildroot}%{_bindir}/" .. c .. "\n"))
end}
%endif

%check
%if %{with test}
# Test-suite works only for python3 flavors
%{python_expand export PYTHON=$python
export PYTHONDONTWRITEBYTECODE=1
cp -r test test-%{$python_bin_suffix}
pushd test-%{$python_bin_suffix}
%make_build check
popd
}
%endif

%if %{without test}
%post
%python_install_alternative %bins

%postun
%python_uninstall_alternative %bins

%files %{python_files}
%license LICENSE
%{lua: for c in string.gmatch(rpm.expand("%bins"), "%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. c .. "\n"))
end}
%{python_sitearch}/ligo/
%{python_sitearch}/python_ligo_lw-%{version}-py%{python_version}.egg-info/
%{python_sitearch}/python_ligo_lw-%{version}-py%{python_version}-nspkg.pth
%endif

%changelog
