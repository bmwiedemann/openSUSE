#
# spec file for package yast2-ntp-client
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


Name:           yast2-ntp-client
Version:        4.2.4
Release:        0
Summary:        YaST2 - NTP Client Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
Url:            https://github.com/yast/yast-ntp-client

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  augeas-lenses
BuildRequires:  autoyast2-installation
# Needed for /etc/cron.* ownership; those directories have special permission handling
BuildRequires:  cron
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
# cwm/popup
BuildRequires:  yast2 >= 4.1.15
BuildRequires:  yast2-country-data
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa) >= 0.6.0
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# proper acting TargetFile when scr is switched
Requires:       augeas-lenses
# cwm/popup
Requires:       yast2 >= 4.1.15
Requires:       yast2-country-data
# needed for network/config agent
# Yast::Lan.dhcp_ntp_servers
Requires:       yast2-network >= 4.1.17
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%rb_default_ruby_abi:cfa) >= 0.6.0

Obsoletes:      yast2-ntp-client-devel-doc

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
# upgrade old name and convert it to chrony (bsc#1079122)
if [ -f /etc/cron.d/novell.ntp-synchronize ]; then
  mv /etc/cron.d/novell.ntp-synchronize /etc/cron.d/suse-ntp_synchronize
  sed -i 's:\* \* \* \* root .*:* * * * root /usr/sbin/chronyd -q \&>/dev/null:' /etc/cron.d/suse-ntp_synchronize
fi

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_yncludedir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_ydatadir}
%{yast_schemadir}
%ghost %{_sysconfdir}/cron.d/suse-ntp_synchronize
%{yast_icondir}
%license COPYING
%doc %{yast_docdir}

%changelog
