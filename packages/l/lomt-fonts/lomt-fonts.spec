#
# spec file for package lomt-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           lomt-fonts
Version:        0.20121218
Release:        0
Summary:        Fonts from the League Of Movable Type project
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://theleagueofmoveabletype.com/

Source:         LOMT.tar.xz
Source2:        LOMT-create.sh
BuildRequires:  fontpackages-devel
BuildRequires:  xz
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A foundry and hand-picked collection of open-source typography.

%package -n lomt-blackout-fonts
Summary:        League Of Movable Type's "Blackout" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-blackout-fonts
A font inspired by the author filling in sans-serif newspaper
headlines.

%package -n lomt-chunk-fonts
Summary:        League Of Movable Type's "Chunk" font
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-chunk-fonts
"Chunk" is an ultra-bold slab serif typeface that is reminiscent of
old American Western woodcuts, broadsides, and newspaper headlines.
Used mainly for display, the fat block lettering is unreserved yet
refined for contemporary use.

%package -n lomt-fanwood-fonts
Summary:        League Of Movable Type's "Fanwood" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-fanwood-fonts
This serif font is based on work of a famous Czech-American type
designer of yesteryear. The package includes roman and italic.

%package -n lomt-goudybookletter-fonts
Summary:        League Of Movable Type's "Goudy Bookletter 1911" font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts

%description -n lomt-goudybookletter-fonts
A serif font based on Frederic Goudy's Kennerley Oldstyle.

%package -n lomt-junction-fonts
Summary:        League Of Movable Type's "Junction" font
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-junction-fonts
Junction is a a humanist sans-serif, and the first open-source type project started by The League of Moveable Type.

%package -n lomt-knewave-fonts
Summary:        League Of Movable Type's "Knewave" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-knewave-fonts
Knewave is a bold, painted font face.

%package -n lomt-leaguegothic-fonts
Summary:        League Of Movable Type's "League Gothic" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-leaguegothic-fonts
League Gothic is a revival of an old classic, Alternate Gothic #1.

%package -n lomt-lindenhill-fonts
Summary:        League Of Movable Type's "Linden Hill" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-lindenhill-fonts
Linden Hill is a digital version of Frederic Goudy's Deepdene. The
package includes roman and italic.

%package -n lomt-orbitron-fonts
Summary:        League Of Movable Type's "Orbitron" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-orbitron-fonts
Orbitron is a geometric sans-serif typeface intended for display
purposes. It features four weights (light, medium, bold, and black),
a stylistic alternative, small caps, and a ton of alternate glyphs.

%package -n lomt-ostrichsans-fonts
Summary:        League Of Movable Type's "Ostrich Sans" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-ostrichsans-fonts
A modern sans-serif with a very long neck. A number of styles and
weights are included: dashed (thin), rounded (medium), ultra light,
normal, bold (race track style double lines) and Black10.

%package -n lomt-prociono-fonts
Summary:        League Of Movable Type's "Prociono" font
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-prociono-fonts
("Prociono" is an Esperanto word meaning either the star Procyon or
the animal species known as the raccoon.) It is a roman serif font
with blackletter elements.

%package -n lomt-script1-fonts
Summary:        League Of Movable Type's "League Script Number One" font
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-script1-fonts
Script #1 is a modern, coquettish script font that intends to look
like handwritten letters from the 1920s. It includes ligatures
included.

%package -n lomt-sniglet-fonts
Summary:        League Of Movable Type's "Sniglet" font
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-sniglet-fonts
A rounded display face intended primarily for headlines. It comes
with a full Latin character set.

%package -n lomt-sortsmillgoudy-fonts
Summary:        League Of Movable Type's "Sorts Mill Goudy" font family
License:        OFL-1.1
Group:          System/X11/Fonts

%description -n lomt-sortsmillgoudy-fonts
A "revival" of Goudy Oldstyle and Italic, with features including
small capitals (in the roman only), oldstyle and lining figures,
superscripts and subscripts, fractions, ligatures, class-based
kerning, case-sensitive forms, and capital spacing. There is support
for many languages using Latin scripts.

%prep
%setup -qn LOMT

%build

%install
c="%buildroot/%_ttfontsdir";
mkdir -p "$c";
for i in *\ *.{otf,ttf}; do
	mv -v "$i" "${i// /_}";
done;

# An improved Raleway is already provided in a separate package we have,
# in raleway-fonts.
rm -f Raleway*.[ot]tf
install -pm0644 *.otf *.ttf "$c/";

%reconfigure_fonts_scriptlets -n lomt-blackout-fonts
%reconfigure_fonts_scriptlets -n lomt-chunk-fonts
%reconfigure_fonts_scriptlets -n lomt-fanwood-fonts
%reconfigure_fonts_scriptlets -n lomt-goudybookletter-fonts
%reconfigure_fonts_scriptlets -n lomt-junction-fonts
%reconfigure_fonts_scriptlets -n lomt-knewave-fonts
%reconfigure_fonts_scriptlets -n lomt-leaguegothic-fonts
%reconfigure_fonts_scriptlets -n lomt-lindenhill-fonts
%reconfigure_fonts_scriptlets -n lomt-orbitron-fonts
%reconfigure_fonts_scriptlets -n lomt-ostrichsans-fonts
%reconfigure_fonts_scriptlets -n lomt-prociono-fonts
%reconfigure_fonts_scriptlets -n lomt-script1-fonts
%reconfigure_fonts_scriptlets -n lomt-sniglet-fonts
%reconfigure_fonts_scriptlets -n lomt-sortsmillgoudy-fonts

%files -n lomt-blackout-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Blackout*.ttf
%doc blackout.markdown

%files -n lomt-chunk-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Chunk.otf
%doc chunk.markdown

%files -n lomt-fanwood-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Fanwood*.otf
%doc fanwood.markdown

%files -n lomt-goudybookletter-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/GoudyBookletter1911.otf
%doc goudy-bookletter-1911.markdown

%files -n lomt-junction-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Junction.otf
%doc junction.markdown

%files -n lomt-knewave-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/knewave*.otf
%doc knewave.markdown

%files -n lomt-leaguegothic-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/LeagueGothic-*.otf
%doc league-gothic.markdown

%files -n lomt-lindenhill-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Linden*Hill*.otf
%doc linden-hill.markdown

%files -n lomt-orbitron-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Orbitron*.otf
%doc orbitron.markdown

%files -n lomt-ostrichsans-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Ostrich*.ttf
%doc ostrich-sans.markdown

%files -n lomt-prociono-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Prociono.otf
%doc prociono.markdown

%files -n lomt-script1-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/LeagueScriptNumberOne.otf
%doc league-script-number-one.markdown

%files -n lomt-sniglet-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/Sniglet*.otf
%doc sniglet.markdown

%files -n lomt-sortsmillgoudy-fonts
%defattr(-,root,root)
%dir %_ttfontsdir
%_ttfontsdir/OFLGoudyStM*.otf
%doc sorts-mill-goudy.markdown

%changelog
