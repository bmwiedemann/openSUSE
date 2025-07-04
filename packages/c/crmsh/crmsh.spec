#
# spec file for package crmsh
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


%bcond_with regression_tests

%global gname haclient
%global uname hacluster
%global crmsh_docdir %{_defaultdocdir}/%{name}

%global upstream_version tip
%global upstream_prefix crmsh
%global crmsh_release 1

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?rhel} || 0%{?fedora}
%define pkg_group System Environment/Daemons
%else
%define pkg_group Productivity/Clustering/HA
%endif

%define use_firewalld 1
%if %{use_firewalld}
%define _fwdefdir %{_prefix}/lib/firewalld/services
%endif

Name:           crmsh
Summary:        High Availability cluster command-line interface
License:        GPL-2.0-or-later
Group:          %{pkg_group}
Version:        5.0.0+20250630.23be67df
Release:        0
URL:            http://crmsh.github.io
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.tmpfiles.d.conf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
# Requiring pacemaker makes crmsh harder to build on other distributions,
# and is mostly a convenience feature. So only do it for SUSE.
Requires(pre):  pacemaker
%endif
Requires:       %{name}-scripts >= %{version}-%{release}
Requires:       /usr/bin/which
Requires:       python3 >= 3.10
Requires:       python3-PyYAML
Requires:       python3-lxml
Requires:       python3-packaging
Recommends:     bash-completion
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%if 0%{?suse_version}
# only require csync2 on SUSE since bootstrap
# only works for SUSE at the moment anyway
Requires:       csync2
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
%endif

%if 0%{?suse_version}
# Suse splits this off into a separate package
Requires:       python3-curses
Requires:       python3-python-dateutil
BuildRequires:  fdupes
BuildRequires:  python3-curses
%else
Requires:       python3-dateutil
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

# Required for core functionality
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  python3

%if 0%{?suse_version}
# xsltproc is necessary for manpage generation; this is split out into
# libxslt-tools as of openSUSE 12.2.  Possibly strictly should be
# required by asciidoc
BuildRequires:  libxslt-tools
%endif

%if 0%{?suse_version} || 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?rhel} || 0%{?fedora}
BuildArch:      noarch
%endif

%description
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.

%package test
Summary:        Test package for crmsh
Group:          %{pkg_group}
Requires:       crmsh
%if %{with regression_tests}
Requires(post): mailx
Requires(post): procps
%if 0%{?suse_version}
Requires(post): python3-python-dateutil
%else
Requires(post): python3-dateutil
%endif
Requires(post): python3-tox
Requires(post): pacemaker
BuildArch:      noarch
Requires(post): python3-PyYAML
%endif

%description test
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.
This package contains the regression test suite for crmsh.

%package scripts
Summary:        Crm Shell Cluster Scripts
Group:          Productivity/Clustering/HA

%description scripts
Cluster scripts for crmsh. The cluster scripts can be run
directly from the crm command line, or used by user interfaces
like hawk to implement configuration wizards.

%prep
%setup -q

# replace the shebang in all the scripts
# with ${_bindir}/python3
find . -type f -exec sed -i \
    -e "s|#!/usr/bin/python3?|#!%{__python3}|" \
    -e "s|#!/usr/bin/env python3?|#!%{__python3}|" \
    {} \;
sed -i -e '1{\@^#!%{_bindir}/python3@d}' crmsh/report/core.py

# this is wrong FIXME
sed -i -e '/data_files/d' setup.py

%build
./autogen.sh

%{configure}            \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_var}             \
    --with-version=%{version}    \
    --docdir=%{crmsh_docdir}

%if 0%{?suse_version}
%python3_pyproject_wheel
%else
%pyproject_buildrequires -t
%pyproject_wheel
%endif

# Generate manpages
for manpg in doc/crm{,sh_crm_report}.8.adoc ; do
    a2x -f manpage $manpg
done

for docad in doc/crm{,sh_crm_report}.8.adoc ; do
    asciidoc --unsafe --backend=xhtml11 $docad
done

%if %{with regression_tests}
tox
if [ ! $? ]; then
    echo "Unit tests failed."
    exit 1
fi
%endif

%install
# make DESTDIR=%%{buildroot} docdir=%%{crmsh_docdir} install
%if 0%{?suse_version}
%python3_pyproject_install
%else
%pyproject_install
%endif

# additional directories
install -d -m0770 %{buildroot}%{_localstatedir}/cache/crm
install -d -m0770 %{buildroot}%{_localstatedir}/log/crmsh
install -d -m0755 %{buildroot}%{_tmpfilesdir}

# install configuration
install -Dm0644 -t %{buildroot}%{_sysconfdir}/crm etc/{crm.conf,profiles.yml}
install -m0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# install manpages
install -Dpm0644 -t %{buildroot}%{_mandir}/man8 doc/*.8
install -Dpm0644 -t %{buildroot}%{_datadir}/crmsh/ doc/crm.8.adoc

# install data
for d in $(cat data-manifest); do
	if [ -x $d ] ; then mode="0755" ; else mode="0644" ; fi
	install -D -m $mode $d %{buildroot}%{_datadir}/crmsh/$d
done
mv %{buildroot}%{_datadir}/crmsh/test{,s}
install -p test/testcases/xmlonly.sh \
	%{buildroot}%{_datadir}/crmsh/tests/testcases/configbasic-xml.filter

install -Dm0644 contrib/bash_completion.sh \
	%{buildroot}%{_datadir}/bash-completion/completions/crm

if [ -f %{buildroot}%{_bindir}/crm ]; then
	install -Dm0755 %{buildroot}%{_bindir}/crm %{buildroot}%{_sbindir}/crm
	rm %{buildroot}%{_bindir}/crm
fi

%if %{use_firewalld}
install -Dm0644 high-availability.xml \
	%{buildroot}%{_fwdefdir}/high-availability.xml
%endif

%if 0%{?suse_version}
%fdupes %{buildroot}
%endif

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%if %{use_firewalld}
%firewalld_reload
%endif

%if %{with regression_tests}
# Run regression tests after installing the package
# NB: this is called twice by OBS, that's why we touch the file
%post test
testfile=`mktemp -t .crmsh_regression_tests_ran_XXXXXX`
# check if time in file is less than 2 minutes ago
if [ -e $testfile ] && [ "$(( $(date +%s) - $(cat $testfile) ))" -lt 120 ]; then
	echo "Skipping regression tests..."
	exit 0
fi
# write current time to file
rm -f "$testfile"
echo "$(date +%s)" > "$testfile"
%{_datadir}/%{name}/tests/regression.sh
result1=$?
cd %{_datadir}/%{name}/tests
./cib-tests.sh
result2=$?
[ $result1 -ne 0 ] && (echo "Regression tests failed."; cat ${buildroot}/crmtestout/regression.out)
[ $result2 -ne 0 ] && echo "CIB tests failed."
[ $result1 -eq 0 -a $result2 -eq 0 ]
%endif

%files
###########################################################
%defattr(-,root,root)

%{_sbindir}/crm
%{python3_sitelib}/crmsh*

%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/tests
%exclude %{_datadir}/%{name}/scripts

%{_tmpfilesdir}/%{name}.conf

%doc doc/*.html
%doc COPYING AUTHORS ChangeLog README.md
%doc contrib/*
%{_mandir}/man8/*

%config %{_sysconfdir}/crm

%dir %attr (770, %{uname}, %{gname}) %{_var}/cache/crm
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/crmsh
%{_datadir}/bash-completion/completions/crm

%if %{use_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_fwdefdir}
%{_fwdefdir}/high-availability.xml
%endif

%files scripts
%defattr(-,root,root)
%{_datadir}/%{name}/scripts

%files test
%defattr(-,root,root)
%{_datadir}/%{name}/tests

%changelog
