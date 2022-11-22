#
# spec file for package yast2-ntp-client
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-ntp-client
Version:        4.5.2
Release:        0
Summary:        YaST2 - NTP Client Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-ntp-client

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  augeas-lenses
BuildRequires:  update-desktop-files
# need as it own /usr/lib/systemd and for systemd macros
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
# Replace PackageSystem with Package
BuildRequires:  yast2 >= 4.4.38
BuildRequires:  yast2-country
BuildRequires:  yast2-country-data
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa) >= 0.6.0
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# Y2Network::NtpServer
BuildRequires:  yast2-network >= 4.2.55
# yast/rspec/helpers.rb
BuildRequires:  yast2-ruby-bindings >= 4.4.7

# proper acting TargetFile when scr is switched
Requires:       augeas-lenses
# Replace PackageSystem with Package
Requires:       yast2 >= 4.4.38
Requires:       yast2-country-data
# needed for network/config agent
# Y2Network::NtpServer
Requires:       yast2-network >= 4.2.55
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%rb_default_ruby_abi:cfa) >= 0.6.0

Obsoletes:      yast2-ntp-client-devel-doc

Supplements:    autoyast(ntp-client)

BuildArch:      noarch

%description
This package contains the YaST2 component for NTP client configuration.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%post
%service_add_post yast-timesync.service

# upgrade old name and convert it to chrony (bsc#1079122)
if [ -f /etc/cron.d/novell.ntp-synchronize ]; then
  mv /etc/cron.d/novell.ntp-synchronize /etc/cron.d/suse-ntp_synchronize
  sed -i 's:\* \* \* \* root .*:* * * * root /usr/sbin/chronyd -q \&>/dev/null:' /etc/cron.d/suse-ntp_synchronize
fi

# and now update cron to systemd timer. We need to support upgrade from SLE12 and also SLE15 SP1.
# jsc#SLE-9113
if [ -f /etc/cron.d/suse-ntp_synchronize ]; then
  /usr/bin/erb timeout=$(grep -o '[[:digit:]]\+' /etc/cron.d/suse-ntp_synchronize) /usr/share/YaST2/data/yast-timesync.timer.erb > /etc/systemd/system/yast-timesync.timer
  /usr/bin/systemctl enable yast-timesync.timer
  /usr/bin/systemctl start yast-timesync.timer
  rm /etc/cron.d/suse-ntp_synchronize
fi

%pre
%service_add_pre yast-timesync.service

%postun
%service_del_postun yast-timesync.service

%preun
%service_del_preun yast-timesync.service

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_yncludedir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_ydatadir}
%{yast_schemadir}
%{yast_icondir}
%{_unitdir}/yast-timesync.service
%license COPYING
%doc %{yast_docdir}

%changelog
