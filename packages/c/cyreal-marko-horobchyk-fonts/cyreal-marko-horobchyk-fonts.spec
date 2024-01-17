#
# spec file for package cyreal-marko-horobchyk-fonts
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


Name:           cyreal-marko-horobchyk-fonts
Version:        1.003
Release:        0
License:        OFL-1.1
Summary:        Marko Horobchyk Font
Url:            http://cyreal.org/archives/696
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=1YF0S32njiGRtYo-qZSuiVtkqrIMaAZWyLYEoB48lSQ -O cyreal-marko-horobchyk-fonts.zip
Source0:        cyreal-marko-horobchyk-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Marko Horobchyk is a brush-inspired typeface for children's literature.

As the name suggests (Horobchyk is Ukrainian for sparrow), the initial
idea was to create a typeface-companion for Marko the sparrow — a
cartoon character by illustrator and type designer Zhenya Spizhovyi.

Marko Horobchyk is simple and smooth, has special inner tension and
eye-catchy detailing. The letterforms are based on calligraphy and
sketches — this is what makes Marko Horobchyk lively, enchanting, and
amiable.

Marko Horobchyk will work best in medium to large sizes and captivating
headlines.
While it is technically optimised for better performance on screen,
carefully adjusted outlines promise good quality in print too.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 MarkoOne-Regular.ttf \
    %{buildroot}%{_ttfontsdir}/MarkoOne-Regular.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/MarkoOne-Regular.ttf

%changelog
