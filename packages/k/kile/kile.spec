#
# spec file for package kile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.9.92
Release:        0
Summary:        A LaTeX Source Editor and TeX Shell
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://kile.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/kile/unstable/kile-3.0b2/kile-%{version}.tar.bz2
# Patches from v3.0b2..09910015
Patch001:       0001-Silence-CMake-s-CMP0071-policy-warning.patch
# Patch002 contains binary data, not supported
Patch003:       0003-Remove-X-DBUS-StartupType-from-desktop-file.patch
Patch004:       0004-GIT_SILENT-made-messages-after-extraction.patch
Patch005:       0005-Fix-minor-EBN-issues.patch
Patch006:       0006-Fix-minor-EBN-issues.patch
Patch007:       0007-GIT_SILENT-made-messages-after-extraction.patch
Patch008:       0008-no-op-open-save-.ui-files.patch
Patch009:       0009-Use-KMessageWidget-in-PostscriptDialog.patch
Patch010:       0010-Fix-minor-EBN-issues.patch
Patch011:       0011-Fix-minor-EBN-issues-explicit-normalize.patch
Patch012:       0012-GIT_SILENT-made-messages-after-extraction.patch
Patch013:       0013-i18n-fix-few-string-puzzles.patch
Patch014:       0014-User-menu-do-not-attempt-to-load-an-empty-file-name.patch
Patch015:       0015-Fix-minor-typo.patch
Patch016:       0016-GIT_SILENT-made-messages-after-extraction.patch
Patch017:       0017-SVN_SILENT-made-messages-.desktop-file-always-resolv.patch
Patch018:       0018-no-need-to-declare-void-functions-with-no-parameters.patch
Patch019:       0019-Fix-tab-icons-for-informing-the-user-of-clandestine-.patch
Patch020:       0020-Use-more-functor-based-signal-slot-connections-in-Ki.patch
Patch021:       0021-Search-for-the-file_save_copy_as-action-inside-KText.patch
Patch022:       0022-Fix-Appstreamercli-minor-issues.patch
Patch023:       0023-GIT_SILENT-made-messages-after-extraction.patch
Patch024:       0024-GIT_SILENT-made-messages-after-extraction.patch
Patch025:       0025-GIT_SILENT-made-messages-after-extraction.patch
Patch026:       0026-GIT_SILENT-made-messages-after-extraction.patch
Patch027:       0027-actually-initialize-kcrash-properly.patch
Patch028:       0028-GIT_SILENT-made-messages-after-extraction.patch
Patch029:       0029-GIT_SILENT-made-messages-after-extraction.patch
Patch030:       0030-GIT_SILENT-made-messages-after-extraction.patch
Patch031:       0031-GIT_SILENT-made-messages-after-extraction.patch
Patch032:       0032-GIT_SILENT-made-messages-after-extraction.patch
Patch033:       0033-GIT_SILENT-made-messages-after-extraction.patch
Patch034:       0034-Avoid-crashing-when-closing-a-document-that-is-being.patch
Patch035:       0035-GIT_SILENT-made-messages-after-extraction.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  khtml-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kinit-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  okular-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core) >= 5.7
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       konsole-part
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
Obsoletes:      kile5 <= %{version}
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
%autosetup -p1 -n kile-%{version}

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
%{_datadir}/kile/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_datadir}/doc/kile/
%{_kf5_htmldir}/en/kile/
%{_kf5_bindir}/kile
%{_libdir}/libkdeinit5_kile.so
%{_kf5_applicationsdir}/org.kde.kile.desktop
%{_kf5_configkcfgdir}/
%{_kf5_dbusinterfacesdir}/net.sourceforge.kile.main.xml
%{_datadir}/kconf_update/
%{_datadir}/mime/packages/kile.xml
%{_kf5_debugdir}/kile.categories
%{_kf5_appstreamdir}/org.kde.kile.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
