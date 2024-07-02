#
# spec file for package python-HyperKitty
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


%bcond_without testsuite

# keep in sync with setup.py
%global django_min_version 3.2
%global django_max_version 4.3
%global django_mailman3_min_version 1.3.13
%global django_gravatar2_min_version 1.0.6
%global djangorestframework_min_version 3.0.0
%global robot_detection_min_version 0.3
%global pytz_min_version 2012
%global django_compressor_min_version 1.3
%global mailmanclient_min_version 3.3.3
# original this was >= 2.0.0, < 3.0 but overwritten by mistune3.patch
%global mistune_min_version 3.0
%global python_dateutil_min_version  2.0
%global networkx_min_version 2.0
%global django_haystack_min_version 2.8.0
%global django_extensions_min_version 1.3.7
%global flufl_lock_min_version 4.0
%global django_q_min_version 1.0.0

%global webapps_dir /srv/www/webapps

%global hyperkitty_pkgname   HyperKitty
%global lowname              hyperkitty

%global hyperkitty_basedir   %{webapps_dir}/mailman/hyperkitty
%global hyperkitty_localedir %{hyperkitty_basedir}/locale
%global hyperkitty_staticdir %{hyperkitty_basedir}/static

%global hyperkitty_etcdir    %{_sysconfdir}/hyperkitty
%global hyperkitty_libdir    %{_localstatedir}/lib/hyperkitty
%global hyperkitty_logdir    %{_localstatedir}/log/hyperkitty
%global hyperkitty_datadir   %{hyperkitty_libdir}/data

%global hyperkitty_services hyperkitty-qcluster.service hyperkitty-runjob-daily.service hyperkitty-runjob-daily.timer hyperkitty-runjob-hourly.service hyperkitty-runjob-hourly.timer hyperkitty-runjob-minutely.service hyperkitty-runjob-minutely.timer hyperkitty-runjob-monthly.service hyperkitty-runjob-monthly.timer hyperkitty-runjob-quarter-hourly.service hyperkitty-runjob-quarter-hourly.timer hyperkitty-runjob-weekly.service hyperkitty-runjob-weekly.timer hyperkitty-runjob-yearly.service hyperkitty-runjob-yearly.timer

# keep in sync with python-postorius/python-mailman-web
# Always only build one flavor: primary python for TW, python311 from the SLE15 python module for 15.x
%if 0%{?suse_version} >= 1550
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif
%global mypython %pythons
%global mypython_sitelib %{expand:%%{%{mypython}_sitelib}}
%global __mypython %{expand:%%{__%{mypython}}}
%define plainpython python

Name:           python-HyperKitty
Version:        1.3.10
Release:        0
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/hyperkitty
#
Source0:        https://gitlab.com/mailman/hyperkitty/-/releases/%{version}/downloads/hyperkitty-%{version}.tar.gz
Source1:        https://gitlab.com/mailman/hyperkitty/-/releases/%{version}/downloads/hyperkitty-%{version}.tar.gz.asc
Source2:        python-HyperKitty.keyring
Source3:        python-HyperKitty-rpmlintrc
#
Source10:       hyperkitty-manage.sh
Source12:       hyperkitty.uwsgi
#
Source20:       hyperkitty-qcluster.service
Source21:       hyperkitty-runjob.service
Source22:       hyperkitty-runjob.timer
#
Source30:       README.SUSE.md
#
# PATCH-FIX-OPENSUSE hyperkitty-settings.patch mcepl@suse.com
# hard-code locations of configuration files
Patch0:         hyperkitty-settings.patch
#
# PATCH-FIX-UPSTREAM gl-mr300-add-opengraph-metadata.patch gl#mailman/hyperkitty#300
Patch98:        gl-mr300-add-opengraph-metadata.patch
# PATCH-FIX-UPSTREAM gl-mr470-introduce-feed-filtering.patch gl#mailman/hyperkitty#470
Patch99:        gl-mr470-introduce-feed-filtering.patch
#
BuildRequires:  %{python_module Django >= %{django_min_version} with %python-Django < %{django_max_version}}
BuildRequires:  %{python_module Whoosh}
BuildRequires:  %{python_module django-compressor >= %{django_compressor_min_version}}
BuildRequires:  %{python_module django-debug-toolbar >= 2.2}
BuildRequires:  %{python_module django-extensions >= %{django_extensions_min_version}}
BuildRequires:  %{python_module django-gravatar2 >= %{django_gravatar2_min_version}}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module mailmanclient >= %{mailmanclient_min_version}}
BuildRequires:  %{python_module mistune >= %{mistune_min_version}}
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xapian-haystack >= 2.1.0}
BuildRequires:  acl
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildRequires:  rsync
BuildRequires:  sassc
BuildRequires:  sudo
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
# use the real python3 primary for rpm pythondistdeps.py
BuildRequires:  python3-packaging
%endif
# SECTION test requirements
BuildRequires:  %{python_module Whoosh >= 2.5.7}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3.2}
BuildRequires:  %{python_module django-haystack >= %{django_haystack_min_version}}
BuildRequires:  %{python_module django-mailman3 >= %{django_mailman3_min_version}}
BuildRequires:  %{python_module django-q >= %{django_q_min_version}}
BuildRequires:  %{python_module djangorestframework >= %{djangorestframework_min_version}}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module flufl.lock >= %{flufl_lock_min_version}}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mistune >= %{mistune_min_version}}
BuildRequires:  %{python_module networkx >= %{networkx_min_version}}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= %{python_dateutil_min_version}}
BuildRequires:  %{python_module pytz >= %{pytz_min_version}}
BuildRequires:  %{python_module robot-detection >= %{robot_detection_min_version}}
# /SECTION

%description
A web interface to access GNU Mailman v3 archives.

%package -n %{hyperkitty_pkgname}
Summary:        A web interface to access GNU Mailman v3 archives
# important sync with
Requires:       (%{mypython}-Django >= %{django_min_version} with %{mypython}-Django < %{django_max_version})
Requires:       %{mypython}-django-compressor >= %{django_compressor_min_version}
Requires:       %{mypython}-django-debug-toolbar >= 2.2
Requires:       %{mypython}-django-extensions >= %{django_extensions_min_version}
Requires:       %{mypython}-django-gravatar2 >= %{django_gravatar2_min_version}
Requires:       %{mypython}-django-haystack >= 2.8.0
Requires:       %{mypython}-django-mailman3 >= %{django_mailman3_min_version}
Requires:       %{mypython}-django-q >= %{django_q_min_version}
Requires:       %{mypython}-djangorestframework >= %{djangorestframework_min_version}
Requires:       %{mypython}-flufl.lock >= %{flufl_lock_min_version}
Requires:       %{mypython}-mailmanclient >= %{mailmanclient_min_version}
Requires:       %{mypython}-mistune >= %{mistune_min_version}
Requires:       %{mypython}-networkx >= %{networkx_min_version}
Requires:       %{mypython}-python-dateutil >= %{python_dateutil_min_version}
Requires:       %{mypython}-pytz >= %{pytz_min_version}
Requires:       %{mypython}-robot-detection >= %{robot_detection_min_version}
Requires:       %{mypython}-xapian-haystack >= %{django_haystack_min_version}
# help in replacing any previously installed flavor package back to the unprefixed package
%if 0%{?suse_version} < 1550
Obsoletes:      python3-%{hyperkitty_pkgname} < %{version}-%{release}
%endif
Provides:       %{mypython}-%{hyperkitty_pkgname} = %{version}-%{release}
Obsoletes:      %{mypython}-%{hyperkitty_pkgname} < %{version}-%{release}
%if 0%{?suse_version} >= 1550
Requires:       sassc
%endif

%description -n %{hyperkitty_pkgname}
A web interface to access GNU Mailman v3 archives.

%package -n %{hyperkitty_pkgname}-web
Summary:        The webroot for GNU Mailman
Requires:       %{hyperkitty_pkgname}
Requires:       acl
Requires:       openssl
Requires:       sudo
Requires:       system-user-%{lowname}

%description -n %{hyperkitty_pkgname}-web
A web user interface for GNU Mailman.

This package holds the web interface.

%package -n %{hyperkitty_pkgname}-web-uwsgi
Summary:        HyperKitty - uwsgi configuration
Requires:       %{hyperkitty_pkgname}-web
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150500
Requires:       %{mypython}-uwsgi-python3
%else
Requires:       uwsgi-python3
%endif

%description -n %{hyperkitty_pkgname}-web-uwsgi
A web user interface for GNU Mailman.

This package holds the uwsgi configuration.

%package -n system-user-%{lowname}
Summary:        System user for HyperKitty
BuildArch:      noarch
BuildRequires:  sysuser-tools
%sysusers_requires

%description -n system-user-%{lowname}
System user for HyperKitty.

%prep
%setup -n hyperkitty-%{version}
cp %{SOURCE30} .
touch settings_local.py

# Copy example_project to just build the static files
rsync -a example_project/* build_static_files

%autopatch -p1

tee > %{lowname}.sysuser <<EOF
u %{lowname} - "HyperKitty" %{hyperkitty_basedir} -
EOF

%build
sed -i 's|^#!/usr/bin/env.*|#!%{__mypython}|' \
    example_project/manage.py
sed -i 's|/usr/bin/python3|%{__mypython}|' %{SOURCE10} %{SOURCE20} %{SOURCE21}
sed -i 's|python3|%{mypython}|' %{SOURCE12}

%pyproject_wheel

# Build static files
export PYTHONPATH=$(pwd)
%python_exec build_static_files/manage.py collectstatic --clear --noinput
%python_exec build_static_files/manage.py compress --force

%sysusers_generate_pre %{lowname}.sysuser %{lowname}

%install
install -d -m 0750 \
    %{buildroot}%{hyperkitty_etcdir} \
    %{buildroot}%{hyperkitty_libdir} \
    %{buildroot}%{hyperkitty_datadir} \
    %{buildroot}%{hyperkitty_datadir}/attachments \
    %{buildroot}%{hyperkitty_logdir}

install -d -m 0755 \
    %{buildroot}%{hyperkitty_basedir} \
    %{buildroot}%{hyperkitty_localedir} \
    %{buildroot}%{hyperkitty_staticdir} \
    %{buildroot}%{hyperkitty_staticdir}/CACHE \
    %{buildroot}%{_unitdir}

%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Copy static files
rsync -a build_static_files/static %{buildroot}%{hyperkitty_basedir}
# Remove the directory
%python_expand rm -rf %{buildroot}%{$python_sitelib}/build_static_files

rsync -a example_project/* %{buildroot}%{hyperkitty_basedir}
chmod -x %{buildroot}%{hyperkitty_basedir}/wsgi.py

for f in \
         README.rst \
         apache.conf \
         crontab \
         qcluster.service \
    ; do
    rm -f %{buildroot}%{hyperkitty_basedir}/$f
done
rm -f %{buildroot}%{hyperkitty_localedir}/.keep
rm -f %{buildroot}%{hyperkitty_basedir}/logs/.keep

%python_expand rm -rf %{buildroot}%{$python_sitelib}/example_project

# Create an empty settings_local.py. This will be filled with a SECRET_KEY in post
install -m 0644 settings_local.py %{buildroot}%{hyperkitty_etcdir}/settings_local.py

ln -svf %{hyperkitty_etcdir}/settings_local.py \
    %{buildroot}/%{hyperkitty_basedir}/settings_local.py

%fdupes %{buildroot}%{hyperkitty_basedir}

# Manage script
install -d -m 0755 %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE10} %{buildroot}%{_sbindir}/hyperkitty-manage

install -d -m 0755 %{buildroot}%{_sysconfdir}/uwsgi/vassals
install -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/uwsgi/vassals/hyperkitty.ini

install -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/hyperkitty-qcluster.service
ln -s /sbin/service %{buildroot}%{_sbindir}/rchyperkitty-qcluster

for job in \
           minutely \
           quarter-hourly \
           hourly \
           daily \
           weekly \
           monthly \
           yearly \
           ; do
    install -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.service
    sed -i "s/@HYPERKITTY_RUNJOB@/${job}/g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.service
    ln -s /sbin/service %{buildroot}%{_sbindir}/rchyperkitty-runjob-${job}

    install -m 0644 %{SOURCE22} %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer

    hyperkitty_runjob_calendar="OnCalendar=${job}"
    hyperkitty_runjob_delay="RandomizedDelaySec=15m"
    hyperkitty_runjob_name="${job}"

    if [ "${job}" = "minutely" ]; then
        hyperkitty_runjob_delay="RandomizedDelaySec=15s"
    elif [ "${job}" = "quarter-hourly" ]; then
        hyperkitty_runjob_calendar="OnCalendar=*:0/15"
        hyperkitty_runjob_delay="RandomizedDelaySec=2m"
        # The real jobname is with an underscore
        hyperkitty_runjob_name="quarter_hourly"
    fi
    sed -i "s#@HYPERKITTY_RUNJOB_CALENDAR@#${hyperkitty_runjob_calendar}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
    sed -i "s#@HYPERKITTY_RUNJOB_DELAY@#${hyperkitty_runjob_delay}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
    sed -i "s#@HYPERKITTY_RUNJOB@#${hyperkitty_runjob_name}#g" %{buildroot}%{_unitdir}/hyperkitty-runjob-${job}.timer
done

install -Dm644 %{lowname}.sysuser %{buildroot}%{_sysusersdir}/%{lowname}.conf

%if %{with testuite}
%check
export PYTHONPATH="$(pwd)"
export LANG=C.UTF-8
%pytest
%endif

%pre -n %{hyperkitty_pkgname}-web
%service_add_pre %{hyperkitty_services}

%pre -n system-user-%{lowname} -f %{lowname}.pre

%post -n %{hyperkitty_pkgname}-web
# We need a SECRET_KEY for manage to work
if ! grep -q "^SECRET_KEY.*" %{hyperkitty_etcdir}/settings_local.py; then
    echo "SECRET_KEY='$(openssl rand -base64 48)'" >> %{hyperkitty_etcdir}/settings_local.py
fi
%{_sbindir}/hyperkitty-manage makemigrations --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings
%{_sbindir}/hyperkitty-manage migrate --pythonpath /srv/www/webapps/mailman/hyperkitty/ --settings settings

%service_add_post %{hyperkitty_services}

%preun -n %{hyperkitty_pkgname}-web
%service_del_preun %{hyperkitty_services}

%postun -n %{hyperkitty_pkgname}-web
%service_del_postun %{hyperkitty_services}

%files -n %{hyperkitty_pkgname}
%doc AUTHORS.txt README.rst example_project
%license COPYING.txt
%{mypython_sitelib}/hyperkitty
%{mypython_sitelib}/hyperkitty-%{version}*-info

%files -n %{hyperkitty_pkgname}-web
%doc README.SUSE.md
%{_sbindir}/hyperkitty-manage
%{_sbindir}/rchyperkitty-qcluster
%{_sbindir}/rchyperkitty-runjob-*
%dir %{webapps_dir}
%dir %{webapps_dir}/mailman
%{_unitdir}/hyperkitty-qcluster.service
%{_unitdir}/hyperkitty-runjob-*.service
%{_unitdir}/hyperkitty-runjob-*.timer

%defattr(-,root,hyperkitty)
%dir %{hyperkitty_basedir}
%{hyperkitty_basedir}/__init__.py
%{hyperkitty_basedir}/manage.py
%{hyperkitty_basedir}/settings.py
%{hyperkitty_basedir}/settings_local.py
%{hyperkitty_basedir}/urls.py
%{hyperkitty_basedir}/wsgi.py

%dir %{hyperkitty_basedir}/static
%{hyperkitty_basedir}/static/admin
%{hyperkitty_basedir}/static/debug_toolbar
%{hyperkitty_basedir}/static/django-mailman3
%{hyperkitty_basedir}/static/django_extensions
%{hyperkitty_basedir}/static/hyperkitty
%{hyperkitty_basedir}/static/rest_framework

# The wsgi needs to write to static/CACHE
%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/manifest.json

%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE/css
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/css/output.*.css

%attr(755,hyperkitty,hyperkitty) %dir %{hyperkitty_basedir}/static/CACHE/js
%attr(644,hyperkitty,hyperkitty) %{hyperkitty_basedir}/static/CACHE/js/output.*.js

%dir %{hyperkitty_localedir}

%attr(750,root,hyperkitty) %dir %{hyperkitty_etcdir}
%attr(640,root,hyperkitty) %config(noreplace) %{hyperkitty_etcdir}/settings_local.py
%attr(750,root,hyperkitty) %dir %{hyperkitty_libdir}
%attr(750,hyperkitty,hyperkitty) %dir %{hyperkitty_datadir}
%attr(770,hyperkitty,hyperkitty) %dir %{hyperkitty_logdir}

%files -n %{hyperkitty_pkgname}-web-uwsgi
%dir %{_sysconfdir}/uwsgi
%dir %{_sysconfdir}/uwsgi/vassals
%config (noreplace) %{_sysconfdir}/uwsgi/vassals/hyperkitty.ini

%files -n system-user-%{lowname}
%{_sysusersdir}/%{lowname}.conf

%changelog
