#
# spec file for package switch_sles_sle-hpc
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


ExclusiveArch:  x86_64 aarch64 noarch
Name:           switch_sles_sle-hpc
Version:        0.2
Release:        0
Summary:        Utility to switch between SLES and SLE-HPC on SLE-12
License:        MIT
Group:          System/Management
URL:            http://www.suse.com
Source0:        switch
Source1:        LICENSE
Source2:        README.SUSE
Source3:        %{name}.8
Requires:       SUSEConnect
Requires:       bash
Requires:       coreutils
Requires:       rpm
Requires:       sed
Requires:       zypper
BuildArch:      noarch

%description
This tool is intended for users who are SLES subscribers but would like
to migrate to the new SLE-HPC subscription.

%prep
%setup -Tc
cp %{S:1} %{S:2} .

%build

%install
install -D -m 0755 %{S:0} %{buildroot}%{_sbindir}/switch_sles_sle-hpc
ln -s %{_sbindir}/switch_sles_sle-hpc %{buildroot}%{_sbindir}/switch_to_sle-hpc
install -D -m 0644 %{S:3} %{buildroot}%{_mandir}/man8/%{basename:%{S:3}}

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define my_license %license
%else
%define my_license %doc
%endif

%files
%defattr(-,root,root,0755)
%my_license LICENSE
%doc README.SUSE
%{_sbindir}/switch_to_sle-hpc
%{_sbindir}/switch_sles_sle-hpc
%{_mandir}/man8/*

%changelog
