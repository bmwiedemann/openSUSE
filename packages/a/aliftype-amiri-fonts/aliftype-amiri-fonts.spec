#
# spec file for package aliftype-amiri-fonts
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


Name:           aliftype-amiri-fonts
Version:        1.000
Release:        0
Summary:        Amiri is a body text Naskh typeface
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/aliftype/amiri
Source0:        https://github.com/aliftype/amiri/releases/download/%{version}/Amiri-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Amiri is a classical Arabic typeface in Naskh style for typesetting
books and other running text. Amiri is a revival of the beautiful typeface
pioneered in early 20th century by Bulaq Press in Cairo, also known as
Amiria Press, after which the font is named. Amiri project aims at the
revival of the aesthetics and traditions of Arabic typesetting, and adapting
it to the era of digital typesetting, in a publicly available form.

%prep
%autosetup -n Amiri-%{version}

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} Amiri*.ttf

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc NEWS.md NEWS-Arabic.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Amiri*.ttf

%changelog
