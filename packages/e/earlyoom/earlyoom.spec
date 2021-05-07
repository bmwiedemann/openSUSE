#
# spec file for package earlyoom
#
# Copyright (c) 2021 SUSE LLC
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


# the tests are quite flaky in a VM
%bcond_with tests
%if ! 0%{?_fillupdir:1}
%global _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           earlyoom
Version:        1.6.2
Release:        0
Summary:        Early OOM Daemon for Linux
License:        MIT
Group:          System/Daemons
URL:            https://github.com/rfjakob/%{name}
Source0:        %{URL}/archive/v%{version}.tar.gz
Source11:       %{name}.sysconfig
# Inject pre-build earlyoom.1, built on x86_64 machine, as pandoc does not exist on all archs
Source12:       earlyoom.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Conflicts:      oomd
%if %{with tests}
BuildRequires:  go
%endif

%description
earlyoom checks the amount of available memory and free swap, and if both are
below critical level, it will kill the largest process (highest oom_score).

%prep
%autosetup
# Test if our pre-build earloom.1 is newer than README.md; if not, fail
# in case of fail, rebuild the earlyoom.1 out of the build system using
#     pandoc MANPAGE.md -s -t man > earlyoom.1
test %{SOURCE12} -nt README.md

# Fix defaults file location
sed -i 's|/default/|/sysconfig/|' earlyoom.service.in

# remove calls to systemctl in install
sed -e '/systemctl/d' -i Makefile

%if %{with tests}
# fix version test
sed -i 's|stderrContains: "earlyoom v",|stderrContains: "earlyoom %{version}",|' testsuite_cli_test.go
%endif

%build
CFLAGS='%{?build_cflags}%{!?build_cflags:%optflags} -DVERSION=\"%{version}\" -std=gnu99'
CPPFLAGS='%{?build_cxxflags}%{!?build_cxxflags:%optflags}'
LDFLAGS="-lrt ${RPM_LD_FLAGS}"
%make_build CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS" PREFIX=%{_prefix}

%check
%if %{with tests}
%make_build test
%endif

%install
%make_install PREFIX=%{_prefix} SYSTEMDUNITDIR=%{_unitdir}
install -D -m644 %{SOURCE11} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}%{_mandir}/man1/
install -m644 %{SOURCE12} %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

%files
%license LICENSE
%doc MANPAGE.md README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%exclude %{_sysconfdir}/default/%{name}
%{_fillupdir}/sysconfig.%{name}
%{_sbindir}/rc%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%pre
%{service_add_pre %{name}.service}

%post
%{fillup_only %{name}}
%{service_add_post %{name}.service}

%preun
%{service_del_preun %{name}.service}

%postun
%{service_del_postun %{name}.service}

%changelog
