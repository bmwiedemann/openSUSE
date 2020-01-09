#
# spec file for package earlyoom
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


%if ! 0%{?_fillupdir:1}
%global _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           earlyoom
Version:        1.3
Release:        0
Summary:        Early OOM Daemon for Linux
License:        MIT
Group:          System/Daemons
URL:            https://github.com/rfjakob/earlyoom
Source0:        https://github.com/rfjakob/earlyoom/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source11:       earlyoom.sysconfig
# pandoc only for `pandoc MANPAGE.md -s -t man > earlyoom.1`
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires(post): insserv-compat
Recommends:     libnotify%{?suse_version:-tools}
Conflicts:      oomd

%description
earlyoom checks the amount of available memory and free swap, and if both are
below critical level, it will kill the largest process (highest oom_score).

%prep
%setup -q

# Fix defaults file location
sed -i 's|/default/|/sysconfig/|' earlyoom.service.in

# Fix LDFLAGS handling
sed -ri '/LDFLAGS/ s|$| -lrt|' Makefile

%build
CFLAGS='%{optflags} -DVERSION=\"%{version}\" -std=gnu99'
make %{?_smp_mflags} CFLAGS="$CFLAGS"

%install
%make_install PREFIX=%{_prefix} SYSTEMDUNITDIR=%{_unitdir}
install -D -m644 %{SOURCE11} %{buildroot}%{_fillupdir}/sysconfig.%{name}

# Files list
%files
%license LICENSE
%doc MANPAGE.md README.md
%{_bindir}/earlyoom
%{_unitdir}/%{name}.service
%exclude %{_sysconfdir}/default/earlyoom
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man1/earlyoom.1%{?ext_man}

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
