#
# spec file for package monitoring-plugins-mem
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           monitoring-plugins-mem
Version:        20120618
Release:        0
Summary:        Check memory plugin for Nagios
License:        MIT
Group:          System/Monitoring
Url:            https://github.com/justintime/nagios-plugins
Source0:        check_mem.tar.bz2
Source1:        monitoring-plugins-mem-apparmor
Source2:        monitoring-plugins-mem-rpmlintrc
Source3:        nrpe-check_mem
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         monitoring-plugins-mem-add_php_to_pnp4nagios_template.patch
Patch1:         monitoring-plugins-mem-min_max_perfdata.patch
%if 0%{?suse_version} > 1010
# nagios can execute the script with embedded perl
Recommends:     perl
%endif
Provides:       nagios-plugins-mem = %{version}-%{release}
Obsoletes:      nagios-plugins-mem < %{version}-%{release}
BuildRequires:  nagios-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
We have always monitored RAM usage on all of boxes. Sure, there's the argument
that unused RAM is money wasted, but I always like to know not just when the
box is swapping, but when it's about to start swapping. There have been a few
plugins over the years that I've used for this - check_ram for Solaris,
check_mem for Linux, and there's also check_mem.pl.

%prep
%setup -q -n check_mem
%patch0 -p1
%patch1 -p1

%build

%install
install -D -m755 check_mem.pl %{buildroot}/%{nagios_plugindir}/check_mem
ln -s %{nagios_plugindir}/check_mem %{buildroot}/%{nagios_plugindir}/check_mem.pl
install -D -m644 check_mem.php %{buildroot}/%{pnp4nagios_templatedir}/check_mem.php
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_mem.pl
sed -e "s|/usr/lib/nagios/plugins/check_mem.pl|/usr/lib/nagios/plugins/check_mem|g" \
	%{SOURCE1} > %{buildroot}%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_mem
install -Dm644 %{SOURCE3} %{buildroot}%{nrpe_sysconfdir}/check_mem.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{_sysconfdir}/apparmor.d
%dir %{nrpe_sysconfdir}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_mem
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_mem.pl
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_mem*
%dir %{pnp4nagios_datarootdir}
%dir %{pnp4nagios_templatedir}
%config(noreplace) %{pnp4nagios_templatedir}/check_mem.php
%config(noreplace) %{nrpe_sysconfdir}/check_mem.cfg

%changelog
