#
# spec file for package warewulf-nhc
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


%{!?sname:%global sname nhc}
%{!?nhc_script_dir:%global nhc_script_dir %{_sysconfdir}/%{sname}/scripts}
%{!?nhc_helper_dir:%global nhc_helper_dir %{_libexecdir}/%{sname}}

Name:           warewulf-nhc
Version:        1.4.2
Release:        0
Summary:        Warewulf Node Health Check (NHC)
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            http://warewulf.lbl.gov/trac
Source0:        https://github.com/mej/nhc/archive/%{version}.tar.gz#./warewulf-nhc-%{version}.tar.gz
Patch0:         test-test_lbnl_file.nhc-Put-all-process-substitution.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  git
BuildRequires:  rpmbuild
BuildRequires:  subversion
Requires:       bash
Requires:       logrotate

%description
Warewulf Node Health Check (NHC) is a periodic "node health check" script to be
executed on each compute node to verify that the node is working properly. Nodes
which are determined to be "unhealthy" can be marked as down or offline so as to
prevent jobs from being scheduled or run on them. This helps increase the
reliability and throughput of a cluster by reducing preventable job failures due
to misconfiguration, hardware failures, etc.

%prep
%setup -q -n %{sname}-%{version}
%autopatch -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -d -m 0755 %{buildroot}/%{_tmpfilesdir}/
cat <<EOF > %{buildroot}/%{_tmpfilesdir}/%{name}.conf
	d /var/run/%{sname} 0755
EOF
chmod 0644 %{buildroot}/%{_tmpfilesdir}/%{name}.conf
# remove hardcoded var
rm -vr %{buildroot}/%{_localstatedir}/run/nhc

mv %{buildroot}/etc/logrotate.d/%{sname} %{buildroot}/etc/logrotate.d/%{name}

# test fails for factory, will be fixed in next release
%if !0%{?suse_version} > 1500 
%check
%{__make} test
%endif

%post 
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%files
%defattr(-, root, root)
%license LICENSE COPYING 
%doc nhc.conf contrib/nhc.cron
%dir %{_sysconfdir}/%{sname}/
%dir %{_localstatedir}/lib/%{sname}/
%dir %{nhc_script_dir}/
%dir %{nhc_helper_dir}/
%config(noreplace) %{_sysconfdir}/%{sname}/%{sname}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{nhc_script_dir}/*.nhc
%{nhc_helper_dir}/*
%{_sbindir}/%{sname}
%{_sbindir}/%{sname}-genconf
%{_sbindir}/%{sname}-wrapper
%{_tmpfilesdir}/%{name}.conf

%changelog
