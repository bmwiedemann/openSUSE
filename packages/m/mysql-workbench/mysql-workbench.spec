#
# spec file for package mysql-workbench
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define edition community
Name:           mysql-workbench
Version:        8.0.15
Release:        0
Summary:        A MySQL visual database modeling, administration and querying tool
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          Productivity/Databases/Clients
Url:            http://wb.mysql.com
Source:         http://dev.mysql.com/get/Downloads/MySQLGUITools/%{name}-%{edition}-%{version}-src.tar.gz
Source1:        openSUSE_Vendor_Package.xml
Source2:        %{name}-%{edition}-%{version}-prebuilt_parsers.tar.gz
Source99:       %{name}.rpmlintrc
#Patches
Patch0:         patch-desktop-categories.patch
# Remove check for update in help
Patch1:         mysql-workbench-no-check-for-updates.patch
# disabled , system scintila is buil with gtk3
Patch7:         mysql-workbench-unbundle-libscintilla.patch
Patch8:         mysql-workbench-preload-sqlparser.patch
# patch from https://bugs.mysql.com/bug.php?id=84886
Patch11:        git_patch_105207009.patch
Patch13:        mysql-workbench-mariadb.patch
# PATCH-FIX-UPSTREAM guillaume@opensuse.org
Patch14:        fix_aarch64_build.patch
# PATCH-FIX-OPENSUSE allow to both support keyring and start without it
Patch15:        mysql-workbench-keyring-check.patch
# PATCH-FIX-OPENSUSE fix build with MariaDB
Patch16:        mysql-workbench-mariadb-8.0.15.patch
# PATCH-FIX-UPSTREAM fix include path for old JDBC api with new mysql-connector-cpp
Patch17:        mysql-workbench-old-api.patch
# PATCH-FIX-UPSTREAM fix warning interpreted as errors
Patch18:        mysql-workbench-warnings-fix.patch
# PATCH-FIX-OPENSUSE disable parser building (while we have no maven in OBS)
Patch19:        mysql-workbench-prebuilt-parsers.patch
# PATCH-FIX-OPENSUSE fix License.txt location
Patch20:        mysql-workbench-license-location.patch
# PATCH-FIX-UPSTREAM fix HiDPI support
Patch21:        mysql-workbench-hidpi.patch
BuildRequires:  Mesa-devel
BuildRequires:  ant
BuildRequires:  binutils-gold
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  freetds-devel
BuildRequires:  gcc-c++
BuildRequires:  gnome-keyring-devel
BuildRequires:  gtkmm3-devel
BuildRequires:  libantlr4-runtime-devel >= 4.7.2
BuildRequires:  libmysqlclient-devel
BuildRequires:  libmysqlcppconn-devel >= 1.1.8
BuildRequires:  libmysqld-devel > 5.1
BuildRequires:  libscintilla-devel
BuildRequires:  libsigc++2-devel
BuildRequires:  libtool
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-paramiko
BuildRequires:  swig
BuildRequires:  tinyxml-devel
BuildRequires:  unixODBC-devel
BuildRequires:  update-desktop-files
BuildRequires:  vsqlite++-devel
BuildRequires:  pkgconfig(cairo) >= 1.5.12
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libctemplate)
#BuildRequires:  pkgconfig(libglade-2.0)
#BuildRequires:  pkgconfig(libgnome-2.0)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libssh) >= 0.8.5
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       libmysqlclient-devel
Requires:       proj
Requires:       python-paramiko
Requires:       python-pexpect
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Suggests:       gnome-keyring
Suggests:       mysqldump
Conflicts:      mysql-workbench-com-se
Conflicts:      mysql-workbench-oss
Provides:       mysql-administrator = %{version}
Provides:       mysql-gui-tools = %{version}
Provides:       mysql-querybrovser = %{version}
Provides:       mysql-workbench-%{edition}
Obsoletes:      mysql-administrator < %{version}
Obsoletes:      mysql-gui-tools < %{version}
Obsoletes:      mysql-querybrovser < %{version}
ExcludeArch:    %arm %ix86
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif

%description
MySQL Workbench is a modeling tool that allows you to design
and generate MySQL databases graphically. It also has administration
and query development modules where you can manage MySQL server instances
and execute SQL queries.
This is the %{edition} build.

%prep
# Add the -D flag if you don't want to delete the source root on each build
%setup -q -n %{name}-%{edition}-%{version}-src
%setup -q -D -T -b 2 -n %{name}-%{edition}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch7 -p1
%patch8 -p1
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
export CFLAGS="%{optflags}"
%define __builder ninja
# build will fail if -Werror is used on recent complires
sed -i "s|-Werror||g" CMakeLists.txt
# fix building on Leap
truncate -s0 library/base/boost_fix.cpp
%cmake \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -Wl,-fuse-ld=gold -pie" \
  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -Wl,-fuse-ld=gold -pie" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -Wl,-fuse-ld=gold -pie" \
  -DMYSQL_CONFIG_PATH=%{_bindir}/mysql_config \
  -DCMAKE_BUILD_TYPE=%{edition} \
  -DREAL_EXECUTABLE_DIR=%{_libdir}/%{name} \
  -DUSE_UNIXODBC=TRUE
%cmake_build

%install
%cmake_install

find %{buildroot}%{_libdir}/%{name} -name \*.a  -exec rm {} \; -print
find %{buildroot} -type f -name "*.la" -delete -print

install -m 0644 "%{SOURCE1}" %{buildroot}%{_datadir}/mysql-workbench/mysql.profiles

mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf
chmod 644 %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf

rm -r %{buildroot}%{_datadir}/mime-info

rm -r %{buildroot}%{_datadir}/doc/mysql-workbench

# Check for duplicate files
%fdupes -s %{buildroot}

%post
/sbin/ldconfig
%icon_theme_cache_post
%mime_database_post
%desktop_database_post

%postun
/sbin/ldconfig
%icon_theme_cache_postun
%mime_database_postun
%desktop_database_postun

%files
%defattr(0644, root, root, 0755)
%license License.txt
%doc README.md AUTHORS ChangeLog
%attr(0755,root,root) %{_bindir}/mysql*
%attr(0755,root,root) %{_bindir}/wbcopytables
%attr(0755,root,root) %{_libdir}/%{name}/%{name}-bin
%attr(0755,root,root) %{_libdir}/%{name}/wbcopytables-bin
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/*
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*
%dir %{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%attr(0755,root,root) %{_datadir}/%{name}/extras/*.sh
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}.conf

%changelog
