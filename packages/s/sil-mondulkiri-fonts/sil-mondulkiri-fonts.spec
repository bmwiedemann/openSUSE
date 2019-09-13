#
# spec file for package sil-mondulkiri-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           sil-mondulkiri-fonts
Version:        7.100
Release:        0
Summary:        The Mondulkiri Font Family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=Mondulkiri
Source0:        Mondulkiri-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Mondulkiri fonts provide Unicode support for the Khmer script.

The Mondulkiri fonts contain all Khmer and all basic Latin characters.
They also contain a limited number of characters used in some languages in
Vietnam and many phonetic characters.

%prep
%setup -q -n Mondulkiri-%{version}
dos2unix *.txt

%build
:

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc *.txt documentation/*.pdf
%{_ttfontsdir}

%changelog
