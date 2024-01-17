#
# spec file for package ktikz
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


Name:           ktikz
Version:        0.13.2
Release:        0
Summary:        Create TikZ diagrams for your publications
License:        GPL-2.0-or-later
URL:            https://github.com/fhackenberger/ktikz
Source0:        https://github.com/fhackenberger/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(poppler-qt5)
Requires:       ktexteditor
Recommends:     poppler-tools

%description
KtikZ is a small application helping you to create TikZ (from the LaTeX pgf
package) diagrams for your publications. It requires qt5, libpoppler, LaTeX
(pdflatex), the LaTeX preview-latex-style package and pgf itself. For
the eps export functionality you also need the poppler-tools package.

%prep
%setup -q

%build
%cmake_kf5
%cmake_build

%install
%make_install
%suse_update_desktop_file %{name} Graphics Viewer
%find_lang %{name}

%post
update-mime-database %{_datadir}/mime

%postun
update-mime-database %{_datadir}/mime

%files -f %{name}.lang
%license LICENSE.GPL2
%doc Changelog TODO README.md HACKING PACKAGING
%doc %lang(en) %{_kf5_htmldir}/en/ktikz/
%{_kf5_bindir}/ktikz
%{_kf5_plugindir}/ktikzpart.so
%{_kf5_applicationsdir}/ktikz.desktop
%{_kf5_iconsdir}/hicolor/*/apps/ktikz.*
%{_kf5_appstreamdir}/ktikz.appdata.xml
%{_kf5_sharedir}/ktikzpart/
%{_kf5_sharedir}/ktikz/
%{_kf5_sharedir}/config.kcfg/
%{_kf5_sharedir}/kxmlgui5/ktikz/
%{_kf5_servicesdir}/ktikzpart.desktop
%{_kf5_mandir}/man1/ktikz.1.gz
%{_datadir}/mime/packages/ktikz.xml

%changelog
