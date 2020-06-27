#
# spec file for package mednafen-server
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


%define _group games
%define _user  mednafen
%define _home  %{_localstatedir}/lib/%{_user}
Name:           %{_user}-server
Version:        0.5.2
Release:        0
Summary:        Mednafen network play server
License:        GPL-2.0-only
Group:          System/Emulators/Other
URL:            https://mednafen.github.io
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}.tar.xz
Source1:        %{_user}.service
Source2:        %{_user}.firewalld
BuildRequires:  gcc-c++
Requires(pre):  shadow

%description
Network play server for mednafen

%prep
%setup -q -n %{name}

%build
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sbindir}
ln -fs %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{_user}
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{_user}.service
install -Dm664 standard.conf %{buildroot}%{_home}/%{name}.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_libexecdir}/firewalld/services/%{_user}.xml

%pre
getent group %{_group} >/dev/null 2>/dev/null || %{_sbindir}/groupadd -r %{_group}
getent passwd %{_user} >/dev/null 2>/dev/null || %{_sbindir}/useradd -rc 'User for for multiple video game console emulator server' -s /bin/false -d %{_home} -g %{_group} %{_user}
%service_add_pre %{_user}.service

%post
%service_add_post %{_user}.service

%preun
%service_del_preun %{_user}.service

%postun
%service_del_postun %{_user}.service

%files
%config(noreplace) %attr(0664,%{_user},%{_group}) %{_home}/%{name}.conf
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}
%{_sbindir}/rc%{_user}
%{_unitdir}/%{_user}.service
%dir %{_libexecdir}/firewalld
%dir %{_libexecdir}/firewalld/services
%{_libexecdir}/firewalld/services/%{_user}.xml
%dir %attr(-,%{_user},%{_group}) %{_home}

%changelog
