#
# spec file for package gerbera
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gerbera
Version:        1.12.1
Release:        0
Summary:        UPnP Media Server
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        config.xml
Source2:        gerbera.sysusers.in
Patch0:         harden_gerbera.service.patch
BuildRequires:  ccache
BuildRequires:  cmake >= 3.13
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gmock_main)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtest_main)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libebml)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libmatroska)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libupnp) >= 1.14.6
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(spdlog) >= 1.8.1
BuildRequires:  pkgconfig(sqlite3) >= 3.7.11
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(taglib) >= 1.12
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Requires:       logrotate
%{?systemd_requires}
%if 0%{?suse_version} <= 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Gerbera is a UPnP media server which allows streaming digital
media through a network and consume it on a variety of UPnP
compatible devices.

%prep
%autosetup -p1

# server test hardcodes alpha strings
sed -i -e '/test_server/d' test/CMakeLists.txt
sed -i -e 's/@USER@/gerbera/' %{SOURCE2}
sed -i -e 's/@GROUP@/gerbera/' %{SOURCE2}

%build
%cmake \
  -DWITH_JS=1 \
  -DWITH_TAGLIB=1 \
  -DWITH_MAGIC=1 \
  -DWITH_AVCODEC=1 \
  -DWITH_EXIF=0 \
  -DWITH_EXIV2=1 \
%if 0%{?suse_version} <= 1550
  -DCMAKE_CXX_COMPILER=g++-10 \
  -DCMAKE_C_COMPILER=gcc-10 \
%endif
  -DWITH_FFMPEGTHUMBNAILER=1 \
  -DWITH_INOTIFY=1 \
  -DWITH_SYSTEMD=1 \
  -DWITH_TESTS=1 \
  -Wno-dev
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/gerbera
touch %{buildroot}%{_sysconfdir}/gerbera/{gerbera.db,gerbera.html}
mkdir -p %{buildroot}%{_localstatedir}/log/gerbera
touch %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p  %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << 'EOF'
%{_localstatedir}/log/gerbera/gerbera {
create 644 gerbera gerbera
      monthly
      compress
      missingok
}
EOF

install -d %{buildroot}%{_sbindir}
ln -s service  %{buildroot}%{_sbindir}/rc%{name}

install -p -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gerbera/config.xml
install -p -D -m0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/gerbera.conf

%check
%ctest

%pre
getent group gerbera >/dev/null || groupadd -r gerbera
getent passwd gerbera >/dev/null || \
useradd -r -g gerbera -d %{_sysconfdir}/gerbera -s /sbin/nologin \
    -c "To run Gerbera" gerbera
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%if 0%{?suse_version} > 1590
%sysusers_create_package %{_sysusersdir}/%{name}.conf
%else
%sysusers_create %{_sysusersdir}/%{name}.conf
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md
%attr(-,gerbera,gerbera)%dir %{_sysconfdir}/%{name}/
%attr(-,gerbera,gerbera)%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(-,gerbera,gerbera) %{_localstatedir}/log/%{name}
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

%changelog
