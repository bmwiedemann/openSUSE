#
# spec file for package awf-gtk3
#
# Copyright (c) 2021-2023 SUSE LLC
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


Name:           awf-gtk3
Version:        2.7.0
Release:        0
Summary:        Theme preview application for GTK 3
Summary(fr):    Application d'aperçu de thème pour GTK 3
License:        GPL-3.0-or-later
URL:            https://github.com/luigifab/awf-extended
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  aspell-fr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
Requires:       gtk3
Requires:       hicolor-icon-theme

%description %{expand:
A widget factory is a theme preview application for GTK. It displays the
various widget types provided by GTK in a single window allowing to see
the visual effect of the applied theme.

This package provides the GTK 3 version.}

%description -l fr %{expand:
La fabrique à widgets est une application d'aperçu de thème pour GTK. Elle
affiche les différents types de widgets fournis par GTK dans une seule
fenêtre permettant de voir l'effet visuel du thème appliqué.

Ce paquet fournit la version GTK 3.}

%prep
%setup -q -n awf-extended-%{version}
sed -i 's/ -eq 2/ -eq -1/g' configure.ac
sed -i 's/ -eq 4/ -eq -1/g' configure.ac
touch {NEWS,AUTHORS,README,ChangeLog}
mv LICENSE COPYING

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
mkdir -p %{buildroot}%{_mandir}/man1/ %{buildroot}%{_mandir}/fr/man1/
for file in icons/*/*/*; do mv $file ${file/\/awf./\/%{name}.}; done
cp -a icons/* %{buildroot}%{_datadir}/icons/hicolor/
for file in src/po/*.po; do
  code=$(basename "$file" .po)
  mkdir -p %{buildroot}%{_datadir}/locale/${code}/LC_MESSAGES/
  msgfmt src/po/${code}.po -o %{buildroot}%{_datadir}/locale/${code}/LC_MESSAGES/%{name}.mo
done
install -p -m 644 debian-gtk/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m 644 debian-gtk/%{name}.fr.1 %{buildroot}%{_mandir}/fr/man1/%{name}.1
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ applications/%{name}.desktop
%find_lang %{name} --with-man

%files -f %{name}.lang
%{_mandir}/man1/%{name}.1*
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
