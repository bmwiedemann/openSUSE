#
# spec file for package pagure
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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


# Prevent dep generators from trying to process static stuff and stall out
# We only need to read the python metadata anyway
%global __provides_exclude_from ^%{python3_sitelib}/pagure/.*$
%global __requires_exclude_from ^%{python3_sitelib}/pagure/.*$

Name:           pagure
Version:        5.14.1
Release:        0
Summary:        A git-centered forge
Group:          Development/Tools/Version Control
# Pagure itself is GPL-2.0-or-later; flask_fas_openid.py is LGPL-2.1-or-later
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://pagure.io/pagure
Source0:        https://pagure.io/pagure/archive/%{version}/%{name}-%{version}.tar.gz

# Vendor in the single file from python-fedora that's needed
# This way, we avoid having to pull in all of python-fedora
# This file is licensed LGPL-2.1-or-later, per https://github.com/fedora-infra/python-fedora/blob/develop/README.rst#license
Source1:        https://raw.githubusercontent.com/fedora-infra/python-fedora/4719f10b3af1cf068e969387eab7df7e935003cd/flask_fas_openid.py

# SUSE-specific README providing a quickstart guide
Source10:       pagure-README.SUSE

# Backports from upstream

# SUSE-specific fixes
## Change the defaults in the example config to match packaging
Patch1000:      pagure-5.0-default-example-cfg.patch
# PATCH-FIX-UPSTREAM 5486.patch https://pagure.io/pagure/pull-request/5486 dominik@wombacher.cc -- Use '==' instead of 'is' in template if condition because to work with older Jinja2 versions. Edge case, avoid 'KeyError' after pagure update if a cached session is used.
Patch1001:      5486.patch


BuildArch:      noarch


BuildRequires:  apache2
BuildRequires:  fdupes
BuildRequires:  nginx
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

BuildRequires:  python3-Flask
BuildRequires:  python3-Flask-WTF
BuildRequires:  python3-Markdown
BuildRequires:  python3-Pillow
BuildRequires:  python3-alembic
BuildRequires:  python3-arrow
BuildRequires:  python3-bcrypt
BuildRequires:  python3-binaryornot
BuildRequires:  python3-bleach
BuildRequires:  python3-blinker
BuildRequires:  python3-chardet
BuildRequires:  python3-cryptography
BuildRequires:  python3-docutils
BuildRequires:  python3-email_validator
BuildRequires:  python3-psutil
BuildRequires:  python3-pygit2 >= 0.26.0
#BuildRequires:      python3-fedora-flask
BuildRequires:  python3-python3-openid
BuildRequires:  python3-SQLAlchemy >= 0.8
BuildRequires:  python3-WTForms
BuildRequires:  python3-munch
BuildRequires:  python3-python-openid-cla
BuildRequires:  python3-python-openid-teams
BuildRequires:  python3-redis
BuildRequires:  python3-straight-plugin
BuildRequires:  python3-whitenoise

# We require OpenSSH 7.4+ for SHA256 support
Requires:       openssh >= 7.4

Requires:       python3-Flask
Requires:       python3-Flask-WTF
Requires:       python3-Markdown
Requires:       python3-Pillow
Requires:       python3-alembic
Requires:       python3-arrow
Requires:       python3-bcrypt
Requires:       python3-binaryornot
Requires:       python3-bleach
Requires:       python3-blinker
Requires:       python3-celery
Requires:       python3-chardet
Requires:       python3-cryptography
Requires:       python3-docutils
Requires:       python3-email_validator
Requires:       python3-psutil
Requires:       python3-pygit2 >= 0.26.0
#Requires:           python3-fedora-flask
Requires:       python3-python3-openid
Requires:       python3-SQLAlchemy > 0.8
Requires:       python3-WTForms
Requires:       python3-munch
Requires:       python3-python-openid-cla
Requires:       python3-python-openid-teams
Requires:       python3-redis
Requires:       python3-straight-plugin
Requires:       python3-whitenoise

# Required for celery
Requires:       python3-pytz

# Required for database setup/migrations
Requires:       python3-dbm
Requires:       python3-kitchen
Requires:       python3-requests

# We want to use cchardet whenever it's available
Recommends:     python3-cchardet

# If using PostgreSQL, the correct driver should be installed
Recommends:     (python3-psycopg2 if postgresql-server)

# If using MariaDB/MySQL, the correct driver should be installed
Recommends:     (python3-PyMySQL if mysql-server)

# If using Apache web server, the correct configuration should be installed
Recommends:     (%{name}-web-apache-httpd if apache2)

# If using Nginx web server, the correct configuration should be installed
Recommends:     (%{name}-web-nginx if nginx)

# The default theme is required
Requires:       %{name}-theme-default

%{?systemd_ordering}

# We use the git tools for some actions due to deficiencies in libgit2 and pygit2
Requires:       git-core

# No dependency of the app per se, but required to make it working.
OrderWithRequires:  gitolite >= 3.0
Requires(pre):  gitolite >= 3.0
Requires:       gitolite >= 3.0
Requires(post): user(wwwrun)

%description
Pagure is a git-centered forge based on pygit2.

Currently, Pagure offers a web-interface for git repositories, a ticket
system and possibilities to create new projects, fork existing ones and
create/merge pull-requests across or within projects.

For steps on how to set up the system after installing this package,
please read %{_docdir}/%{name}/README.SUSE.

%package            web-apache-httpd
Summary:        Apache HTTPD configuration for Pagure
Requires:       %{name} = %{version}-%{release}
Requires:       apache2-mod_wsgi-python3
# Apache config moved out to its own subpackage
Obsoletes:      %{name} < 5.10
Conflicts:      %{name} < 5.10

%description        web-apache-httpd
This package provides the configuration files for deploying
a Pagure server using the Apache HTTPD server.

%package            web-nginx
Summary:        Nginx configuration for Pagure
Requires:       %{name} = %{version}-%{release}
Requires:       nginx
Requires:       python3-gunicorn

%description        web-nginx
This package provides the configuration files for deploying
a Pagure server using the Nginx web server.

%package            theme-upstream
Summary:        Base theme for the Pagure web interface
Requires:       %{name} = %{version}-%{release}

%description        theme-upstream
This package provides the web interface assets for styling
a Pagure server with the base upstream look and feel.

%package            theme-pagureio
Summary:        Pagure web interface theme used on Pagure.io
Requires:       %{name} = %{version}-%{release}

%description        theme-pagureio
This package provides the web interface assets for styling
a Pagure server with the same look and feel as Pagure.io.

%package            theme-srcfpo
Summary:        Pagure web interface theme used on src.fedoraproject.org
Requires:       %{name} = %{version}-%{release}

%description        theme-srcfpo
This package provides the web interface assets for styling
a Pagure server with the same look and feel as src.fedoraproject.org.

%package            theme-chameleon
Summary:        Pagure web interface theme based on openSUSE's chameleon theme
Requires:       %{name} = %{version}-%{release}

%description        theme-chameleon
This package provides the web interface assets for styling
a Pagure server with the same look and feel as openSUSE Infrastructure.

%package            theme-default-upstream
Summary:        Configuration for pagure to default to the upstream web interface theme
Conflicts:      %{name}-theme-default
Provides:       %{name}-theme-default
Requires:       %{name}-theme-upstream = %{version}-%{release}

%description        theme-default-upstream
This package sets the default web interface assets used for
a Pagure server running as shipped by upstream.

%package            theme-default-openSUSE
Summary:        Configuration for pagure to default to the openSUSE web interface theme
Conflicts:      %{name}-theme-default
Provides:       %{name}-theme-default
Requires:       %{name}-theme-chameleon = %{version}-%{release}
Enhances:       (%{name} and branding-openSUSE)
Removepathpostfixes:.openSUSE

%description        theme-default-openSUSE
This package sets the default web interface assets used for
a Pagure server running on openSUSE.

%package            milters
Summary:        Milter to integrate pagure with emails
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pymilter
%{?systemd_requires}
# It would work with sendmail but we configure things (like the tempfile)
# to work with postfix
Requires:       postfix

%description        milters
Milters (Mail filters) allowing the integration of pagure and emails.
This is useful for example to allow commenting on a ticket by email.

%package            ev
Summary:        EventSource server for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
Requires:       python3-Trololio
%{?systemd_requires}

%description        ev
Pagure comes with an eventsource server allowing live update of the pages
supporting it. This package provides it.

%package            webhook
Summary:        Web-Hook server for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
%{?systemd_requires}

%description        webhook
Pagure comes with an webhook server allowing http callbacks for any action
done on a project. This package provides it.

%package            ci
Summary:        A CI service for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
Requires:       python3-python-jenkins
%{?systemd_requires}

%description        ci
Pagure comes with a continuous integration service, currently supporting
only jenkins but extendable to others.
With this service, your CI server will be able to report the results of the
build on the pull-requests opened to your project.

%package            logcom
Summary:        The logcom service for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
%{?systemd_requires}

%description        logcom
pagure-logcom contains the service that logs commits into the database so that
the activity calendar heatmap is filled.

%package            loadjson
Summary:        The loadjson service for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
%{?systemd_requires}

%description        loadjson
pagure-loadjson is the service allowing to update the database with the
information provided in the JSON blobs that are stored in the tickets (and
in the future pull-requests) git repo.

%package            mirror
Summary:        The mirroring service for pagure
BuildRequires:  systemd-rpm-macros
Requires:       %{name} = %{version}-%{release}
%{?systemd_requires}

%description        mirror
pagure-mirror is the service mirroring projects that asked for it outside
of this pagure instance.

%prep
%autosetup -p1

# Vendor in the file needed from python-fedora
install -pm 0644 %{SOURCE1} pagure/ui
sed -e "s/import flask_fas_openid/from pagure.ui import flask_fas_openid as flask_fas_openid/" -i pagure/ui/fas_login.py

# Install README.SUSE file
install -pm 0644 %{SOURCE10} README.SUSE

%build
%py3_build

%install
%py3_install

# Install apache configuration file
mkdir -p %{buildroot}/%{_sysconfdir}/apache2/vhosts.d
install -p -m 644 files/pagure-apache-httpd.conf %{buildroot}/%{_sysconfdir}/apache2/vhosts.d/pagure.conf

# Install nginx configuration file
mkdir -p %{buildroot}/%{_sysconfdir}/nginx/vhosts.d/
install -p -m 644 files/pagure-nginx.conf %{buildroot}/%{_sysconfdir}/nginx/vhosts.d/pagure.conf

# Install configuration file
mkdir -p %{buildroot}/%{_sysconfdir}/pagure
install -p -m 644 files/pagure.cfg.sample %{buildroot}/%{_sysconfdir}/pagure/pagure.cfg

# Install WSGI file
mkdir -p %{buildroot}/%{_datadir}/pagure
install -p -m 644 files/pagure.wsgi %{buildroot}/%{_datadir}/pagure/pagure.wsgi
install -p -m 644 files/doc_pagure.wsgi %{buildroot}/%{_datadir}/pagure/doc_pagure.wsgi

# Install the createdb script
install -p -m 644 createdb.py %{buildroot}/%{_datadir}/pagure/pagure_createdb.py

# Install the api_key_expire_mail.py script
install -p -m 644 files/api_key_expire_mail.py %{buildroot}/%{_datadir}/pagure/api_key_expire_mail.py

# Install the mirror_project_in.py script
install -p -m 644 files/mirror_project_in.py %{buildroot}/%{_datadir}/pagure/mirror_project_in.py

# Install the keyhelper and aclcheck scripts
mkdir -p %{buildroot}/%{_libexecdir}/pagure
install -p -m 755 files/aclchecker.py %{buildroot}/%{_libexecdir}/pagure/aclchecker.py
install -p -m 755 files/keyhelper.py %{buildroot}/%{_libexecdir}/pagure/keyhelper.py

# Install the alembic configuration file
install -p -m 644 files/alembic.ini %{buildroot}/%{_sysconfdir}/pagure/alembic.ini

# Install the alembic revisions
cp -r alembic %{buildroot}/%{_datadir}/pagure

# Install the systemd file for the web frontend
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 files/pagure_web.service \
    %{buildroot}/%{_unitdir}/pagure_web.service

# Install the systemd file for the docs web frontend
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 files/pagure_docs_web.service \
    %{buildroot}/%{_unitdir}/pagure_docs_web.service

# Install the systemd file for the worker
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 files/pagure_worker.service \
    %{buildroot}/%{_unitdir}/pagure_worker.service

# Install the systemd file for the authorized_keys worker
install -p -m 644 files/pagure_authorized_keys_worker.service \
    %{buildroot}/%{_unitdir}/pagure_authorized_keys_worker.service

# Install the systemd file for the gitolite worker
install -p -m 644 files/pagure_gitolite_worker.service \
    %{buildroot}/%{_unitdir}/pagure_gitolite_worker.service

# Install the systemd file for the web-hook
install -p -m 644 files/pagure_webhook.service \
    %{buildroot}/%{_unitdir}/pagure_webhook.service

# Install the systemd file for the ci service
install -p -m 644 files/pagure_ci.service \
    %{buildroot}/%{_unitdir}/pagure_ci.service

# Install the systemd file for the logcom service
install -p -m 644 files/pagure_logcom.service \
    %{buildroot}/%{_unitdir}/pagure_logcom.service

# Install the systemd file for the loadjson service
install -p -m 644 files/pagure_loadjson.service \
    %{buildroot}/%{_unitdir}/pagure_loadjson.service

# Install the systemd file for the mirror service
install -p -m 644 files/pagure_mirror.service \
    %{buildroot}/%{_unitdir}/pagure_mirror.service

# Install the systemd file for the script sending reminder about API key
# expiration
install -p -m 644 files/pagure_api_key_expire_mail.service \
    %{buildroot}/%{_unitdir}/pagure_api_key_expire_mail.service
install -p -m 644 files/pagure_api_key_expire_mail.timer \
    %{buildroot}/%{_unitdir}/pagure_api_key_expire_mail.timer

# Install the systemd file for the script updating mirrored project
install -p -m 644 files/pagure_mirror_project_in.service \
    %{buildroot}/%{_unitdir}/pagure_mirror_project_in.service
install -p -m 644 files/pagure_mirror_project_in.timer \
    %{buildroot}/%{_unitdir}/pagure_mirror_project_in.timer

# Install the milter files
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -p -m 0644 pagure-milters/milter_tempfile.conf \
    %{buildroot}/%{_tmpfilesdir}/%{name}-milter.conf
install -p -m 644 pagure-milters/pagure_milter.service \
    %{buildroot}/%{_unitdir}/pagure_milter.service
install -p -m 644 pagure-milters/comment_email_milter.py \
    %{buildroot}/%{_datadir}/pagure/comment_email_milter.py

# Install the eventsource
mkdir -p %{buildroot}/%{_libexecdir}/pagure-ev
install -p -m 755 pagure-ev/pagure_stream_server.py \
    %{buildroot}/%{_libexecdir}/pagure-ev/pagure_stream_server.py
install -p -m 644 pagure-ev/pagure_ev.service \
    %{buildroot}/%{_unitdir}/pagure_ev.service

# Switch all systemd units to use the correct libexecdir
sed -e "s|/usr/libexec|%{_libexecdir}|g" -i %{buildroot}/%{_unitdir}/*.service

# Change default_config.py to use the correct libexecdir
sed -e "s|/usr/libexec|%{_libexecdir}|g" -i %{buildroot}/%{python3_sitelib}/pagure/default_config.py

# Fix the shebang for various scripts
sed -e "s|#!/usr/bin/env python|#!%{__python3}|" -i \
    %{buildroot}/%{_libexecdir}/pagure-ev/*.py \
    %{buildroot}/%{_libexecdir}/pagure/*.py \
    %{buildroot}/%{_datadir}/pagure/*.py \
    %{buildroot}/%{python3_sitelib}/pagure/hooks/files/*.py \
    %{buildroot}/%{python3_sitelib}/pagure/hooks/files/hookrunner \
    %{buildroot}/%{python3_sitelib}/pagure/hooks/files/post-receive \
    %{buildroot}/%{python3_sitelib}/pagure/hooks/files/pre-receive \
    %{buildroot}/%{python3_sitelib}/pagure/hooks/files/repospannerhook

# Switch interpreter for systemd units to correct Python interpreter
sed -e "s|/usr/bin/python|%{__python3}|g" -i %{buildroot}/%{_unitdir}/*.service

# Make symlinks for default theme packages
mv %{buildroot}/%{python3_sitelib}/pagure/themes/default %{buildroot}/%{python3_sitelib}/pagure/themes/upstream
ln -sr %{buildroot}/%{python3_sitelib}/pagure/themes/upstream %{buildroot}/%{python3_sitelib}/pagure/themes/default
ln -sr %{buildroot}/%{python3_sitelib}/pagure/themes/chameleon %{buildroot}/%{python3_sitelib}/pagure/themes/default.openSUSE

# Run fdupes
%fdupes %{buildroot}/%{python3_sitelib}
%fdupes doc/_build/html

# Make log directory and files
mkdir -p %{buildroot}/%{_localstatedir}/log/pagure
logfiles="web docs_web"

for logfile in $logfiles; do
   touch %{buildroot}/%{_localstatedir}/log/pagure/access_${logfile}.log
   touch %{buildroot}/%{_localstatedir}/log/pagure/error_${logfile}.log
done

# Regenerate clobbered symlinks (Cf. https://pagure.io/pagure/issue/3782)
runnerhooks="post-receive pre-receive"

for runnerhook in $runnerhooks; do
   rm -rf %{buildroot}/%{python3_sitelib}/pagure/hooks/files/$runnerhook
   ln -sf hookrunner %{buildroot}/%{python3_sitelib}/pagure/hooks/files/$runnerhook
done

# Make the rcFOO symlinks for systemd services
mkdir -p %{buildroot}/%{_sbindir}
paguresvcs="api_key_expire_mail ci ev authorized_keys_worker gitolite_worker loadjson logcom milter mirror webhook worker mirror_project_in"
for paguresvc in $paguresvcs; do
   ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcpagure_$paguresvc
done

# Install the basic directory structure
mkdir -p %{buildroot}/srv/www/pagure-releases
mkdir -p %{buildroot}/srv/gitolite/pseudo
mkdir -p %{buildroot}/srv/gitolite/repositories/{,docs,forks,requests,tickets}
mkdir -p %{buildroot}/srv/gitolite/remotes
mkdir -p %{buildroot}/srv/gitolite/.gitolite/{conf,keydir,logs}
mkdir -p %{buildroot}/srv/gitolite/.ssh

# Add empty gitolite config file
touch %{buildroot}/srv/gitolite/.gitolite/conf/gitolite.conf

# Install gitolite rc file
install -p -m 644 files/gitolite3.rc %{buildroot}/srv/gitolite/.gitolite.rc

%pre
# Do nothing, but ensure dependency is evaluated...

%post
echo "Create wsgi rundir if it doesn't exist..."
mkdir -p /srv/www/run || :

echo "See %{_docdir}/%{name}/README.SUSE to continue"
%systemd_post pagure_worker.service
%systemd_post pagure_authorized_keys_worker.service
%systemd_post pagure_gitolite_worker.service
%systemd_post pagure_api_key_expire_mail.timer
%systemd_post pagure_mirror_project_in.timer

%post web-nginx
%systemd_post pagure_web.service
%systemd_post pagure_docs_web.service

%post milters
%tmpfiles_create %{_tmpfilesdir}/%{name}-milter.conf
%systemd_post pagure_milter.service

%post ev
%systemd_post pagure_ev.service

%post webhook
%systemd_post pagure_webhook.service

%post ci
%systemd_post pagure_ci.service

%post logcom
%systemd_post pagure_logcom.service

%post loadjson
%systemd_post pagure_loadjson.service

%post mirror
%systemd_post pagure_mirror.service

%preun
%systemd_preun pagure_worker.service
%systemd_preun pagure_authorized_keys_worker.service
%systemd_preun pagure_gitolite_worker.service
%systemd_preun pagure_api_key_expire_mail.timer
%systemd_preun pagure_mirror_project_in.timer

%preun web-nginx
%systemd_preun pagure_web.service
%systemd_preun pagure_docs_web.service

%preun milters
%systemd_preun pagure_milter.service

%preun ev
%systemd_preun pagure_ev.service

%preun webhook
%systemd_preun pagure_webhook.service

%preun ci
%systemd_preun pagure_ci.service

%preun logcom
%systemd_preun pagure_logcom.service

%preun loadjson
%systemd_preun pagure_loadjson.service

%preun mirror
%systemd_preun pagure_mirror.service

%postun
%systemd_postun_with_restart pagure_worker.service
%systemd_postun_with_restart pagure_authorized_keys_worker.service
%systemd_postun_with_restart pagure_gitolite_worker.service
%systemd_postun pagure_api_key_expire_mail.timer
%systemd_postun pagure_mirror_project_in.timer

%postun web-nginx
%systemd_postun_with_restart pagure_web.service
%systemd_postun_with_restart pagure_docs_web.service

%postun milters
%systemd_postun_with_restart pagure_milter.service

%postun ev
%systemd_postun_with_restart pagure_ev.service

%postun webhook
%systemd_postun_with_restart pagure_webhook.service

%postun ci
%systemd_postun_with_restart pagure_ci.service

%postun logcom
%systemd_postun_with_restart pagure_logcom.service

%postun loadjson
%systemd_postun_with_restart pagure_loadjson.service

%postun mirror
%systemd_postun_with_restart pagure_mirror.service

%files
%doc README.SUSE README.rst UPGRADING.rst files/gitolite3.rc files/pagure.cfg.sample
%license LICENSE
%config(noreplace) %{_sysconfdir}/pagure/pagure.cfg
%config(noreplace) %{_sysconfdir}/pagure/alembic.ini
%dir %{_sysconfdir}/pagure/
%dir %{_datadir}/pagure/
%{_datadir}/pagure/*.py*
%exclude %{_datadir}/pagure/comment_email_milter.py*
%{_datadir}/pagure/alembic/
%{_libexecdir}/pagure/
%{python3_sitelib}/pagure/
%exclude %{python3_sitelib}/pagure/themes/default
%exclude %{python3_sitelib}/pagure/themes/default.openSUSE
%exclude %{python3_sitelib}/pagure/themes/upstream
%exclude %{python3_sitelib}/pagure/themes/pagureio
%exclude %{python3_sitelib}/pagure/themes/srcfpo
%exclude %{python3_sitelib}/pagure/themes/chameleon
%{python3_sitelib}/pagure*.egg-info
%{_bindir}/pagure-admin
%{_unitdir}/pagure_worker.service
%{_unitdir}/pagure_authorized_keys_worker.service
%{_unitdir}/pagure_gitolite_worker.service
%{_unitdir}/pagure_api_key_expire_mail.service
%{_unitdir}/pagure_api_key_expire_mail.timer
%{_unitdir}/pagure_mirror_project_in.service
%{_unitdir}/pagure_mirror_project_in.timer
%{_sbindir}/rcpagure_api_key_expire_mail
%{_sbindir}/rcpagure_worker
%{_sbindir}/rcpagure_authorized_keys_worker
%{_sbindir}/rcpagure_gitolite_worker
%{_sbindir}/rcpagure_mirror_project_in
# Pagure data content
%attr(-,git,git) %dir /srv/gitolite/pseudo
%attr(-,git,git) %dir /srv/gitolite/remotes
%attr(-,git,git) %dir /srv/gitolite/repositories/{,docs,forks,requests,tickets}
%attr(-,git,git) %dir /srv/gitolite/.gitolite/{,conf,keydir,logs}
%attr(750,git,git) %dir /srv/gitolite/.ssh
%attr(-,git,git) %config(noreplace) /srv/gitolite/.gitolite/conf/gitolite.conf
%attr(-,git,git) %config(noreplace) /srv/gitolite/.gitolite.rc
%attr(-,git,git) %dir /srv/www/pagure-releases
%attr(-,git,git) %dir %{_localstatedir}/log/pagure

%files web-apache-httpd
%license LICENSE
%doc files/pagure-apache-httpd.conf
%config(noreplace) %{_sysconfdir}/apache2/vhosts.d/pagure.conf
%config(noreplace) %{_datadir}/pagure/*.wsgi

%files web-nginx
%license LICENSE
%doc files/pagure-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/vhosts.d/pagure.conf
%{_unitdir}/pagure_web.service
%{_unitdir}/pagure_docs_web.service
%ghost %{_localstatedir}/log/pagure/access_*.log
%ghost %{_localstatedir}/log/pagure/error_*.log

%files theme-upstream
%license LICENSE
%{python3_sitelib}/pagure/themes/upstream/

%files theme-pagureio
%license LICENSE
%{python3_sitelib}/pagure/themes/pagureio/

%files theme-srcfpo
%license LICENSE
%{python3_sitelib}/pagure/themes/srcfpo/

%files theme-chameleon
%license LICENSE
%{python3_sitelib}/pagure/themes/chameleon/

%files theme-default-upstream
%license LICENSE
%{python3_sitelib}/pagure/themes/default

%files theme-default-openSUSE
%license LICENSE
%{python3_sitelib}/pagure/themes/default.openSUSE

%files milters
%license LICENSE
%dir %{_datadir}/pagure/
%{_tmpfilesdir}/%{name}-milter.conf
%{_unitdir}/pagure_milter.service
%{_datadir}/pagure/comment_email_milter.py*
%{_sbindir}/rcpagure_milter

%files ev
%license LICENSE
%{_libexecdir}/pagure-ev/
%{_unitdir}/pagure_ev.service
%{_sbindir}/rcpagure_ev

%files webhook
%license LICENSE
%{_unitdir}/pagure_webhook.service
%{_sbindir}/rcpagure_webhook

%files ci
%license LICENSE
%{_unitdir}/pagure_ci.service
%{_sbindir}/rcpagure_ci

%files logcom
%license LICENSE
%{_unitdir}/pagure_logcom.service
%{_sbindir}/rcpagure_logcom

%files loadjson
%license LICENSE
%{_unitdir}/pagure_loadjson.service
%{_sbindir}/rcpagure_loadjson

%files mirror
%license LICENSE
%{_unitdir}/pagure_mirror.service
%{_sbindir}/rcpagure_mirror

%changelog
