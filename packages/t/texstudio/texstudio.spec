#
# spec file for package texstudio
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


Name:           texstudio
Version:        4.4.0
Release:        0
Summary:        LaTeX Editor
License:        Apache-2.0 AND GPL-2.0-only AND GPL-3.0-only AND MPL-1.1
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://www.texstudio.org
Source0:        https://github.com/texstudio-org/texstudio/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(poppler-qt5)
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

%qmake5 CONFIG-=debug %{?crashhandler} texstudio.pro
%make_jobs

%install
make INSTALL_ROOT=%{buildroot} install

rm -f %{buildroot}%{_datadir}/texstudio/{AUTHORS,COPYING,CHANGELOG.txt}
%fdupes -s %{buildroot}%{_datadir}/texstudio/

%files
%license utilities/COPYING
%doc utilities/AUTHORS utilities/manual/CHANGELOG.txt
%{_bindir}/texstudio
%{_datadir}/texstudio/
%{_datadir}/applications/texstudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/texstudio.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/texstudio.metainfo.xml

%changelog
