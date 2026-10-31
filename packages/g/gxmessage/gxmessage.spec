#
# spec file for package gxmessage
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gxmessage
Version:        4.1.1
Release:        0
Summary:        GTK-based xmessage clone
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gxmessage/
Source:         https://ftp.gnu.org/pub/gnu/gxmessage/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/gxmessage/%{name}-%{version}.tar.gz.sig
Source3:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4) >= 4.12

%description
Gxmessage opens a pop-up window to display a message obtained from the
command-line, from a file, or from stdin. The window can include a row of
user-defined buttons, each of which causes the program to exit with a different
return code.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%check
%make_build check

%files
%license COPYING COPYING.icon
%doc NEWS README TODO AUTHORS
%{_bindir}/gxmessage
%{_mandir}/man1/gxmessage.1%{?ext_man}
%{_infodir}/gxmessage.info%{?ext_info}
%{_datadir}/applications/com.dreamhosters.trmusson.Gxmessage.desktop
%{_datadir}/icons/hicolor/48x48/apps/com.dreamhosters.trmusson.Gxmessage.png
%{_datadir}/icons/hicolor/scalable/apps/com.dreamhosters.trmusson.Gxmessage.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.dreamhosters.trmusson.Gxmessage-symbolic.svg

%files lang -f %{name}.lang
%license COPYING

%changelog
