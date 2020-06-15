#
# spec file for package onedrive
#
# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2018 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%{!?_userunitdir: %{expand: %%global _userunitdir %{_unitdir}/../user}}
%define docdir %{_defaultdocdir}/%{name}

Name:           onedrive
Version:        2.4.2
Release:        0
License:        GPL-3.0
Summary:        Client for One Drive Service for Linux
Url:            https://github.com/abraunegg/onedrive/
Group:          Productivity/Networking/Other
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  dmd
BuildRequires:  sqlite3-devel
BuildRequires:  libcurl-devel
BuildRequires:  phobos-devel-static
BuildRequires:  help2man
Recommends:       logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OneDrive is a client for Microsoft file serving service

%prep
%setup -q
#sed -i /chown/d Makefile
sed -i 's/^docdir.*/docdir = @docdir@/g' Makefile.in

%build
%configure --docdir=%{docdir} --with-systemduserunitdir=%_userunitdir --with-systemdsystemunitdir=%_unitdir
make %{?_smp_mflags} %{name}

%install
%make_install
install -D -m 0644 config %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

%pre
%service_add_pre %{name}@.service
%service_add_pre %{name}.service

%post
%service_add_post %{name}@.service
%service_add_post %{name}.service

%preun
%service_del_preun %{name}@.service
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}@.service
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%license LICENSE
%doc USAGE.md Office365.md INSTALL.md Docker.md CHANGELOG.md config LICENSE README.md
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/%{name}
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%attr(0644, root, root) %{_mandir}/man1/%{name}.1*
%{_localstatedir}/log/%{name}
