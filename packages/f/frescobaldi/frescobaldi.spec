#
# spec file for package frescobaldi
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.3.0
Release:        0
URL:            http://www.frescobaldi.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://github.com/frescobaldi/frescobaldi/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %mypython-ly
BuildRequires:  %mypython-pip
BuildRequires:  %mypython-setuptools
BuildRequires:  %mypython-wheel
BuildRequires:  appstream-glib-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %mypython-ly
Requires:       %mypython-poppler-qt5
Requires:       %mypython-qpageview
Requires:       %mypython-qt5
Requires:       %mypython-qt5-sip
Requires:       %mypython-qtwebengine-qt5
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
rm setup.cfg
sed -i '1{/env python/d}' frescobaldi_app/language_names/generate.py frescobaldi_app/unicode_blocks.py

%build
rm -rf %{name}_app/icons/Tango
make -C i18n
make -C linux
%pyproject_wheel

%install
%pyproject_install
%suse_update_desktop_file org.frescobaldi.Frescobaldi AudioVideo Music
%fdupes %{buildroot}%{mypython_sitelib}

%files
%doc README.md THANKS CHANGELOG.md
%license COPYING
%doc %{_mandir}/man1/frescobaldi*
%{_bindir}/frescobaldi
%{_datadir}/applications/org.frescobaldi.Frescobaldi.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.frescobaldi.Frescobaldi.svg
%{_datadir}/metainfo/org.frescobaldi.Frescobaldi.metainfo.xml
%{mypython_sitelib}/frescobaldi_app
%{mypython_sitelib}/frescobaldi-%{version}.dist-info

%changelog
