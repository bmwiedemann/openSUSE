#
# spec file for package xdmsc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           xdmsc
PreReq:         fillup
Provides:       Xterminal
Version:        0.6
Release:        0
Url:            https://build.opensuse.org/package/show/X11:Utilities/xdmsc
Summary:        XTerminal -- Use SUSE Linux as an X Terminal
License:        GPL-2.0
Group:          System/X11/Utilities
Source:         Xterminal-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Some useful scripts for using SUSE Linux as an X terminal.

You will find the documentation in the following directory

/usr/share/doc/packages/xdmsc/


%prep
%setup -n Xterminal-%{version}

%build
    make -f Makefile.Linux compile

%install
    make -f Makefile.Linux DESTDIR=%{buildroot} ETCRCC=%{_fillupdir} install

%pre
%service_add_pre %{name}@.service

%post
%{fillup_only}
%service_add_post %{name}@.service

%preun
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}@.service

%files
%defattr(-,root,root)
%doc README COPYING
%{_unitdir}/xdmsc@.service
%dir /usr/lib/xdmsc/
%attr(0755,root,root) /usr/lib/xdmsc/rx
%{_fillupdir}/sysconfig.xdmsc

%changelog
