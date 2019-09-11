#
# spec file for package qputty-qt5
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

%define puttyvr 0.70
Name:           qputty-qt5
Version:        506
Release:        0
Summary:        A QT5 port of putty, the free telnet/ssh client
License:        MIT AND LGPL-3.0+
Group:          System/X11/Utilities
# original home page at http://qputty.sourceforge.net
URL:            https://github.com/dsmorozov/qputty-qt5
Source0:        https://github.com/dsmorozov/qputty-qt5/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://the.earth.li/~sgtatham/putty/latest/putty-%{puttyvr}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libgssglue)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
Conflicts:      qPutty

%description
A QT5 port of putty, the free telnet/ssh client.
Fork of the abandoned Qt4 qputty.

%prep
%setup -q -a 1
gzip -d < icons/qputty.svgz > icons/qputty.svg

%build
%qmake5 PUTTY_SRC_VERSION=%{puttyvr} PUTTY_HOME=putty-%{puttyvr} \
   PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install
install -Dm0644 icons/qputty.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qputty.svg
%suse_update_desktop_file -r qPutty "Qt Network RemoteAccess"

%files
%doc README.md LICENSE icons/COPYING-ICONS
%{_bindir}/qPutty
%{_datadir}/applications/qPutty.desktop
%{_datadir}/icons/hicolor/scalable/apps/qputty.svg

%changelog
