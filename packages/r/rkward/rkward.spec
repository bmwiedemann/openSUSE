#
# spec file for package rkward
#
# Copyright (c) 2025 SUSE LLC
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
Version:        0.8.2
Release:        0
Summary:        Graphical frontend for R language
Summary(fr):    Interface graphique pour le langage R
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://rkward.kde.org/
Source0:        https://files.kde.org/rkward/testing/for_packaging/rkward-%{version}.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-fortran
BuildRequires:  gettext
BuildRequires:  kf6-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6BreezeIcons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
Recommends:     kate-plugins
Suggests:       kbibtex
Suggests:       pandoc
# rkward needs the R-base version it was compiled with - boo#993268
%requires_eq    R-base
Conflicts:      rkward

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

%lang_package

%prep
%autosetup -p1 -n rkward-%{version}

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_kf6
%{kf6_build}

%install
%{kf6_install}

%suse_update_desktop_file -n org.kde.rkward

%find_lang rkward %{?no_lang_C}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%ctest

%files -f rkward.lang
%doc README TODO AUTHORS
%doc %{_kf6_mandir}/man1/rkward.1.gz
%dir %{_kf6_sharedir}/doc/HTML/en/rkwardplugins
%doc %{_kf6_sharedir}/doc/HTML/en/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/en/rkwardplugins/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/en/rkwardplugins/menu_hierarchy_example.png
%doc %{_kf6_sharedir}/doc/HTML/en/rkwardplugins/t_test_plugin_example.png
%doc %{_kf6_sharedir}/doc/HTML/ca/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/ca/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/ca/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/ca/rkwardplugins/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/en/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/en/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/it/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/it/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/nl/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/nl/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/nl/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/nl/rkwardplugins/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/sl/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/sl/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/sl/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/sl/rkwardplugins/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/sv/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/sv/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/sv/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/sv/rkwardplugins/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/uk/rkward/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/uk/rkward/index.docbook
%doc %{_kf6_sharedir}/doc/HTML/uk/rkwardplugins/index.cache.bz2
%doc %{_kf6_sharedir}/doc/HTML/uk/rkwardplugins/index.docbook
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.rkward.desktop
%{_datadir}/metainfo/org.kde.rkward.metainfo.xml
%{_kf6_sharedir}/icons/hicolor/16x16/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/22x22/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/32x32/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/48x48/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/64x64/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/128x128/apps/rkward.png
%{_kf6_sharedir}/icons/hicolor/scalable/apps/rkward.svgz
%{_kf6_sharedir}/ktexteditor_snippets/
%{_kf6_bindir}/rkward*
%if %{pkg_vcmp kf6-filesystem >= 20220307}
%{_libexecdir}/rkward.rbackend
%else
%{_kf6_libdir}/libexec/
%endif
%{_kf6_sharedir}/rkward/
%{_datadir}/kio/servicemenus/rkward.protocol
%{_libdir}/librkward.rbackend.lib.so
%{_kf6_sharedir}/mime/packages/vnd.kde.rkward-output.xml
%{_kf6_sharedir}/mime/packages/vnd.kde.rmarkdown.xml
%{_kf6_sharedir}/mime/packages/vnd.rkward.r.xml
%dir %{_datadir}/doc/HTML/ca/rkward
%dir %{_datadir}/doc/HTML/ca/rkwardplugins
%dir %{_datadir}/doc/HTML/en/rkward
%dir %{_datadir}/doc/HTML/it/rkward
%dir %{_datadir}/doc/HTML/nl/rkward
%dir %{_datadir}/doc/HTML/nl/rkwardplugins
%dir %{_datadir}/doc/HTML/sl/rkward
%dir %{_datadir}/doc/HTML/sl/rkwardplugins
%dir %{_datadir}/doc/HTML/sv/rkward
%dir %{_datadir}/doc/HTML/sv/rkwardplugins
%dir %{_datadir}/doc/HTML/uk/rkward
%dir %{_datadir}/doc/HTML/uk/rkwardplugins
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%{_datadir}/locale/ca/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/ca/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/de/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/eo/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/es/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/et/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/eu/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/eu/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/fi/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/fr/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/gl/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/he/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/it/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/ka/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/nl/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/pl/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/pt/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/ru/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/sl/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/sv/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/tr/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__analysis.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__data.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__distributions.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__embedded.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__graphics_device.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__import_export.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__item_response_theory.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__pages.mo
%{_datadir}/locale/uk/LC_MESSAGES/rkward__plots.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/rkward__graphics_device.mo
%{_mandir}/ca/man1/rkward.1%{?ext_man}
%{_mandir}/de/man1/rkward.1%{?ext_man}
%{_mandir}/it/man1/rkward.1%{?ext_man}
%{_mandir}/nl/man1/rkward.1%{?ext_man}
%{_mandir}/sl/man1/rkward.1%{?ext_man}
%{_mandir}/sv/man1/rkward.1%{?ext_man}
%{_mandir}/uk/man1/rkward.1%{?ext_man}

%changelog
