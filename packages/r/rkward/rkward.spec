#
# spec file for package rkward
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


Name:           rkward
Version:        0.7.1b
Release:        0
Summary:        Graphical frontend for R language
Summary(fr):    Interface graphique pour le langage R
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://rkward.kde.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  gettext
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdewebkit-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  knotifications-devel
BuildRequires:  kparts-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
# rkward needs the R-base version it was compiled with - boo#993268
%requires_eq    R-base

%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%description -l fr
RKWard fournis un environnement de développement graphique intégré
aisément extensible et simple d'utilisation. RKWard tente de
combiner la puissance du langage R et la (relative) simplicité d'utilisation
des outils statistiques commerciaux. L'objectif à long terme est de voir son
intégration dans les suites bureautiques.

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DNO_R_XML=1
%make_jobs

%install
%make_install -C build

%suse_update_desktop_file -n org.kde.rkward

%find_lang %{name}

%files -f %{name}.lang
%doc README TODO AUTHORS
%doc %{_kf5_mandir}/man1/rkward.1.gz
%dir %{_kf5_sharedir}/doc/HTML/en/rkwardplugins
%doc %{_kf5_sharedir}/doc/HTML/en/rkwardplugins/index.cache.bz2
%doc %{_kf5_sharedir}/doc/HTML/en/rkwardplugins/index.docbook
%doc %{_kf5_sharedir}/doc/HTML/en/rkwardplugins/menu_hierarchy_example.png
%doc %{_kf5_sharedir}/doc/HTML/en/rkwardplugins/t_test_plugin_example.png
%license COPYING
%{_kf5_applicationsdir}/org.kde.rkward.desktop
%{_kf5_appstreamdir}/org.kde.rkward.appdata.xml
%{_kf5_sharedir}/icons/hicolor/16x16/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/22x22/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/32x32/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/48x48/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/64x64/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/128x128/apps/rkward.png
%{_kf5_sharedir}/icons/hicolor/scalable/apps/rkward.svgz
%{_kf5_bindir}/rkward*
%{_kf5_libdir}/libexec/
%{_kf5_sharedir}/rkward/
%{_kf5_servicesdir}/rkward.protocol
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?sle_version} >= 120300)
# we have the syntax-highlighting framework since Leap 42.3
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting/syntax
%{_kf5_sharedir}/org.kde.syntax-highlighting/syntax/rkward.xml
%else
%dir %{_kf5_sharedir}/katepart5
%dir %{_kf5_sharedir}/katepart5/syntax
%{_kf5_sharedir}/katepart5/syntax/rkward.xml
%endif
%{_kf5_sharedir}/mime/packages/vnd.rkward.r.xml

# language files

%dir %{_kf5_sharedir}/rkward/po/
%lang(ca) %{_kf5_sharedir}/rkward/po/ca/
%lang(es) %{_kf5_sharedir}/rkward/po/es/
%lang(gl) %{_kf5_sharedir}/rkward/po/gl/
%lang(nl) %{_kf5_sharedir}/rkward/po/nl/
%lang(pl) %{_kf5_sharedir}/rkward/po/pl/
%lang(pt) %{_kf5_sharedir}/rkward/po/pt/
%lang(pt_BR) %{_kf5_sharedir}/rkward/po/pt_BR/
%lang(sv) %{_kf5_sharedir}/rkward/po/sv/
%lang(uk) %{_kf5_sharedir}/rkward/po/uk/
%lang(x-test) %{_kf5_sharedir}/rkward/po/x-test/

%doc %lang(en) %{_kf5_sharedir}/doc/HTML/en/rkward/

%changelog
