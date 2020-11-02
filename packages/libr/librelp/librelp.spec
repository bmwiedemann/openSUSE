#
# spec file for package librelp
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


%define library_name librelp0
Name:           librelp
Version:        1.8.0
Release:        0
Summary:        A reliable logging library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.librelp.com/
Source:         http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls) >= 2.0.0
BuildRequires:  pkgconfig(openssl)

%description
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

RELP (and hence) librelp assures that no message is lost, not even when
connections break and a peer becomes unavailable. The current version of RELP
has a minimal window of opportunity for message duplication after a session has
been broken due to network problems. In this case, a few messages may be
duplicated (a problem that also exists with plain tcp syslog). Future versions
of RELP will address this shortcoming.

Please note that RELP is a general-purpose, extensible logging protocol. Even
though it was designed to solve the urgent need of rsyslog-to-rsyslog
communication, RELP supports many more applications. Extensible command verbs
provide ample opportunity to extend the protocol without affecting existing
applications.

%package -n %{library_name}
Summary:        A reliable logging library
Group:          Development/Libraries/C and C++

%description -n %{library_name}
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

RELP (and hence) librelp assures that no message is lost, not even when
connections break and a peer becomes unavailable. The current version of RELP
has a minimal window of opportunity for message duplication after a session has
been broken due to network problems. In this case, a few messages may be
duplicated (a problem that also exists with plain tcp syslog). Future versions
of RELP will address this shortcoming.

Please note that RELP is a general-purpose, extensible logging protocol. Even
though it was designed to solve the urgent need of rsyslog-to-rsyslog
communication, RELP supports many more applications. Extensible command verbs
provide ample opportunity to extend the protocol without affecting existing
applications.

%package devel
Summary:        A reliable logging library
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}
Requires:       libgnutls-devel >= 2.0.0
Requires:       pkgconfig(openssl)

%description devel
librelp is an easy to use library for the RELP protocol. RELP in turn provides
reliable event logging over the network (and consequently RELP stands for
Reliable Event Logging Protocol). RELP was initiated by Rainer Gerhards after
he was finally upset by the lossy nature of plain tcp syslog and wanted a cure
for all these dangling issues.

RELP (and hence) librelp assures that no message is lost, not even when
connections break and a peer becomes unavailable. The current version of RELP
has a minimal window of opportunity for message duplication after a session has
been broken due to network problems. In this case, a few messages may be
duplicated (a problem that also exists with plain tcp syslog). Future versions
of RELP will address this shortcoming.

Please note that RELP is a general-purpose, extensible logging protocol. Even
though it was designed to solve the urgent need of rsyslog-to-rsyslog
communication, RELP supports many more applications. Extensible command verbs
provide ample opportunity to extend the protocol without affecting existing
applications.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --with-pic \
  --enable-tls=yes

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/librelp.la

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files -n librelp0
%license COPYING
%{_libdir}/librelp.so.*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README doc/*.html
%{_includedir}/librelp.h
%{_libdir}/librelp.so
%{_libdir}/pkgconfig/relp.pc

%changelog
