#
# spec file for package rtasdispd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           rtasdispd
Version:        0.1
Release:        0
Summary:        Shows System Status Messages on pSeries Panel Displays
License:        GPL-2.0-or-later
Group:          System/Monitoring
Source:         rtasdispd-%{version}.tar.gz
Source1:        sysconfig.rtasdispd
Source2:        rc.rtasdispd
Patch1:         rtasdispd.open-mode.patch
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
ExclusiveArch:  ppc ppc64 ppc64le

%description
This daemon can show system status information, such as load, uptime,
memory usage, and more on the 2 line front panel display of IBM pSeries
machines.

%prep
%autosetup  -p1

%build
%make_build CFLAGS="%{optflags} -Wall"

%install
mv rtasdispd.1 rtasdispd.8
make DESTDIR=%{buildroot} install MANS=rtasdispd.8
mkdir -p %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_fillupdir}
install -m 755 %{SOURCE2} %{buildroot}%{_initddir}/rtasdispd
ln -s ../..%{_initddir}/rtasdispd %{buildroot}%{_sbindir}/rcrtasdispd
install -m 644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.rtasdispd

%post
%{fillup_and_insserv -y rtasdispd}

%postun
%insserv_cleanup

%files
%license COPYING
%config %{_initddir}/rtasdispd
%{_sbindir}/*
%{_mandir}/man8/*
%{_fillupdir}/sysconfig.rtasdispd

%changelog
