#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
# Tests known to fail on 32 bit due to fp precision
ExcludeArch:    %{ix86}
%else
%bcond_with test
%define psuffix %{nil}
%endif

# NEP 29: numpy, matplotlib do not have a python36 flavor package in TW
%define skip_python36 1

%define ligocommands ligolw_print_tables dmtdq_seg_insert ldbdc ldbdd ldg_submit_dax \
        ligolw_cbc_glitch_page ligolw_combine_segments ligolw_diff ligolw_dq_active ligolw_dq_active_cats \
        ligolw_dq_grapher ligolw_dq_query ligolw_geo_fr_to_dq ligolw_inspiral2mon \
        ligolw_publish_dqxml ligolw_segment_diff ligolw_segment_insert ligolw_segment_intersect \
        ligolw_segment_query ligolw_segment_union ligolw_segments_from_cats ligolw_segments_from_cats_split \
        ligolw_veto_def_check ligolw_veto_sngl_trigger segdb_coalesce

%define modname glue
Name:           lscsoft-glue%{psuffix}
Version:        2.1.0
Release:        0
Summary:        Grid LSC User Environment
License:        GPL-2.0-only
URL:            http://software.ligo.org/lscsoft
Source:         http://software.ligo.org/lscsoft/source/lscsoft-glue-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lscsoft-glue-python-3.10-fixes.patch badshah400@gmail.com -- Fix python3.10 compatibility; patch taken from upstream merge request [https://git.ligo.org/lscsoft/glue/-/merge_requests/83]
Patch0:         lscsoft-glue-python-3.10-fixes.patch
# PATCH-FIX-UPSTREAM lscsoft-glue-disable-doctest.patch badshah400@gmail.com -- Disable some doctests not yet ready for python 3.10
Patch1:         lscsoft-glue-disable-doctest.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ligo-segments
Requires:       python-numpy
Provides:       python-glue = %{version}-%{release}
Obsoletes:      python-glue < %{version}-%{release}
%define oldpython python
Provides:       %{oldpython}-glue = %{version}-%{release}
Obsoletes:      %{oldpython}-glue < %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module lscsoft-glue = %{version}}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

%prep
%autosetup -p1 -n lscsoft-glue-%{version}

%build
%python_build

%install
%if ! %{with test}
%python_install

# SECTION Remove non-library config/php files
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}
rm -fr %{buildroot}%{_prefix}%{_localstatedir}
# /SECTION

%{lua: for c in string.gmatch(rpm.expand("%ligocommands"), "%S+") do
  print(rpm.expand("%python_clone -a %{buildroot}%{_bindir}/" .. c .. "\n"))
end}

%python_expand %fdupes -s %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
%{python_expand export PYTHON=$python
export PYTHONDONTWRITEBYTECODE=1
cp -r test test-%{$python_bin_suffix}
pushd test-%{$python_bin_suffix}
%make_build check
popd
}
%endif

%if ! %{with test}
%post
%python_install_alternative %ligocommands

%postun
# arguments after the master item are ignored
%python_uninstall_alternative %ligocommands

%files %{python_files}
%doc README.md
%license LICENSE
%{lua: for c in string.gmatch(rpm.expand("%ligocommands"), "%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. c .. "\n"))
end}
%{python_sitearch}/glue
%{python_sitearch}/lscsoft_glue-%{version}*-info
%endif

%changelog
