#
# spec file for package supportutils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define support_libdir /usr/lib/supportconfig

Name:           supportutils
Version:        3.1.1
Release:        0
Summary:        Support Troubleshooting Tools
License:        GPL-2.0
Group:          System/Monitoring
Url:            https://github.com/g23guy/supportutils
Source:         %{name}-%{version}.tar.gz
Requires:       iproute2
Requires:       kmod-compat
Requires:       ncurses-utils
Requires:       net-tools
Requires:       sysfsutils
Requires:       tar
Requires:       util-linux-systemd
Requires:       which
Provides:       supportconfig-plugin-icommand
Provides:       supportconfig-plugin-resource
Provides:       supportconfig-plugin-tag
BuildArch:      noarch

%description
A package containing troubleshooting tools. This package contains
the following: supportconfig, chkbin, getappcore, analyzevmcore

%prep
%setup -q

%build
gzip -9f man/*3
gzip -9f man/*5
gzip -9f man/*8

%install
pwd;ls -la
install -d %{buildroot}/sbin
install -d %{buildroot}/etc
install -d %{buildroot}%{_mandir}/man3
install -d %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{support_libdir}/resources
install -d %{buildroot}%{support_libdir}/plugins
install -d %{buildroot}%{_docdir}/%{name}
install -m 544 bin/supportconfig %{buildroot}/sbin
install -m 544 bin/chkbin %{buildroot}/sbin
install -m 544 bin/getappcore %{buildroot}/sbin
install -m 544 bin/analyzevmcore %{buildroot}/sbin
install -m 444 bin/scplugin.rc %{buildroot}%{support_libdir}/resources
install -m 444 bin/supportconfig.rc %{buildroot}%{support_libdir}/resources
install -m 644 man/*.3.gz %{buildroot}%{_mandir}/man3
install -m 644 man/*.5.gz %{buildroot}%{_mandir}/man5
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8
install -m 644 man/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}

%files
%defattr(-,root,root)
/sbin/supportconfig
/sbin/chkbin
/sbin/getappcore
/sbin/analyzevmcore
%dir %{support_libdir}
%dir %{support_libdir}/resources
%dir %{support_libdir}/plugins
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%if 0%{?suse_version} < 1500
%doc %{_docdir}/%{name}/COPYING.GPLv2
%else
%license %{_docdir}/%{name}/COPYING.GPLv2
%endif

%{support_libdir}/resources/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man8/*

%changelog
