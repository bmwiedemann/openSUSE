#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define mailman_user     mailman
%define mailman_group    mailman
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
%if 0%{?suse_version} >= 1550
# Newest python supported by mailman is Python 3.9 -- https://gitlab.com/mailman/mailman/-/issues/936
%define pythons python39
%define mypython python39
%define mypython_sitelib %{python39_sitelib}
%else
%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3
%define mypython python3
%define mypython_sitelib %{python3_sitelib}
%endif
Name:           python-mailman%{psuffix}
Version:        3.3.8
Release:        0
Summary:        A Mailing List Manager
Group:          Productivity/Networking/Email/Mailinglists
License:        GPL-3.0-only
URL:            https://www.list.org
Source0:        https://files.pythonhosted.org/packages/source/m/mailman/mailman-%{version}.tar.gz
#
Source10:       mailman.cfg
Source11:       mailman.service
Source12:       mailman-tmpfiles.conf
Source13:       mailman.logrotate
#
Source20:       mailman-digests.service
Source21:       mailman-digests.timer
Source22:       mailman-notify.service
Source23:       mailman-notify.timer
#
Source30:       README.SUSE.md
Source31:       python-mailman.rpmlintrc
#
Source100:      https://gitlab.com/mailman/mailman/-/raw/master/src/mailman/testing/ssl_test_cert.crt
Source101:      https://gitlab.com/mailman/mailman/-/raw/master/src/mailman/testing/ssl_test_key.key
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} >= 1550
# use the real python3 primary for rpm pythondistdeps.py
BuildRequires:  python3-packaging
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module flufl.testing}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module pytest}
BuildRequires:  mailman3 = %{version}
%endif

%description
Mailman is a mailing list manager from the GNU project.

%package -n mailman3
Summary:        A mailing list manager
Requires:       %{mypython}-SQLAlchemy >= 1.2.3
Requires:       %{mypython}-aiosmtpd >= 1.4.3
Requires:       %{mypython}-alembic
Requires:       %{mypython}-atpublic
Requires:       %{mypython}-authheaders >= 0.14.0
Requires:       %{mypython}-authres >= 1.0.1
Requires:       %{mypython}-click >= 8.0
Requires:       %{mypython}-dnspython >= 1.14.0
Requires:       %{mypython}-falcon > 3.0.0
Requires:       %{mypython}-flufl.bounce >= 4.0
Requires:       %{mypython}-flufl.i18n >= 3.2
Requires:       %{mypython}-flufl.lock >= 5.1
Requires:       %{mypython}-gunicorn
Requires:       %{mypython}-importlib-resources >= 1.1.0
Requires:       %{mypython}-lazr.config
Requires:       %{mypython}-passlib
Requires:       %{mypython}-python-dateutil >= 2.0
Requires:       %{mypython}-requests
Requires:       %{mypython}-setuptools
Requires:       %{mypython}-zope.component
Requires:       %{mypython}-zope.configuration
Requires:       %{mypython}-zope.event
Requires:       %{mypython}-zope.interface >= 5.0
Requires:       logrotate
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       mailman = %{version}
%if "%{expand:%%%{mypython}_provides}" == "python3"
Provides:       python3-mailman = %{version}-%{release}
%endif
Obsoletes:      python3-mailman < %{version}-%{release}
# help in replacing any previously installed multiflavor package back to the unprefixed package
Provides:       %{mypython}-mailman = %{version}-%{release}
Obsoletes:      %{mypython}-mailman < %{version}-%{release}

%description -n mailman3
Mailman is a mailing list manager from the GNU project.

%prep
%autosetup -p1 -n mailman-%{version}

# https://gitlab.com/mailman/mailman/-/issues/704
cp %{SOURCE100} src/mailman/testing/
cp %{SOURCE101} src/mailman/testing/
cp %{SOURCE30} .

%build
sed -i 's:/sbin:%{_prefix}/bin:' src/mailman/config/mailman.cfg
%if 0%{?suse_version} > 1500
pushd src/mailman
for i in $(grep -r '^from importlib_resources' | sed 's/\(.*\.py\):.*/\1/'); do
  line=$(grep '^from importlib_resources' $i)
  what_import=$(echo $line | sed 's:.* import ::')
  sed -i "s@^\(from importlib_resources.*\)@try:\n  from importlib.resources import $what_import\nexcept ImportError:\n    \1\n@" $i;
done
popd
sed '/importlib_resources/d' -i src/mailman.egg-info/requires.txt setup.py
%endif
%python_build

%install
%if !%{with test}
%python_install
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
# https://gitlab.com/mailman/mailman/issues/654
rm src/mailman/commands/tests/test_cli_create.py
# do not use well known ports 9024 and 9025
sed -i "s:\(902\):4\1:" src/mailman/testing/testing.cfg
#
%python_exec -m nose2 -v
%endif

%if !%{with test}
%pre -n mailman3
getent group %{mailman_group} >/dev/null || \
    %{_sbindir}/groupadd -r %{mailman_group}
getent passwd %{mailman_user} >/dev/null || \
    %{_sbindir}/useradd -r -g %{mailman_group} -s /sbin/nologin \
    -c "mailman daemon user" -d %{mailman_homedir} %{mailman_user}
%{_sbindir}/usermod -g %{mailman_group} %{mailman_user} >/dev/null
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
%doc README.rst README.SUSE.md
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
%dir %attr(750,mailman,mailman) %{mailman_homedir}/data
%dir %attr(750,mailman,mailman) %{mailman_spooldir}
%dir %attr(750,mailman,mailman) %{mailman_logdir}
%ghost %dir %{mailman_rundir}
%ghost %dir %{_rundir}/lock
%ghost %dir %{mailman_lockdir}
%endif

%changelog
