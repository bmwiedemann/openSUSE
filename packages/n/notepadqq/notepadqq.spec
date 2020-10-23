#
# spec file for package notepadqq
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


Name:           notepadqq
Version:        1.4.8
Release:        0
Summary:        Notepad++-like editor
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://notepadqq.com/
Source:         https://github.com/notepadqq/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.3
BuildRequires:  pkgconfig(Qt5Gui) >= 5.3
BuildRequires:  pkgconfig(Qt5Network) >= 5.3
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.3
BuildRequires:  pkgconfig(Qt5Svg) >= 5.3
BuildRequires:  pkgconfig(Qt5Test) >= 5.3
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.3
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.3
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.3

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

%build
%qmake5 \
  PREFIX=%{_prefix} \
  QMAKE_CXXFLAGS="%{optflags}" \
  LRELEASE=%{_libqt5_bindir}/lrelease \
  notepadqq.pro
make %{?_smp_mflags} V=1

%install
%qmake5_install
%suse_update_desktop_file -r %{name} Utility TextEditor

find %{buildroot}/ -name '.*' -print0 | xargs -0 rm -rf

sed -i '1 s|^#!%{_bindir}/env bash|#!%{_bindir}/bash|' %{buildroot}%{_datadir}/%{name}/extension_tools/node_modules/archiver/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/test/generate.sh

%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%if 0%{?suse_version} < 1500
%dir %{_datadir}/metainfo/
%endif
%{_datadir}/metainfo/notepadqq.appdata.xml

%changelog
