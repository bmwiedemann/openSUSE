#
# spec file for package frescobaldi
#
# Copyright (c) 2019 SUSE LLC
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


Name:           frescobaldi
Summary:        Lilypond editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Version:        3.1
Release:        0
URL:            http://www.frescobaldi.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://github.com/frescobaldi/frescobaldi/archive/v%{version}/%{name}-%{version}.tar.gz
# New package, was before part of frescobaldi
# Url: https://pypi.python.org/pypi/python-ly
# Keep in this package, because frescobaldi is the only one using it.
Source1:        https://files.pythonhosted.org/packages/01/ca/e86c73614a690d778ec9831adee0a728a495f4fb717fab263b5e4887b086/python-ly-0.9.5.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       lilypond
Requires:       python3-poppler-qt5
Requires:       python3-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-sip
Recommends:     libportmidi0
BuildArch:      noarch

%description
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful, yet 
lightweight and easy to use.

You can edit LilyPond documents and build and preview them with a mouse click. 
Clicking on notes in the PDF preview places the text cursor in the right place. 
A score wizard is provided to quickly setup a music score. There are editing 
tools to manipulate the rhythm, acticulations, lyrics hyphenation, etc.


%prep
%setup -q -a 1

%build
rm -rf %{name}_app/icons/Tango
python3 setup.py build
make -C i18n

%install
%suse_update_desktop_file %{name} Multimedia AudioVideoEditing
# first install python-ly
cd python-ly-0.9.5
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
cd ..
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr (-,root,root)
%doc README.md THANKS ChangeLog
%license COPYING
%doc %{_mandir}/man1/frescobaldi*
%{_bindir}/frescobaldi
%{_bindir}/ly*
%{_datadir}/applications/frescobaldi.desktop
%{_datadir}/icons/hicolor/scalable/apps/frescobaldi.svg
%{python3_sitelib}/*

%changelog
