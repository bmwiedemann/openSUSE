#
# spec file for package twilio-utils
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2013 Archie L. Cobbs <archie@dellroad.org>
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


%define twilogdir   %{_var}/lib/twilog
%define pkgdir      %{_datadir}/%{name}
%define defaultconf %{_sysconfdir}/twilio.conf

Name:           twilio-utils
Version:        1.0.5
Release:        0
Summary:        Command line utilities for Twilio users
License:        Apache-2.0
Group:          Productivity/Text/Utilities
Source:         %{name}-%{version}.tar.gz
Url:            http://twilio-utils.googlecode.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  libxslt-tools
BuildRequires:  make
BuildRequires:  php
BuildRequires:  xmlstarlet
Requires:       curl >= 7.18
Requires:       libxslt-tools
Requires:       php
Requires:       xmlstarlet
%if %suse_version < 1320
BuildRequires:  util-linux
Requires:       util-linux
%else
BuildRequires:  util-linux-systemd
Requires:       util-linux-systemd
%endif

%description
The twilio-utils project contains a few UNIX command-line utilities
that are handy when working with Twilio:

* sendsms - Send an outbound SMS message via Twilio
* smslen - Calculate SMS payload length
* twilog - Download Twilio notifications into syslog 

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

# Install twilog state directory
install -d %{buildroot}%{twilogdir}

# Install the sample config file as the default config
install -d %{buildroot}`dirname %{defaultconf}`
install %{buildroot}%{_docdir}/%{name}/twilio.conf.sample %{buildroot}%{defaultconf}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/%{name}
%attr(600,root,root) %config(noreplace) %verify(not size md5 mtime) %{defaultconf}
%{_datadir}/%{name}
%{twilogdir}

%changelog
