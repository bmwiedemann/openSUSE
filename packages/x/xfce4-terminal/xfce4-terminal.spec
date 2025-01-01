#
# spec file for package xfce4-terminal
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Guido Berhoerster.
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


%bcond_with git
Name:           xfce4-terminal
Version:        1.1.4
Release:        0
Summary:        Terminal Emulator for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/X11/Terminals
URL:            https://docs.xfce.org/apps/terminal/start
Source0:        https://archive.xfce.org/src/apps/xfce4-terminal/1.1/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE relax-x11-version.patch lower required X11 version to allow building for Leap which only has 1.6.5, which is enough, though
Patch1:         relax-x11-version.patch
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.7.0
BuildRequires:  pkgconfig(libpcre2-8) >= 10.00
BuildRequires:  pkgconfig(libxfce4kbd-private-3) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.17.5
BuildRequires:  pkgconfig(libxfconf-0) >= 4.16.0
BuildRequires:  pkgconfig(vte-2.91) >= 0.51.3
BuildRequires:  pkgconfig(x11) >= 1.6.5
Recommends:     %{name}-lang

%description
xfce4-terminal is a lightweight and easy to use terminal emulator for the Xfce
desktop environment. Its major features include a simple configuration
interface, the ability to use multiple tabs with terminals within a single
window, the possibility to have a pseudo-transparent terminal background, and a
compact mode where both the menubar and the window decorations are hidden which
helps to save space on the desktop.

%lang_package

%prep
%autosetup -p1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --with-utempter
%else
%configure \
    --with-utempter
%endif
%make_build

%install
%make_install

# create a list of localized man directories, these need to be owned
(
    printf '%%%%defattr(-,root,root)\n'
    cd '%{buildroot}'
    for dir in ".%{_mandir}/"*; do
        [ -d "${dir}" ] || continue
        case ${dir##*/} in
            man*)   continue ;;
            *)      lang="${dir##*/}"
                    printf "%%%%dir %%%%lang(%%s) %%s\n" "${lang}" "${dir#.}"
                    for subdir in "${dir}/"*; do
                        [ -d "${subdir}" ] || continue
                        printf "%%%%dir %%%%lang(%%s) %%s\n" "${lang}" \
                            "${subdir#.}"
                    done
                    ;;
        esac
    done
) >> %{name}.lang

# Fix name issue with xfce4-terminal-settings desktop file name entries boo#1125146
desktop-file-edit %{buildroot}%{_datadir}/applications/%{name}-settings.desktop --set-name='Xfce Terminal Settings'

%find_lang %{name} --with-man %{?no_lang_C}

%files
%doc AUTHORS HACKING NEWS README.md THANKS
%license COPYING
%{_bindir}/xfce4-terminal
%dir %{_datadir}/xfce4
%{_datadir}/xfce4/terminal
%{_datadir}/icons/hicolor/*/apps/org.xfce.terminal*
%{_datadir}/applications/xfce4-terminal.desktop
%{_datadir}/applications/xfce4-terminal-settings.desktop
%{_mandir}/man1/xfce4-terminal.1*

%files lang -f %{name}.lang

%changelog
