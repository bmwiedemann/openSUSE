#
# spec file for package mplus-fonts
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


Name:           mplus-fonts
Version:        20230116
Release:        0
Summary:        Font set incorporating all Kanji until level 2, and latin glyphs
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://mplusfonts.github.io/
Source0:        MPLUS_FONTS-%{version}.tar.xz
Requires:       mplus1-fonts
Requires:       mplus2-fonts
BuildRequires:  fontpackages-devel
BuildRequires:  xz
BuildArch:      noarch

%description
This is a metapackage containing the non-variable M PLUS 1/2 fonts.

%package -n mplus1-fonts
Summary:        Non-variable M PLUS 1 Sans Serif font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus1-fonts
M PLUS 1 is a Sans Serif font with 9 weights from Thin to Black,
supporting GF Latin Plus glyph set with 5,700+ Kanjis for Japanese.

%package -n mplus1-variable-fonts
Summary:        Variable M PLUS 1 Sans Serif font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus1-variable-fonts
M PLUS 1 is a Sans Serif variable font, supporting GF Latin Plus
glyph set with 5,700+ Kanjis for Japanese.

%package -n mplus2-fonts
Summary:        Non-variable M PLUS 2 Sans Serif font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus2-fonts
M PLUS 2 is a Sans Serif font with 9 weights from Thin to Black,
supporting GF Latin Plus glyph set with 5,700+ Kanjis for Japanese.

%package -n mplus2-variable-fonts
Summary:        Variable M PLUS 2 Sans Serif font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus2-variable-fonts
M PLUS 2 is a Sans Serif variable font, supporting GF Latin Plus
glyph set with 5,700+ Kanjis for Japanese.

%package -n mplus1-code-fonts
Summary:        Non-variable M PLUS 1 Code font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus1-code-fonts
7 weights from Thin to Bold. A monospaced font combining
full-width Japanese glyphs (shared with M PLUS 1) and half-width
alphanumeric glyphs (shared with M PLUS Code Latin 50 described below).

%package -n mplus1-code-variable-fonts
Summary:        Variable M PLUS 1 Code font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus1-code-variable-fonts
A monospaced variable font combining full-width Japanese glyphs
(shared with M PLUS 1) and half-width alphanumeric glyphs
(shared with M PLUS Code Latin 50 described below).

%package -n mplus-code-latin50-fonts
Summary:        Non-variable M PLUS Code Latin 60 font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus-code-latin50-fonts
A monospaced font with 7 weights from Thin to Bold.
M PLUS Code Latin 50 has a 50% character width.

%package -n mplus-code-latin60-fonts
Summary:        Non-variable M PLUS Code Latin 60 font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus-code-latin60-fonts
A monospaced font with 7 weights from Thin to Bold.
M PLUS Code Latin 60 has a 60% character width.

%package -n mplus-code-latin-variable-fonts
Summary:        Variable M PLUS Code Latin font
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n mplus-code-latin-variable-fonts
A monospaced variable font that can be adjusted for both
weight and width.

%prep
%autosetup -n MPLUS_FONTS-%{version}

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} fonts/ttf/*.ttf

%reconfigure_fonts_scriptlets -n mplus1-fonts
%reconfigure_fonts_scriptlets -n mplus1-variable-fonts
%reconfigure_fonts_scriptlets -n mplus2-fonts
%reconfigure_fonts_scriptlets -n mplus2-variable-fonts
%reconfigure_fonts_scriptlets -n mplus1-code-fonts
%reconfigure_fonts_scriptlets -n mplus1-code-variable-fonts
%reconfigure_fonts_scriptlets -n mplus-code-latin50-fonts
%reconfigure_fonts_scriptlets -n mplus-code-latin60-fonts
%reconfigure_fonts_scriptlets -n mplus-code-latin-variable-fonts

%files
%license OFL.txt

%files -n mplus1-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/Mplus1-*.ttf

%files -n mplus1-variable-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MPLUS1[wght].ttf

%files -n mplus2-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/Mplus2-*.ttf

%files -n mplus2-variable-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MPLUS2[wght].ttf

%files -n mplus1-code-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/Mplus1Code-*.ttf

%files -n mplus1-code-variable-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MPLUS1Code[wght].ttf

%files -n mplus-code-latin50-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MplusCodeLatin50-*.ttf

%files -n mplus-code-latin60-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MplusCodeLatin60-*.ttf

%files -n mplus-code-latin-variable-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/MPLUSCodeLatin[wdth,wght].ttf

%changelog
