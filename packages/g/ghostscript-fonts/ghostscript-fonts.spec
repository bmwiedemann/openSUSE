#
# spec file for package ghostscript-fonts
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ghostscript-fonts
BuildArch:      noarch
# Prepare spec file for dropping SuSEconfig.fonts
# see https://features.opensuse.org/313536
%if 0%{?suse_version} > 1220
BuildRequires:  fontpackages-devel
%endif
URL:            http://www.ghostscript.com/
Summary:        Ghostscript's free fonts
# The version is the same version as the current ghostscript package.
# Reasoning: Before the Ghostscript package clean-up (see bnc#735824)
# the packages ghostscript-fonts-std and ghostscript-fonts-other
# have been sub-packages of the ghostscript-library package
# so that the ghostscript-fonts-* packages inhertited their version
# from the ghostscript-library package which has the version of Ghostscript.
# To provide the new ghostscript-fonts-* packages under a higher version
# than the old ghostscript-fonts-* sub-packages, the existing versioning scheme
# is still used here. This versioning scheme makes sense because this
# ghostscript-fonts-* packages are the right ones for this Ghostscript version:
License:        GPL-2.0-only
Group:          Productivity/Publishing/PS
Version:        9.06
Release:        0
# Source0...Source9 is for sources from upstream:
# URL for Source0: http://mirror.cs.wisc.edu/pub/mirrors/ghost/fonts/ghostscript-fonts-std-8.11.tar.gz
Source0:        ghostscript-fonts-std-8.11.tar.gz
# URL for Source1: http://mirror.cs.wisc.edu/pub/mirrors/ghost/fonts/ghostscript-fonts-other-6.0.tar.gz
Source1:        ghostscript-fonts-other-6.0.tar.gz
# Patch0...Patch9 is for patches from upstream:
#
# Source10...Source99 is for sources from SUSE which are intended for upstream:
#
# Patch10...Patch99 is for patches from SUSE which are intended for upstream:
#
# Source100...Source999 is for sources from SUSE which are not intended for upstream:
#
# Patch100...Patch999 is for patches from SUSE which are not intended for upstream:
#
BuildRequires:  ttf-converter
# An older fontforge version should work, but 20200314 fixes bugs
# that appear when converting n021023l.pfb from
# ghostscript-fonts-std
BuildRequires:  fontforge >= 20200314
BuildRequires:  fontpackages-devel
# The main-package ghostscript-fonts alone is useless because it does not contain any font file.
# The font files are provided via its sub-packages. Nevertheless when a user selects only
# the main-package to be installed, he probably wants "all Ghostscript's free fonts"
# and therefore all sub-packages are recommended:
Recommends:     ghostscript-fonts-std
Recommends:     ghostscript-fonts-other
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Two sets of free fonts are supplied
by Ghostscript:

Basic fonts for Ghostscript
in the package ghostscript-fonts-std.

Optional Fonts for Ghostscript
in the package ghostscript-fonts-other.


%package std
Summary:        Basic Fonts for Ghostscript
Group:          Productivity/Publishing/PS
PreReq:         coreutils %suseconfig_fonts_prereq
Provides:       urw-fonts

%description std
Several Type 1 basic PostScript fonts.
Times, Helvetica, Courier, Symbol, etc.
Contributed by URW++ Design and Development
Incorporated, of Hamburg, Germany.


%package other
Summary:        Optional Fonts for Ghostscript
# ghostscript-fonts-std contains /usr/share/ghostscript/fonts/fonts.dir
# and /usr/share/ghostscript/fonts/fonts.scale which are needed
# to map Ghostscript's font files to X logical font description (XLFD),
# see the section "Using Ghostscript fonts on X Windows displays"
# in doc/Fonts.htm in the Ghostscript sources:
Group:          Productivity/Publishing/PS
Requires:       ghostscript-fonts-std

%description other
A miscellaneous set including Cyrillic,
kana, and fonts derived from the free
Hershey fonts, with improvements (such as
adding accented characters) by Thomas Wolff.
The Hershey-based fonts are quite different
from traditional printer or display fonts;
you can read about them in more detail in
the documentation on Hershey fonts.

%package std-converted
Summary:        Basic Fonts for Ghostscript converted to truetype
Group:          Productivity/Publishing/PS
Requires(post): fonts-config
Requires(posttrans): fonts-config
Requires(postun): fonts-config
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
# In TW and SLE 15 SP2/Leap 15.2 we have pango >= 1.44.0 which
# doesn't support Type1 fonts (boo1169444)
Supplements:    packageand(ghostscript-fonts-std:libpango-1_0-0)
%endif

%description std-converted
This package contains the Type1 (.pfb) fonts from
ghostscript-fonts-std converted to TrueType format, so they can
be used by applications that don't support Type1 fonts.

%prep
# Be quiet when unpacking and
# create directory (and change to it) before unpacking Source0 and
# additionally unpack Source1 after changing directory:
%setup -q -c %{name}-%{version} -a 1

%build
# There is nothing to "make" as the sources contain plain font files.
ttf-converter --input-dir fonts/ --output-dir generated

# There's already a version of these fonts included in xorg-x11-fonts-converted
rm generated/CharterBT-*
rm generated/Utopia-*

%install
# Install the fonts into the /usr/share/ghostscript/fonts/ directory
# which is the Ghostscript upstream standard directory where
# Ghostscript looks first and foremost for its fonts
# see section "3.1 Fonts" in doc/Install.htm in the Ghostscript sources:
FONT_INSTALL_DIR=%{buildroot}%{_datadir}/ghostscript/fonts
install -d -m755 $FONT_INSTALL_DIR
install -m644 fonts/fonts.* $FONT_INSTALL_DIR
for SUFFIX in afm gsf pfa pfb pfm
do install -m644 fonts/*.$SUFFIX $FONT_INSTALL_DIR
done
# Provide a link to make the Ghostscript fonts also appear in the directory
# /usr/share/fonts/ where applications (including X11) search for fonts.
# A usr/share/fonts/ sub-directory does not exist in the buildroot:
install -d -m 755 %{buildroot}%{_datadir}/fonts
# Using an absolute path as source in symbolic link to avoid an issue with /usr/sbin/Check
# in SLE11, SLE_11_SP1, and SLE_11_SP2 that would wrongly convert a relative
# path ../ghostscript/fonts into a ../ghostscript/fonts.gz file,
# see http://lists.opensuse.org/opensuse-packaging/2012-09/msg00239.html
# Afterwards /usr/lib/rpm/brp-symlink converts it to a relative path so that the binary RPM
# gets the intended symbolic link /usr/share/fonts/ghostscript -> ../ghostscript/fonts
ln -s %{_datadir}/ghostscript/fonts %{buildroot}%{_datadir}/fonts/ghostscript

# Install also the fonts converted to truetype format
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
cp generated/*.ttf %{buildroot}/%{_datadir}/fonts/truetype

# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_post.
# Since openSUSE 12.2 there is no SuSEconfig.pango (have it only in the scriptlet if suse_version < 1220):
%post std
%if 0%{?suse_version} > 1220
%reconfigure_fonts_post
%else
if test -x sbin/conf.d/SuSEconfig.fonts
then %run_suseconfig -m fonts
fi
%endif
%if 0%{?suse_version} < 1220
if test -x sbin/conf.d/SuSEconfig.pango
then %run_suseconfig -m pango
fi
%endif
exit 0

%reconfigure_fonts_scriptlets -n ghostscript-fonts-std-converted

# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_postun.
# Since openSUSE 12.2 there is no SuSEconfig.pango (have it only in the scriptlet if suse_version < 1220):
%postun std
%if 0%{?suse_version} > 1220
%reconfigure_fonts_postun
%else
if test -x sbin/conf.d/SuSEconfig.fonts
then %run_suseconfig -m fonts
fi
%endif
%if 0%{?suse_version} < 1220
if test -x sbin/conf.d/SuSEconfig.pango
then %run_suseconfig -m pango
fi
%endif
exit 0

%if 0%{?suse_version} > 1220
# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_posttrans:
%posttrans std
%reconfigure_fonts_posttrans
exit 0
%endif

# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_post.
# Since openSUSE 12.2 there is no SuSEconfig.pango (have it only in the scriptlet if suse_version < 1220):
%post other
%if 0%{?suse_version} > 1220
%reconfigure_fonts_post
%else
if test -x sbin/conf.d/SuSEconfig.fonts
then %run_suseconfig -m fonts
fi
%endif
%if 0%{?suse_version} < 1220
if test -x sbin/conf.d/SuSEconfig.pango
then %run_suseconfig -m pango
fi
%endif
exit 0

# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_postun.
# Since openSUSE 12.2 there is no SuSEconfig.pango (have it only in the scriptlet if suse_version < 1220):
%postun other
%if 0%{?suse_version} > 1220
%reconfigure_fonts_postun
%else
if test -x sbin/conf.d/SuSEconfig.fonts
then %run_suseconfig -m fonts
fi
%endif
%if 0%{?suse_version} < 1220
if test -x sbin/conf.d/SuSEconfig.pango
then %run_suseconfig -m pango
fi
%endif
exit 0

%if 0%{?suse_version} > 1220
# Use traditional bash scriptlet with an explicite "exit 0" line at the end to be fail safe
# see http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Only if suse_version > 1220 it BuildRequires fontpackages-devel which provides reconfigure_fonts_posttrans:
%posttrans other
%reconfigure_fonts_posttrans
exit 0
%endif

%files
%defattr(-, root, root)
%doc fonts/COPYING fonts/ChangeLog fonts/README fonts/README.tweaks fonts/TODO

%files std
%defattr(0644,root,root,0755)
%verify(not md5 size mtime) %{_datadir}/ghostscript/fonts/fonts.*
%{_datadir}/fonts/ghostscript
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/fonts
%{_datadir}/ghostscript/fonts/fonts.dir
%{_datadir}/ghostscript/fonts/fonts.scale
%{_datadir}/ghostscript/fonts/a010013l.afm
%{_datadir}/ghostscript/fonts/a010015l.afm
%{_datadir}/ghostscript/fonts/a010033l.afm
%{_datadir}/ghostscript/fonts/a010035l.afm
%{_datadir}/ghostscript/fonts/b018012l.afm
%{_datadir}/ghostscript/fonts/b018015l.afm
%{_datadir}/ghostscript/fonts/b018032l.afm
%{_datadir}/ghostscript/fonts/b018035l.afm
%{_datadir}/ghostscript/fonts/c059013l.afm
%{_datadir}/ghostscript/fonts/c059016l.afm
%{_datadir}/ghostscript/fonts/c059033l.afm
%{_datadir}/ghostscript/fonts/c059036l.afm
%{_datadir}/ghostscript/fonts/d050000l.afm
%{_datadir}/ghostscript/fonts/n019003l.afm
%{_datadir}/ghostscript/fonts/n019004l.afm
%{_datadir}/ghostscript/fonts/n019023l.afm
%{_datadir}/ghostscript/fonts/n019024l.afm
%{_datadir}/ghostscript/fonts/n019043l.afm
%{_datadir}/ghostscript/fonts/n019044l.afm
%{_datadir}/ghostscript/fonts/n019063l.afm
%{_datadir}/ghostscript/fonts/n019064l.afm
%{_datadir}/ghostscript/fonts/n021003l.afm
%{_datadir}/ghostscript/fonts/n021004l.afm
%{_datadir}/ghostscript/fonts/n021023l.afm
%{_datadir}/ghostscript/fonts/n021024l.afm
%{_datadir}/ghostscript/fonts/n022003l.afm
%{_datadir}/ghostscript/fonts/n022004l.afm
%{_datadir}/ghostscript/fonts/n022023l.afm
%{_datadir}/ghostscript/fonts/n022024l.afm
%{_datadir}/ghostscript/fonts/p052003l.afm
%{_datadir}/ghostscript/fonts/p052004l.afm
%{_datadir}/ghostscript/fonts/p052023l.afm
%{_datadir}/ghostscript/fonts/p052024l.afm
%{_datadir}/ghostscript/fonts/s050000l.afm
%{_datadir}/ghostscript/fonts/z003034l.afm
%{_datadir}/ghostscript/fonts/a010013l.pfm
%{_datadir}/ghostscript/fonts/a010015l.pfm
%{_datadir}/ghostscript/fonts/a010033l.pfm
%{_datadir}/ghostscript/fonts/a010035l.pfm
%{_datadir}/ghostscript/fonts/b018012l.pfm
%{_datadir}/ghostscript/fonts/b018015l.pfm
%{_datadir}/ghostscript/fonts/b018032l.pfm
%{_datadir}/ghostscript/fonts/b018035l.pfm
%{_datadir}/ghostscript/fonts/n019003l.pfm
%{_datadir}/ghostscript/fonts/n019004l.pfm
%{_datadir}/ghostscript/fonts/n019023l.pfm
%{_datadir}/ghostscript/fonts/n019024l.pfm
%{_datadir}/ghostscript/fonts/n019064l.pfm
%{_datadir}/ghostscript/fonts/n021003l.pfm
%{_datadir}/ghostscript/fonts/n021004l.pfm
%{_datadir}/ghostscript/fonts/n021023l.pfm
%{_datadir}/ghostscript/fonts/n021024l.pfm
%{_datadir}/ghostscript/fonts/z003034l.pfm
%{_datadir}/ghostscript/fonts/a010013l.pfb
%{_datadir}/ghostscript/fonts/a010015l.pfb
%{_datadir}/ghostscript/fonts/a010033l.pfb
%{_datadir}/ghostscript/fonts/a010035l.pfb
%{_datadir}/ghostscript/fonts/b018012l.pfb
%{_datadir}/ghostscript/fonts/b018015l.pfb
%{_datadir}/ghostscript/fonts/b018032l.pfb
%{_datadir}/ghostscript/fonts/b018035l.pfb
%{_datadir}/ghostscript/fonts/c059013l.pfb
%{_datadir}/ghostscript/fonts/c059016l.pfb
%{_datadir}/ghostscript/fonts/c059033l.pfb
%{_datadir}/ghostscript/fonts/c059036l.pfb
%{_datadir}/ghostscript/fonts/d050000l.pfb
%{_datadir}/ghostscript/fonts/n019003l.pfb
%{_datadir}/ghostscript/fonts/n019004l.pfb
%{_datadir}/ghostscript/fonts/n019023l.pfb
%{_datadir}/ghostscript/fonts/n019024l.pfb
%{_datadir}/ghostscript/fonts/n019043l.pfb
%{_datadir}/ghostscript/fonts/n019044l.pfb
%{_datadir}/ghostscript/fonts/n019063l.pfb
%{_datadir}/ghostscript/fonts/n019064l.pfb
%{_datadir}/ghostscript/fonts/n021003l.pfb
%{_datadir}/ghostscript/fonts/n021004l.pfb
%{_datadir}/ghostscript/fonts/n021023l.pfb
%{_datadir}/ghostscript/fonts/n021024l.pfb
%{_datadir}/ghostscript/fonts/n022003l.pfb
%{_datadir}/ghostscript/fonts/n022004l.pfb
%{_datadir}/ghostscript/fonts/n022023l.pfb
%{_datadir}/ghostscript/fonts/n022024l.pfb
%{_datadir}/ghostscript/fonts/p052003l.pfb
%{_datadir}/ghostscript/fonts/p052004l.pfb
%{_datadir}/ghostscript/fonts/p052023l.pfb
%{_datadir}/ghostscript/fonts/p052024l.pfb
%{_datadir}/ghostscript/fonts/s050000l.pfb
%{_datadir}/ghostscript/fonts/z003034l.pfb

%files other
%defattr(0644,root,root,0755)
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/fonts
%{_datadir}/ghostscript/fonts/bchb.afm
%{_datadir}/ghostscript/fonts/bchbi.afm
%{_datadir}/ghostscript/fonts/bchr.afm
%{_datadir}/ghostscript/fonts/bchri.afm
%{_datadir}/ghostscript/fonts/fcyr.afm
%{_datadir}/ghostscript/fonts/fcyri.afm
%{_datadir}/ghostscript/fonts/u003043t.afm
%{_datadir}/ghostscript/fonts/u004006t.afm
%{_datadir}/ghostscript/fonts/fcyr.gsf
%{_datadir}/ghostscript/fonts/fcyri.gsf
%{_datadir}/ghostscript/fonts/fhirw.gsf
%{_datadir}/ghostscript/fonts/fkarw.gsf
%{_datadir}/ghostscript/fonts/hrgerb.gsf
%{_datadir}/ghostscript/fonts/hrgerd.gsf
%{_datadir}/ghostscript/fonts/hrgero.gsf
%{_datadir}/ghostscript/fonts/hrgkc.gsf
%{_datadir}/ghostscript/fonts/hrgks.gsf
%{_datadir}/ghostscript/fonts/hrgrrb.gsf
%{_datadir}/ghostscript/fonts/hrgrro.gsf
%{_datadir}/ghostscript/fonts/hritrb.gsf
%{_datadir}/ghostscript/fonts/hritro.gsf
%{_datadir}/ghostscript/fonts/hrpldb.gsf
%{_datadir}/ghostscript/fonts/hrpldbi.gsf
%{_datadir}/ghostscript/fonts/hrplr.gsf
%{_datadir}/ghostscript/fonts/hrplrb.gsf
%{_datadir}/ghostscript/fonts/hrplrbo.gsf
%{_datadir}/ghostscript/fonts/hrplro.gsf
%{_datadir}/ghostscript/fonts/hrpls.gsf
%{_datadir}/ghostscript/fonts/hrplsb.gsf
%{_datadir}/ghostscript/fonts/hrplsbo.gsf
%{_datadir}/ghostscript/fonts/hrplso.gsf
%{_datadir}/ghostscript/fonts/hrpltb.gsf
%{_datadir}/ghostscript/fonts/hrpltbi.gsf
%{_datadir}/ghostscript/fonts/hrsccb.gsf
%{_datadir}/ghostscript/fonts/hrscco.gsf
%{_datadir}/ghostscript/fonts/hrscsb.gsf
%{_datadir}/ghostscript/fonts/hrscso.gsf
%{_datadir}/ghostscript/fonts/hrsyr.gsf
%{_datadir}/ghostscript/fonts/u003043t.gsf
%{_datadir}/ghostscript/fonts/u004006t.gsf
%{_datadir}/ghostscript/fonts/bchb.pfa
%{_datadir}/ghostscript/fonts/bchbi.pfa
%{_datadir}/ghostscript/fonts/bchr.pfa
%{_datadir}/ghostscript/fonts/bchri.pfa
%{_datadir}/ghostscript/fonts/hrger.pfa
%{_datadir}/ghostscript/fonts/hrgrr.pfa
%{_datadir}/ghostscript/fonts/hritr.pfa
%{_datadir}/ghostscript/fonts/hrpld.pfa
%{_datadir}/ghostscript/fonts/hrpldi.pfa
%{_datadir}/ghostscript/fonts/hrplt.pfa
%{_datadir}/ghostscript/fonts/hrplti.pfa
%{_datadir}/ghostscript/fonts/hrscc.pfa
%{_datadir}/ghostscript/fonts/hrscs.pfa
%{_datadir}/ghostscript/fonts/putb.pfa
%{_datadir}/ghostscript/fonts/putbi.pfa
%{_datadir}/ghostscript/fonts/putr.pfa
%{_datadir}/ghostscript/fonts/putri.pfa
%{_datadir}/ghostscript/fonts/fhirw.pfm
%{_datadir}/ghostscript/fonts/fkarw.pfm
%{_datadir}/ghostscript/fonts/u003043t.pfm
%{_datadir}/ghostscript/fonts/u004006t.pfm

%files std-converted
%defattr(0644,root,root,0755)
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/CenturySchL-*.ttf
%{_datadir}/fonts/truetype/Dingbats.ttf
%{_datadir}/fonts/truetype/NimbusMonL-*.ttf
%{_datadir}/fonts/truetype/NimbusRomNo9L-*.ttf
%{_datadir}/fonts/truetype/NimbusSanL-*.ttf
%{_datadir}/fonts/truetype/StandardSymL.ttf
%{_datadir}/fonts/truetype/URWBookmanL-*.ttf
%{_datadir}/fonts/truetype/URWChanceryL-MediItal.ttf
%{_datadir}/fonts/truetype/URWGothicL-*.ttf
%{_datadir}/fonts/truetype/URWPalladioL-*.ttf

%changelog
