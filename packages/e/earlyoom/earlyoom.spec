#
# spec file for package earlyoom
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


# The tests are quite flaky in a VM
%bcond_with tests
%if ! 0%{?_fillupdir:1}
%global _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           earlyoom
Version:        1.8.2
Release:        0
Summary:        Early OOM Daemon for Linux
License:        MIT
Group:          System/Daemons
URL:            https://github.com/rfjakob/%{name}
Source0:        https://github.com/rfjakob/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.sysconfig
# pandoc MANPAGE.md -s -t man > earlyoom.1
Source2:        earlyoom.1
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
%autosetup -p1
sed -i 's|/default/|/sysconfig/|' earlyoom.service.in
sed -e '/systemctl/d' -i Makefile

%build
CFLAGS='%{?build_cflags}%{!?build_cflags:%optflags} -DVERSION=\"%{version}\" -std=gnu99'
CPPFLAGS='%{?build_cxxflags}%{!?build_cxxflags:%optflags}'
LDFLAGS="-lrt ${RPM_LD_FLAGS}"
%make_build CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS" PREFIX=%{_prefix}

%check
test %{SOURCE2} -nt README.md
%if %{with tests}
sed -i 's|stderrContains: "earlyoom v",|stderrContains: "earlyoom %{version}",|' testsuite_cli_test.go
%make_build test
%endif

%install
%make_install PREFIX=%{_prefix} SYSTEMDUNITDIR=%{_unitdir}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1

mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}

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
