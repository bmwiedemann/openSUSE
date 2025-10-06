#
# spec file for package monitoring-plugins-nwc_health
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2014-2024, Martin Hauke <mardnh@gmx.de>
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


%define         realname check_nwc_health
Name:           monitoring-plugins-nwc_health
Version:        12.8
Release:        0
Summary:        This plugin checks the health of network components and interfaces
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://labs.consol.de/nagios/check_nwc_health/
#Git-Clone      https://github.com/lausser/check_nwc_health.git
Source:         %{realname}-%{version}.tar.gz
# https://raw.githubusercontent.com/lausser/check_nwc_health/master/check_nwc_health.php
Source1:        check_nwc_health.php
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-nwc_health = %{version}-%{release}
Obsoletes:      nagios-plugins-nwc_health < %{version}-%{release}
Requires:       perl-Nagios-Plugin
Requires:       perl-Net-SNMP
Requires:       perl(File::Slurp)
Requires:       perl(JSON)
Requires:       perl(JSON::XS)
BuildArch:      noarch

%description
This plugin checks the hardware health and various interface metrics of
network components like switches and routers.

%prep
%autosetup -n %{realname}-%{version}

%build
autoreconf -fiv
%configure \
	--libexecdir=%{nagios_plugindir} \
	--with-nagios-user=%{nagios_user} \
	--with-nagios-group=%{nagios_group} \
	--with-perl=%{_bindir}/perl \
	--with-degrees=celsius \
	--enable-perfdata \
	--enable-hwinfo
%make_build

%install
%make_install
install -D -m644 %{SOURCE1} %{buildroot}/%{pnp4nagios_templatedir}/check_nwc_health.php

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%license COPYING
# avoid build dependency of nagios - own the dirs
%dir %{nagios_libdir}
%{nagios_plugindir}/
%dir %{pnp4nagios_datadir}
%dir %{pnp4nagios_templatedir}
%{pnp4nagios_templatedir}/check_nwc_health.php

%changelog
