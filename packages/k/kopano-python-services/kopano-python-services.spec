#
# spec file for package kopano-python-services
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Kopano B.V.
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


# Kopano OBS: And if you add new %%package(s), update core:*:dist too
%define version_unconverted 10.0.5

Name:           kopano-python-services
Version:        10.0.5
Release:        0
Summary:        Python services for Kopano Groupware Core
License:        AGPL-3.0-only
Group:          Productivity/Networking/Email/Servers
URL:            https://kopano.io/
Source:         kopanocore-%version.tar.xz
Source3:        %name-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-setuptools >= 3.6
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?fedora_version} || 0%{?centos_version}
BuildRequires:  xapian-core-libs
%else
BuildRequires:  python3-xapian
%endif
%if 0%{?suse_version}
BuildRequires:  python-xml
%else
BuildRequires:  libxml2-python
%endif

%description
Kopano provides email storage on the server side and brings its own
Ajax-based mail client called WebAccess. Kopano is designed to
integrate with Kopano WebApp, Push clients and other mail services as an
alternative to Microsoft Exchange and other comparable mail servers.
Personal address book, calendar, notes and tasks, "Public Folders" and shared
calendar functionalities (inviting internal and external users,
resource management) can be handled by the software as well.

%package -n kopano-backup
Summary:        Utility to back up and restore Kopano stores
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common
Requires:       python3-bsddb3
Requires:       python3-kopano = %version

%description -n kopano-backup
kopano-backup is a MAPI-level backup/restore tool. It can sync
complete users/stores to disk using ICS to incrementally sync the
respective MAPI items, and can process stores in parallel.

%package -n kopano-dagent-pytils
Summary:        Additional message handlers for kopano-dagent
Group:          Productivity/Networking/Email/Servers

%description -n kopano-dagent-pytils
DAgent can execute external scripts for certain message types.
Included here is a handler that will process meeting request and
response messages and edit the participants' calendars accordingly.

%package -n kopano-migration-pst
Summary:        Utility to import PST files
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common
Requires:       python3-kopano = %version

%description -n kopano-migration-pst
kopano-migration-pst is a utility to import PST files into Kopano. As PST
files are basically MAPI dumps, and Kopano also uses MAPI internally, there
should be practically no data loss, even including calendar data.

%package -n kopano-python-utils
Summary:        Additional Python-based command-line utils for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires:       python3-bsddb3
Requires:       python3-kopano = %version

%description -n kopano-python-utils
Command-line clients to manipulate mailboxes (stores) in various ways.

%package -n kopano-search
Summary:        Indexed search engine for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common
Requires:       python3-bsddb3
Requires:       python3-kopano = %version
Requires:       python3-magic
Requires:       python3-xapian
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version}
Requires:       elinks
Requires:       poppler-utils
%else
Requires:       poppler-tools
Requires:       w3m
%endif

%description -n kopano-search
kopano-search creates indexes for messages and attachments per user.
When this service is running, search queries on the server will use
this index to quickly find messages and contents of attached
documents, enhancing the search performance of kopano-server.

%package -n kopano-spamd
Summary:        ICS-driven spam learning daemon for Kopano/SpamAssassin
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common
Requires:       python3-bsddb3
Requires:       python3-kopano = %version

%description -n kopano-spamd
A program which can teach SpamAssassin about spam based upon
the mails a user has moved to his Kopano junk folder.

%package -n python3-kopano
Summary:        High-level Python bindings for Kopano
Group:          Development/Languages/Python
%if 0%{?suse_version}
Requires:       python3-python-daemon
%endif
%if 0%{?centos_version} || 0%{?fedora_version}
Requires:       python3-daemon
%endif
Requires:       python3-dateutil
Requires:       python3-mapi
Requires:       python3-pytz
%if 0%{?suse_version}
Recommends:     python3-Pillow
%endif
%if 0%{?fedora_version}
Recommends:     python3-pillow
%endif

%description -n python3-kopano
Object-Oriented Python bindings for Kopano. Uses python-mapi to do
the low level work. Can be used for many common system administration
tasks.

%prep
%setup -qn kopanocore-%version

%build
autoreconf -fi
PYTHON_CFLAGS=$(pkg-config python3 --cflags)
PYTHON_LIBS=$(pkg-config python3 --libs)

%define _configure ./configure

%configure \
    --docdir="%_docdir/kopano" --disable-base \
    PYTHON="$(which python3)"
echo "%version" >version
make V=1 %{?_smp_mflags}

%install
b="%buildroot"
%make_install

%if 0%{?fdupes:1}
    %fdupes %buildroot/%_prefix
%endif

# use sh version
rm -f "$b/%_sbindir/kopano-autorespond"
# some default dirs
mkdir -p "$b/var/lib/kopano/autorespond" "$b/var/lib/kopano/spamd/spam"
mkdir -p "$b/%_localstatedir/log/kopano"
chmod 750 "$b/%_localstatedir/log/kopano"

%triggerpostun -n kopano-backup -- kopano-backup
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/backup.cfg" -a \
     -e "%_sysconfdir/kopano/backup.cfg.rpmsave" ]; then
    mv -v "%_sysconfdir/kopano/backup.cfg.rpmsave" \
        "%_sysconfdir/kopano/backup.cfg"
fi

%triggerpostun -n kopano-migration-pst -- kopano-migration-pst
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/migration-pst.cfg" -a \
     -e "%_sysconfdir/kopano/migration-pst.cfg.rpmsave" ]; then
    mv -v "%_sysconfdir/kopano/migration-pst.cfg.rpmsave" \
        "%_sysconfdir/kopano/migration-pst.cfg"
fi

%pre -n kopano-search
%{?_unitdir:%{?suse_version:%service_add_pre kopano-search.service}}

%post -n kopano-search
%{?_unitdir:%{?suse_version:%service_add_post kopano-search.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-search.service}}

%preun -n kopano-search
%{?_unitdir:%{?suse_version:%service_del_preun kopano-search.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-search.service}}
%{!?_unitdir:%stop_on_removal kopano-search}

%postun -n kopano-search
%{?_unitdir:%{?suse_version:%service_del_postun kopano-search.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-search.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-search}

%triggerpostun -n kopano-search -- kopano-search
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/search.cfg" -a \
    -e "%_sysconfdir/kopano/search.cfg.rpmsave" ]; then
        mv -v "%_sysconfdir/kopano/search.cfg.rpmsave" \
        "%_sysconfdir/kopano/search.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-search.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-search.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-search}

%pre -n kopano-spamd
%{?_unitdir:%{?suse_version:%service_add_pre kopano-spamd.service}}

%post -n kopano-spamd
%{?_unitdir:%{?suse_version:%service_add_post kopano-spamd.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-spamd.service}}

%preun -n kopano-spamd
%{?_unitdir:%{?suse_version:%service_del_preun kopano-spamd.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-spamd.service}}
%{!?_unitdir:%stop_on_removal kopano-spamd}

%postun -n kopano-spamd
%{?_unitdir:%{?suse_version:%service_del_postun kopano-spamd.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-spamd.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-spamd}

%files -n kopano-backup
%defattr(-,root,root)
%_sbindir/kopano-backup
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/backup.cfg
%_mandir/man*/kopano-backup.*
%python3_sitelib/kopano_backup/
%python3_sitelib/kopano_backup-*.egg-info

%files -n kopano-dagent-pytils
%defattr(-,root,root)
%_sbindir/kopano-mr-accept
%_sbindir/kopano-mr-process
%_mandir/man*/kopano-autorespond.*
%_mandir/man*/kopano-mr-accept.*
%_mandir/man*/kopano-mr-process.*
%_datadir/kopano-dagent/
%_datadir/kopano-spooler/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/dagent/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/spooler/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/autorespond.cfg
%python3_sitelib/kopano_utils/
%python3_sitelib/kopano_utils-*.egg-info

%files -n kopano-migration-pst
%defattr(-,root,root)
%_sbindir/kopano-migration-pst
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/migration-pst.cfg
%_mandir/man*/kopano-migration-pst.*
%python3_sitelib/kopano_migration_pst/
%python3_sitelib/kopano_migration_pst-*.egg-info

%files -n kopano-python-utils
%defattr(-,root,root)
%_sbindir/kopano-archiver-*
%_sbindir/kopano-cachestat
%_sbindir/kopano-cli
%_sbindir/kopano-fix-ipm-subtree
%_sbindir/kopano-mailbox-permissions
%_sbindir/kopano-recreate-systemfolders
%_sbindir/kopano-search-upgrade-findroots.py
%_mandir/man*/kopano-archiver-*.8*
%_mandir/man*/kopano-cachestat.*
%_mandir/man*/kopano-cli.*
%_mandir/man*/kopano-mailbox-permissions.*
%_docdir/kopano-gateway/
%dir %_docdir/kopano/
%_docdir/kopano/update-resource-recipients
%python3_sitelib/kopano_cli/
%python3_sitelib/kopano_cli*.egg-info

%files -n kopano-search
%defattr(-,root,root)
%dir %_sysconfdir/kopano/
%dir %_sysconfdir/kopano/searchscripts/
%config(noreplace) %attr(0640,root,kopano) %_sysconfdir/kopano/searchscripts/*.db
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/*.xslt
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/attachments_parser
%config(noreplace) %attr(-,root,kopano) %_sysconfdir/kopano/searchscripts/zmktemp
%_sbindir/kopano-search
%_sbindir/kopano-search-xapian-compact.py
%_prefix/lib/systemd/system/kopano-search.service
%_mandir/man*/kopano-search.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/search/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/search.cfg
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-search
%python3_sitelib/kopano_search/
%python3_sitelib/kopano_search-*.egg-info

%files -n kopano-spamd
%defattr(-,root,root)
%_sbindir/kopano-spamd
%_prefix/lib/systemd/system/kopano-spamd.service
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/spamd/
%_mandir/man*/kopano-spamd.*
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/spamd.cfg
%python3_sitelib/kopano_spamd/
%python3_sitelib/kopano_spamd*.egg-info

%files -n python3-kopano
%defattr(-,root,root)
%python3_sitelib/kopano/
%python3_sitelib/kopano-*.egg-info

%changelog
