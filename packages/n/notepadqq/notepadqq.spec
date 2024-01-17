#
# spec file for package notepadqq
#
# Copyright (c) 2021 SUSE LLC
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


Name:           notepadqq
Version:        2.0.0~20201022T180930.03cdde0
Release:        0
Summary:        Notepad++-like editor
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://notepadqq.com/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(uchardet)

%description
Text editor with support for multiple programming languages,
multiple encodings, and plugins.

%prep
%setup -q

find src/extension_tools/node_modules/ -type f -name '*.js' -exec sed -i '1s/^\(#!.\+\)env /\1/' {} \;
sed -i '1s/^\(#!.\+\)env /\1/' src/extension_tools/node_modules/shelljs/bin/shjs

pushd src/extension_tools/node_modules/archiver/node_modules
chmod 0755 tar-stream/node_modules/bl/test/sauce.js
chmod 0755 glob/node_modules/minimatch/node_modules/brace-expansion/test/generate.sh
popd
chmod 0644 src/editor/libs/codemirror/mode/sas/sas.js

# W: script-without-shebang
chmod -x src/editor/libs/throttle-debounce/*

%build
%qmake5 \
  PREFIX=%{_prefix} \
  QMAKE_CXXFLAGS="%{optflags}" \
  LRELEASE=%{_libqt5_bindir}/lrelease \
  notepadqq.pro
%make_build

%install
%qmake5_install
%suse_update_desktop_file -r %{name} Utility TextEditor

find %{buildroot}/ -name '.*' -print0 | xargs -0 rm -rf

sed -i '1 s|^#!%{_bindir}/env bash|#!%{_bindir}/bash|' %{buildroot}%{_datadir}/%{name}/extension_tools/node_modules/archiver/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/test/generate.sh

%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/notepadqq.appdata.xml

%changelog
