#
# spec file for package wlmaker
#
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>
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

# libbase is a utility library from the same upstream that is only used
# by this project and is statically linked into the build
%global libbase_commit a6c6a27e1f8fa2af3b36e9b2f60dbc0bfa0bcb0e
%global libbase_url https://github.com/phkaeser/libbase

%bcond docs 1

Name:           wlmaker
Version:        0.7.1
Release:        0
Summary:        Wayland compositor inspired by WindowMaker
License:        Apache-2.0
URL:            https://github.com/phkaeser/wlmaker
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{libbase_url}/archive/%{libbase_commit}/libbase-%{libbase_commit}.tar.gz

Patch0:         0001-remove-google-chrome.patch
Patch1:         0002-allow-for-config-in-usr-etc.patch

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  ghostscript-fonts
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  plantuml
%endif

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xwayland)

Recommends:     foot
Recommends:     firefox
Recommends:     wdisplays

%description
A Wayland compositor inspired by Window Maker

Key features:
  - Compositor for windows in stacking mode
  - Supports multiple workspaces
  - Appearance inspired by Window Maker, following the look and feel of
    NeXTSTEP
  - Easy to use, lightweight, low gimmicks and fast
  - Dock and clip, to be extended for dockable apps

%package        doc
Summary:        Developer documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
This package provides additional developer documentation for %{name}

%prep
%autosetup -p1 -b 1

# Drop bundled dependencies
rm -r dependencies

# Ensure libbase can be found; we move instead of symlinking because the
# build uses relative paths for the includes and that confuses things
rm -r submodules/libbase
mv ../libbase-%{libbase_commit}/ submodules/libbase

# Do not abort on warnings
sed -i 's/-Werror//' CMakeLists.txt submodules/libbase/CMakeLists.txt

%conf
%cmake -Dconfig_OPTIM=ON

%build
%make_build -C build
%if %{with docs}
%make_build -C build doc
%endif

%install
%make_install -C build
%if %{with docs}
# Changed to manual installation of docs, so fdupes picks them up
mkdir -p %{buildroot}%{_docdir}/wlmaker-doc
cp -r build/doc/html %{buildroot}%{_docdir}/wlmaker-doc/
%endif

%fdupes %{buildroot}

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/{%{name},%{name}.wlmclock,%{name}.wlmcpugraph,%{name}.wlmeyes,%{name}.wlmmemgraph,%{name}.wlmnetgraph}.desktop

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_bindir}/wlmclock
%{_bindir}/wlmeyes
%{_bindir}/wlmcpugraph
%{_bindir}/wlmmemgraph
%{_bindir}/wlmnetgraph
%{_bindir}/wlmtool
%{_datadir}/icons/hicolor/*/apps/
%{_datadir}/%{name}/icons/
%{_datadir}/wayland-sessions/
%{_distconfdir}/xdg/%{name}/
%{_datadir}/applications/

%if %{with docs}
%files doc
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md doc/ROADMAP.md build/doc/html/
%endif

%changelog

