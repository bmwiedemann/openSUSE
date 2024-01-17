#
# spec file for package cyreal-lora-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           cyreal-lora-fonts
Version:        3.005
Release:        0
Summary:        Serif family for text. Variable Open Source Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.cyreal.org/fonts/lora/
Source0:        https://github.com/cyrealtype/Lora-Cyrillic/releases/download/v%{version}/Lora-v%{version}.zip
Source1:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/README.md
Source2:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/AUTHORS.txt
Source3:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/CONTRIBUTORS.txt
Source4:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/TRADEMARKS.txt
Source5:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/FONTLOG.txt
Source6:        https://github.com/cyrealtype/Lora-Cyrillic/raw/v%{version}/documentation/Lora-sample.png
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Lora is a well-balanced contemporary serif with roots in calligraphy. It is
a text typeface with moderate contrast well suited for body text. A paragraph
set in Lora will make a memorable appearance because of its brushed curves
in contrast with driving serifs. The overall typographic voice of Lora perfectly
conveys the mood of a modern-day story, or an art essay.

Technically Lora is optimised for screen appearance, and works equally well in
print.

Designed by Olga Karpushina, and Alexei Vanyashin for Cyreal.

%prep
%autosetup -c
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%build

%install
install -dm0755 %{buildroot}%{_ttfontsdir}
install -m0644 fonts/otf/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc README.md {AUTHORS,CONTRIBUTORS,TRADEMARKS,FONTLOG}.txt Lora-sample.png
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%changelog
