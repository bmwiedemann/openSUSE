#
# spec file for package urw-base35-fonts
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           urw-base35-fonts
Version:        20200910
Release:        0
Summary:        Core Font Set containing 35 freely distributable fonts from (URW)++
License:        AGPL-3.0-only WITH PS-or-PDF-font-exception-20170817
Group:          System/X11/Fonts
Url:            https://github.com/ArtifexSoftware/urw-base35-fonts/
Source0:        https://github.com/ArtifexSoftware/urw-base35-fonts/archive/refs/tags/%{version}.tar.gz#/urw-base35-fonts-%{version}.tar.gz
Source1:        urw-postscript-aliases.conf
BuildRequires:  fontpackages-devel
# needed for directory ownership
BuildRequires:  fontconfig
Requires:       urw-base35-fonts-C059
Requires:       urw-base35-fonts-D050000L
Requires:       urw-base35-fonts-NimbusMonoPS
Requires:       urw-base35-fonts-NimbusRoman
Requires:       urw-base35-fonts-NimbusSans
Requires:       urw-base35-fonts-P052
Requires:       urw-base35-fonts-StandardSymbolsPS
Requires:       urw-base35-fonts-URWBookman
Requires:       urw-base35-fonts-URWGothic
Requires:       urw-base35-fonts-Z003
Conflicts:      ghostscript-fonts-std-converted
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
The URW++ Base 35 fonts are a metric compatible substitute for the
Adobe Postscript(c) Level 2 Base 35 fonts.

%package C059
Summary:        An alternative font family for New Century Schoolbook typeface
Supplements:    urw-base35-fonts

%description C059
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package D050000L
Summary:        An alternative font for ITC Zapf Dingbats typeface
Supplements:    urw-base35-fonts

%description D050000L
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package NimbusMonoPS
Summary:        An alternative font family for Courier typeface
Supplements:    urw-base35-fonts

%description NimbusMonoPS
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package NimbusRoman
Summary:        An alternative font family for Times New Roman typeface
Supplements:    urw-base35-fonts

%description NimbusRoman
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package NimbusSans
Summary:        An alternative font family for Helvetica typeface
Supplements:    urw-base35-fonts

%description NimbusSans
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package StandardSymbolsPS
Summary:        An alternative font for Symbol typeface
Supplements:    urw-base35-fonts

%description StandardSymbolsPS
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package P052
Summary:        An alternative font family for Palatino typeface
Supplements:    urw-base35-fonts

%description P052
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package URWBookman
Summary:        An alternative font family for ITC Bookman typeface
Supplements:    urw-base35-fonts

%description URWBookman
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package URWGothic
Summary:        An alternative font family for ITC Avant Garde Gothic typeface
Supplements:    urw-base35-fonts

%description URWGothic
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%package Z003
Summary:        An alternative font for ITC Zapf Chancery typeface
Supplements:    urw-base35-fonts

%description Z003
This serif font family is an alternative for the New Century Schoolbook
typeface, and is part of Level 2 Core Font Set - PostScript specification
of 35 base fonts that can be used with any PostScript file.

%prep
%setup -q

%build
# nothing to do

%install
install -d %{buildroot}%{_datadir}/metainfo/
install -m 644 -t %{buildroot}%{_datadir}/metainfo/ appstream/*.xml
install -d %{buildroot}%{_ttfontsdir}/
install -m 644 -t %{buildroot}%{_ttfontsdir}/ fonts/*.otf
# Do not disturb the order in fontconfig/conf.avail/60-latin.conf
pushd fontconfig
for fc in *.conf; do
        mv $fc 61-$fc
        %install_fontsconf 61-$fc
done
popd
cp -p %{SOURCE1} 61-urw-postscript-aliases.conf
%install_fontsconf 61-urw-postscript-aliases.conf

# post/postun/postrans scriplets
%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n urw-base35-fonts-C059
%reconfigure_fonts_scriptlets -n urw-base35-fonts-D050000L
%reconfigure_fonts_scriptlets -n urw-base35-fonts-NimbusMonoPS
%reconfigure_fonts_scriptlets -n urw-base35-fonts-NimbusRoman
%reconfigure_fonts_scriptlets -n urw-base35-fonts-NimbusSans
%reconfigure_fonts_scriptlets -n urw-base35-fonts-P052
%reconfigure_fonts_scriptlets -n urw-base35-fonts-StandardSymbolsPS
%reconfigure_fonts_scriptlets -n urw-base35-fonts-URWBookman
%reconfigure_fonts_scriptlets -n urw-base35-fonts-URWGothic
%reconfigure_fonts_scriptlets -n urw-base35-fonts-Z003

%files
%license COPYING LICENSE
%doc README.md
%dir %{_ttfontsdir}/
%files_fontsconf_availdir
%{_datadir}/metainfo/de.urwpp.URWCoreFontSetLevel2.metainfo.xml
%files_fontsconf_file -l 61-urw-fallback-backwards.conf
%files_fontsconf_file -l 61-urw-fallback-generics.conf
%files_fontsconf_file -l 61-urw-fallback-specifics.conf
%files_fontsconf_file -l 61-urw-postscript-aliases.conf

%files C059
%{_ttfontsdir}/C059-*.otf
%files_fontsconf_file -l 61-urw-c059.conf
%{_datadir}/metainfo/de.urwpp.C059.metainfo.xml

%files D050000L
%{_ttfontsdir}/D050000L.otf
%files_fontsconf_file -l 61-urw-d050000l.conf
%{_datadir}/metainfo/de.urwpp.D050000L.metainfo.xml

%files NimbusMonoPS
%{_ttfontsdir}/NimbusMonoPS-*.otf
%files_fontsconf_file -l 61-urw-nimbus-mono-ps.conf
%{_datadir}/metainfo/de.urwpp.NimbusMonoPS.metainfo.xml

%files NimbusRoman
%{_ttfontsdir}/NimbusRoman-*.otf
%files_fontsconf_file -l 61-urw-nimbus-roman.conf
%{_datadir}/metainfo/de.urwpp.NimbusRoman.metainfo.xml

%files NimbusSans
%{_ttfontsdir}/NimbusSans-*.otf
%{_ttfontsdir}/NimbusSansNarrow-*.otf
%files_fontsconf_file -l 61-urw-nimbus-sans.conf
%{_datadir}/metainfo/de.urwpp.NimbusSans.metainfo.xml

%files P052
%{_ttfontsdir}/P052-*.otf
%files_fontsconf_file -l 61-urw-p052.conf
%{_datadir}/metainfo/de.urwpp.P052.metainfo.xml

%files StandardSymbolsPS
%{_ttfontsdir}/StandardSymbolsPS.otf
%files_fontsconf_file -l 61-urw-standard-symbols-ps.conf
%{_datadir}/metainfo/de.urwpp.StandardSymbolsPS.metainfo.xml

%files URWBookman
%{_ttfontsdir}/URWBookman-*.otf
%files_fontsconf_file -l 61-urw-bookman.conf
%{_datadir}/metainfo/de.urwpp.URWBookman.metainfo.xml

%files URWGothic
%{_ttfontsdir}/URWGothic-*.otf
%files_fontsconf_file -l 61-urw-gothic.conf
%{_datadir}/metainfo/de.urwpp.URWGothic.metainfo.xml

%files Z003
%{_ttfontsdir}/Z003-*.otf
%{_datadir}/metainfo/de.urwpp.Z003.metainfo.xml
%files_fontsconf_file -l 61-urw-z003.conf

%changelog
