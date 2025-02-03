#
# spec file for package kile
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2009 Johannes Engel <jcnengel@googlemail.com>
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kile
Version:        2.9.95git.20250201T013505~e5dac14
Release:        0
Summary:        A LaTeX Source Editor and TeX Shell
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kile
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Okular6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(poppler-qt6)
Requires:       konsole-part
Requires:       okular
Requires:       texlive-context
Requires:       texlive-latex
Requires:       texlive-tex-bin
Requires:       texlive-xetex
Recommends:     ImageMagick
Recommends:     dblatex
Recommends:     ghostscript-library
Recommends:     kbibtex
Recommends:     latex2html
Recommends:     lilypond
Recommends:     psutils
Recommends:     texlive-dvipdfmx
Recommends:     texlive-dvips
Recommends:     texlive-ling-macros
Recommends:     texlive-metapost
Recommends:     texlive-pdfsync
Recommends:     texlive-tex4ht
Recommends:     texlive-tree-dvips
Recommends:     zip
Suggests:       texlive-doc
Suggests:       texlive-latex-doc

%description
Kile is a TeX/LaTeX editor by KDE.

The main features are:

 * Compile, convert and view your document with one click.
 * Auto-completion of (La)TeX commands.
 * Templates and wizards make starting a new document very little work.
 * Easy insertion of many standard tags and symbols and the option to define
   (an arbitrary number of) user defined tags.
 * Inverse and forward search: click in the DVI viewer and jump to the
   corresponding LaTeX line in the editor, or jump from the editor to the
   corresponding page in the viewer.
 * Finding chapter or sections is very easy, Kile constructs a list of all the
   chapter etc. in your document. You can use the list to jump to the
   corresponding section.
 * Collect documents that belong together into a project.
 * Easy insertion of citations and references when using projects.
 * Flexible and smart build system to compile your LaTeX documents.
 * QuickPreview, preview a selected part of your document.
 * Easy access to various help sources.
 * Advanced editing commands.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Packaged with %%doc
rm -r %{buildroot}%{_kf6_sharedir}/doc/kile

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}

%files
%license COPYING*
%doc README README.cwl kile-remote-control.txt
%doc %{_kf6_htmldir}/en/kile/
%{_kf6_applicationsdir}/org.kde.kile.desktop
%{_kf6_appstreamdir}/org.kde.kile.appdata.xml
%{_kf6_bindir}/kile
%{_kf6_configkcfgdir}/kile.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.kile.main.xml
%{_kf6_debugdir}/kile.categories
%dir %{_kf6_iconsdir}/hicolor/150x150
%dir %{_kf6_iconsdir}/hicolor/150x150/apps
%dir %{_kf6_iconsdir}/hicolor/310x310
%dir %{_kf6_iconsdir}/hicolor/310x310/apps
%dir %{_kf6_iconsdir}/hicolor/44x44
%dir %{_kf6_iconsdir}/hicolor/44x44/apps
%{_kf6_iconsdir}/hicolor/*/apps/kile.*
%{_kf6_iconsdir}/hicolor/*/actions/*
%{_kf6_sharedir}/kconf_update/*
%{_kf6_sharedir}/kile/
%{_kf6_sharedir}/mime/packages/kile.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kile/

%changelog
