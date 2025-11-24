#
# spec file for package golly
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           golly
Version:        5.0
Release:        0
Summary:        Tool for exploring Game of Life and other automata
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
URL:            https://golly.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source1:        %{name}.desktop
BuildRequires:  SDL2-devel
BuildRequires:  c++_compiler
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  wxGTK3-devel >= 3.1.5
BuildRequires:  zlib-devel
Requires:       %{name}-assets = %{version}
Requires:       python3 >= 3.3

%description
Key features:
- Supports both bounded and unbounded universes.
- Supports various topologies (plane, torus, Klein bottle, etc.).
- Supports multi-state universes (cells can have up to 256 states).
- Includes the QuickLife algorithm.
- Uses the HashLife algorithm to see large patterns evolve at huge time scales.
- Supports many different rules, including Wolfram's 1D rules, WireWorld, Generations, and John von Neumann's 29-state CA.
- Uses the RuleLoader algorithm to load custom rules.
- Reads RLE, macrocell, Life 1.05/1.06, dblife, and MCell files.
- Can also read common graphic formats: BMP, PNG, GIF, TIFF.
- Can extract patterns, scripts and rules from zip files.
- Downloads files from online archives.
- Includes a pattern collection.
- Paste in patterns from the clipboard.
- Unlimited undo/redo.
- Unbounded zooming out for astronomical patterns.
- Auto fit option keeps a generating pattern within view.
- Full screen option (no menu/status/tool/scroll bars).
- Supports multiple layers, including cloned layers.
- HTML-based help with an integrated Life Lexicon.
- Scriptable via Lua or Python.
- User-configurable keyboard shortcuts.

%package assets
Summary:        Assets for %{name}
Group:          Amusements/Toys/Graphics
BuildArch:      noarch

%description assets
This package contains assets for %{name}: Help, rules, patterns and scripts.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains header files and libraries needed to develop applications
that use %{name}.

%prep
%setup -q -n %{name}-%{version}-src
rm -v {Help/Lexicon/modify.pl,docs/Build.html}

%build
%set_build_flags
export GOLLYDIR=%{_datadir}/%{name}
cd gui-wx
%make_build -f makefile-gtk

%install
install -D -m 0755 bgolly golly -t %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
for i in Help Patterns Rules Scripts; do
  find ./$i -type d -exec chmod 755 {} \;
  find ./$i -type f -exec chmod 644 {} \;
  cp -a $i %{buildroot}%{_datadir}/%{name}/$i
done
install -D -m 0644 gui-wx/icons/appicon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications
%fdupes %{buildroot}%{_datadir}
chrpath --delete %{buildroot}%{_bindir}/*golly

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license docs/License.html
%doc docs/ReadMe.html docs/ToDo.html
%{_bindir}/*%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%files assets
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/Rules/TableGenerators
%exclude %{_datadir}/%{name}/Rules/TreeGenerators

%files devel
%{_datadir}/%{name}/Rules/TableGenerators
%{_datadir}/%{name}/Rules/TreeGenerators

%changelog
