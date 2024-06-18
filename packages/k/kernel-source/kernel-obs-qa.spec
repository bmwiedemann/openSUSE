#
# spec file for package kernel-obs-qa
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
# needsrootforbuild


%define patchversion 6.9.5
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

Name:           kernel-obs-qa
Version:        6.9.5
%if 0%{?is_kotd}
Release:        <RELEASE>.gc9c2e24
%else
Release:        0
%endif
Summary:        Basic QA tests for the kernel
License:        GPL-2.0-only
Group:          SLES
BuildRequires:  kernel-default
# kernel-obs-build must be also configured as VMinstall, but is required
# here as well to avoid that qa and build package build parallel
BuildRequires:  kernel-obs-build
BuildRequires:  modutils
%if ! 0%{?is_kotd} || %{?is_kotd_qa}%{!?is_kotd_qa:0}
ExclusiveArch:  aarch64 armv6hl armv7hl ppc64le riscv64 s390x x86_64
%else
ExclusiveArch:  do_not_build
%endif

%description
This package is using the kernel compiled within Open Build Service(OBS)
projects and runs basic tests.

%files
/usr/share/%name

%prep

%build

%check
# More tests are comming, currently the main test is the existens of
# this spec file. It does trigger a build within OBS VM which is using
# the kernel of the same project.

# test suites should be packaged in other packages, but build required
# and called here.

krel=$(uname -r)
if test ! -d "/lib/modules/$krel/kernel" && test ! -d "/usr/lib/modules/$krel/kernel"; then
	echo "Kernel package for $krel not installed; exiting"
	exit 0
fi
/sbin/modprobe loop

%install
mkdir -p %{buildroot}/usr/share/%name
touch %{buildroot}/usr/share/%name/logfile

%changelog
