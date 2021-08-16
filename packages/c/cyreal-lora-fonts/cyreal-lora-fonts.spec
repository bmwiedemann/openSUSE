#
# spec file for package cyreal-lora-fonts
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.202
Release:        0
Summary:        Serif family for text. Variable Open Source Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.cyreal.org/2012/07/lora/
Source:         https://github.com/cyrealtype/Lora-Cyrillic/archive/v%{version}.tar.gz#/Lora-Cyrillic-%{version}.tar.gz
BuildRequires:  fontpackages-devel
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
%setup -q -n Lora-Cyrillic-%{version}

%build

%install
install -dm0755 %{buildroot}%{_ttfontsdir}
install -m0644 fonts/OTF/*.otf %{buildroot}%{_ttfontsdir}
%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf
%defattr(0644,root,root)
%doc README.md {AUTHORS,CONTRIBUTORS,FONTLOG,TRADEMARKS}.txt sources/sample*.png
%license OFL.txt

%changelog
