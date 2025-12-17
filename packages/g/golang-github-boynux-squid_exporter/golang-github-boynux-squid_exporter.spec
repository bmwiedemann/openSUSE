#
# spec file for package golang-github-boynux-squid_exporter
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2019 João Cavalheiro <jcavalheiro@suse.com>
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


# Templating vars to simplify and standardize Prometheus exporters spec files
%define	githubrepo    github.com/boynux/squid-exporter
%define	upstreamname  squid-exporter
%define	targetname    prometheus-squid_exporter
%define	serviceuser   prometheus

%if 0%{?rhel} == 8
%global debug_package %{nil}
%endif

%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

Name:           golang-github-boynux-squid_exporter
Version:        1.13.0
Release:        0
Summary:        Squid Prometheus Exporter
License:        MIT
Group:          System/Management
URL:            http://%{githubrepo}
Source:         %{upstreamname}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{targetname}.service
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
BuildRequires:  gcc11-c++
%endif
%if 0%{?rhel}
BuildRequires:  golang >= 1.15
%else
BuildRequires:  golang(API) >= 1.23
%endif
%if 0%{?rhel}
Requires(pre):  shadow-utils
%else
Requires(pre):  shadow
%endif
ExcludeArch:    s390
%systemd_ordering

%description
Exports squid metrics in Prometheus format

%prep
%setup -q -a1 -n %{upstreamname}-%{version}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
%ifarch s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl
export CGO_ENABLED=1
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
export CC=gcc-11
export CXX=g++-11
%endif
%endif
go build

%install
install -D -m0755 %{_builddir}/%{upstreamname}-%{version}/%{upstreamname} %{buildroot}/%{_bindir}/%{targetname}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{targetname}

%check
%if 0%{?rhel}
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug/%{_bindir}/%{targetname}-%{version}-*.debug
%endif

%pre
%if 0%{?suse_version}
%service_add_pre %{targetname}.service
%endif
getent group %{serviceuser} >/dev/null || %{_sbindir}/groupadd -r %{serviceuser}
getent passwd %{serviceuser} >/dev/null || %{_sbindir}/useradd -r -g %{serviceuser} -d %{_localstatedir}/lib/%{serviceuser} -M -s /sbin/nologin %{serviceuser}

%post
%if 0%{?rhel}
%systemd_post %{targetname}.service
%else
%service_add_post %{targetname}.service
%endif

%preun
%if 0%{?rhel}
%systemd_preun %{targetname}.service
%else
%service_del_preun %{targetname}.service
%endif

%postun
%if 0%{?rhel}
%systemd_postun %{targetname}.service
%else
%service_del_postun %{targetname}.service
%endif

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{targetname}
%{_unitdir}/%{targetname}.service
%{_sbindir}/rc%{targetname}

%changelog
