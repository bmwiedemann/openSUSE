#
# spec file for package notepadqq
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


%define qt6_version 6.4.0

Name:           notepadqq
Version:        2.1.1
Release:        0
Summary:        Notepad++-like editor
License:        GPL-3.0-or-later
URL:            https://notepadqq.com/
Source0:        https://github.com/notepadqq/notepadqq/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(uchardet)
ExclusiveArch:  %{x86_64} aarch64 riscv64

%description
Text editor with support for multiple programming languages,
multiple encodings, and plugins.

%prep
%autosetup -p1

find src/extension_tools/node_modules/ -type f -name '*.js' -exec sed -i '1s/^\(#!.\+\)env /\1/' {} \;
sed -i '1s/^\(#!.\+\)env /\1/' src/extension_tools/node_modules/shelljs/bin/shjs
sed -i '1 s|^#!%{_bindir}/env bash|#!%{_bindir}/bash|' src/extension_tools/node_modules/archiver/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/test/generate.sh

chmod 0644 src/editor/libs/codemirror/mode/sas/sas.js

# W: script-without-shebang
chmod -x src/editor/libs/throttle-debounce/*

%build
%cmake_qt6 \
  -DCMAKE_SKIP_RPATH:BOOL=TRUE

%qt6_build

%install
%qt6_install

find %{buildroot} -name '.*' -print0 | xargs -0 rm -r

pushd %{buildroot}%{_datadir}/notepadqq/extension_tools/node_modules
chmod 0755 \
  archiver/node_modules/async/support/sync-package-managers.js \
  archiver/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/test/generate.sh \
  archiver/node_modules/tar-stream/node_modules/bl/test/sauce.js \
  shelljs/bin/shjs \
  shelljs/scripts/generate-docs.js \
  shelljs/scripts/run-tests.js
popd

%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_bindir}/notepadqq
%{_datadir}/notepadqq/
%{_datadir}/applications/notepadqq.desktop
%{_datadir}/icons/hicolor/*/apps/notepadqq.*
%{_datadir}/metainfo/com.notepadqq.Notepadqq.metainfo.xml
%{_mandir}/man1/notepadqq.1%{?ext_man}

%changelog
