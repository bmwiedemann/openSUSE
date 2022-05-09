#
# spec file for package setroubleshoot
#
# Copyright (c) 2021 SUSE LLC
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


Name:           setroubleshoot
Version:        3.3.26
Release:        0
Summary:        Helps troubleshoot SELinux problems
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://pagure.io/setroubleshoot/
Source:         https://releases.pagure.org/setroubleshoot/%{name}-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}.tmpfiles
Source3:        system-user-setroubleshoot.conf
Patch0:         setroubleshoot-desktop.patch
Patch1:         setroubleshoot-Stop-SetroubleshootFixit-after-10-seconds-of-inactiv.patch
Patch2:         setroubleshoot-Do-not-use-Python-slip-package.patch
Patch3:         setroubleshoot-Gracefully-handle-unavailable-libreport.patch
BuildRequires:  audit-devel
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcap-ng-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  python-setools
BuildRequires:  python3
BuildRequires:  python3-dasbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-selinux >= 1.30.15
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires:       %{name}-plugins >= 3.3.10
Requires:       %{name}-server = %{version}
Requires:       python3-dasbus
Requires:       python3-dbus-python
Requires:       python3-selinux >= 1.30.15
Requires:       selinux-policy
Requires:       xdg-utils

%description
SETroubleShoot GUI. Application that allows you to view setroubleshoot-server
messages. Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%package server
Summary:        SELinux troubleshoot server
Group:          Productivity/Security
Requires:       %{name}-plugins >= 3.3.10
Requires:       audit >= 1.2.6-3
Requires:       python3-audit
Requires:       python3-dasbus
Requires:       python3-dbus-python
Requires:       policycoreutils-python
Requires:       python3-gobject
Requires:       python3-selinux
Requires:       python3-rpm
Requires:       python3-setools
Requires:       python3-libxml2
Requires:       python3-systemd
# Requires: python-slip-dbus
Recommends:     logrotate

%description server
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%package doc
Summary:        Setroubleshoot documentation
Group:          Productivity/Security
Requires(pre):  %{name} = %{version}
BuildArch:      noarch

%description doc
Setroubleshoot documentation package

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE3} %{name}-server setroubleshoot.conf
%configure \
    --enable-seappletlegacy=no \
    --with-auditpluginsdir=/etc/audisp/plugins.d
    
%make_build pkgrundir=%{_rundir}/setroubleshoot pid_file=%{_rundir}/setroubleshootd.pid

%install
%make_install dbus_systemdir=%{_datadir}/dbus-1/system.d
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-server
%suse_update_desktop_file %{name}

# fix documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/doc/%{name}-%{version}/* %{buildroot}%{_docdir}/%{name}/
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
touch %{buildroot}%{_localstatedir}/lib/%{name}/audit_listener_database.xml
touch %{buildroot}%{_localstatedir}/lib/%{name}/email_alert_recipients
touch %{buildroot}%{_localstatedir}/lib/%{name}/setroubleshoot_database.xml


# create /run/setroubleshoot on boot
install -m644 -D %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{_buildroot}%{_rundir}/%{name}

mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/setroubleshoot.conf

%fdupes %{buildroot}
%find_lang %{name}

%pre server -f %{name}-server.pre

%post server
%tmpfiles_create %{_tmpfilesdir}/setroubleshoot.conf

%files
%{_datadir}/%{name}/gui
%{_sysconfdir}/xdg/autostart/*
%{_datadir}/icons/hicolor
%dir %attr(0755,root,root) %{python3_sitelib}/%{name}
%dir %{_datadir}/%{name}
%{python3_sitelib}/%{name}/browser.py
%{python3_sitelib}/%{name}/gui_utils.py
%{python3_sitelib}/%{name}/__pycache__/browser*.pyc
%{python3_sitelib}/%{name}/__pycache__/gui_utils*.pyc
%{_bindir}/seapplet

%files server -f %{name}.lang
%{_bindir}/sealert
%{_sbindir}/sedispatch
%{_sbindir}/setroubleshootd
%{_sysusersdir}/setroubleshoot.conf
%dir %attr(0755,root,root) %{_sysconfdir}/%{name}
%dir %attr(0755,root,root) %{python3_sitelib}/%{name}
%{_datadir}/dbus-1/services/sealert.service
%{_datadir}/applications/%{name}.desktop
%exclude %{python3_sitelib}/%{name}/__pycache__/browser*.pyc
%exclude %{python3_sitelib}/%{name}/__pycache__/gui_utils*.pyc
%{python3_sitelib}/%{name}/__pycache__/
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/Plugin.py
%{python3_sitelib}/%{name}/__init__.py
%{python3_sitelib}/%{name}/access_control.py
%{python3_sitelib}/%{name}/analyze.py
%{python3_sitelib}/%{name}/audit_data.py
%{python3_sitelib}/%{name}/avc_audit.py
%{python3_sitelib}/%{name}/config.py
%{python3_sitelib}/%{name}/email_alert.py
%{python3_sitelib}/%{name}/errcode.py
%{python3_sitelib}/%{name}/html_util.py
%{python3_sitelib}/%{name}/rpc.py
%{python3_sitelib}/%{name}/rpc_interfaces.py
%{python3_sitelib}/%{name}/server.py
%{python3_sitelib}/%{name}/serverconnection.py
%{python3_sitelib}/%{name}/signature.py
%{python3_sitelib}/%{name}/util.py
%{python3_sitelib}/%{name}/uuid.py
%{python3_sitelib}/%{name}/xml_serialize.py
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%ghost %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.fedoraproject.setroubleshootfixit.policy
%{_datadir}/dbus-1/system.d/org.fedoraproject.Setroubleshootd.conf
%{_datadir}/dbus-1/system.d/org.fedoraproject.SetroubleshootFixit.conf
%{_datadir}/dbus-1/system.d/org.fedoraproject.SetroubleshootPrivileged.conf
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootFixit.service
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootPrivileged.service
%dir %attr(0750,setroubleshoot,setroubleshoot) %{_localstatedir}/lib/%{name}
%ghost %attr(0600,setroubleshoot,setroubleshoot) %{_localstatedir}/lib/%{name}/audit_listener_database.xml
%ghost %attr(0644,setroubleshoot,setroubleshoot) %{_localstatedir}/lib/%{name}/email_alert_recipients
%ghost %attr(0644,setroubleshoot,setroubleshoot) %{_localstatedir}/lib/%{name}/setroubleshoot_database.xml
%ghost %attr(0711,setroubleshoot,setroubleshoot) %{_rundir}/%{name}
%ghost %dir %{_localstatedir}/log/%{name}
%{_mandir}/man8/se*.8%{?ext_man}
%{_mandir}/man1/se*.1%{?ext_man}
%{_tmpfilesdir}/setroubleshoot.conf
%dir %{_sysconfdir}/audisp
%dir %{_sysconfdir}/audisp/plugins.d
%config %{_sysconfdir}/audisp/plugins.d/sedispatch.conf
%{_datadir}/dbus-1/system-services/org.fedoraproject.Setroubleshootd.service
%{_datadir}/appdata/setroubleshoot.appdata.xml

%files doc
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/*

%changelog
