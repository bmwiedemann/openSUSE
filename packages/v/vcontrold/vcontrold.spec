#
# spec file for package vcontrold
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vcontrold
Version:        v0.98.10+git20210418.977e6f5
Release:        0
Summary:        Daemon for communication with Viessmann heating controllers
License:        GPL-3.0-or-later
Url:            https://github.com/openv/vcontrold
Source0:        %{name}-%{version}.tar
Source1:        system-user-vcontrold.conf
Source2:        vcontrold.service
Source3:        vcontrold-tmpfiles.conf
BuildRequires:  c_compiler
BuildRequires:  python3-docutils
BuildRequires:  cmake
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires:       group(dialout)
%sysusers_requires

%description
vcontrold is a software daemon written in C for communication with
the "Optolink" interface of Viessmann heating controllers.

%prep
%setup -q
sed -i -e 's/nobody/vcontrold/' xml/300/vcontrold.xml

%build
%sysusers_generate_pre "%{SOURCE1}" "%{name}"
#
%cmake
%cmake_build

%install
%cmake_install
#
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/
#
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
#
mkdir -p %{buildroot}%{_datadir}/factory/etc/vcontrold
cp xml/300/* %{buildroot}%{_datadir}/factory/etc/vcontrold
#
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
#
mkdir -p %{buildroot}%{_sysconfdir}/vcontrold
touch %{buildroot}%{_sysconfdir}/vcontrold/{vcontrold,vito}.xml
#
ln -s service %{buildroot}%{_sbindir}/rcvcontrold

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%tmpfiles_create %_tmpfilesdir/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc README.md COPYING
%doc doc/examples xml
%{_bindir}/vclient
%{_sbindir}/vcontrold
%{_sbindir}/rcvcontrold
%{_mandir}/man1/*
%{_datadir}/factory
%{_sysconfdir}/vcontrold
%config %ghost %{_sysconfdir}/vcontrold/vito.xml
%config %ghost %{_sysconfdir}/vcontrold/vcontrold.xml
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/system-user-%{name}.conf

%changelog

