#
# spec file for package libqt4-sql-plugins
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
# nodebuginfo


%if 0%{?suse_version} >= 1330
%bcond_with mysql
%else
%bcond_without mysql
%endif

Name:           libqt4-sql-plugins
BuildRequires:  alsa-devel
BuildRequires:  cups-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(gl)
%if %{with mysql}
BuildRequires:  libmysqlclient-devel
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  libnsl-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  unixODBC-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Summary:        Qt 4 SQL related libraries
License:        SUSE-LGPL-2.1-with-digia-exception-1.1 OR GPL-3.0-only
Group:          System/Libraries
Url:            http://qt.digia.com/
# COMMON-VERSION-BEGIN
# COMMON-VERSION-BEGIN
%define base_name libqt4
%define tar_version everywhere-opensource-src-%{version}
Version:        4.8.7
Release:        0
# COMMON-VERSION-END
# COMMON-VERSION-END
BuildRequires:  libqt4-devel >= %{version}
# COMMON-BEGIN
# COMMON-BEGIN
Source:         http://download.qt-project.org/official_releases/qt/4.8/%{version}/qt-%{tar_version}.tar.gz
# to get mtime of file:
Source1:        libqt4.changes
Source2:        baselibs.conf
Source3:        macros.qt4
Source10:       qt4config.desktop
Source11:       designer4.desktop
Source12:       linguist4.desktop
Source13:       assistant4.desktop
Source14:       assistant.png
Source15:       designer.png
Source16:       linguist.png
Source17:       qt_lt.ts

Patch2:         qt-never-strip.diff
Patch3:         plastik-default.diff
Patch6:         use-freetype-default.diff
Patch8:         link-tools-shared.diff
Patch39:        0191-listview-alternate-row-colors.diff
Patch40:        0188-fix-moc-parser-same-name-header.diff
Patch43:        0195-compositing-properties.diff
Patch60:        0180-window-role.diff
Patch61:        qt4-fake-bold.patch
Patch70:        0225-invalidate-tabbar-geometry-on-refresh.patch
Patch75:        qt-debug-timer.diff
Patch87:        qfatal-noreturn.diff
Patch101:       no-moc-date.diff
Patch107:       webkit-ia64_s390x.patch
Patch109:       libqt4-libtool-nodate.diff
Patch113:       ppc64-webkit-link-fix.diff
Patch118:       rcc-stable-dirlisting.diff
Patch119:       hppa_ldcw_fix.diff
Patch120:       hppa_unaligned_access_fix_458133.diff
Patch123:       use-cups-default-print-settings-bnc552218.diff
Patch128:       build-qvfb-tool.diff
Patch131:       disable-im-for-password.diff
Patch136:       handle-tga-files-properly.diff
Patch137:       qdbusconnection-no-warning-output.patch
# PATCH-FIX-UPSTREAM  fix_assistant_segfault_QTBUG-25324.patch [bnc#780763] [QTBUG#25324]
Patch140:       fix_assistant_segfault_QTBUG-25324.patch
# PATCH-FIX-OPENSUSE  fix build on s390x failing to link in qnetworkconfigmanager.o
Patch141:       qt4-fix-s390x-build.diff
Patch149:       qatomic-generic.patch
# PATCH-FEATURE-OPENSUSE QSystemTrayicon.diff -- adds support for sni-qt plugin, which allows Qt applications to communicate via KStatusNotifier spec -- needed for
# Plasma Next
Patch150:       QSystemTrayicon.diff
Patch152:       fix-moc-from-choking-on-boost-headers.patch
# PATCH-FIX-OPENSUSE qlocale_icu-no-warning-output.patch -- qWarnings about icu libraries and symbols are now only emmited in debug builds
Patch153:       qlocale_icu-no-warning-output.patch
# PATCH-FIX-OPENSUSE kde4_qt_plugin_path.patch
Patch154:       kde4_qt_plugin_path.patch
Patch160:       ppc64le.diff
# LO filepicker integration (3 patches)
# PATCH-FIX-OPENSUSE exclude socket notifiers from the glib event loop - needed for LO KDE4 filepicker integration (1/3)
Patch162:       glib-honor-ExcludeSocketNotifiers-flag.diff
# PATCH-FIX-OPENSUSE fix recursive repaint errors which lead to crashes - needed for LO KDE4 filepicker integration (2/3)
Patch163:       qtcore-4.8.5-qeventdispatcher-recursive.patch
# PATCH-FIX-OPENSUSE fix clipboard delay when pasting with LO and KFileDialog open - needed for LO KDE4 filepicker integration (3/3)
Patch164:       l-qclipboard_delay.patch
# PATCH-FIX-OPENSUSE fix_qrasterpixmapdata_bnc847880.diff -- fix image rect copy optimization that copied "garbage" when used in qemu/cirrus (bnc#847880)
Patch165:       fix_qrasterpixmapdata_bnc847880.diff
# PATCH-FIX-UPSTREAM 0001-Fix-exclusion-of-anonymous-ciphers.patch -- Exclude more ciphers from being used by default
Patch166:       0001-Fix-exclusion-of-anonymous-ciphers.patch
# PATCH-FIX-OPENSUSE disable-insecure-ciphers-bnc865241.diff -- Disable insecure ciphers (rc4, aecdh, adh, exp-adh, <128 bits)
Patch167:       disable-rc4-ciphers-bnc865241.diff
# PATCH-FIX-OPENSUSE fix-gcc6-detection.diff -- Fix GCC6 detection
Patch168:       fix-gcc6-detection.diff
# PATCH-FIX-UPSTREAM fix-moc-parsing-with-glibc-2.25.patch -- Fixes moc parsing correctly glibc 2.25 system headers
Patch169:       fix-moc-parsing-with-glibc-2.25.patch
# PATCH-FIX-OPENSUSE fix-build-icu59.patch -- Workaround C++11 requirement
Patch170:       fix-build-icu59.patch
# PATCH-FIX-UPSTREAM fix bolder fonts in qt4 apps [boo#956357] [QTBUG#27301]
Patch171:       fix-medium-font.diff
# PATCH-FIX-OPENSUSE no-ssl3.patch
Patch200:       no-ssl3.patch
# PATCH-FIX-OPENSUSE qt4-openssl-1.1.0pre-3.patch
Patch201:       qt4-openssl-1.1.0pre-3.patch
# PATCH-FIX-OPENSUSE qt-everywhere-opensource-src-4.8.7-openssl.patch
Patch202:       qt-everywhere-opensource-src-4.8.7-openssl.patch
# PATCH-FIX-OPENSUSE libqt4-toplevel-asm.patch
Patch203:       libqt4-toplevel-asm.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
  %define common_options --opensource -fast -no-separate-debug-info -shared -xkb -openssl-linked -xrender -xcursor -dbus-linked -xfixes -xrandr -xinerama -sm -no-nas-sound -no-rpath -system-libjpeg -system-libpng -accessibility -cups -stl -nis -system-zlib -prefix /usr -L %{_libdir} -libdir %{_libdir} -docdir %_docdir/%{base_name} -examplesdir %{_libdir}/qt4/examples -demosdir %{_libdir}/qt4/demos -plugindir %plugindir -translationdir %{_datadir}/qt4/translations -iconv -sysconfdir /etc/settings -datadir %{_datadir}/qt4/ -no-pch -reduce-relocations -exceptions -system-libtiff -glib -optimized-qmake -no-webkit -no-xmlpatterns -system-sqlite -qt3support -no-sql-mysql -importdir %plugindir/imports  -xsync -xinput -gtkstyle
%define check_config \
  grep '# define' src/corelib/global/qconfig.h | egrep -v 'QT_(ARCH|USE)';             \
  if test -f %{_datadir}/qt4/mkspecs/qconfig.pri ; then                                 \
    diff -u %{_datadir}/qt4/mkspecs/qconfig.pri mkspecs/qconfig.pri || exit 1;           \
  fi                                                                                   \

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.
# COMMON-END
# COMMON-DESC-BEGIN
%package -n libqt4-sql-unixODBC
Summary:        Qt 4 unixODBC plugin
Group:          Development/Libraries/C and C++
Requires:       libqt4-sql = %{version}
Provides:       libqt4_sql_backend = %{version}
Obsoletes:      qt-sql-unixODBC < 4.6.0
Provides:       qt-sql-unixODBC = 4.6.0

%description -n libqt4-sql-unixODBC
Qt unixODBC plugin to support databases via unixODBC within Qt
applications.

%package -n libqt4-sql-postgresql
Summary:        Qt 4 PostgreSQL plugin
Group:          Development/Libraries/C and C++
Requires:       libqt4-sql = %{version}
Provides:       libqt4_sql_backend = %{version}
Obsoletes:      qt-sql-postgresql < 4.6.0
Provides:       qt-sql-postgresql = 4.6.0

%description -n libqt4-sql-postgresql
Qt SQL plugin to support PostgreSQL servers in Qt applications.

%package -n libqt4-sql-mysql
Summary:        Qt 4 MySQL support
Group:          Development/Libraries/C and C++
Requires:       libqt4-sql = %{version}
Provides:       libqt4_sql_backend = %{version}
Obsoletes:      qt-sql-mysql < 4.6.0
Provides:       qt-sql-mysql = 4.6.0

%description -n libqt4-sql-mysql
A plugin to support MySQL server in Qt applications.
# COMMON-DESC-END
# COMMON-PREP-BEGIN
%prep
%define plugindir %{_libdir}/qt4/plugins
%setup -q -n qt-%tar_version
%patch2
%patch3
%patch6
# needs rediffing
#%patch8
%patch39
%patch40
%patch43
%patch60
# bnc#374073 comment #8
#%patch61
%patch70
%patch75
%patch87
%patch101
# ### 48 rediff
#%patch107
%patch109
# ### 48 rediff
#%patch113
%patch118 -p1
%ifarch hppa
%patch119
%patch120
%endif
%patch123
cp %{SOURCE17} translations/
%patch128
%patch131 -p1
%patch136
%patch137
%patch140 -p1
%patch141 -p0
%patch149 -p1
%patch150 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch160
%patch162 -p1
%patch163 -p0
%patch164
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%if 0%{?suse_version} >= 1330
%patch200 -p1
%patch201 -p1
%patch202 -p1
%endif
%patch203

# be sure not to use them
rm -rf src/3rdparty/{libjpeg,freetype,libpng,zlib,libtiff,fonts}
# COMMON-PREP-END
# COMMON-PREP-END

%build
export QTDIR=$PWD
export PATH=$PWD/bin:$PATH
export LD_LIBRARY_PATH=$PWD/lib/
%ifarch ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
export MAKEFLAGS="%{?_smp_mflags}"
%ifarch sparc64
platform="-platform linux-g++-64"
%else
platform=""
%endif
echo yes | ./configure %common_options $platform \
   -no-webkit -no-xmlpatterns -nomake examples \
   -plugin-sql-psql -I/usr/include -I/usr/include/pgsql/ -I/usr/include/pgsql/server \
%if %{with mysql}
   -plugin-sql-mysql -I/usr/include/mysql/ \
%else
   -no-sql-mysql \
%endif
   -no-sql-sqlite -no-sql-sqlite2 \
   -plugin-sql-odbc

rpm -ql libqt4-devel | grep %{_bindir}/ | sed 's#%{_bindir}/##' | \
    ( while read file; do test -e bin/$file || ln -s %{_bindir}/$file bin/ ; done )
rpm -ql libqt4-devel | grep %{_libdir}/lib | sed 's#%{_libdir}/##' | \
    ( while read file; do test -e lib/$file || ln -s %{_libdir}/$file lib/ ; done )
make %{?_smp_mflags} -C src/sql
make %{?_smp_mflags} -C src/plugins/sqldrivers

%install
export QTDIR=$PWD
make INSTALL_ROOT=%{buildroot} -C src/sql install
make INSTALL_ROOT=%{buildroot} -C src/plugins/sqldrivers install

# argggh, qmake is such a piece of <censored>
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
find  %{buildroot}/%{_libdir} -type f -name '*.pc' -exec mv {} %{buildroot}/%{_libdir}/pkgconfig \;
# fix more qmake errors
mkdir -p %{buildroot}/%{_libdir}/qt
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}/%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
rm -rf %{buildroot}%{_prefix}/include
rm -rf %{buildroot}%{_libdir}/pkgconfig
mkdir %{buildroot}/%{_libdir}/backup
mv %{buildroot}/%{_libdir}/libQtSql*.so.* %{buildroot}/%{_libdir}/backup
rm -f %{buildroot}/%{_libdir}/lib*
mv %{buildroot}/%{_libdir}/backup/libQtSql*.so.* %{buildroot}/%{_libdir}
rmdir %{buildroot}/%{_libdir}/backup
rm -rf %{buildroot}%{_prefix}/bin
for i in %{buildroot}/%plugindir/*; do
  case "$i" in
    *sqldriv*): ;;
    *) rm -rf $i
  esac
done
rm -f %{buildroot}/%{_libdir}/libQtSql*

%files -n libqt4-sql-unixODBC
%defattr(-,root,root,755)
%dir %plugindir/sqldrivers
%plugindir/sqldrivers/libqsqlodbc*.so

%files -n libqt4-sql-postgresql
%defattr(-,root,root,755)
%dir %plugindir/sqldrivers
%plugindir/sqldrivers/libqsqlpsql*.so

%if %{with mysql}
%files -n libqt4-sql-mysql
%defattr(-,root,root,755)
%dir %plugindir/sqldrivers
%plugindir/sqldrivers/libqsqlmysql*.so
%endif

%changelog
