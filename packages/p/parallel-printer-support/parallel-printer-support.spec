#
# spec file for package parallel-printer-support
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Silviu Marin-Caea
# Copyright (c) 2011 B1 Systems GmbH, Vohburg, Germany.
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


Name:           parallel-printer-support
Version:        1.00
Release:        0
Summary:        Parallel Printer Support
License:        BSD-2-Clause
Group:          Hardware/Printing
Url:            http://www.opensuse.org
Source:         README.SUSE
Source1:        parallel-printer.conf
# For /usr/bin/systemd-tmpfiles
Requires(post):	systemd
Requires:       aaa_base
Requires:       udev
%if 0%{?suse_version} >= 1330
Requires(pre):  group(lp)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package creates static udev nodes for the parallel ports.  The
purpose is to load the "lp" kernel module automatically the first time
data is sent to the parallel port.

Since the lp kernel module can't autodetect devices, this is the only
way to load the parallel printer modules without manual intervention.

%prep
%setup -c -q -T
cp %{SOURCE0} .

%install
%if 0%{?sles_version} == 11
mkdir -p $RPM_BUILD_ROOT/lib/udev/devices
%endif
%if 0%{suse_version} > 1220
mkdir -p $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/
%endif
%build

%if 0%{suse_version} > 1220
%post
# Create devices nodes at installation time
systemd-tmpfiles --create /usr/lib/tmpfiles.d/parallel-printer.conf

%endif

%files
%defattr(-,root,root,0755)
%doc README.SUSE
%if %{suse_version} > 1220
%dir /usr/lib/tmpfiles.d/
/usr/lib/tmpfiles.d/parallel-printer.conf
%else
%if 0%{?sles_version} == 11
%dir /lib/udev
%dir /lib/udev/devices
%endif
%attr(660,root,lp) %dev(char,6,0) /lib/udev/devices/lp0
%attr(660,root,lp) %dev(char,6,1) /lib/udev/devices/lp1
%attr(660,root,lp) %dev(char,6,2) /lib/udev/devices/lp2
%attr(660,root,lp) %dev(char,6,3) /lib/udev/devices/lp3
%endif

%changelog
