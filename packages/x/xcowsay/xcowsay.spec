#
# spec file for package xcowsay
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


Name:           xcowsay
Version:        1.5.1
Release:        0
Summary:        Tool that displays a cow and message on the X11 desktop
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://www.doof.me.uk/xcowsay/
Source:         https://github.com/nickg/xcowsay/releases/download/r%{version}/xcowsay-%{version}.tar.gz
Source1:        xcowsay.desktop
Source2:        xcowsay.svg
Source3:        xcowhelp.desktop
Source4:        xcowhelp.svg
Source5:        xcowhelp
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       fortune
Requires:       gtk2

%description
xcowsay displays a cow and message on the X11 desktop.
Inspired by the original cowsay.

xcowsay includes all these amazing features:
- Fully configurable.
- Calculates display time from amount of text
- Dream mode — display images in the bubble
- Can draw thought and speech bubbles
- Daemon mode. Send your cow messages over DBus.
- Three different sized cows provided
- fortune(6) wrapper program - (unavailable temporarily)
- Replace the naffness that is xmessage(1)
- Should work with any window manager
- Supports UTF-8 characters properly
- Automatic word wrapping
- Use alternative non-cow images if you like

%prep
%setup -q

%build
%configure --enable-dbus
%make_build

%install
%make_install
%find_lang xcowsay
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -a %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -a %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
chmod +x %{SOURCE5}
cp -a %{SOURCE5} %{buildroot}%{_bindir}/
%suse_update_desktop_file -i xcowsay
%suse_update_desktop_file -i xcowhelp
rm %{buildroot}%{_datadir}/pixmaps/xcowhelp

%files -f xcowsay.lang
%license COPYING
%doc ChangeLog README AUTHORS
%{_bindir}/xcowdream
%{_bindir}/xcowsay
%{_bindir}/xcowthink
%{_bindir}/xcowfortune
%{_bindir}/xcowhelp
%{_mandir}/man6/xcowsay.6%{?ext_man}
%{_datadir}/xcowsay
%{_datadir}/applications/xcowhelp.desktop
%{_datadir}/applications/xcowsay.desktop
%{_datadir}/icons/hicolor/

%changelog
