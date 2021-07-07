#
# spec file for package gerbera
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


Name:           gerbera
Version:        1.8.2
Release:        0
Summary:        UPnP Media Server
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source3:        gerbera.tmpfile.in
Source4:        gerbera.sysusers.in
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  file-devel
%if 0%{?suse_version} <= 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  ccache
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
BuildRequires:  pkgconfig(libupnp) >= 1.14.0
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(taglib) >= 1.11
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
%{?systemd_requires}

%description
Gerbera is a UPnP media server which allows streaming digital
media through a network and consume it on a variety of UPnP
compatible devices.

%prep
%autosetup

# server test hardcodes alpha strings
sed -i -e '/test_server/d' test/CMakeLists.txt

for _file in %{SOURCE3} %{SOURCE4}; do
  sed -e 's/@USER@/gerbera/' \
      -e 's/@GROUP@/gerbera/' \
      < $_file > ${_file##*/}
done

%build
%cmake \
  -DWITH_AVCODEC=1 \
  -DWITH_EXIF=0 \
  -DWITH_EXIV2=1 \
%if 0%{?suse_version} <= 1550
  -DCMAKE_CXX_COMPILER=g++-10 \
  -DCMAKE_C_COMPILER=gcc-10 \
%endif
  -DWITH_FFMPEGTHUMBNAILER=1 \
  -Wno-dev
%cmake_build

%install
%cmake_install

install -d %{buildroot}%{_sbindir}
ln -s service  %{buildroot}%{_sbindir}/rc%{name}
install -Dm 0644 %{name}.tmpfile.in %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dm 0644 %{name}.sysusers.in %{buildroot}%{_sysusersdir}/%{name}.conf

install -d %{buildroot}%{_localstatedir}/lib/%{name}
touch %{buildroot}%{_localstatedir}/lib/%{name}/{config.xml,%{name}.db,%{name}.html}

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
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%sysusers_create %{_sysusersdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%{_mandir}/man?/%{name}.?%{?ext_man}
%ghost %attr(-,gerbera,gerbera) %dir %{_localstatedir}/lib/%{name}
%ghost %attr(0660,gerbera,gerbera) %{_localstatedir}/lib/%{name}/config.xml
%ghost %attr(0750,gerbera,gerbera) %{_localstatedir}/lib/%{name}/%{name}.db
%ghost %attr(0660,gerbera,gerbera) %{_localstatedir}/lib/%{name}/%{name}.html

%changelog
