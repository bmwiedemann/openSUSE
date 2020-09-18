#
# spec file for package highlight
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


%bcond_without gui
Name:           highlight
Version:        3.58
Release:        0
Summary:        Universal Source Code to Formatted Text Converter
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://www.andre-simon.de/
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
Source1:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2.asc
Source99:       highlight.keyring
# PATCH-FIX-OPENSUSE highlight-3.45-fix-doc-dir.patch
Patch0:         highlight-3.45-fix-doc-dir.patch
# PATCH-FIX-OPENSUSE highlight-3.58-use_optflags.patch
Patch1:         highlight-3.58-use_optflags.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  lua-devel

%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX, XML or ANSI
escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%if %{with gui}
%package gui
Summary:        Graphical Interface for %{name}
Group:          Development/Tools/Other
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  update-desktop-files
Requires:       %{name} = %{version}

%description gui
This package provides graphical interface for %{name}.

%lang_package -n highlight-gui

%endif

%prep
%autosetup -p1
dos2unix extras/pandoc/* extras/themes-resources/base16/*

%build
%make_build OPTFLAGS="%{optflags}" cli
%if %{with gui}
# Don't call gui and cli targets in the same make invocation
# as it leads to concurrency issues.
%make_build OPTFLAGS="%{optflags}" gui
%endif

%install
%makeinstall \
%if %{with gui}
  install-gui
%suse_update_desktop_file -G "Text converter" -r %{name} Utility TextEditor
%find_lang %{name} --with-qt
%endif

rm %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%{_bindir}/%{name}
%{_docdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/filetypes.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/langDefs
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/themes
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/filetypes.conf.5%{?ext_man}

%if %{with gui}
%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/gui_files
%dir %{_datadir}/%{name}/gui_files/ext
%{_datadir}/%{name}/gui_files/ext/fileopenfilter.conf
%{_datadir}/pixmaps/%{name}.xpm

%files gui-lang -f %{name}.lang
%dir %{_datadir}/%{name}/gui_files/l10n
%endif

%changelog
