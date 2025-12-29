#
# spec file for package python-mailman
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global aiosmtpd_min_version 1.4.3
# normally it would be 1.6.2,!=1.7.0 but to avoid super comlex constructs in the spec file ... lets go with the version that we have in TW
%global alembic_min_version 1.12
%global authheaders_min_version 0.16
%global authres_min_version 1.0.1
%global click_min_version 8.0.0
%global dnspython_min_version 1.14.0
%global falcon_min_version 3.1.3
%global flufl_bounce_min_version 4.0
%global flufl_i18n_min_version 3.2
%global flufl_lock_min_version 5.1
%global python_dateutil_min_version 2.0
%global sqlalchemy_min_version 1.4.0
%global zope_interface_min_version 5.0

%define mailman_name     mailman
%define mailman_homedir  %{_localstatedir}/lib/%{mailman_name}
%define mailman_logdir   %{_localstatedir}/log/%{mailman_name}
%define mailman_spooldir %{_localstatedir}/spool/%{mailman_name}
%define mailman_rundir   %{_rundir}/%{mailman_name}
%define mailman_lockdir  %{_rundir}/lock/%{mailman_name}
%global mailman_services %{mailman_name}.service %{mailman_name}-digests.service %{mailman_name}-digests.timer %{mailman_name}-notify.service %{mailman_name}-notify.timer

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# Keep this in sync with HyperKitty und Postorius
# Always only build one flavor
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%{?sle15_python_module_pythons}
%elif %{defined primary_python}
%define pythons %{primary_python}
%else
%define pythons python3
%endif
%global mypython %pythons
%global mypython_sitelib %{expand:%%{%{mypython}_sitelib}}
%define plainpython python

Name:           python-mailman%{psuffix}
Version:        3.3.10
Release:        0
Summary:        A Mailing List Manager
Group:          Productivity/Networking/Email/Mailinglists
License:        GPL-3.0-only
URL:            https://www.list.org
Source0:        https://gitlab.com/mailman/mailman/-/releases/v%{version}/downloads/mailman-%{version}.tar.gz
Source1:        https://gitlab.com/mailman/mailman/-/releases/v%{version}/downloads/mailman-%{version}.tar.gz.asc
Source2:        python-mailman.keyring
#
Source10:       mailman.cfg
Source11:       mailman.service
Source12:       mailman-tmpfiles.conf
Source13:       mailman.logrotate
Source14:       mailman-user.conf
#
Source20:       mailman-digests.service
Source21:       mailman-digests.timer
Source22:       mailman-notify.service
Source23:       mailman-notify.timer
#
Source30:       README.SUSE.md
Source31:       python-mailman.rpmlintrc
#
# PATCH-FIX-UPSTREAM mailman-fix-python-313-posixpath.patch https://gitlab.com/mailman/mailman/-/commit/685d9a7bdbd382d9e8d4a2da74bd973e93356e05.patch
Patch0:         mailman-fix-python-313-posixpath.patch
#
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sysuser-tools
%if 0%{?suse_version} >= 1550
# use the real python3 primary for rpm pythondistdeps.py
BuildRequires:  python3-packaging
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flufl.testing}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module pytest}
BuildRequires:  (mailman3 = %{version} with %mypython-mailman3)
%endif

%description
Mailman is a mailing list manager from the GNU project.

%package -n mailman3
Summary:        A mailing list manager
Requires:       %{mypython}-SQLAlchemy >= %{sqlalchemy_min_version}
Requires:       %{mypython}-aiosmtpd >= %{aiosmtpd_min_version}
Requires:       %{mypython}-alembic >= %{alembic_min_version}
Requires:       %{mypython}-atpublic
Requires:       %{mypython}-authheaders >= %{authheaders_min_version}
Requires:       %{mypython}-authres >= %{authres_min_version}
Requires:       %{mypython}-click >= %{click_min_version}
Requires:       %{mypython}-dnspython >= %{dnspython_min_version}
Requires:       %{mypython}-falcon >= %{falcon_min_version}
Requires:       %{mypython}-flufl.bounce >= %{flufl_bounce_min_version}
Requires:       %{mypython}-flufl.i18n >= %{flufl_i18n_min_version}
Requires:       %{mypython}-flufl.lock >= %{flufl_lock_min_version}
Requires:       %{mypython}-gunicorn
Requires:       %{mypython}-lazr.config
Requires:       %{mypython}-passlib
Requires:       %{mypython}-psycopg2
Requires:       %{mypython}-python-dateutil >= %{python_dateutil_min_version}
Requires:       %{mypython}-requests
Requires:       %{mypython}-zope.component
Requires:       %{mypython}-zope.configuration
Requires:       %{mypython}-zope.event
Requires:       %{mypython}-zope.interface >= %{zope_interface_min_version}
%if %{python_version_nodots} >= 313
Requires:       %{mypython}-standard-nntplib
%endif
Requires:       logrotate
Requires(pre):  /usr/sbin/groupadd
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       mailman = %{version}
# help in replacing any previously installed flavor package back to the unprefixed package
%if 0%{?suse_version} < 1550
Requires:       %{mypython}-importlib-resources >= 1.1.0
Obsoletes:      python3-mailman < %{version}-%{release}
Obsoletes:      python3-mailman3 < %{version}-%{release}
%endif
Provides:       %{mypython}-mailman = %{version}-%{release}
Obsoletes:      %{mypython}-mailman < %{version}-%{release}
Provides:       %{mypython}-mailman3 = %{version}-%{release}
Obsoletes:      %{mypython}-mailman3 < %{version}-%{release}

%description -n mailman3
Mailman is a mailing list manager from the GNU project.

%package -n system-user-%{mailman_name}
Summary:        System user and group mailman
Requires(pre):  group(lock)
Requires(pre):  group(mail)
%sysusers_requires

%description -n system-user-%{mailman_name}
System user for use by the mailman client.

%prep
%autosetup -p1 -n mailman-%{version}

# README.SUSE.md
cp %{SOURCE30} .

%build
sed -i 's:/sbin:%{_prefix}/bin:' src/mailman/config/mailman.cfg

%pyproject_wheel
./generate_mo.sh

%sysusers_generate_pre %{SOURCE14} mailman system-user-%{mailman_name}.conf

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -d -m 0755 \
            %{buildroot}%{_sysconfdir} \
            %{buildroot}%{_sysconfdir}/%{mailman_name}.d \
            %{buildroot}%{_tmpfilesdir} \
            %{buildroot}%{_sbindir} \
            %{buildroot}%{_unitdir} \
            %{buildroot}%{mailman_homedir} \
            %{buildroot}%{mailman_homedir}/data \
            %{buildroot}%{mailman_rundir} \
            %{buildroot}%{mailman_lockdir} \
            %{buildroot}%{mailman_logdir} \
            %{buildroot}%{mailman_spooldir}

%if 0%{?suse_version} > 1500
install -d -m 0755  %{buildroot}%{_distconfdir}/logrotate.d
install -m 0644 %{SOURCE13} %{buildroot}%{_distconfdir}/logrotate.d/%{mailman_name}
sed -i 's,@LOGDIR@,%{mailman_logdir},g;s,@BINDIR@,%{_bindir},g' \
        %{buildroot}%{_distconfdir}/logrotate.d/%{mailman_name}
%else
install -d -m 0755  %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/logrotate.d/%{mailman_name}
sed -i 's,@LOGDIR@,%{mailman_logdir},g;s,@BINDIR@,%{_bindir},g' \
        %{buildroot}%{_sysconfdir}/logrotate.d/%{mailman_name}
%endif

install -m 0640 %{SOURCE10} %{buildroot}%{_sysconfdir}/%{mailman_name}.cfg
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{mailman_name}.service
install -m 0644 %{SOURCE12} %{buildroot}%{_tmpfilesdir}/%{mailman_name}.conf

install -D -m 0644 %{SOURCE14} %{buildroot}%{_sysusersdir}/system-user-%{mailman_name}.conf

install -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/%{mailman_name}-digests.service
install -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/%{mailman_name}-digests.timer
install -m 0644 %{SOURCE22} %{buildroot}%{_unitdir}/%{mailman_name}-notify.service
install -m 0644 %{SOURCE23} %{buildroot}%{_unitdir}/%{mailman_name}-notify.timer

ln -s /sbin/service %{buildroot}%{_sbindir}/rc%{mailman_name}
ln -s /sbin/service %{buildroot}%{_sbindir}/rc%{mailman_name}-digests
ln -s /sbin/service %{buildroot}%{_sbindir}/rc%{mailman_name}-notify

%endif

%check
%if %{with test}
export LANG=C.UTF-8
%if 0%{?suse_version} <= 1500
# mailman.rest.tests.test_wsgiapp.TestSupportedContentType
# AssertionError: 'application/json; charset=UTF-8' != 'application/json'
rm src/mailman/rest/tests/test_wsgiapp.py
%endif
# doctest fails miserably
find -name '*.rst' -exec rm {} \;
# used to have ports 902{4,5}
rm src/mailman/mta/tests/test_aliases.py
# PermissionError: [Errno 13] Permission denied: '/usr/bin/master'
rm src/mailman/core/tests/test_logging.py
# PermissionError: [Errno 13] Permission denied: '/usr/bin/master'
rm src/mailman/commands/tests/test_cli_control.py
# do not use well known ports 9024 and 9025
sed -i "s:\(902\):4\1:" src/mailman/testing/testing.cfg
# https://gitlab.com/mailman/mailman/-/issues/1125
rm src/mailman/handlers/tests/test_avoid_duplicates.py
# Looks like this is racy, https://gitlab.com/mailman/mailman/-/issues/1236
rm src/mailman/commands/tests/test_cli_syncmembers.py
#
%python_exec -m nose2 -v
%endif

%if !%{with test}
%pre -n system-user-%{mailman_name} -f mailman.pre

%pre -n mailman3
%service_add_pre %{mailman_services}
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/%{mailman_name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans  -n mailman3
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/%{mailman_name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post -n mailman3
%tmpfiles_create %{_tmpfilesdir}/%{mailman_name}.conf
%service_add_post %{mailman_services}

%preun -n mailman3
%service_del_preun %{mailman_services}

%postun -n mailman3
%service_del_postun %{mailman_services}

%files -n mailman3
%doc README.md README.SUSE.md src/mailman/docs/NEWS.rst
%license COPYING
%{_sbindir}/rc%{mailman_name}*
%{_bindir}/runner
%{_bindir}/mailman
%{_bindir}/master
%{mypython_sitelib}/mailman
%{mypython_sitelib}/mailman-%{version}*-info
%{_unitdir}/%{mailman_name}.service
%{_unitdir}/%{mailman_name}-digests.service
%{_unitdir}/%{mailman_name}-digests.timer
%{_unitdir}/%{mailman_name}-notify.service
%{_unitdir}/%{mailman_name}-notify.timer
%{_tmpfilesdir}/%{mailman_name}.conf
%config(noreplace) %attr(640,root,mailman) %{_sysconfdir}/mailman.cfg
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/%{mailman_name}
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/%{mailman_name}
%endif
%dir %attr(750,root,mailman) %{_sysconfdir}/%{mailman_name}.d
%dir %attr(750,mailman,mailman) %{mailman_homedir}
%dir %attr(770,mailman,mail) %{mailman_homedir}/data
%dir %attr(750,mailman,mailman) %{mailman_spooldir}
%dir %attr(750,mailman,mailman) %{mailman_logdir}
%ghost %dir %{mailman_rundir}
%ghost %dir %{_rundir}/lock
%ghost %dir %{mailman_lockdir}

%files -n system-user-%{mailman_name}
%{_sysusersdir}/system-user-%{mailman_name}.conf
%endif

%changelog
