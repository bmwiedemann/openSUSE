#
# spec file for package owncloud-client
#
# Copyright (c) 2020 SUSE LLC
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


Name:           owncloud-client

Version:        2.6.3.14058
Release:        0

Summary:        The ownCloud synchronization client
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://owncloud.org/download
Source0:        https://download.owncloud.com/desktop/stable/owncloudclient-%{version}.tar.xz
Source1:        https://download.owncloud.com/desktop/stable/owncloudclient-%{version}.tar.xz.asc
Source2:        101-sync-inotify.conf
Source3:        README.source

# PATCH-FIX-UPSTREAM fix position of systray menu https://github.com/owncloud/client/issues/5968
# for all except tumbleweed and ongoing, as the Qt bug is fixed in there.
Patch0:         fix-systray-menu-pos.patch
Patch1:         no_theme_icons.patch
Patch2:         fix-qpainterpath.patch

%define cmake_args -DSYSCONF_INSTALL_DIR=%{_sysconfdir}

# Build the dolphin overlays for 42.2 ongoing, SLE and Tumbleweed
%if 0%{?sle_version} > 120100 || %{?suse_version} > 1320
%define build_dolphin_overlays 1
%endif

# The client can be branded, not the case so far
%define has_branding 0

# The minimum required version of qtkeychain, stay with 0.4.0 for now
# to stay compatible with 13.2
%define keychain_version 0.4.0

######################################################################### BuildRequires only below here.

BuildRequires:  cmake >= 2.8.11
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qtkeychain-qt5-devel >= %{keychain_version}

BuildRequires:  libcloudproviders-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(zlib)

%if 0%{?build_dolphin_overlays}
BuildRequires:  kio-devel
%endif

BuildRequires:  libopenssl-devel
BuildRequires:  update-desktop-files

BuildRequires:  sqlite3-devel

BuildRequires:  hicolor-icon-theme

######################################################################### Requires only below here.

Suggests:       %{name}-nautilus
Supplements:    packageand(%{name}:nautilus)
Suggests:       %{name}-nemo

Requires:       %{name}-l10n
Requires:       libowncloudsync0 = %{version}

######################################################################### Obsoletes only below here.

Obsoletes:      libocsync-devel
Obsoletes:      libocsync-devel-doc
Obsoletes:      libocsync-doc
Obsoletes:      libocsync-plugin-owncloud
Obsoletes:      libocsync0

######################################################################### Package Descriptions start here.

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ownCloud sync client - github.com/owncloud/client

ownCloud client enables you to connect to your private
ownCloud Server. With it you can create folders in your home
directory, and keep the contents of those folders synced with your
ownCloud server. Simply copy a file into the directory and the
ownCloud Client does the rest.

ownCloud gives you anytime and anywhere access to the files you
need, whether through this desktop application, our mobile apps,
the web interface, or other WebDAV clients. With it, you can
easily view and share documents and information in a secure,
flexible and controlled architecture. You can extend ownCloud
with plug-ins from the community, or that you build yourself.

%package -n %{name}-doc
Summary:        Documentation for ownCloud
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-doc
Documentation for the ownCloud desktop application.

%package -n %{name}-l10n
Summary:        Localization for ownCloud
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-l10n
Localization files for the ownCloud desktop application.

%package -n libowncloudsync0
Requires:       libqt5keychain1 => %{keychain_version}

Summary:        The ownCloud synchronization library
Group:          Development/Libraries/C and C++

%description -n libowncloudsync0
The ownCloud synchronization library. It implements the ownCloud
sync algorithm that keeps a local directory in sync with the
content on your cloud.

%package -n libowncloudsync-devel
Summary:        Development files for the ownCloud synchronization library
Group:          Development/Libraries/C and C++
Requires:       libowncloudsync0 = %{version}

%description -n libowncloudsync-devel
Development files for the ownCloud synchronization library. It
implements the ownCloud sync algorithm that keeps a local directory
in sync with the content on your cloud.

%package -n %{name}-nautilus
Summary:        Nautilus overlay icons
Group:          Productivity/Networking/Other
Requires:       nautilus
Supplements:    packageand(%{name}:nautilus)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-nautilus

%description -n %{name}-nautilus
This package provides overlay icons to visualize the synchronization state
in the Nautilus file manager.

%package -n %{name}-nemo
Summary:        Nemo overlay icons
Group:          Productivity/Networking/Other
Requires:       nemo
Supplements:    packageand(%{name}:nemo)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python-nemo

%description -n %{name}-nemo
This package provides overlay icons to visualize the synchronization state
in the Nemo file manager.

%package -n %{name}-caja
Summary:        Caja overlay icons
Group:          Productivity/Networking/Other
Requires:       nemo
Supplements:    packageand(%{name}:caja}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python-caja

%description -n %{name}-caja
This package provides overlay icons to visualize the synchronization state
in the Caja file manager.

%if 0%{?build_dolphin_overlays}
%package -n %{name}-dolphin
Summary:        Dolphin overlay icons
Group:          Productivity/Networking/Other
Requires:       dolphin
Supplements:    packageand(%{name}:dolphin)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-dolphin
This package provides the necessary plugin libraries for the KDE
Framework 5 based Dolphin filemanager to display overlay icons.

%endif

%prep
%setup -q -n owncloudclient-%{version} 

%if 0%{?suse_version} <= 1500
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%build
# see README.source
rm -rf src/3rdparty/libcrashreporter-qt
rm -rf shell_integration/windows
rm -rf shell_integration/MacOSX

echo suse_version   0%{?suse_version}

# http://www.cmake.org/Wiki/CMake_RPATH_handling#Default_RPATH_settings
%cmake .. -DWITH_DOC=TRUE \
  -DKDE_INSTALL_USE_QT_SYS_PATHS=1 \
  -DCMAKE_C_FLAGS:STRING="%{optflags}" \
  -DCMAKE_CXX_FLAGS:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if %{_lib} == lib64
  -DLIB_SUFFIX=64 \
%endif
%if %{has_branding}
  -DOEM_THEME_DIR=$PWD/../ownCloud/syncclient \
%endif
  %cmake_args

# documentation here?
if [ -e conf.py ];
then
  # for old cmake versions we need to move the conf.py.
  mv conf.py doc/
fi

env LD_RUN_PATH=%{_libdir}/owncloud:%{_libdir}/owncloud make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

# Copy the source README here to be picked up by doc macro
cp %{SOURCE3} .

if [ -d %{buildroot}%{_mandir}/man1 ]; then
  gzip %{buildroot}%{_mandir}/man1/*.1
fi

%define extdir %{buildroot}%{_datadir}/nautilus-python/extensions
test -f %{extdir}/ownCloud.py  && mv %{extdir}/ownCloud.py  %{extdir}/owncloud.py  || true
test -f %{extdir}/ownCloud.pyo && mv %{extdir}/ownCloud.pyo %{extdir}/owncloud.pyo || true
test -f %{extdir}/ownCloud.pyc && mv %{extdir}/ownCloud.pyc %{extdir}/owncloud.pyc || true

# https://github.com/owncloud/client/issues/4107
install -m 0755 -D %{SOURCE2} %{buildroot}/etc/sysctl.d/101-sync-inotify.conf

%suse_update_desktop_file -n owncloud
# workaround for https://github.com/owncloud/ownbrander/issues/322
for desktop_icon_dir in $RPM_BUILD_ROOT/usr/share/icons/hicolor/*/apps; do
  # copy shortname to executable name, if missing.
  if [ -f $desktop_icon_dir/owncloud.png -a ! -f $desktop_icon_dir/owncloud.png ]; then
    cp $desktop_icon_dir/owncloud.png $desktop_icon_dir/owncloud.png
  fi
done

%post   -n libowncloudsync0 -p /sbin/ldconfig
%postun -n libowncloudsync0 -p /sbin/ldconfig

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root,-)
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/icons/hicolor
%{_datadir}/mime/packages/owncloud.xml
%{_libdir}/ownCloud/plugins/owncloudsync_vfs_suffix.so
%dir %{_libdir}/ownCloud/
%dir %{_libdir}/ownCloud/plugins
%doc CONTRIBUTING.md README.md 
%license COPYING COPYING.documentation

%config /etc/ownCloud
# https://github.com/owncloud/client/issues/4107
%config /etc/sysctl.d/101-sync-inotify.conf

%files -n %{name}-l10n
%defattr(-,root,root,-)
%{_datadir}/owncloud/

%files -n libowncloudsync0
%defattr(-,root,root,-)
%{_libdir}/libowncloudsync.so.*
%{_libdir}/libowncloud_csync.so.*

%files -n libowncloudsync-devel
%defattr(-,root,root,-)
%{_libdir}/libowncloudsync.so
%{_libdir}/libowncloud_csync.so
%{_includedir}/owncloudsync/

%files -n %{name}-nautilus
%defattr(-,root,root,-)
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/nautilus-python/extensions/syncstate*.py*
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions/

%files -n %{name}-nemo
%defattr(-,root,root,-)
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/nemo-python/extensions/syncstate*.py*
%dir %{_datadir}/nemo-python
%dir %{_datadir}/nemo-python/extensions/

%files -n %{name}-caja
%defattr(-,root,root,-)
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/caja-python/extensions/syncstate*.py*
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions/

%if 0%{?build_dolphin_overlays}
%files -n %{name}-dolphin
%defattr(-,root,root,-)
%{_libdir}/*dolphinpluginhelper.so
%{_libdir}/qt5/plugins/kf5/overlayicon/*dolphinoverlayplugin.so
%{_libdir}/qt5/plugins/*dolphinactionplugin.so

%{_datadir}/kservices5/*dolphinactionplugin.desktop
%dir %{_libdir}/qt5/plugins/kf5/overlayicon
%endif # build_dolphin_overlays

%changelog
