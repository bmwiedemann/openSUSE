#
# spec file for package fcitx5
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

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif

%if ! %{defined _environmentdir}
%define _environmentdir %{_prefix}/lib/environment.d
%endif

Name:           fcitx5
Version:        5.0.13
Release:        0
Summary:        Next generation of fcitx
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        en_dict-20121020.tar.gz
Source2:        https://raw.githubusercontent.com/fcitx/fcitx-artwork/master/logo/Fcitx.svg
Source3:        xim.d-fcitx5
Source4:        macros.fcitx5
Source100:      input-method.py3
Source101:      99-fcitx5.conf
Source102:      fcitx5.service
Patch0:         fcitx5-no-download.patch
Patch1:         fcitx5-gcc7.patch
Patch2:         fcitx5-5.0.13-memfd.patch
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  cairo-devel
BuildRequires:  cldr-emoji-annotation-devel
BuildRequires:  cmake
BuildRequires:  dbus-1-devel
BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  fmt-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc8-c++
%endif
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  iso-codes-devel
BuildRequires:  libevent-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libpresage-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  pango-devel
BuildRequires:  systemd-devel
BuildRequires:  update-desktop-files
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xcb-imdkit-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xkeyboard-config
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif
Provides:       fcitx = %{version}
Obsoletes:      fcitx <= 4.2.9.8
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
%systemd_requires

%description
Fcitx 5 is a generic input method framework.

%package devel
Summary:        Development files for fcitx5
Group:          Development/Libraries/C and C++
Requires:       fcitx5 = %{version}
Requires:       libFcitx5Config6 = %{version}
Requires:       libFcitx5Core7 = %{version}
Requires:       libFcitx5Utils2 = %{version}
Provides:       fcitx-devel = %{version}
Obsoletes:      fcitx-devel <= 4.2.9.8

%description devel
This package provides development files for fcitx5.

%package -n libFcitx5Config6
Summary:        Configuration library for fcitx5
Group:          System/Libraries
Provides:       libFcitx5Config5 = %{version}
Obsoletes:      libFcitx5Config5 < %{version}

%description -n libFcitx5Config6
This package provides configuration libraries for fcitx5.

%package -n libFcitx5Core7
Summary:        Core library for fcitx5
Group:          System/Libraries
Provides:       libfcitx-4_2_9 = %{version}
Obsoletes:      libfcitx-4_2_9 <= 4.2.9.8
Provides:       libFcitx5Core5 = %{version}
Obsoletes:      libFcitx5Core5 < %{version}

%description -n libFcitx5Core7
This package provides core libraries for fcitx5.

%package -n libFcitx5Utils2
Summary:        Utility library for fcitx5
Group:          System/Libraries
Provides:       libFcitx5Utils1 = %{version}
Obsoletes:      libFcitx5Utils1 < %{version}

%description -n libFcitx5Utils2
This package provides utility libraries for fcitx5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -r %{SOURCE1} src/modules/spell/dict/

%build
%if 0%{?suse_version} < 1550
export CC=%{_bindir}/gcc-8
export CXX=%{_bindir}/g++-8
%endif
%cmake -DENABLE_PRESAGE=On -DCMAKE_SKIP_RPATH=OFF -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%make_build

%install
%cmake_install
# recreate soft link
rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
ln -sf %{_datadir}/applications/org.fcitx.Fcitx5.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

# create autostart
mkdir -p %{buildroot}%{_distconfdir}/X11/xim.d/
install -m 644 %{SOURCE3} %{buildroot}%{_distconfdir}/X11/xim.d/fcitx5

priority=30
pushd  %{buildroot}%{_distconfdir}/X11/xim.d/
    for lang in am ar as bn el fa gu he hi hr ja ka kk kn ko lo ml my \
                pa ru sk vi zh_TW zh_CN zh_HK zh_SG \
                de fr it es nl cs pl da nn nb fi en sv ; do
        mkdir $lang
        pushd $lang
            ln -s ../fcitx5 $priority-fcitx5
        popd
    done
popd

# install environment generator for wayland
install -D -m 0755 %{SOURCE100} %{buildroot}%{_systemd_user_env_generator_dir}/99-fcitx5.py3
install -D -m 0644 %{SOURCE101} %{buildroot}%{_environmentdir}/99-fcitx5.conf
install -D -m 0644 %{SOURCE102} %{buildroot}%{_userunitdir}/fcitx5.service

# install icons
for i in 16 22 24 32 48 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/
  rsvg-convert -h $i -w $i %{SOURCE2} -o %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/fcitx.png
done
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fcitx.svg

# install desktop files
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/org.fcitx.Fcitx5.desktop Utility DesktopUtility
%suse_update_desktop_file -r fcitx5-configtool Settings DesktopSettings

# own directories
mkdir -p %{buildroot}%{_datadir}/fcitx5/inputmethod
mkdir -p %{buildroot}%{_libdir}/fcitx5/qt5

# install macros.fcitx5
install -Dm 0644 %{SOURCE4} %{buildroot}%{_prefix}/lib/rpm/macros.d/macros.fcitx5

%find_lang fcitx5
%fdupes %{buildroot}

%if 0%{?suse_version} >= 1550
%systemd_user_pre fcitx5.service
%systemd_user_post fcitx5.service
%systemd_user_preun fcitx5.service
%systemd_user_postun fcitx5.service
%else
%pre
if [ -x /usr/bin/systemctl ]; then
  if [ ! -e "/usr/lib/systemd/user/%{name}.service" ]; then
    mkdir -p /run/systemd/rpm/needs-user-preset
    touch "/run/systemd/rpm/needs-user-preset/%{name}.service"
  fi
fi
%post
if [ -x /usr/bin/systemctl ]; then
  if [ -e "/run/systemd/rpm/needs-user-preset/%{name}.service" ]; then
    /usr/bin/systemctl --global preset "%{name}.service" || :
    rm "/run/systemd/rpm/needs-user-preset/%{name}.service" || :
  fi
fi
%preun
if [ %{name}.service -eq 0 -a -x /usr/bin/systemctl ]; then
  /usr/bin/systemctl --global disable fcitx5.service || :
fi
%endif

%post -n libFcitx5Config6 -p /sbin/ldconfig
%post -n libFcitx5Core7 -p /sbin/ldconfig
%post -n libFcitx5Utils2 -p /sbin/ldconfig
%postun -n libFcitx5Config6 -p /sbin/ldconfig
%postun -n libFcitx5Core7 -p /sbin/ldconfig
%postun -n libFcitx5Utils2 -p /sbin/ldconfig

%files -f fcitx5.lang
%doc README.md
%license LICENSES
%dir %{_systemd_user_env_generator_dir}
%dir %{_environmentdir}
%{_distconfdir}/X11/xim.d/
%{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
%{_bindir}/fcitx5
%{_bindir}/fcitx5-configtool
%{_bindir}/fcitx5-remote
%{_bindir}/fcitx5-diagnose
%{_libdir}/fcitx5
%{_systemd_user_env_generator_dir}/99-fcitx5.py3
%{_environmentdir}/99-fcitx5.conf
%{_userunitdir}/fcitx5.service
%{_datadir}/applications/org.fcitx.Fcitx5.desktop
%{_datadir}/applications/fcitx5-configtool.desktop
%{_datadir}/fcitx5
%{_datadir}/icons/hicolor/*/apps/fcitx.*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.*
%{_datadir}/dbus-1/services/org.fcitx.Fcitx5.service
%{_datadir}/metainfo/org.fcitx.Fcitx5.metainfo.xml

%files devel
%{_prefix}/lib/rpm/macros.d/macros.fcitx5
%{_includedir}/Fcitx5
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5Config.so
%{_libdir}/libFcitx5Core.so
%{_libdir}/libFcitx5Utils.so
%{_libdir}/pkgconfig/Fcitx5*.pc

%files -n libFcitx5Config6
%{_libdir}/libFcitx5Config.so.6
%{_libdir}/libFcitx5Config.so.%{version}

%files -n libFcitx5Core7
%{_libdir}/libFcitx5Core.so.7
%{_libdir}/libFcitx5Core.so.%{version}

%files -n libFcitx5Utils2
%{_libdir}/libFcitx5Utils.so.2
%{_libdir}/libFcitx5Utils.so.%{version}

%changelog