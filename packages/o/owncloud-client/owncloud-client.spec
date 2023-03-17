#
# spec file for package owncloud-client
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


%define cmake_args -DSYSCONF_INSTALL_DIR=%{_sysconfdir}

# The client can be branded, not the case so far
%define has_branding 0

# The minimum required version of qtkeychain, stay with 0.4.0 for now
# to stay compatible with 13.2
%define keychain_version 0.4.0

Name:           owncloud-client
Version:        3.2.0
Release:        0
Summary:        The ownCloud synchronization client
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://owncloud.org/download
Source0:        ownCloud_os-%{version}.tar.xz
Source2:        69-sync-inotify.conf
Source3:        README.source
Source4:        ownCloud.conf

######################################################################### BuildRequires only below here.

BuildRequires:  cmake >= 2.8.11
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(LibreGraphAPI)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain) >= %{keychain_version}
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

######################################################################### Requires only below here.

Suggests:       %{name}-nautilus
Supplements:    (%{name} and nautilus)
Suggests:       %{name}-nemo

Requires:       libowncloudsync0 = %{version}

######################################################################### Obsoletes only below here.

Obsoletes:      libocsync-devel
Obsoletes:      libocsync-devel-doc
Obsoletes:      libocsync-doc
Obsoletes:      libocsync-plugin-owncloud
Obsoletes:      libocsync0
Obsoletes:      owncloud-client-l10n

######################################################################### Package Descriptions start here.

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

%package -n libowncloudsync0
Summary:        The ownCloud synchronization library
Group:          Development/Libraries/C and C++
Requires:       libqt5keychain1 >= %{keychain_version}

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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus
Requires:       python3-nautilus
Supplements:    (%{name} and nautilus)

%description -n %{name}-nautilus
This package provides overlay icons to visualize the synchronization state
in the Nautilus file manager.

%package -n %{name}-nemo
Summary:        Nemo overlay icons
Group:          Productivity/Networking/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nemo
Requires:       python-nemo
Supplements:    (%{name} and nemo)

%description -n %{name}-nemo
This package provides overlay icons to visualize the synchronization state
in the Nemo file manager.

%package -n %{name}-caja
Summary:        Caja overlay icons
Group:          Productivity/Networking/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nemo
Requires:       python-caja
Supplements:    (%{name} and caja)

%description -n %{name}-caja
This package provides overlay icons to visualize the synchronization state
in the Caja file manager.

%package -n %{name}-dolphin
Summary:        Dolphin overlay icons
Group:          Productivity/Networking/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dolphin
Supplements:    (%{name} and dolphin)

%description -n %{name}-dolphin
This package provides the necessary plugin libraries for the KDE
Framework 5 based Dolphin filemanager to display overlay icons.

%prep
%autosetup -p1 -n ownCloud_os-%{version}

%build

echo suse_version   0%{?suse_version}

# http://www.cmake.org/Wiki/CMake_RPATH_handling#Default_RPATH_settings
%cmake -DWITH_DOC=TRUE \
  -DKDE_INSTALL_USE_QT_SYS_PATHS=1 \
  -DCMAKE_C_FLAGS:STRING="%{optflags}" \
  -DCMAKE_CXX_FLAGS:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
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
install -m 0644 -D %{SOURCE2} %{buildroot}/%{_sysctldir}/69-sync-inotify.conf
# do not allow to call home
install -m 0755 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/ownCloud/

%suse_update_desktop_file -n owncloud
# workaround for https://github.com/owncloud/ownbrander/issues/322
for desktop_icon_dir in %{buildroot}%{_datadir}/icons/hicolor/*/apps; do
  # copy shortname to executable name, if missing.
  if [ -f $desktop_icon_dir/owncloud.png -a ! -f $desktop_icon_dir/owncloud.png ]; then
    cp $desktop_icon_dir/owncloud.png $desktop_icon_dir/owncloud.png
  fi
done

%ldconfig_scriptlets -n libowncloudsync0

%files
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/mime/packages/owncloud.xml
%{_datadir}/cloud-providers/
%{_libdir}/qt5/plugins/owncloudsync_vfs_*.so
%if 0%{?suse_version} < 1550
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%endif
%doc CONTRIBUTING.md README.md
%license COPYING COPYING.documentation

%config %{_sysconfdir}/ownCloud
# https://github.com/owncloud/client/issues/4107
%{_sysctldir}/69-sync-inotify.conf

%files -n libowncloudsync0
%{_libdir}/libowncloudsync.so.*
%{_libdir}/libowncloud_csync.so.*
%{_libdir}/libowncloudResources.so.*

%files -n libowncloudsync-devel
%{_libdir}/libowncloudsync.so
%{_libdir}/libowncloud_csync.so
%{_libdir}/libowncloudResources.so
%dir %{_libdir}/cmake/ownCloud
%{_libdir}/cmake/ownCloud/ownCloud*.cmake
%{_includedir}/ownCloud

%files -n %{name}-nautilus
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/nautilus-python/extensions/syncstate*.py*
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions/

%files -n %{name}-nemo
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/nemo-python/extensions/syncstate*.py*
%dir %{_datadir}/nemo-python
%dir %{_datadir}/nemo-python/extensions/

%files -n %{name}-caja
# Fedora also has *.pyc and *.pyo files here.
%{_datadir}/caja-python/extensions/syncstate*.py*
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions/

%files -n %{name}-dolphin
%{_libdir}/*dolphinpluginhelper.so
%{_libdir}/qt5/plugins/kf5/overlayicon/*dolphinoverlayplugin.so
%{_libdir}/qt5/plugins/*dolphinactionplugin.so

%{_datadir}/kservices5/*dolphinactionplugin.desktop
%dir %{_libdir}/qt5/plugins/kf5/overlayicon

%changelog
