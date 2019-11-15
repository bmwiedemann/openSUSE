#
# spec file for package kile
#
# Copyright (c) 2019 SUSE LLC.
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


%bcond_without lang
Name:           kile
Version:        2.9.93
Release:        0
Summary:        A LaTeX Source Editor and TeX Shell
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://kile.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/kile/unstable/kile-3.0b3/kile-%{version}.tar.bz2
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  okular-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.7
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(poppler-qt5)
Requires:       konsole-part
Requires:       okular
Requires:       texlive-context
Requires:       texlive-latex
Requires:       texlive-xetex
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     ImageMagick
Recommends:     dblatex
Recommends:     ghostscript-library
Recommends:     kbibtex
Recommends:     latex2html
Recommends:     lilypond
Recommends:     psutils
Recommends:     texlive-dvipdfmx
Recommends:     texlive-dvips
Recommends:     texlive-metapost
Recommends:     texlive-pdfsync
Recommends:     texlive-tex4ht
Recommends:     zip
Suggests:       aspell
Suggests:       texlive-doc
Suggests:       texlive-latex-doc
# was in Factory for a short while, in version 2.9.92
Provides:       kile5 = %{version}
Obsoletes:      kile5 < %{version}

%description
Kile is a user-friendly TeX/LaTeX editor by KDE.

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
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%if %{with lang}
  %find_lang %{name} --all-name
  %{kf5_find_htmldocs}
%endif

%suse_update_desktop_file -r org.kde.kile Qt KDE Office WordProcessor
%fdupes %{buildroot}

%files
%license COPYING*
%doc README
%dir %{_kf5_iconsdir}/hicolor/150x150
%dir %{_kf5_iconsdir}/hicolor/150x150/apps
%dir %{_kf5_iconsdir}/hicolor/310x310
%dir %{_kf5_iconsdir}/hicolor/310x310/apps
%dir %{_kf5_iconsdir}/hicolor/44x44
%dir %{_kf5_iconsdir}/hicolor/44x44/apps
%{_kf5_applicationsdir}/org.kde.kile.desktop
%{_kf5_appstreamdir}/org.kde.kile.appdata.xml
%{_kf5_bindir}/kile
%{_kf5_configkcfgdir}/
%{_kf5_dbusinterfacesdir}/net.sourceforge.kile.main.xml
%{_kf5_debugdir}/kile.categories
%{_kf5_htmldir}/en/kile/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_sharedir}/doc/kile/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kile/
%{_kf5_sharedir}/mime/packages/kile.xml
%{_libdir}/libkdeinit5_kile.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
