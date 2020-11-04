#
# spec file for package fcitx-ui-light
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fcitx-ui-light
Version:        0.1.3
Release:        0
Summary:        Light Weight UI for Fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-ui-light
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fcitx-ui-light provides an alternative light weight UI for Fcitx, only using Xpm and Xft.
if you are not a light weight desktop environment user, strongly recommends you to use the normal "fcitx" package.

%prep
%setup -q

%build
%cmake
%make_jobs
%install
%cmake_install

%if 0%{?suse_version}
%suse_update_desktop_file fcitx-light Utility DesktopUtility
%endif
%if 0%{?fedora_version}
desktop-file-install --add-category="Utility" --delete-original --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/fcitx-light.desktop
%endif

%find_lang fcitx-light-ui

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f fcitx-light-ui.lang
%defattr(-,root,root)
%{_libdir}/fcitx/fcitx-light-ui.so
%{_datadir}/applications/fcitx-light.desktop
%{_datadir}/fcitx/addon/fcitx-light-ui.conf
%{_datadir}/fcitx/configdesc/fcitx-light-ui.desc

%changelog
