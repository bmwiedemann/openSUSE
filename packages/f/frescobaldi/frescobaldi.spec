#
# spec file for package frescobaldi
#
# Copyright (c) 2025 SUSE LLC
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


ExcludeArch:    i586
%{?sle15_python_module_pythons}%{?!sle15_python_module_pythons:%define pythons python3}
%define mypython %{pythons}
%global mypython_sitelib %{expand:%%%{mypython}_sitelib}

Name:           frescobaldi
Summary:        Lilypond editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Version:        4.0.1
Release:        0
URL:            http://www.frescobaldi.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://github.com/frescobaldi/frescobaldi/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %mypython-ly >= 0.9.9
BuildRequires:  %mypython-pip
BuildRequires:  %mypython-setuptools
BuildRequires:  %mypython-tox
BuildRequires:  %mypython-wheel
BuildRequires:  appstream-glib-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %mypython-PyQt6-sip
Requires:       %mypython-ly
Requires:       %mypython-qpageview >= 1.0.0
Requires:       %mypython-qt6
Requires:       %mypython-qtwebengine-qt6
Requires:       lilypond
Recommends:     %mypython-pycups
Recommends:     libportmidi2
BuildArch:      noarch

%description
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet
lightweight and easy to use.

You can edit LilyPond documents and build and preview them with a mouse click.
Clicking on notes in the PDF preview places the text cursor in the right place.
A score wizard is provided to quickly setup a music score. There are editing
tools to manipulate the rhythm, acticulations, lyrics hyphenation, etc.

%prep
%setup -q
tox -e mo-generate
tox -e linux-generate

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 linux/org.frescobaldi.Frescobaldi.desktop \
    %{buildroot}%{_datadir}/applications/org.frescobaldi.Frescobaldi.desktop
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 0644 linux/org.frescobaldi.Frescobaldi.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo
%suse_update_desktop_file org.frescobaldi.Frescobaldi AudioVideo Music

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp frescobaldi/icons/org.frescobaldi.Frescobaldi.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%fdupes %{buildroot}%{mypython_sitelib}

%files
%doc README* THANKS CHANGELOG.md
%license LICENSE
%{_bindir}/frescobaldi
%{_datadir}/applications/org.frescobaldi.Frescobaldi.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.frescobaldi.Frescobaldi.svg
%{_datadir}/metainfo/org.frescobaldi.Frescobaldi.metainfo.xml
%{mypython_sitelib}/frescobaldi
%{mypython_sitelib}/frescobaldi-%{version}.dist-info

%changelog
