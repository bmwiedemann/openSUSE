#
# spec file for package monitoring-plugins-rsync
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


Name:           monitoring-plugins-rsync
Summary:        Check rsync servers availability
License:        GPL-2.0-or-later
Group:          System/Monitoring
Version:        1.02
Release:        0
URL:            https://www.monitoringexchange.org/inventory/Check-Plugins/Network/check_rsync
Source0:        check_rsync
Source1:        COPYING
Patch1:         monitoring-plugins-rsync-timeout.patch
Patch2:         monitoring-plugins-rsync-hidden_modules.patch
Patch3:         monitoring-plugins-rsync-option_binary.patch
BuildRequires:  nagios-rpm-macros
%if 0%{?suse_version} > 1010
# nagios can execute the script with embedded perl
Recommends:     perl
%endif
Requires:       rsync
Requires:       perl(Getopt::Long)
Provides:       nagios-plugins-rsync = %{version}-%{release}
Obsoletes:      nagios-plugins-rsync <= %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Checks rsync servers availability, as well as (optionally) individual
modules availability. It also supports authentication on modules.

Usage: check_rsync -H  [-p ] [-m [,,] [-m [,,]...]]

The only required argument is -H, in which case it will only try to
list modules on the Rsync server.

%prep
%setup -q -T -c %name
install -m644 %{SOURCE0} .
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build

%install
mkdir -p %buildroot/%{nagios_plugindir}
sed -e "s|/usr/local/nagios/libexec|%{nagios_plugindir}|g" check_rsync > %buildroot/%{nagios_plugindir}/check_rsync
chmod +x %buildroot/%{nagios_plugindir}/check_rsync

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_rsync

%changelog
