#
# spec file for package plocate
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


%bcond_without  apparmor

Name:           plocate
Version:        1.1.22
Release:        0
Summary:        A much faster locate(1)
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://plocate.sesse.net
Source:         https://plocate.sesse.net/download/%{name}-%{version}.tar.gz
Source1:        updatedb.conf
Source2:        %{name}-updatedb.service
Source3:        sysconfig.locate
%if %{with apparmor}
Source5:        usr.bin.plocate
Source6:        usr.sbin.updatedb
%endif
Patch0:         disable-visibility.patch
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libzstd)
%if %{with apparmor}
Requires:       apparmor-abstractions
%endif
Requires:       group(nobody)
Requires:       user(nobody)
Requires(post): %fillup_prereq
# other packages depend on mlocate or findutils-locate, we have to provide fake versions.
# mlocate provides findutils-locate = 5.%%{version}
Provides:       findutils:%{_bindir}/locate
Provides:       mlocate = 6.%{version}-%{release}
Obsoletes:      mlocate < 6.%{version}-%{release}
Provides:       findutils-locate = 6.%{version}-%{release}
Obsoletes:      findutils-locate < 6.%{version}-%{release}
%{?systemd_requires}

%description
plocate is a locate based on posting lists, completely replacing mlocate
with a much faster (and smaller) index. It is suitable as a default locate
on your system.

%prep
%autosetup

%build
%meson -Dsystemunitdir=%{_unitdir} -Dinstall_systemd=true -Dlocategroup=nobody
%meson_build

%install
%meson_install
# remove set-group bit:
chmod 00755 %{buildroot}%{_bindir}/%{name}
# install auxiliary files:
install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/updatedb.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-updatedb.service
install -Dm644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.locate
# compat symlinks:
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/locate
ln -sr %{buildroot}%{_mandir}/man1/%{name}.1%{?ext_man} %{buildroot}%{_mandir}/man1/locate.1%{?ext_man}
ln -s  %{_sbindir}/updatedb %{buildroot}%{_bindir}/updatedb
ln -s  %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-updatedb
%if %{with apparmor}
install -Dm644 %{SOURCE5} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.plocate
install -Dm644 %{SOURCE6} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.updatedb
%endif

%check

%pre
%service_add_pre %{name}-updatedb.service %{name}-updatedb.timer

%post
%{fillup_only -n locate}
%service_add_post %{name}-updatedb.service %{name}-updatedb.timer

%preun
%service_del_preun %{name}-updatedb.service %{name}-updatedb.timer

%postun
%service_del_postun %{name}-updatedb.service %{name}-updatedb.timer

%files
%license COPYING
%doc NEWS README
%{_bindir}/locate
%{_bindir}/%{name}
%{_unitdir}/%{name}-updatedb.service
%{_unitdir}/%{name}-updatedb.timer
%{_sbindir}/updatedb
%{_bindir}/updatedb
%{_sbindir}/%{name}-build
%{_sbindir}/rc%{name}-updatedb
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/locate.1%{?ext_man}
%{_mandir}/man5/updatedb.conf.5%{?ext_man}
%{_mandir}/man8/%{name}-build.8%{?ext_man}
%{_mandir}/man8/updatedb.8%{?ext_man}
%{_fillupdir}/sysconfig.locate
%dir %{_sharedstatedir}/%{name}/
%{_sharedstatedir}/%{name}/CACHEDIR.TAG
%ghost %{_sharedstatedir}/%{name}/%{name}.db
%config(noreplace) %{_sysconfdir}/updatedb.conf
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d/
%config %{_sysconfdir}/apparmor.d/usr.bin.plocate
%config %{_sysconfdir}/apparmor.d/usr.sbin.updatedb
%endif

%changelog
