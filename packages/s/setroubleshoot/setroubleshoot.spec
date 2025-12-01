#
# spec file for package setroubleshoot
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2006-2024 Red Hat, Inc.
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
Group:          Productivity/Security
Name:           setroubleshoot
Version:        3.3.35
Release:        0
URL:            https://gitlab.com/setroubleshoot/setroubleshoot
Source0:        https://gitlab.com/setroubleshoot/setroubleshoot/-/archive/%{version}/setroubleshoot-%{version}.tar.bz2
Source1:        %{name}.tmpfiles
Source2:        %{name}.sysusers
Source3:        %{name}.logrotate
Patch0:         setroubleshoot-desktop.patch
Patch1:         remove-pip-from-makefile.patch
Patch2:         disable-send-bug-report-button.patch
# git format-patch -N 3.3.30
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcap-ng-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  polkit-devel
BuildRequires:  python3-dasbus
BuildRequires:  pkgconfig(audit) >= 3.0.1
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(python3)
#BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-pip
BuildRequires:  python3-selinux
BuildRequires:  python3-setuptools
# for the _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros
# for the sysusers
BuildRequires:  sysuser-tools
Requires:       %{name}-server = %{version}-%{release}
Requires:       gtk3
Requires:       libnotify
Requires:       python3-dasbus
Requires:       python3-gobject
# libreport is available only in factory for now
# setroubleshoot version 3.35-4 added remove submit bug button from browser
# when libreport is not available. For TW we keep the button there just
# remove actual send button so people can copypaste bug report
%if 0%{?suse_version} >= 1600 && 0%{sles_version}
Requires:       libreport-gtk_1 >= 2.2.1-2
Requires:       python3-libreport
%endif
Requires(post): desktop-file-utils
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
%{_datadir}/metainfo/org.fedoraproject.setroubleshoot.appdata.xml
%else
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/dbus-1/services/org.fedoraproject.sealert.service
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
%python3_fix_shebang
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}/%{_datadir}/%{name}/*
%endif

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
Group:          Productivity/Security

Requires:       %{name}-plugins >= 3.3.10
Requires:       audit >= 3.0.1
Requires:       audit-libs-python3
Requires:       policycoreutils-python-utils
Requires:       python3-dbus-python
Requires:       python3-gobject >= 3.11
Requires:       python3-libxml2
Requires:       python3-rpm
Requires:       python3-selinux  >= 2.1.5-1
Requires:       python3-six
Requires:       python3-systemd >= 206-1
BuildRequires:  gettext
BuildRequires:  intltool
#BuildRequires:  python3
BuildRequires:  pkgconfig(python3)
Requires:       dbus-1
Requires:       polkit
Requires:       python3-dasbus
Recommends:     logrotate

%description server
Provides tools to help diagnose SELinux problems. When AVC messages
are generated an alert can be generated that will give information
about the problem and help track its resolution. Alerts can be configured
to user preference. The same tools can be run on existing log files.

%pre server -f %{name}-server.pre
%service_add_pre setroubleshootd.service

%post server
%if 0%{?suse_version}
%tmpfiles_create %{_tmpfilesdir}/setroubleshoot.conf
/usr/bin/systemctl try-reload-or-restart auditd.service >/dev/null 2>&1 || : #bsc1237388
%else
/sbin/service auditd reload >/dev/null 2>&1 || :
%endif
%service_add_post setroubleshootd.service

%postun server
%if 0%{?suse_version}
/usr/bin/systemctl try-reload-or-restart auditd.service >/dev/null 2>&1 || : #bsc1237388
%else
/sbin/service auditd reload >/dev/null 2>&1 || :
%endif
%service_del_postun setroubleshootd.service

%preun server
%service_del_preun setroubleshootd.service

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
%{_unitdir}/setroubleshootd.service
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
