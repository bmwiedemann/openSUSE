#
# spec file for package MirrorCache
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


%define mirrorcache_services_restart mirrorcache.service mirrorcache-backstage.service mirrorcache-backstage-hashes.service mirrorcache-subtree.service
%define mirrorcache_services %{mirrorcache_services_restart} mirrorcache-hypnotoad.service
%define assetpack_requires perl(CSS::Minifier::XS) >= 0.01 perl(JavaScript::Minifier::XS) >= 0.11 perl(Mojolicious::Plugin::AssetPack) >= 1.36 perl(IO::Socket::SSL)
%define main_requires %{assetpack_requires} perl(Carp) perl(DBD::Pg) >= 3.7.4 perl(DBI) >= 1.632 perl(DBIx::Class) >= 0.082801 perl(DBIx::Class::DynamicDefault) perl(DateTime) perl(Encode) perl(Time::Piece) perl(Time::Seconds) perl(Time::ParseDate) perl(DateTime::Format::Pg) perl(Exporter) perl(File::Basename) perl(LWP::UserAgent) perl(Mojo::Base) perl(Mojo::ByteStream) perl(Mojo::IOLoop) perl(Mojo::JSON) perl(Mojo::Pg) perl(Mojo::URL) perl(Mojo::Util) perl(Mojolicious::Commands) perl(Mojolicious::Plugin) perl(Mojolicious::Plugin::RenderFile) perl(Mojolicious::Static) perl(Net::OpenID::Consumer) perl(POSIX) perl(Sort::Versions) perl(URI::Escape) perl(XML::Writer) perl(base) perl(constant) perl(diagnostics) perl(strict) perl(warnings) shadow rubygem(sass) perl(Net::DNS) perl(LWP::Protocol::https) perl(Digest::SHA) perl(Config::IniFiles)
%define build_requires %{assetpack_requires} rubygem(sass) tidy sysuser-shadow sysuser-tools
Name:           MirrorCache
Version:        1.052
Release:        0
Summary:        WebApp to redirect and manage mirrors
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/openSUSE/MirrorCache
Source0:        %{name}-%{version}.tar.xz
Source1:        cache.tar.xz
Source2:        %{name}-user.conf
Source3:        %{name}-tmpfilesd.conf
# use update-cache (or tools/generate-packed-assets) to generate/update cache.tar.xz
Source101:      update-cache.sh
BuildRequires:  %{build_requires}
Requires:       %{main_requires}
Requires:       perl(Minion) >= 10.0
BuildArch:      noarch
%sysusers_requires

%description
Mirror redirector web service, which automatically scans the main server and mirrors

%prep
%setup -q -a1

%build
# make {?_smp_mflags}
%sysusers_generate_pre %{SOURCE2} %{name}

%check

%install
%make_install
# DEST_DIR={_datadir}
mkdir -p %{buildroot}%{_sbindir}
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcmirrorcache
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcmirrorcache-hypnotoad
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcmirrorcache-backstage
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcmirrorcache-backstage-hashes
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcmirrorcache-subtree
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%pre -f %{name}.pre
%service_add_pre %{mirrorcache_services}

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{mirrorcache_services}

%preun
%service_del_preun %{mirrorcache_services}

%postun
%service_del_postun %{mirrorcache_services_restart}
%service_del_postun_without_restart mirrorcache-hypnotoad.service

%files
%doc README.md
%license LICENSE
%{_sbindir}/rcmirrorcache
%{_sbindir}/rcmirrorcache-hypnotoad
%{_sbindir}/rcmirrorcache-backstage
%{_sbindir}/rcmirrorcache-backstage-hashes
%{_sbindir}/rcmirrorcache-subtree
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %attr(-,root,mirrorcache) %{_sysconfdir}/mirrorcache/
%ghost %dir %attr(0750,mirrorcache,-) %{_localstatedir}/lib/mirrorcache/
# init
%dir %{_unitdir}
%{_unitdir}/mirrorcache.service
%{_unitdir}/mirrorcache-hypnotoad.service
%{_unitdir}/mirrorcache-backstage.service
%{_unitdir}/mirrorcache-backstage-hashes.service
%{_unitdir}/mirrorcache-subtree.service
# web libs
%{_datadir}/mirrorcache

%changelog
