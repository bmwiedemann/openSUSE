#
# spec file for package wxmp3gain
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wxmp3gain
Version:        4.0
Release:        0
Summary:        Front-end for mp3gain based on wxWidgets
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://wxmp3gain.sourceforge.io
Source0:        https://sourceforge.net/projects/wxmp3gain/files/%{version}/wxmp3gain-%{version}-src.tar.gz
# PATCH-FEATURE-OPENSUSE wxmp3gain-docs.patch aloisio@gmx.com -- do not install docs
Patch1:         wxmp3gain-docs.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
Requires:       mp3gain

%description
A front-end for mp3gain based on the wxWidgets toolkit.

%lang_package

%prep
%autosetup -p1

dos2unix docs/AUTHORS docs/CHANGELOG docs/README docs/TODO

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file %{name} AudioVideoEditing

%files
%doc docs/AUTHORS docs/CHANGELOG docs/README docs/TODO
%license docs/COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/resource
%{_datadir}/%{name}/resource/*.ico
%{_datadir}/%{name}/resource/toolbar

%files lang
%dir %{_datadir}/%{name}/resource/msg
%dir %{_datadir}/%{name}/resource/msg/cs
%dir %{_datadir}/%{name}/resource/msg/de
%dir %{_datadir}/%{name}/resource/msg/es
%dir %{_datadir}/%{name}/resource/msg/hr_HR
%dir %{_datadir}/%{name}/resource/msg/pt_BR
%dir %{_datadir}/%{name}/resource/msg/ru
%dir %{_datadir}/%{name}/resource/msg/tr
%lang(cs) %{_datadir}/%{name}/resource/msg/cs/%{name}.mo
%lang(de) %{_datadir}/%{name}/resource/msg/de/%{name}.mo
%lang(es) %{_datadir}/%{name}/resource/msg/es/%{name}.mo
%lang(hr) %{_datadir}/%{name}/resource/msg/hr_HR/%{name}.mo
%lang(pt) %{_datadir}/%{name}/resource/msg/pt_BR/%{name}.mo
%lang(ru) %{_datadir}/%{name}/resource/msg/ru/%{name}.mo
%lang(tr) %{_datadir}/%{name}/resource/msg/tr/%{name}.mo

%changelog
