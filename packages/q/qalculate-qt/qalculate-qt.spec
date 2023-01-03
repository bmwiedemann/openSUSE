#
# spec file for package qalculate-qt
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


Name:           qalculate-qt
Version:        4.5.0
Release:        0
Summary:        Multi-purpose cross-platform desktop calculator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://qalculate.github.io
Source0:        https://github.com/Qalculate/qalculate-qt/releases/download/v%{version}/qalculate-qt-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
# compilation fails on 5.12.x
BuildRequires:  pkgconfig(Qt5Core) >= 5.15.0
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libqalculate) >= %{version}
BuildRequires:  pkgconfig(libxml-2.0)

%description
Qalculate! is a multi-purpose cross-platform desktop calculator. It is
simple to use but provides power and versatility normally reserved for
complicated math packages, as well as useful tools for everyday needs
(such as currency conversion and percent calculation). Features include a
large library of customizable functions, unit calculations and conversion,
symbolic calculations (including integrals and equations), arbitrary
precision, uncertainty propagation, interval arithmetic, plotting, and a
user-friendly interface (QT, GTK+ and CLI).

%prep
%autosetup -p1

%build
%qmake5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%qmake5_install

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/io.github.Qalculate.qalculate-qt.desktop
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/qalculate-qt.png
%dir %{_datadir}/icons/hicolor/22x22
%dir %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/qalculate-qt.png
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/qalculate-qt.png
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%{_datadir}/icons/hicolor/64x64/apps/qalculate-qt.png
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/qalculate-qt.png
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/qalculate-qt.svg
%{_mandir}/man?/%{name}.?%{ext_man}
%{_datadir}/metainfo/io.github.Qalculate.qalculate-qt.metainfo.xml
%dir %{_datadir}/qalculate-qt
%dir %{_datadir}/qalculate-qt/translations
%{_datadir}/qalculate-qt/translations/qalculate-qt_ca.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_de.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_es.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_fr.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_nl.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_pt_BR.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_ru.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_sl.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_sv.qm
%{_datadir}/qalculate-qt/translations/qalculate-qt_zh_CN.qm

%changelog
