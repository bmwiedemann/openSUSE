#
# spec file for package kde-cli-tools5
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


%define kf5_version 5.54.0
%bcond_without lang
Name:           kde-cli-tools5
Version:        5.20.0
Release:        0
Summary:        Additional CLI tools for KDE applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         kde-cli-tools-%{version}.tar.xz
%if %{with lang}
Source1:        kde-cli-tools-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE kdesu-add-some-i18n-love.patch -- boo#852256
Patch0:         kdesu-add-some-i18n-love.patch
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5Init) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Su) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
# Needs KWorkSpace::detectPlatform
BuildRequires:  cmake(LibKWorkspace) >= 5.12.4
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Svg) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
# for kquitapp5
Requires:       kdbusaddons-tools
%if %{with lang}
Recommends:     %{name}-lang
%endif
Requires(post):     update-alternatives
Requires(postun):   update-alternatives

%description
Additional CLI tools for KDE applications and workspaces.

%lang_package
%prep
%setup -q -n kde-cli-tools-%{version}
%autopatch -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %kf5_find_htmldocs
%endif

  # create a dummy target for /etc/alternatives/kdesu
  install -d -m 755 %{buildroot}%{_sysconfdir}/alternatives/
  touch %{buildroot}%{_sysconfdir}/alternatives/kdesu
  chmod +x %{buildroot}%{_sysconfdir}/alternatives/kdesu
  ln -s -f %{_sysconfdir}/alternatives/kdesu %{buildroot}%{_kf5_bindir}/kdesu
  touch %{buildroot}%{_sysconfdir}/alternatives/kdesu.1%{?ext_man}
  mv %{buildroot}%{_kf5_mandir}/man1/kdesu.1 %{buildroot}%{_kf5_mandir}/man1/kdesu-5.1
  ln -s -f %{_sysconfdir}/alternatives/kdesu.1%{?ext_man} %{buildroot}%{_kf5_mandir}/man1/kdesu.1%{?ext_man}

%post
/sbin/ldconfig
%if 0%{?suse_version} > 1320 || 0%{?is_opensuse}
%{_sbindir}/update-alternatives \
    --install %{_kf5_bindir}/kdesu kdesu %{_kf5_libexecdir}/kdesu 25 \
    --slave %{_kf5_mandir}/man1/kdesu.1.gz kdesu.1%{?ext_man} %{_kf5_mandir}/man1/kdesu-5.1%{?ext_man}
%else
%{_sbindir}/update-alternatives \
    --install %{_kf5_bindir}/kdesu kdesu %{_kf5_libexecdir}/kdesu 15 \
    --slave %{_kf5_mandir}/man1/kdesu.1.gz kdesu.1%{?ext_man} %{_kf5_mandir}/man1/kdesu-5.1%{?ext_man}
%endif

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove kdesu \
        %{_kf5_libexecdir}/kdesu
fi

%files
%license COPYING*
%{_kf5_bindir}/kdesu
%{_kf5_bindir}/kcmshell5
%{_kf5_bindir}/kdecp5
%{_kf5_bindir}/kde-inhibit
%{_kf5_bindir}/kdemv5
%{_kf5_bindir}/kde-open5
%{_kf5_bindir}/keditfiletype5
%{_kf5_bindir}/kioclient5
%{_kf5_bindir}/kmimetypefinder5
%{_kf5_bindir}/ksvgtopng5
%{_kf5_bindir}/kstart5
%{_kf5_bindir}/ktraderclient5
%{_kf5_bindir}/kbroadcastnotification
%{_kf5_servicesdir}/
%{_kf5_libexecdir}/
%{_kf5_applicationsdir}/org.kde.keditfiletype.desktop
%ghost %{_sysconfdir}/alternatives/kdesu
%{_kf5_plugindir}/
%ghost %{_sysconfdir}/alternatives/kdesu.1%{?ext_man}
%doc %{_kf5_htmldir}/en
%{_kf5_mandir}/man1/kdesu*.*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
