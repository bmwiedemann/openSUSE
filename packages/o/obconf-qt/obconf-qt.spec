#
# spec file for package obconf-qt
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


Name:           obconf-qt
Version:        0.16.0
Release:        0
Summary:        OpenBox window manager configuration tool
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
Requires(post): desktop-file-utils
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(pre):  desktop-file-utils
Recommends:     %{name}-lang
Conflicts:      obconf

%description
Configuration tool for the OpenBox Window Manager.
This tool is used by LXQt to configure OpenBox, since it is
used as the default WindowManager in LXQt.

%lang_package

%prep
%setup -q

%build
%cmake \
      -DUSE_QT5=ON \
      -DPULL_TRANSLATIONS=OFF
%make_jobs

%install
%cmake_install
install -dm 755 %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/obconf
ln -s %{_sysconfdir}/alternatives/obconf \
    %{buildroot}%{_bindir}/obconf

%find_lang %{name} --with-qt

%post
%{_sbindir}/update-alternatives --install \
    %{_bindir}/obconf \
    obconf \
    %{_bindir}/%{name} \
    40

%postun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove obconf \
        %{_bindir}/%{name}
fi

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/obconf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%ghost %{_sysconfdir}/alternatives/obconf

%files lang -f %{name}.lang 
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*

%changelog
