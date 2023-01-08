#
# spec file for package post-build-checks
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


Name:           post-build-checks
Summary:        post checks for build after rpms have been created
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        84.87+git20230106.3a359c5
Release:        0
PreReq:         aaa_base
PreReq:         permissions
PreReq:         sed
Requires:       aaa_base-malloccheck
Requires:       gawk
URL:            https://github.com/openSUSE/post-build-checks
#
# Note: don't rebuild this manually. Instead submit your patches
# for inclusion in the git repo!
#
# git clone https://github.com/openSUSE/post-build-checks.git
# osc service dr
#
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
some scripts to check for problems like test-installing the newly
created rpms and checking the logfile for errors.

This package will also set/change the following sysconfig variables, so
it may not be a good idea to install this to a running system:
/etc/sysconfig/security:PERMISSION_SECURITY="secure"
/etc/sysconfig/clock:TIMEZONE="UTC"

%prep
%setup -q

%build
%define _lto_cflags %{nil}
# nothing to do

%install
install -d $RPM_BUILD_ROOT/usr/lib/build/checks
install -d $RPM_BUILD_ROOT/usr/lib/build/post-mkbaselibs-checks
install -d $RPM_BUILD_ROOT/usr/lib/build/checks-data
install -d $RPM_BUILD_ROOT/usr/lib/build/helper
install -d $RPM_BUILD_ROOT/usr/lib/build/finalize-system
install -m 755 checks/* $RPM_BUILD_ROOT/usr/lib/build/checks
install -m 755 post-mkbaselibs-checks/* $RPM_BUILD_ROOT/usr/lib/build/post-mkbaselibs-checks
install -m 644 checks-data/* $RPM_BUILD_ROOT/usr/lib/build/checks-data
install -m 755 helper/* $RPM_BUILD_ROOT/usr/lib/build/helper
install -m 755 finalize-system/* $RPM_BUILD_ROOT/usr/lib/build/finalize-system
install -m 644 -D suse-buildsystem.sh  $RPM_BUILD_ROOT/etc/profile.d/suse-buildsystem.sh
install -m 644 -D suse-ignored-rpaths.conf $RPM_BUILD_ROOT/etc/suse-ignored-rpaths.conf
chmod 755 $RPM_BUILD_ROOT/usr/lib/build/checks-data/check*

%files
%license COPYING
/usr/lib/build
/etc/profile.d/suse-buildsystem.sh
/etc/suse-ignored-rpaths.conf

%changelog
