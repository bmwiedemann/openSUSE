#
# spec file for package tint2
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tint2
Version:        17.0.2
Release:        0
Summary:        A lightweight X11 desktop panel and task manager
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://gitlab.com/o9000/tint2
Source0:        https://gitlab.com/o9000/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:        tint2conf.1
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%description
tint2 is a simple panel/taskbar made for modern X window managers. It was
specifically made for Openbox3 but should also work with other window managers.

%lang_package

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}
%cmake_build

%install
%cmake_install

# create tint2 config directory
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/tint2/

desktop-file-install	\
	--set-key=NoDisplay  --set-value=true	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2.desktop

desktop-file-install	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2conf.desktop

# install man page for tint2conf (written for Debian package)
install -m 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/

%find_lang tint2conf

%files
%license COPYING
%doc AUTHORS CONTRIBUTING.md ChangeLog README.md
%doc %{_defaultdocdir}/tint2/
%dir %{_sysconfdir}/skel/.config/
%dir %{_sysconfdir}/xdg/tint2
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_sysconfdir}/skel/.config/tint2/
%{_bindir}/tint2
%{_bindir}/tint2conf
%{_datadir}/tint2/
%{_datadir}/applications/tint2conf.desktop
%{_datadir}/applications/tint2.desktop
%{_datadir}/icons/hicolor/*/apps/tint*
%{_datadir}/mime/packages/tint2conf.xml
%{_mandir}/man1/tint*.1%{?ext_man}

%files lang -f tint2conf.lang

%changelog
