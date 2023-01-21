#
# spec file for package cyreal-alice-fonts
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


Name:           cyreal-alice-fonts
Version:        2.003
Release:        0
Summary:        Alice Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.cyreal.org/fonts/alice/
Source0:        https://github.com/cyrealtype/Alice/releases/download/v2.003/Alice-v2.003.zip
Source1:        https://github.com/cyrealtype/Alice/raw/v%{version}/README.md
Source2:        https://github.com/cyrealtype/Alice/raw/v%{version}/AUTHORS.txt
Source3:        https://github.com/cyrealtype/Alice/raw/v%{version}/CONTRIBUTORS.txt
Source4:        https://github.com/cyrealtype/Alice/raw/v%{version}/TRADEMARKS.txt
Source5:        https://github.com/cyrealtype/Alice/raw/v%{version}/FONTLOG.txt
Source6:        https://github.com/cyrealtype/Alice/raw/v%{version}/documents/Alice.png
Source7:        https://github.com/cyrealtype/Alice/raw/v%{version}/documents/AliceCyr.png
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Ksenia Erulevich, designer of the Alice typeface, was inspired by Lewis
Carrol’s novel and decided to make a typeface that will be suitable for
typesetting that book.

It came out eclectic and quaint, old-fashioned, having widened
proportions, open aperture, and soft rounded features; perfect for long
meditative text-setting and headlines.

%prep
%autosetup -c
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} .
chmod 0644 OFL.txt
sed -i 's/\r$//g' OFL.txt

%build

%install
install -dm0755 %{buildroot}%{_ttfontsdir}
install -m0644 fonts/otf/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf
%doc README.md {AUTHORS,CONTRIBUTORS,TRADEMARKS,FONTLOG}.txt Alice*.png
%license OFL.txt

%changelog
