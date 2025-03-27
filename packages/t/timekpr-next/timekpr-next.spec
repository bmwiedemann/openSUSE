#
# spec file for package timekpr-next
#
# Copyright (c) 2024 SUSE LLC
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
%define         shortname timekpr
%define         _confdir %{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}
%define         _sitelib %( echo %{python3_sitelib} | cut -c 10- )
Name:           %{shortname}-next
Version:        0.5.7
Release:        0
Summary:        Keep control of computer usage
License:        GPL-3.0-only
URL:            https://launchpad.net/%{shortname}-next
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        system-group-%{shortname}.conf
Source2:        README.SUSE.md
Patch0:         tmp_file_issue_1cec26bd22b73f00b4a834b7f66cd92895b2901d.patch
Patch1:         tmp_file_issue_07e0b29763def53d95611f9ee4a2f54ae50df38c.patch
BuildRequires:  appstream-glib
BuildRequires:  sysuser-tools
BuildRequires:  python3-base
Requires(pre):  system-group-%{shortname} = %{version}
Requires(post): systemd
Requires:       python3-dbus-python
Requires:       python3-psutil
Requires:       typelib-1_0-AppIndicator3-0_1
Recommends:     pkexec
Recommends:     python3-espeak
Recommends:     logrotate
BuildArch:      noarch

%description
Timekpr-nExT is a program that tracks and controls the computer usage
of your user accounts. You can limit their daily usage based on a
timed access duration and configure periods of day when they can or
cannot log in.
.
This may be used for parental control to limit the amount of screen time
a child spends in front of the computer.

%package -n system-group-%{shortname}
Summary:        System group %{shortname} for %{name}
%sysusers_requires

%description -n system-group-%{shortname}
System group %{shortname} for package %{name}

%lang_package

%prep
%autosetup -n %{name} -p1
sed -i 's|python3/dist-packages|%{_sitelib}|g' bin/* client/*.py debian/install \
   resource/server/systemd/timekpr.service server/timekprd.py
sed -i 's|syslog|journal|g' resource/server/systemd/timekpr.service

%build

%install
# install files
grep -v -e '^#' -e '^$' debian/install | sed -e 's| etc/dbus-1/| usr/share/dbus-1/|g' \
     -e 's|/$||' -e 's| lib/systemd/| usr/lib/systemd/|g' \
     -e 's|^\(.\+/\)\(.*\) \(.*\)/\?$|mkdir -p %{buildroot}/\3 ; cp \1\2 %{buildroot}/\3|g' | sh -
%if 0%{?suse_version} > 1500
install -d %{buildroot}%{_distconfdir}/xdg/autostart
install -d %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/xdg/autostart/timekpr-client.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/timekpr-client.desktop
%endif
mv %{buildroot}/%{_sysconfdir}/logrotate.d/%{shortname} %{buildroot}%{_confdir}/logrotate.d/%{name}

# appdata file
install -Dpm 644 resource/appstream/org.%{shortname}.%{name}.metainfo.xml %{buildroot}%{_datadir}/metainfo/org.%{shortname}.%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{shortname}.%{name}.metainfo.xml

# README.SUSE
cp -a %{SOURCE2} .

%find_lang %{shortname}

# group
install -m 644 -Dt %{buildroot}%{_sysusersdir} %{SOURCE1}

%pre
%service_add_pre %{shortname}.service

%post
%service_add_post %{shortname}.service
systemctl reload dbus

%post -n system-group-%{shortname}
%sysusers_create system-group-%{shortname}.conf

%preun
%service_del_preun %{shortname}.service

%postun
%service_del_postun %{shortname}.service

%files
%doc README.md README.SUSE.md
%license debian/copyright
%{_bindir}/*
%{_unitdir}/%{shortname}.service
%{_confdir}/xdg/autostart/%{shortname}-client.desktop
%config %{_confdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{shortname}
%config(noreplace) %{_sysconfdir}/%{shortname}/%{shortname}.conf
%{_datadir}/dbus-1
%{_datadir}/polkit-1
%{_datadir}/applications/*
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/org.timekpr.timekpr-next.metainfo.xml
%{_datadir}/%{shortname}
%{python3_sitelib}/%{shortname}
%{_sharedstatedir}/%{shortname}

%files lang -f %{shortname}.lang
%dir %{_datadir}/locale/*/*

%files -n system-group-%{shortname}
%_sysusersdir/system-group-%{shortname}.conf

%changelog
