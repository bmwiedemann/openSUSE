#
# spec file for package lynis
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2009-2013 Sascha Manns <saigkill@opensuse.org>
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define _includedir       %{_datadir}/lynis/include
%define _pluginsdir       %{_datadir}/lynis/plugins
%define _dbdir            %{_datadir}/lynis/db
Name:           lynis
Version:        3.0.1
Release:        0
Summary:        Security and System auditing tool
License:        GPL-3.0-only
Group:          System/Monitoring
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%{name}-%{version}.tar.gz
Source2:        tests_binary_rpath
Source3:        tests_file_permissionsDB
Source4:        tests_file_permissions_ww
Source5:        tests_network_allowed_ports
Source6:        tests_system_dbus
Source7:        tests_system_proc
Source8:        tests_tmp_symlinks
Source9:        tests_users_wo_password
Source10:       prepare_for_suse.sh
Source11:       dbus-whitelist.db.openSUSE_12.2_x86_64
Source12:       fileperms.db.openSUSE_12.2_x86_64
Source13:       https://downloads.cisofy.com/lynis/%{name}-%{version}.tar.gz.asc
Source14:       https://cisofy.com/files/cisofy-software.pub#/%{name}.keyring
Source15:       %{name}-rpmlintrc
# PATCH-OPENSUSE-FIX -- thomas@novell.com - modifying for openSUSE
Patch0:         %{name}_1.3.5_lynis.diff
# PATCH-OPENSUSE-FIX -- thomas@novell.com - modifying for openSUSE
Patch2:         %{name}_1.3.1_include_consts.diff
Patch5:         %{name}_1.3.6_include-osdetection.diff
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
Requires:       bash
Requires:       cron
Requires:       findutils
Requires:       logrotate
Requires:       netcfg
Requires:       wget
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
BuildArch:      noarch

%description
Lynis is a security and system auditing tool. It scans a system on the
most interesting parts useful for audits, like:
     - Security enhancements
     - Logging and auditing options
     - Banner identification
     - Software availability

%prep
%setup -q -n %{name}
%patch0
%patch2
%patch5

%build

%install

# Install Profile (default.prf)
install -d %{buildroot}%{_sysconfdir}/%{name}
install -m 644 default.prf %{buildroot}%{_sysconfdir}/%{name}/default.prf
# install binary
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install %{name} %{buildroot}%{_bindir}
install %{SOURCE10} %{buildroot}%{_datadir}/%{name}
# install man-page
install -d %{buildroot}%{_mandir}/man8
install -pm 644 %{name}.8 %{buildroot}%{_mandir}/man8
# install functions/includes
install -d %{buildroot}%{_includedir}
install include/* %{buildroot}%{_includedir}
install %{SOURCE2} %{buildroot}%{_includedir}
install %{SOURCE3} %{buildroot}%{_includedir}
install %{SOURCE4} %{buildroot}%{_includedir}
install %{SOURCE5} %{buildroot}%{_includedir}
install %{SOURCE6} %{buildroot}%{_includedir}
install %{SOURCE7} %{buildroot}%{_includedir}
install %{SOURCE8} %{buildroot}%{_includedir}
install %{SOURCE9} %{buildroot}%{_includedir}
# install plugins
install -d %{buildroot}%{_pluginsdir}
install -pm 644 plugins/* %{buildroot}%{_pluginsdir}
# install database files
install -d %{buildroot}%{_dbdir}
install -pm 644 db/*.db %{buildroot}%{_dbdir}
install -d %{buildroot}%{_dbdir}/languages
install -pm 644 db/languages/* %{buildroot}%{_dbdir}/languages
install -pm 644 %{SOURCE11} %{buildroot}%{_dbdir}/dbus-whitelist.db
install -pm 644 %{SOURCE12} %{buildroot}%{_dbdir}/fileperms.db
#rm %%{buildroot}%%{_dbdir}/fileperms.db
#ln -s $(basename %%{SOURCE11}) %%{_dbdir}/dbus-whitelist.db
#ln -s $(basename %%{SOURCE12}) %%{_dbdir}/fileperms.db

# pacify rpmlint
chmod +x %{buildroot}%{_pluginsdir}/custom_plugin.template

%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.prf
%{_dbdir}/*
%{_includedir}/*
%{_pluginsdir}/*
%dir %{_sysconfdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db
%dir %{_datadir}/%{name}/include
%attr(640,root,root) %{_datadir}/%{name}/include/*
%dir %{_datadir}/%{name}/plugins
%license LICENSE
%doc CHANGELOG.md CONTRIBUTORS.md FAQ README
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_datadir}/%{name}/prepare_for_suse.sh

%changelog
