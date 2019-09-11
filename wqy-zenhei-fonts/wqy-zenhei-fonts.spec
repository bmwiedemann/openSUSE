#
# spec file for package wqy-zenhei-fonts
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


%define enable_setup_ui 0
Name:           wqy-zenhei-fonts
Version:        0.9.47+snapshot20141019
Release:        0
Summary:        Open-source Chinese Font for Hei Ti
License:        GPL-2.0-with-font-exception
Group:          System/X11/Fonts
Url:            http://wenq.org
Source0:        wqy-zenhei-0.9.47-nightlybuild.tar.gz
Patch0:         wqy-zenhei.conf.diff
Patch1:         wqy-zenhei-sharp.conf.diff
Patch2:         zenhei-config.desktop.diff
Patch3:         zenheiset.diff
BuildRequires:  fontpackages-devel
Requires(pre):  fontconfig
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       scalable-font-zh-TW
Provides:       ttf-wqy-zenhei = %{version}
Provides:       locale(zh_TW;zh_CN;zh_SG)
Obsoletes:      ttf-wqy-zenhei <= 0.9.41
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The WenQuanYi Zen Hei is the first open-source Chinese font
for Hei Ti, a sans-serif font style that are widely used for
general purpose text formatting, and on-screen
display of Chinese characters (such as in Windows Vista and Mac OS).
Simple and elegant font outlines and slightly emboldened strokes
makes the glyphs presenting higher contrast and therefore easy
to read. The unique style of this font also provide a simple
interface for adding grid-fitting information for further
fine-tuning of the on-screen performance.

WenQuanYi Zen Hei contains arguably the largest number of Chinese
Hanzi glyphs of all known open-source outline Chinese fonts: it has
20194 Hanzi glyphs covering 97% of the Unicode CJK Unified
Ideographics [4]. This font provides full coverage to the required
code points for zh_cn, zh_sg, zh_tw, zh_hk and zh_mo locales. The
total vector glyphs in this font is over 35000 including Latin characters,
Japanese kanas, hanguls and symbols from many other languages.

Highly regarded WenQuanYi Bitmap Song fonts were embedded into this
font for those who prefer shaper look of the text rendering, The
embedded bitmap glyphs cover font sizes at 9pt, 10pt, 11pt
and 12pt.

The primary purpose of developing this font is to provide CJK
(Chinese-Japanese-Korean) users a visually pleasing, standard
compliant, platform independent and compact solution for displaying
and printing Chinese on their computers.

We wish you enjoying the font, and joining us to continuously
improve this font for better performance and wider applications.

%if %{enable_setup_ui}
%package -n zenhei-config
Summary:        Wqy-zenhei-font configuration tool
Group:          System/I18n/Chinese
BuildRequires:  update-desktop-files
Requires:       %{name} = %{version}
Requires:       zenity

%description -n zenhei-config
Wqy-zenhei-font configuration tool, use it to set the preference of zenhei-font
%endif

%prep
%setup -q -n wqy-zenhei
%patch0
%patch1
%patch2
%patch3

%build
# Do nothing for build

%install

%if %{enable_setup_ui}
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 zenheiset %{buildroot}%{_bindir}/zenheiset
install -c -m 755 wqy-zenhei-cfg %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
install -c -m 644 zenhei-config.desktop %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file zenhei-config

for lang in zh zh_CN zh_HK zh_TW ; do
	mkdir -p %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
        cp i18n/$lang/wqy-zenhei.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/wqy-zenhei-cfg.mo
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -c -m 644 pixmap/wqy-zenhei-cfg.png %{buildroot}%{_datadir}/pixmaps/
%endif

mkdir -p %{buildroot}%{_ttfontsdir}
mkdir -p %{buildroot}%{_fontsconfavaildir}
install -c -m 644 wqy-zenhei.ttc %{buildroot}%{_ttfontsdir}
#44- is too early to include in, embeddedbitmap will be enabled later, so move to 57-
install -c -m 644 44-wqy-zenhei.conf %{buildroot}%{_fontsconfavaildir}/57-wqy-zenhei.conf
install -c -m 644 43-wqy-zenhei-sharp.conf %{buildroot}%{_fontsconfavaildir}/57-wqy-zenhei-sharp.conf
%link_avail_to_system_fontsconf 57-wqy-zenhei.conf

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%if %{enable_setup_ui}
%doc ChangeLog AUTHORS COPYING README
%else
%doc ChangeLog AUTHORS COPYING README zenheiset
%endif
%dir %{_datadir}/fonts/truetype
%{_ttfontsdir}/wqy-zenhei.ttc
%{files_fontsconf_availdir}
%files_fontsconf_file -l 57-wqy-zenhei.conf
%files_fontsconf_file 57-wqy-zenhei-sharp.conf

%if %{enable_setup_ui}
%files -n zenhei-config
%defattr(-, root,root)
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/locale/*/LC_MESSAGES/wqy-zenhei-cfg.mo
%endif

%changelog
