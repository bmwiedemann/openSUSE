#
# spec file for package google-croscore-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define arname  croscorefonts

Name:           google-croscore-fonts
Version:        1.31.0
Release:        0
Summary:        Croscore fonts 
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://gsdview.appspot.com/chromeos-localmirror/distfiles/
Source0:        %{arname}-%{version}.tar.bz2
Source1:        LICENSE
BuildRequires:  fontpackages-devel
Provides:       locale(bg;el;ru;bg)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       google-arimo-fonts
Requires:       google-cousine-fonts
Requires:       google-tinos-fonts

%description
A collection of fonts which are metric-compatible to "Arial", "Times
New Roman" and "Courier New". Croscore fonts are based on the
Liberation fonts and extend its glyph coverage.

%package -n google-arimo-fonts
%reconfigure_fonts_prereq
Summary:        Monospace Sans Serif Font
Group:          System/X11/Fonts

%description -n google-arimo-fonts
Arimo was designed by Steve Matteson as a sans serif design that is
metrically compatible with Arial. Arimo offers improved on-screen
readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts
to address document portability across platforms.

%package -n google-cousine-fonts
%reconfigure_fonts_prereq
Summary:        Monospace Sans Serif Font
Group:          System/X11/Fonts

%description -n google-cousine-fonts
Cousine was designed by Steve Matteson as a sans serif design that is
metrically-compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL
character set and solves the needs of developers looking for
width-compatible fonts to address document portability across
platforms.

%package -n google-tinos-fonts
%reconfigure_fonts_prereq
Summary:        Monospace Sans Serif Font
Group:          System/X11/Fonts

%description -n google-tinos-fonts
Tinos was designed by Steve Matteson as an serif design that is
metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL
character set and solves the needs of developers looking for
width-compatible fonts to address document portability across
platforms.

%prep
%setup -q -n %{arname}-%{version}

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n google-arimo-fonts

%reconfigure_fonts_scriptlets -n google-cousine-fonts

%reconfigure_fonts_scriptlets -n google-tinos-fonts

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_ttfontsdir}

%files -n google-arimo-fonts
%defattr(-,root,root)
%{_ttfontsdir}/Arimo*.ttf

%files -n google-cousine-fonts
%defattr(-,root,root)
%{_ttfontsdir}/Cousine*.ttf

%files -n google-tinos-fonts
%defattr(-,root,root)
%{_ttfontsdir}/Tinos*.ttf

%changelog
