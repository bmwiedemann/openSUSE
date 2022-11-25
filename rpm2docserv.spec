#
# spec file for package rpm2docserv
#
# Copyright (c) 2022 SUSE LLC
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


Name:           rpm2docserv
Version:        20221125.be8d83b
Release:        0
Summary:        Make manpages from RPMs accessible in a web browser
License:        Apache-2.0
URL:            https://github.com/thkukuk/rpm2docserv
Source:         rpm2docserv-%{version}.tar.xz
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  golang(API) >= 1.18
# To re-create:
# git clone https://github.com/Debian/debiman
# cd rpm2docserv; make vendor; cd ..
# osc service

%description
rpm2docserv extracts manual pages from RPM packages and makes them accessible in a web browser.

%package -n docserv-auxserver
Summary:        Docserv auxiliary service endpoints
%{sysusers_requires}

%description -n docserv-auxserver
docserv-auxserver has a very efficient, small map to redirect to the correct manual page for rpm2docserv created html repositories.

%package -n docserv-minisrv
Summary:        Simple docserv webserver
%{sysusers_requires}

%description -n docserv-minisrv
Simple docserv webserver with integrated auxserver for development and test purposes. Not for production.

%package -n docserv-sitemap
Summary:        Generate sitemap xml files for rpm2docserv

%description -n docserv-sitemap
This tool generates sitemap xml files from a rpm2docserv generated docserv directory for search engines.

%package -n docserv-config-nginx
Summary:        Configuration files for nginx to serve docserv directory
BuildArch:      noarch

%description -n docserv-config-nginx
This package contains example configuration files for nginx to act as web server for docserv manpages.

%package -n docserv-config-apache2
Summary:        Configuration files for Apache 2.4 to serve docserv directory
BuildArch:      noarch

%description -n docserv-config-apache2
This package contains example configuration files for Apache 2.4 to act as web server for docserv manpages.

%prep
%setup -q

%build
%make_build build VERSION=%{version} USE_VENDOR="-mod vendor"

%sysusers_generate_pre systemd/system-user-docserv-aux.conf docserv-aux system-user-docserv-aux.conf
%sysusers_generate_pre systemd/system-user-docserv-srv.conf docserv-srv system-user-docserv-srv.conf

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/rpm2docserv %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sbindir}
install -m 755 bin/docserv-auxserver %{buildroot}%{_sbindir}/
install -m 755 bin/docserv-minisrv %{buildroot}%{_sbindir}/
install -m 755 bin/docserv-idx2rwmap %{buildroot}%{_bindir}/
install -m 755 bin/docserv-sitemap %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r assets %{buildroot}%{_datadir}/%{name}

install -D -m 0644 systemd/docserv-auxserver.service %{buildroot}%{_unitdir}/docserv-auxserver.service
install -D -m 0644 systemd/docserv-auxserver.default %{buildroot}%{_distconfdir}/default/docserv-auxserver
install -D -m 0644 systemd/docserv-minisrv.service %{buildroot}%{_unitdir}/docserv-minisrv.service
install -D -m 0644 systemd/docserv-minisrv.default %{buildroot}%{_distconfdir}/default/docserv-minisrv
mkdir -p %{buildroot}%{_sysusersdir}/
install -m 644 systemd/system-user-*.conf %{buildroot}%{_sysusersdir}/

# nginx container
mkdir -p %{buildroot}%{_datadir}/docserv/nginx
install -m 755 nginx/*.sh %{buildroot}%{_datadir}/docserv/nginx/
install -m 644 nginx/*.conf %{buildroot}%{_datadir}/docserv/nginx/

# apache configuration
mkdir -p %{buildroot}%{_datadir}/docserv/apache2
install -m 644 apache2/* %{buildroot}%{_datadir}/docserv/apache2/

%pre -n docserv-auxserver -f docserv-aux.pre
%service_add_pre docserv-auxserver.service

%post -n docserv-auxserver
%service_add_post docserv-auxserver.service

%preun -n docserv-auxserver
%service_del_preun docserv-auxserver.service

%postun -n docserv-auxserver
%service_del_postun docserv-auxserver.service

%pre -n docserv-minisrv -f docserv-srv.pre
%service_add_pre docserv-minisrv.service

%post -n docserv-minisrv
%service_add_post docserv-minisrv.service

%preun -n docserv-minisrv
%service_del_preun docserv-minisrv.service

%postun -n docserv-minisrv
%service_del_postun docserv-minisrv.service

%files
%license LICENSE
%{_bindir}/rpm2docserv
%{_bindir}/docserv-idx2rwmap
%{_datadir}/%{name}

%files -n docserv-auxserver
%license LICENSE
%{_sbindir}/docserv-auxserver
%{_unitdir}/docserv-auxserver.service
%{_sysusersdir}/system-user-docserv-aux.conf
%{_distconfdir}/default/docserv-auxserver

%files -n docserv-minisrv
%license LICENSE
%{_sbindir}/docserv-minisrv
%{_unitdir}/docserv-minisrv.service
%{_sysusersdir}/system-user-docserv-srv.conf
%{_distconfdir}/default/docserv-minisrv

%files -n docserv-sitemap
%license LICENSE
%{_bindir}/docserv-sitemap

%files -n docserv-config-nginx
%dir %{_datadir}/docserv
%{_datadir}/docserv/nginx

%files -n docserv-config-apache2
%dir %{_datadir}/docserv
%{_datadir}/docserv/apache2

%changelog
