#
# spec file for package openSUSE-driverupdate (Version 11.1)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           openSUSE-driverupdate
#BuildRequires:  yast2-pkg-bindings
Url:            http://www.suse.com
License:        BSD-3-Clause
Group:          System/YaST
AutoReqProv:    off
Version:        11.1
Release:        4
Summary:        Driverupdate for openSUSE releases
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         dud.config
Source1:        logo.png
Source2:        newfiles
Source3:        COPYING
Prefix:         /CD1
#
%ifarch	%ix86
%define myarch	i386
%else
%define	myarch	%{_target_cpu}
%endif

%description
Driverupdate for openSUSE - only available online



%prep

%build

%install
basedir=$RPM_BUILD_ROOT/CD1/linux/suse/%{myarch}-%{version}
mkdir -p $basedir
install -D -m 644 %{SOURCE0} $basedir/dud.config
install -D -m 644 %{SOURCE1} $basedir/inst-sys/usr/share/YaST2/theme/openSUSE/wizard/logo.png
grep -v '^#' %{SOURCE2} | while read filepath; do
    test -n "$filepath" || continue
    echo "$filepath"
    test -f $filepath && cp -v -a --parents $filepath $basedir/inst-sys/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/CD1

%changelog
* Mon Mar 16 2009 coolo@suse.de
- reset needed files
* Fri Dec 12 2008 mvidner@suse.de
- Included fix from yast2-ntp-client-2.17.10:
- At install time, do not overwrite the original ntp.conf but add our
  changes instead. Specifically netconfig needs the key config
  preserved (bnc#449615).
- Due to [that] change, the Configure button at install time
  would access settings that would be ignored. Removed it.
  (bnc#449615 c15)
* Thu Nov 27 2008 coolo@suse.de
- trying it with real files
* Tue Nov 25 2008 coolo@suse.de
- do not hardcode 11.0
* Mon Nov 24 2008 coolo@suse.de
- reset for 11.1
* Wed Jul 16 2008 coolo@suse.de
- include Xvnc (bnc#389386)
* Mon Jun 16 2008 coolo@suse.de
- initial package to build driver updates for all archs
