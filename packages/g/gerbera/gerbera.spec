#
# spec file for package gerbera
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

Name:           gerbera
Version:        2.4.1
Release:        0
Summary:        UPnP Media Server
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        config.xml
Source2:        gerbera.sysusers.in
Source10:       %{name}-vhost-apache.conf
Source11:       %{name}-vhost-nginx.conf
Source90:       README.SUSE
Patch0:         harden_gerbera.service.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  ccache
BuildRequires:  cmake >= 3.13
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(duktape) >= 2.6.0
BuildRequires:  pkgconfig(exiv2) >= 0.26
BuildRequires:  pkgconfig(fmt) >= 9.1.0
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gmock_main)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtest_main)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libebml)
BuildRequires:  pkgconfig(libffmpegthumbnailer) >= 2.2.2
BuildRequires:  pkgconfig(libmatroska) >= 1.6.3
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libupnp) >= 1.14.6
BuildRequires:  pkgconfig(pugixml) >= 1.10
BuildRequires:  pkgconfig(spdlog) >= 1.11.0
BuildRequires:  pkgconfig(sqlite3) >= 3.35.5
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(taglib) >= 1.12
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Requires:       diffutils
Requires:       logrotate
%{?systemd_requires}
%sysusers_requires
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12

%description
Gerbera is a UPnP media server which allows streaming digital
media through a network and consume it on a variety of UPnP
compatible devices.

%package apache
Summary:        Apache configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  apache2
Requires:       %{name} = %{version}
Requires:       apache2
Supplements:    (apache2 and %{name})
Conflicts:      %{name}-nginx

%description apache
This subpackage contains the Apache configuration files

%package nginx
Summary:        Nginx configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  nginx
Requires:       %{name} = %{version}
Requires:       nginx
Supplements:    (nginx and %{name})
Conflicts:      %{name}-apache

%description nginx
This subpackage contains the nginx configuration files

%prep
%autosetup -p1
install -m 644 %{SOURCE90} .

rm -f web/.gitignore

# server test hardcodes alpha strings
sed -i -e '/test_server/d' test/CMakeLists.txt
#sed -i -e 's/@USER@/gerbera/' %%{SOURCE2}
#sed -i -e 's/@GROUP@/gerbera/' %%{SOURCE2}

%build
%cmake \
  -DWITH_JS=1 \
  -DWITH_TAGLIB=1 \
  -DWITH_MAGIC=1 \
  -DWITH_AVCODEC=1 \
  -DWITH_EXIF=0 \
  -DWITH_EXIV2=1 \
%if 0%{?force_gcc_version}
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-%{?force_gcc_version} \
%endif
  -DWITH_FFMPEGTHUMBNAILER=1 \
  -DWITH_INOTIFY=1 \
  -DWITH_SYSTEMD=1 \
  -DWITH_TESTS=1 \
  -Wno-dev
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/gerbera.html
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
touch %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p  %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << 'EOF'
%{_localstatedir}/log/gerbera/gerbera {
      su gerbera gerbera
      monthly
      compress
      missingok
}
EOF
cat > %{buildroot}%{_sysconfdir}/%{name}/_INFO_ << 'EOF'
gerbera.xml         <- active configuration file
gerbera-example.xml <- example configuration with almost all options
gerbera-new.xml     <- new configuration file after update of package
gerbera-diff.xml    <- diff between gerbera.xml and gerbera-new.xml
EOF

install -d %{buildroot}%{_sbindir}
ln -s service  %{buildroot}%{_sbindir}/rc%{name}

#install -p -D -m0644 %%{SOURCE1} %%{buildroot}%%{_sysconfdir}/gerbera/config.xml
install -p -D -m0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/gerbera.conf

# vhost config apache and nginx
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d
install -D -m0644 %{SOURCE10} %{buildroot}%{apache_sysconfdir}/vhosts.d/%{name}.conf
# nginx config
mkdir -p %{buildroot}%{_sysconfdir}/nginx/vhosts.d/
install -D -m0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/nginx/vhosts.d/%{name}.conf

%sysusers_generate_pre %{buildroot}%{_sysusersdir}/gerbera.conf gerbera gerbera.conf

%check
%ctest

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
# only do on install
if [ "$1" -eq 1 ]; then
  echo "o Create config.xml..." || :
  gerbera --create-config | sudo tee /etc/gerbera/config.xml || :
  sed -i -e 's|<home>/root/</home>|<home>/etc/gerbera</home>|g' /etc/gerbera/config.xml || :
  sed -i -e 's|<database-file>gerbera.db</database-file>|<database-file>/var/lib/gerbera/gerbera.db</database-file>|g' /etc/gerbera/config.xml || :
fi
# only do on upgrade
if [ "$1" -gt 1 ]; then
  echo "o Create config-diff.xml from own config to new config..." || :
  gerbera --create-config | sudo tee /etc/gerbera/config-new.xml || :
  sed -i -e 's|<home>/root/</home>|<home>/etc/gerbera</home>|g' /etc/gerbera/config-new.xml || :
  sed -i -e 's|<database-file>gerbera.db</database-file>|<database-file>/var/lib/gerbera/gerbera.db</database-file>|g' /etc/gerbera/config-new.xml || :
  diff /etc/gerbera/config.xml /etc/gerbera/config-new.xml > /etc/gerbera/config-diff.xml || :
fi
echo "o Create new config-example.xml with almost all options..." || :
gerbera --create-example-config | sudo tee /etc/gerbera/config-example.xml || :

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md README.SUSE
%dir %attr(0750,gerbera,gerbera) %{_sysconfdir}/%{name}
%attr(640,gerbera,gerbera)%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %attr(0750,gerbera,gerbera) %{_localstatedir}/log/%{name}
%dir %attr(0750,gerbera,gerbera) %{_localstatedir}/lib/%{name}
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/gerbera.service
%{_sysusersdir}/gerbera.conf
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/gerbera/mysql-upgrade.xml
%{_datadir}/gerbera/mysql.sql
%{_datadir}/gerbera/sqlite3-upgrade.xml
%{_datadir}/gerbera/sqlite3.sql
%dir %{_datadir}/gerbera
%dir %{_datadir}/gerbera/js
%dir %{_datadir}/gerbera/web
%{_datadir}/gerbera/js/*
%{_datadir}/gerbera/web/*
%exclude %{apache_sysconfdir}/vhosts.d/%{name}.conf
%exclude %{_sysconfdir}/nginx/vhosts.d/%{name}.conf

%files apache
%config(noreplace) %{apache_sysconfdir}/vhosts.d/%{name}.conf

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/vhosts.d/%{name}.conf

%changelog
