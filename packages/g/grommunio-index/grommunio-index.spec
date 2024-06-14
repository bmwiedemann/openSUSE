#
# spec file for package grommunio-index
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


Name:           grommunio-index
Version:        1.0.6.f40d25b
Release:        0
Summary:        Generator for grommunio-web search indexes
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         %name-%version.tar.xz
BuildRequires:  cmake
%if 0%{?suse_version} && 0%{?suse_version} < 1550
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version}
BuildRequires:  libmysqlclient-devel >= 5.6
%else
BuildRequires:  mariadb-devel >= 5.6
%endif
BuildRequires:  libexmdbpp-devel >= 1.8.0
BuildRequires:  libexmdbpp0 >= 1.8.0
BuildRequires:  pkgconfig(libHX) >= 3.27
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
Requires:       libexmdbpp0 >= 1.8.0
%if 0%{?suse_version} >= 1500
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
%endif
Requires(pre):  group(groweb)
Requires(pre):  group(gromoxcf)
Requires:       group(gromoxcf)
Requires:       group(groweb)
Requires:       user(groindex)
%define services grommunio-index.service grommunio-index.timer

%description
A C++17 program for the generation of grommunio-web fulltext search indexes.

%prep
%autosetup -p1

%build
>user.pre
%if 0%{?suse_version} >= 1500
%sysusers_generate_pre %_sourcedir/system-user-groindex.conf user system-user-groindex.conf
%endif

pushd .
%if 0%{?suse_version} && 0%{?suse_version} < 1550
%cmake -DCMAKE_CXX_COMPILER=%_bindir/g++-11
%else
%cmake
%endif
%cmake_build
popd

%install
pushd .
%cmake_install
popd
mkdir -p "%buildroot/%_datadir/%name"

%pre -f user.pre
%if 0%{?rhel} || 0%{?fedora_version}
getent group groindex >/dev/null || %_sbindir/groupadd -r groindex
getent passwd groindex >/dev/null || %_sbindir/useradd -g groindex -s /bin/false \
        -r -c "user for %name" -d / groindex
usermod groindex -aG groweb
usermod groindex -aG gromoxcf
%endif
%if 0%{?service_add_pre:1}
%service_add_pre %services
%endif

%post
find /var/lib/grommunio-web/sqlite-index/ -mindepth 1 "(" -type d -o -type f ")" -exec chmod g+w,o-w {} + || :
find /var/lib/grommunio-web/sqlite-index/ -mindepth 1 "(" -type d -o -type f ")" -exec chgrp -h groweb {} + || :
%if 0%{?service_add_post:1}
%service_add_post %services
%else
%systemd_post %services
%endif

%preun
%if 0%{?service_del_preun:1}
%service_del_preun %services
%else
%systemd_preun %services
%endif

%postun
%if 0%{?service_del_postun:1}
%service_del_postun %services
%else
%systemd_postun_with_restart %services
%endif

%files
%_bindir/grommunio-index*
%_datadir/%name/
%_sysusersdir/*.conf
%_unitdir/*
%license LICENSE.txt

%changelog
