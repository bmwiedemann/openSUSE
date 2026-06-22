#
# spec file for package texstudio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           texstudio
Version:        4.9.5
Release:        0
Summary:        LaTeX Editor
License:        Apache-2.0 AND GPL-2.0-only AND GPL-3.0-only AND MPL-1.1
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://www.texstudio.org
Source0:        https://github.com/texstudio-org/texstudio/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(quazip1-qt6)
Requires:       hunspell
Requires:       texlive-latex

%description
TeXstudio is a program based on texmaker, that integrates many tools needed
to develop documents with LaTeX, in just one application. Using its editor
you can write your documents with the help of interactive spell checking,
syntax highlighting, automatically code completion and more.

%prep
%setup -q

%build
%ifarch aarch64 %{arm} s390x
%define crashhandler NO_CRASH_HANDLER=true
%endif

%cmake
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/metainfo
cp utilities/texstudio.metainfo.xml %{buildroot}%{_datadir}/metainfo/texstudio.metainfo.xml

rm -f %{buildroot}%{_datadir}/doc/texstudio/{AUTHORS,COPYING,CHANGELOG.txt}
%fdupes -s %{buildroot}%{_datadir}/texstudio/

%files
%license utilities/COPYING
%doc utilities/AUTHORS utilities/manual/CHANGELOG.txt
%{_bindir}/texstudio
%{_datadir}/texstudio
%{_datadir}/doc/texstudio
%{_datadir}/applications/texstudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/texstudio.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/texstudio.metainfo.xml

%changelog
