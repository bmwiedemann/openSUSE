#
# spec file for package awf-qt6
#
# Copyright (c) 2021-2026 SUSE LLC
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


Name:           awf-qt6
Version:        4.2.0
Release:        0
Summary:        Theme preview application for Qt 6
Summary(fr):    Application d'aperçu de thème pour Qt 6
License:        GPL-3.0-or-later
URL:            https://github.com/luigifab/awf-extended
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  aspell-fr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt6-base-devel
Requires:       libQt6Core6
Requires:       hicolor-icon-theme
Recommends:     qt6-platformtheme-gtk3
Recommends:     qt6-globalqss
Recommends:     libQt6Svg6
Suggests:       libnotify >= 0.7.0

%description %{expand:
A widget factory is a theme preview application for GTK and Qt. It
displays the various widget types in a single window allowing to see
the visual effect of the applied theme.

This package provides the program for Qt 6.}

%description -l fr %{expand:
La fabrique à widgets est une application d'aperçu de thème pour GTK
et Qt. Elle affiche les différents types de widgets dans une seule
fenêtre permettant de voir l'effet visuel du thème appliqué.

Ce paquet fournit le programme pour Qt 6.}

%prep
%setup -q -n awf-extended-%{version}

%build
%if 0%{?suse_version} < 1600
export CXX=g++-13
%endif
autoreconf -fi
%configure --enable-only-qt6
%make_build

%install
%make_install
%find_lang %{name} --with-man

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
