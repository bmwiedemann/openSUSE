#
# spec file for package iso-codes
#
# Copyright (c) 2022 SUSE LLC
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


Name:           iso-codes
Version:        4.12.0
Release:        0
Summary:        ISO Code Lists and Translations
License:        LGPL-2.1-or-later
URL:            https://salsa.debian.org/iso-codes-team/iso-codes
Source0:        https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/v%{version}/iso-codes-v%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildArch:      noarch

%description
This package provides the ISO-639 language code list, the ISO-3166
territory code list, ISO-3166-2 subterritory lists, and all their
translations in gettext .po form.

%package devel
Summary:        ISO code lists and translations
Requires:       %{name} = %{version}

%description devel
This package provides the ISO-639 Language code list, the ISO-3166
Territory code list, and ISO-3166-2 sub-territory lists, and all their
translations in gettext .po form.

%lang_package

%prep
%setup -q -n %{name}-v%{version}

%build
%configure
%make_build

%install
%make_install
%find_lang iso_639 %{name}.lang
%find_lang iso_639-2 %{name}.lang
%find_lang iso_639-3 %{name}.lang
%find_lang iso_639_3 %{name}.lang
%find_lang iso_639-5 %{name}.lang
%find_lang iso_639_5 %{name}.lang
%find_lang iso_3166 %{name}.lang
%find_lang iso_3166-1 %{name}.lang
%find_lang iso_3166-2 %{name}.lang
%find_lang iso_3166_2 %{name}.lang
%find_lang iso_3166-3 %{name}.lang
%find_lang iso_4217 %{name}.lang
%find_lang iso_15924 %{name}.lang

%files
%doc CHANGELOG.md README.md TODO
%{_datadir}/xml/iso-codes/
%{_datadir}/iso-codes/

%files lang -f %{name}.lang

%files devel
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
