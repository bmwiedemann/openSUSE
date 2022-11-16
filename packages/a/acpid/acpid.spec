#
# spec file for package acpid
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


Name:           acpid
Version:        2.0.34
Release:        0
Summary:        Daemon to execute actions on ACPI events
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://sourceforge.net/projects/acpid2/
Source:         https://downloads.sourceforge.net/project/acpid2/%{name}-%{version}.tar.xz
Source3:        README.SUSE
Source5:        events.power_button
Source6:        thinkpad_handler
Source7:        power_button
Source8:        acpid.service
Source9:        events.thinkpad
Source10:       events.sleep_button
Source11:       sleep_button
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         acpid-makefile.patch
BuildRequires:  systemd-rpm-macros
%systemd_ordering

%description
ACPID is a flexible, extensible daemon for delivering ACPI events. It
listens to a file (/proc/acpi/event) and, when an event occurs,
executes programs to handle the event. The start script loads all
needed modules.

%prep
%setup -q
%patch1

cp %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE9} %{SOURCE10} %{SOURCE11} .

%build
export CFLAGS="%{optflags}"
export LDFLAGS="-Wl,-z,relro,-z,now"
%configure
%make_build

%install
%make_install BINDIR=%{_sbindir}
install -Dm 744 thinkpad_handler %{buildroot}%{_libexecdir}/acpid/thinkpad_handler
install -Dm 644 events.thinkpad %{buildroot}%{_sysconfdir}/acpi/events/thinkpad
mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE8} %{buildroot}/%{_unitdir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcacpid

# formerly installed, but no longer useful with systemd. Keep as documentation.
cp -p events.power_button events.sleep_button power_button sleep_button samples/
# for the rpmlint fascists
mv samples examples
# keep the logfile
install -dm 755 %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/acpid

%pre
%service_add_pre acpid.service

%post
%service_add_post acpid.service

%postun
%service_del_postun acpid.service

%preun
%service_del_preun acpid.service

%files
%dir %{_sysconfdir}/acpi
%dir %{_sysconfdir}/acpi/events
%{_sysconfdir}/acpi/events/thinkpad
%{_libexecdir}/acpid
%{_unitdir}/%{name}.service
%{_sbindir}/rcacpid
%{_sbindir}/acpid
%{_sbindir}/kacpimon
%{_bindir}/acpi_listen
%doc README.SUSE README Changelog examples
%{_mandir}/man8/acpid.8%{?ext_man}
%{_mandir}/man8/acpi_listen.8%{?ext_man}
%{_mandir}/man8/kacpimon.8%{?ext_man}
%ghost %config(noreplace,missingok) %{_localstatedir}/log/acpid

%changelog
