#
# spec file for package python-mailman
#
# Copyright (c) 2020 SUSE LLC
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-mailman%{psuffix}
Version:        3.3.1
Release:        0
Summary:        Mailman -- the GNU mailing list manager
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
#
Source30:       README.SUSE.md
#
Source100:      https://gitlab.com/mailman/mailman/-/raw/master/src/mailman/testing/ssl_test_cert.crt
Source101:      https://gitlab.com/mailman/mailman/-/raw/master/src/mailman/testing/ssl_test_key.key
# whitespace fix
Patch0:         python-mailman-test_interact_default_banner.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 1.2.3
Requires:       python-aiosmtpd >= 1.1
Requires:       python-alembic
Requires:       python-atpublic
Requires:       python-authheaders >= 0.9.2
Requires:       python-authres >= 1.0.1
Requires:       python-click >= 7.0
Requires:       python-dnspython >= 1.14.0
Requires:       python-falcon > 1.0.0
Requires:       python-flufl.bounce
Requires:       python-flufl.i18n >= 2.0
Requires:       python-flufl.lock >= 3.1
Requires:       python-gunicorn
Requires:       python-importlib_resources >= 1.1.0
Requires:       python-lazr.config
Requires:       python-passlib
Requires:       python-python-dateutil >= 2.0
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-zope.component
Requires:       python-zope.configuration
Requires:       python-zope.event
Requires:       python-zope.interface >= 5.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       mailman = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy >= 1.2.3}
BuildRequires:  %{python_module aiosmtpd >= 1.1}
BuildRequires:  %{python_module alembic}
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module authheaders >= 0.9.2}
BuildRequires:  %{python_module authres >= 1.0.1}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module dnspython >= 1.14.0}
BuildRequires:  %{python_module falcon > 1.0.0}
BuildRequires:  %{python_module flufl.bounce}
BuildRequires:  %{python_module flufl.i18n >= 2.0}
BuildRequires:  %{python_module flufl.lock >= 3.1}
BuildRequires:  %{python_module flufl.testing}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module importlib_resources >= 1.1.0}
BuildRequires:  %{python_module lazr.config}
BuildRequires:  %{python_module mailman >= %{version}}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.interface >= 5.0}
%endif
%python_subpackages

%description
Mailman -- the GNU mailing list manager

%prep
%setup -q -n mailman-%{version}
%patch0 -p1

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
%python_clone -a %{buildroot}%{_bindir}/master
%python_clone -a %{buildroot}%{_bindir}/mailman
%python_clone -a %{buildroot}%{_bindir}/runner
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -d -m 0755 \
            %{buildroot}%{_sysconfdir} \
            %{buildroot}%{_sysconfdir}/logrotate.d \
            %{buildroot}%{_sysconfdir}/%{mailman_name}.d \
            %{buildroot}%{_tmpfilesdir} \
            %{buildroot}%{_unitdir} \
            %{buildroot}%{mailman_homedir} \
            %{buildroot}%{mailman_homedir}/data \
            %{buildroot}%{mailman_rundir} \
            %{buildroot}%{mailman_lockdir} \
            %{buildroot}%{mailman_logdir} \
            %{buildroot}%{mailman_spooldir}

install -m 0640 %{SOURCE10} %{buildroot}%{_sysconfdir}/%{mailman_name}.cfg
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{mailman_name}.service
install -m 0644 %{SOURCE12} %{buildroot}%{_tmpfilesdir}/%{mailman_name}.conf
install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/logrotate.d/%{mailman_name}
sed -i 's,@LOGDIR@,%{mailman_logdir},g;s,@BINDIR@,%{_bindir},g' \
        %{buildroot}%{_sysconfdir}/logrotate.d/%{mailman_name}

install -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/%{mailman_name}-digests.service
install -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/%{mailman_name}-digests.timer
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
%pre
getent group %{mailman_group} >/dev/null || \
    %{_sbindir}/groupadd -r %{mailman_group}
getent passwd %{mailman_user} >/dev/null || \
    %{_sbindir}/useradd -r -g %{mailman_group} -s /sbin/nologin \
    -c "mailman daemon user" -d %{mailman_homedir} %{mailman_user}
%{_sbindir}/usermod -g %{mailman_group} %{mailman_user} >/dev/null
%service_add_pre %{mailman_name}.service

%post
%python_install_alternative master
%python_install_alternative mailman
%python_install_alternative runner
%tmpfiles_create %{_tmpfilesdir}/%{mailman_name}.conf
%service_add_post %{mailman_name}.service

%preun
%service_del_preun %{mailman_name}.service

%postun
%service_del_postun %{mailman_name}.service
%python_uninstall_alternative master
%python_uninstall_alternative mailman
%python_uninstall_alternative runner

%files %{python_files}
%doc README.rst README.SUSE.md
%license COPYING
%python_alternative %{_bindir}/runner
%python_alternative %{_bindir}/mailman
%python_alternative %{_bindir}/master
%{python_sitelib}/*

%{_unitdir}/%{mailman_name}.service
%{_unitdir}/%{mailman_name}-digests.service
%{_unitdir}/%{mailman_name}-digests.timer
%{_tmpfilesdir}/%{mailman_name}.conf

%config(noreplace) %attr(640,root,mailman) %{_sysconfdir}/mailman.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{mailman_name}

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
