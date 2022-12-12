#
# spec file for package setroubleshoot
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


# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

Summary:        Helps troubleshoot SELinux problems
License:        GPL-2.0-or-later
Name:           setroubleshoot
Version:        3.3.30
Release:        2%{?dist}
URL:            https://gitlab.com/setroubleshoot/setroubleshoot
Source0:        https://gitlab.com/setroubleshoot/setroubleshoot/-/archive/%{version}/setroubleshoot-%{version}.tar.gz
Source1:        %{name}.tmpfiles
Source2:        %{name}.sysusers
Source3:	%{name}.logrotate
Patch0:		setroubleshoot-desktop.patch
# git format-patch -N 3.3.30
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcap-ng-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  audit-devel >= 3.0.1
BuildRequires:  dbus-1-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  polkit-devel
BuildRequires:  python3-dasbus
BuildRequires:  python3-gobject
BuildRequires:  python3-selinux
# for the _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros
# for the sysusers
BuildRequires:  sysuser-tools
Requires:       %{name}-server = %{version}-%{release}
Requires:       gtk3
Requires:       libnotify
Requires:       python3-dasbus
Requires:       python3-gobject
# Redhat library for reporting bugs - do we have SUSE alternative?
#Requires:       libreport-gtk >= 2.2.1-2
#Requires:       python3-libreport
Requires(post): desktop-file-utils
Requires(post): dbus-1
Requires(postun): dbus-1
Requires(postun): desktop-file-utils

BuildRequires:  xdg-utils
Requires:       xdg-utils

%global pkgpythondir  %{python3_sitelib}/%{name}
%global pkgguidir     %{_datadir}/%{name}/gui
%global pkgdatadir    %{_datadir}/%{name}
%global pkglibexecdir %{_prefix}/libexec/%{name}
%global pkgvardatadir %{_localstatedir}/lib/%{name}
%global pkgconfigdir  %{_sysconfdir}/%{name}
%global pkgdatabase   %{pkgvardatadir}/setroubleshoot_database.xml

%description
setroubleshoot GUI. Application that allows you to view setroubleshoot-server
messages.
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%files
%{pkgguidir}
%config(noreplace) %{_sysconfdir}/xdg/autostart/*
%{_datadir}/applications/*.desktop
%if 0%{?suse_version}
%{_datadir}/metainfo/setroubleshoot.appdata.xml
%else
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/dbus-1/services/sealert.service
%{_datadir}/icons/hicolor/*/*/*
%dir %attr(0755,root,root) %{pkgpythondir}
%{pkgpythondir}/browser.py
%{pkgpythondir}/__pycache__/browser.cpython*
%{pkgpythondir}/gui_utils.py
%{pkgpythondir}/__pycache__/gui_utils.cpython*
%{_bindir}/seapplet

%prep
%autosetup -p 1

%build
./autogen.sh
%if 0%{?suse_version}
%configure PYTHON=%{__python3} --enable-seappletlegacy=no --with-auditpluginsdir=/etc/audit/plugins.d
%sysusers_generate_pre %{SOURCE2} %{name}-server setroubleshoot.conf
%make_build pkgrundir=%{_rundir}/setroubleshoot pid_file=%{_rundir}/setroubleshootd.pid
%else
%configure PYTHON=%{__python3} --enable-seappletlegacy=no --with-auditpluginsdir=/etc/audit/plugins.d
make
%endif

%install
%make_install dbus_systemdir=%{_datadir}/dbus-1/system.d PREFIX=/usr
desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{pkgvardatadir}
mkdir -p %{buildroot}%{_rundir}/setroubleshoot
touch %{buildroot}%{pkgdatabase}
touch %{buildroot}%{pkgvardatadir}/email_alert_recipients

# fix documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/
ls %{buildroot}%{_datadir}/doc/
mv %{buildroot}%{_datadir}/doc/%{name}/* %{buildroot}%{_docdir}/%{name}/
ls %{buildroot}/%{_datadir}/doc/
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

# create /run/setroubleshoot on boot
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -p -m644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

# install logrotate file
install -D -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-server

%find_lang %{name}


%package doc
Summary:        Setroubleshoot documentation
Group:          Productivity/Security
Requires(pre):  %{name} = %{version}
BuildArch:      noarch

%description doc
Setroubleshoot documentation package

%files doc
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/*

%package server
Summary:        SELinux troubleshoot server

Requires:       %{name}-plugins >= 3.3.10
Requires:       audit >= 3.0.1
Requires:       audit-libs-python3
Requires:       python3-selinux  >= 2.1.5-1
Requires:       python3-libxml2
Requires:       python3-dbus-python
Requires:       python3-rpm
Requires:       python3-systemd >= 206-1
Requires:       python3-gobject >= 3.11
Requires:       policycoreutils-python-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-devel
Requires:       dbus-1
Requires:       polkit
Requires:       python3-dasbus
Recommends:	logrotate

%description server
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.


%pre server -f %{name}-server.pre

%post server
%if 0%{?suse_version}
%tmpfiles_create %{_tmpfilesdir}/setroubleshoot.conf
%else
/sbin/service auditd reload >/dev/null 2>&1 || :
%endif

%postun server
/sbin/service auditd reload >/dev/null 2>&1 || :

%files server -f %{name}.lang
%{_bindir}/sealert
%{_sbindir}/sedispatch
%{_sbindir}/setroubleshootd
%{python3_sitelib}/setroubleshoot*.egg-info
%dir %attr(0755,root,root) %{pkgconfigdir}
%dir %{pkgpythondir}
%dir %{pkgpythondir}/__pycache__
%{pkgpythondir}/Plugin.py
%{pkgpythondir}/__init__.py
%{pkgpythondir}/access_control.py
%{pkgpythondir}/analyze.py
%{pkgpythondir}/audit_data.py
%{pkgpythondir}/avc_audit.py
%{pkgpythondir}/config.py
%{pkgpythondir}/email_alert.py
%{pkgpythondir}/errcode.py
%{pkgpythondir}/html_util.py
%{pkgpythondir}/rpc.py
%{pkgpythondir}/serverconnection.py
%{pkgpythondir}/rpc_interfaces.py
%{pkgpythondir}/server.py
%{pkgpythondir}/signature.py
%{pkgpythondir}/util.py
%{pkgpythondir}/uuid.py
%{pkgpythondir}/xml_serialize.py
%{pkgpythondir}/__pycache__/Plugin.cpython*
%{pkgpythondir}/__pycache__/__init__.cpython*
%{pkgpythondir}/__pycache__/access_control.cpython*
%{pkgpythondir}/__pycache__/analyze.cpython*
%{pkgpythondir}/__pycache__/audit_data.cpython*
%{pkgpythondir}/__pycache__/avc_audit.cpython*
%{pkgpythondir}/__pycache__/config.cpython*
%{pkgpythondir}/__pycache__/email_alert.cpython*
%{pkgpythondir}/__pycache__/errcode.cpython*
%{pkgpythondir}/__pycache__/html_util.cpython*
%{pkgpythondir}/__pycache__/rpc.cpython*
%{pkgpythondir}/__pycache__/rpc_interfaces.cpython*
%{pkgpythondir}/__pycache__/server.cpython*
%{pkgpythondir}/__pycache__/serverconnection.cpython*
%{pkgpythondir}/__pycache__/signature.cpython*
%{pkgpythondir}/__pycache__/util.cpython*
%{pkgpythondir}/__pycache__/uuid.cpython*
%{pkgpythondir}/__pycache__/xml_serialize.cpython*
%dir %{pkgdatadir}
%{pkgdatadir}/SetroubleshootFixit.py
%{pkgdatadir}/SetroubleshootPrivileged.py
%config(noreplace) %{pkgconfigdir}/%{name}.conf
%attr(0700,setroubleshoot,setroubleshoot) %dir %{pkgvardatadir}
%ghost %attr(0600,setroubleshoot,setroubleshoot) %{pkgdatabase}
%ghost %attr(0600,setroubleshoot,setroubleshoot) %{pkgvardatadir}/email_alert_recipients
%{_mandir}/man1/seapplet.1.gz
%{_mandir}/man8/sealert.8.gz
%{_mandir}/man8/sedispatch.8.gz
%{_mandir}/man8/setroubleshootd.8.gz
%attr(750,root,root) %dir %{_sysconfdir}/audit
%attr(750,root,root) %dir %{_sysconfdir}/audit/plugins.d
%attr(640,root,root)%config %{_sysconfdir}/audit/plugins.d/sedispatch.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%{_datadir}/dbus-1/system-services/org.fedoraproject.Setroubleshootd.service
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootPrivileged.service
%{_datadir}/polkit-1/actions/org.fedoraproject.setroubleshootfixit.policy
%{_datadir}/dbus-1/system-services/org.fedoraproject.SetroubleshootFixit.service
%{_datadir}/dbus-1/system.d/org.fedoraproject.Setroubleshootd.conf
%{_datadir}/dbus-1/system.d/org.fedoraproject.SetroubleshootPrivileged.conf
%{_datadir}/dbus-1/system.d/org.fedoraproject.SetroubleshootFixit.conf
%attr(0644,root,root) %{_tmpfilesdir}/%{name}.conf
%attr(0644,root,root) %{_sysusersdir}/%{name}.conf
%if 0%{?suse_version} 
%ghost %attr(0711,setroubleshoot,setroubleshoot) %dir %{_rundir}/setroubleshoot
%else
%attr(0711,setroubleshoot,setroubleshoot) %dir %{_rundir}/setroubleshoot
%endif 
%doc AUTHORS COPYING ChangeLog DBUS.md NEWS README TODO

%changelog
