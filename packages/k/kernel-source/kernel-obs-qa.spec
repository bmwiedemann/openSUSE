#
# spec file for package kernel-obs-qa
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# needsrootforbuild


%define patchversion 5.12.0
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

Name:           kernel-obs-qa
BuildRequires:  kernel-default
# kernel-obs-build must be also configured as VMinstall, but is required
# here as well to avoid that qa and build package build parallel
BuildRequires:  kernel-obs-build
BuildRequires:  modutils
ExclusiveArch:  aarch64 armv6hl armv7hl ppc64 ppc64le riscv64 s390x x86_64
%if 0%{?suse_version} < 1200
# for SLE 11
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
Summary:        Basic QA tests for the kernel
License:        GPL-2.0
Group:          SLES
Version:        5.12.0
%if 0%{?is_kotd}
Release:        <RELEASE>.gc4830af
%else
Release:        0
%endif

%description
This package is using the kernel compiled within Open Build Service(OBS)
projects and runs basic tests.

%prep

%build

%check
# More tests are comming, currently the main test is the existens of
# this spec file. It does trigger a build within OBS VM which is using
# the kernel of the same project.

# test suites should be packaged in other packages, but build required
# and called here.

krel=$(uname -r)
if test ! -d "/lib/modules/$krel/kernel"; then
	echo "Kernel package for $krel not installed; exiting"
	exit 0
fi
/sbin/modprobe loop

%install
mkdir -p %{buildroot}/usr/share/%name
touch %{buildroot}/usr/share/%name/logfile

%files
%defattr(-,root,root)
/usr/share/%name

%changelog
