#
# spec file for package prelude-lml
#
# Copyright (c) 2020 SUSE LLC
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


Name:           prelude-lml
Version:        5.2.0
Release:        0
Summary:        The prelude log analyzer
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
# libmissing/test is GPL-3.0+
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-or-later
Group:          System/Daemons
URL:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
Source3:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz.sig
Source4:        https://www.prelude-siem.org/attachments/download/233/RPM-GPG-KEY-Prelude-IDS#/%{name}.keyring
# Add default syslog format to work out of the box
Patch0:         %{name}-conf_rsyslog.patch
# Fix make check
Patch1:         %{name}-fix_check.patch
# Fix etc files permissions
Patch2:         %{name}-fix_etc_perms.patch
BuildRequires:  gamin-devel
BuildRequires:  libprelude-devel >= 5.2.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls) >= 1.0.17
BuildRequires:  pkgconfig(icu-io) >= 3.0
BuildRequires:  pkgconfig(libpcre) >= 4.1
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
Prelude-LML is a log analyser that allows Prelude to collect and
analyze information from all kind of applications emitting logs or
syslog messages in order to detect suspicious activities and transform
them into Prelude-IDMEF alerts. Prelude-LML handles events generated
by a large set of applications

%package devel
Summary:        Header files and libraries for prelude-lml development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libprelude-devel >= 5.2.0

%description devel
Libraries, include files, etc you can use to develop custom
Prelude LML plugins.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
%configure
%make_build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/ruleset/
mkdir -p %{buildroot}/%{_sbindir}
%make_install
rm -f %{buildroot}/%{_libdir}/%{name}/debug.la
rm -f %{buildroot}/%{_libdir}/%{name}/pcre.la
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/%{_var}/lib/%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
rm -rf %{buildroot}/%{_localstatedir}/run/%{name}
install -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%post
/sbin/ldconfig
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
/sbin/ldconfig
%service_del_postun %{name}.service

%files
%license COPYING
%doc NEWS HACKING.README README
%attr(0770,-,-) %dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,-,-) %{_sysconfdir}/%{name}/plugins.rules
%config(noreplace) %attr(0640,-,-) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0770,-,-) %dir %{_sysconfdir}/%{name}/ruleset/
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/debug.so
%{_libdir}/%{name}/pcre.so
%{_sbindir}/rc%{name}
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%dir %{_var}/lib/%{name}
%ghost /run/%{name}

%files devel
%license COPYING
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/%{name}.h

%changelog
