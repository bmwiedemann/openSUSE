#
# spec file for package suse-hpc
#
# Copyright (c) 2025 SUSE LLC
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


Summary:        SUSE HPC Environment
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
Name:           suse-hpc
Version:        0.5.20250102.dbdcd3e
Release:        0
Source0:        macros.hpc
Source1:        dlinfo.c
Source2:        hpc_elf.pl
Source3:        hpc_elf.attr
Source4:        hpc_elflib.attr
Source5:        LICENSE
URL:            http://www.suse.com/hpc

%description
Provide rpm macros for building and installing SUSE HPC
packages.

%prep
cp %{S:1} .

%build
gcc -o dlinfo dlinfo.c -ldl

%install
mkdir -p  %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{S:0} %{buildroot}%{_rpmconfigdir}/macros.d
mkdir -p  %{buildroot}%{_rpmconfigdir}/fileattrs
install -m 755 %{S:2} dlinfo %{buildroot}%{_rpmconfigdir}
install -m 644 %{S:3} %{S:4} %{buildroot}%{_rpmconfigdir}/fileattrs
cp %{S:5} .

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define mylicense %license
%else
%define mylicense %doc
%endif

%files
%mylicense LICENSE
%{_rpmconfigdir}/macros.d/macros.hpc
%{_rpmconfigdir}/dlinfo
%{_rpmconfigdir}/hpc_elf.pl
%{_rpmconfigdir}/fileattrs/*

%changelog
