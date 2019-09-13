#
# spec file for package cyreal-marmelad-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cyreal-marmelad-fonts
Version:        1.000
Release:        0
License:        OFL-1.1
Summary:        Marmelad Cyrillic Font
Url:            http://cyreal.org/archives/719
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=QIelOrO-KOxb0c1cQM-C_i3USBnSvpkopQaUR-2r7iU -O cyreal-marmelad-fonts.zip
Source0:        cyreal-marmelad-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Marmelad is designed specifically for medium to large-size headlines and
remains well-balanced for long text setting because of its regular
proportions and medium contrast. Ascenders and descenders are elegant
and details refined. The name and overall feel refers to marmalade
sweets – soft and ductile.

All vertical strokes are rounded towards the baseline, which is why
technically there is no sense for overshoots in rounded letters like O.
Marmelad performs well on screen because of its soft rounded features
and generous x-height.

The font supports Latin-1, Cyrillic and Turkish (Latin-5) encoding.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 Marmelad-Regular.ttf \
    %{buildroot}%{_ttfontsdir}/Marmelad-Regular.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Marmelad-Regular.ttf

%changelog
