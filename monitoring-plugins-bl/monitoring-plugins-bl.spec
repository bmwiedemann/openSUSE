#
# spec file for package monitoring-plugins-bl
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


Name:           monitoring-plugins-bl
%define         realname nagios-check_bl
Summary:        Check anti-spam blocklists for given server
License:        GPL-2.0+
Group:          System/Monitoring
Version:        1.0
Release:        0
Url:            https://github.com/opinkerfi/nagios-plugins/tree/master/check_bl
Source:         %realname-%version.tar.bz2
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-bl = %{version}-%{release}
Obsoletes:      nagios-plugins-bl < %{version}-%{release}
Requires:       perl(Net::DNS)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This monitoring plugin will check whether the specified server is in any of the
numerous anti-spam blocklists.

%prep
%setup -q -n %realname-%version

%build

%install
install -Dm0755 check_bl %{buildroot}/%{nagios_plugindir}/check_bl

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_bl

%changelog
