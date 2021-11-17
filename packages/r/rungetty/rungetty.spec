#
# spec file for package rungetty
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           rungetty
Version:        1.2
Release:        0
Summary:        Minimal Getty for Virtual Consoles
License:        GPL-2.0-or-later
Group:          System/Base
Source:         %{name}-%{version}.tar.bz2
Patch1:         01_rungetty-remove_sys_errlist.patch
Patch2:         02_rungetty-manpage.patch
Patch3:         03_rungetty-disable_path.patch
Patch4:         04_rungetty-use_signed_int.patch
Patch5:         05_rungetty-missing-call-to-setgroups-before-setuid.patch
Patch6:         06_rungetty-get_supplementary_groups_for_process.patch
Patch7:         07_rungetty-allow_autologin-on-all-ttys.patch
Provides:       sysvinit:/sbin/mingetty

%description
rungetty might be the getty you were looking for when you want to run any
program, not just login. If a different program than login is used it usually
is run as nobody:nogroup, or the user/group specified on the commandline.
rungetty can even be configured to autologin, under certain circumstances.
See the manual page for more information.

You have to change some lines in %{_sysconfdir}/inittab for having any effect after
installing the package.  rungetty is based on mingetty and therefore not
suitable for serial use.

%prep
%autosetup -p1 

%build
%make_build CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
install -m 755 rungetty %{buildroot}%{_sbindir}/
install -m 644 rungetty.8 %{buildroot}%{_mandir}/man8/

%files
%license COPYING
%doc CHANGELOG README THANKS
%{_mandir}/man8/rungetty.8%{?ext_man}
%{_sbindir}/rungetty

%changelog
