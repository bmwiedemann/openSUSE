#
# spec file for package scim-tables
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scim-tables
Version:        0.5.14.1
Release:        0
Summary:        Data Files for SCIM Generic Table Input Method Module
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/scim-im/scim-tables
Source:         https://github.com/scim-im/scim-tables/archive/%{name}-%{version}.tar.gz
#PATCH-FIX-SLE define G_GNUC_BEGIN/END_xx for glib < 2.32
Patch:          G_GNUC_BEGIN_IGNORE_DEPRECATIONS.patch
#PATCH-FIX-UPSTREAM delete unused variables
Patch1:         unused-variable.patch
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  scim-devel
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sles_version}
BuildRequires:  gtk2-devel
%else
BuildRequires:  gtk3-devel
%endif

%description
Data files for SCIM generic table input method module.

%package zh
Summary:        SCIM Chinese Data Files
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       locale(scim-tables:zh)

%description zh
This package includes SCIM table IM data files in Chinese.

The data files come from UNICON and XCIN.

%package ja
Summary:        SCIM Japanese Data Files
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
Provides:       locale(scim-tables:ja)

%description ja
This package includes the SCIM table IM data files in Japanese.

The data files come from UNICON.

%package ko
Summary:        SCIM Korean Data Files
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Provides:       locale(scim-tables:ko)

%description ko
This package includes SCIM table IM data files in Korean.

The data files come from UNICON.

%package additional
Summary:        Input Method data for non-CJK languages, including Russian etc
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       locale(scim-tables:am;ar;bn;gu;hi;kn;ml;ne;pa;ru;ta;te;th;vi)

%description additional
Input Method data for non-CJK languages, including Russian etc. for the
scim-tables input method module.

%lang_package

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -p1
%patch1 -p1

%build
./bootstrap
%configure \
    --enable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.a" -delete -print
find %{buildroot} -name "*.la" -delete -print
%find_lang %{name}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/scim-make-table
%{_mandir}/man1/scim-make-table.1%{ext_man}
%{_scim_enginedir}/table.so
%{_scim_uidir}/table-imengine-setup.so
%{_scim_icondir}/table.png

%files zh
%defattr(-,root,root)
%doc tables/zh/README-CangJie.txt
%doc tables/zh/README-Erbi.txt
%doc tables/zh/README-Wu.txt
%{_scim_tabledir}/Array30.bin
%{_scim_tabledir}/CangJie.bin
%{_scim_tabledir}/CangJie3.bin
%{_scim_tabledir}/CangJie5.bin
%{_scim_tabledir}/Cantonese.bin
%{_scim_tabledir}/CantonHK.bin
%{_scim_tabledir}/CNS11643.bin
%{_scim_tabledir}/Dayi3.bin
%{_scim_tabledir}/Erbi.bin
%{_scim_tabledir}/Erbi-QS.bin
%{_scim_tabledir}/EZ-Big.bin
%{_scim_tabledir}/Jyutping.bin
%{_scim_tabledir}/Quick.bin
%{_scim_tabledir}/Simplex.bin
%{_scim_tabledir}/Stroke5.bin
%{_scim_tabledir}/Wu.bin
%{_scim_tabledir}/Wubi.bin
%{_scim_tabledir}/ZhuYin.bin
%{_scim_tabledir}/ZhuYin-Big.bin
%{_scim_tabledir}/Ziranma.bin
%{_scim_icondir}/Array30.png
%{_scim_icondir}/CangJie.png
%{_scim_icondir}/CangJie3.png
%{_scim_icondir}/Cantonese.png
%{_scim_icondir}/CantonHK.png
%{_scim_icondir}/CNS11643.png
%{_scim_icondir}/Dayi.png
%{_scim_icondir}/EZ.png
%{_scim_icondir}/Erbi-QS.png
%{_scim_icondir}/Erbi.png
%{_scim_icondir}/Jyutping.png
%{_scim_icondir}/Quick.png
%{_scim_icondir}/Simplex.png
%{_scim_icondir}/Stroke5.png
%{_scim_icondir}/Wu.png
%{_scim_icondir}/Wubi.png
%{_scim_icondir}/ZhuYin.png
%{_scim_icondir}/Ziranma.png

%files ja
%defattr(-,root,root)
%{_scim_tabledir}/HIRAGANA.bin
%{_scim_tabledir}/KATAKANA.bin
%{_scim_tabledir}/Nippon.bin
%{_scim_icondir}/HIRAGANA.png
%{_scim_icondir}/KATAKANA.png
%{_scim_icondir}/Nippon.png

%files ko
%defattr(-,root,root)
%{_scim_tabledir}/Hangul.bin
%{_scim_tabledir}/Hanja.bin
%{_scim_tabledir}/HangulRomaja.bin
%{_scim_icondir}/Hangul.png
%{_scim_icondir}/Hanja.png

%files additional
%defattr(-, root, root)
%{_scim_tabledir}/Amharic.bin
%{_scim_tabledir}/Arabic.bin
%{_scim_tabledir}/Nepali_Rom.bin
%{_scim_tabledir}/Nepali_Trad.bin
%{_scim_tabledir}/Yawerty.bin
%{_scim_tabledir}/Viqr.bin
%{_scim_tabledir}/IPA-X-SAMPA.bin
%{_scim_tabledir}/LaTeX.bin
%{_scim_tabledir}/Bengali-inscript.bin
%{_scim_tabledir}/Bengali-probhat.bin
%{_scim_tabledir}/Gujarati-inscript.bin
%{_scim_tabledir}/Gujarati-phonetic.bin
%{_scim_tabledir}/Hindi-inscript.bin
%{_scim_tabledir}/Hindi-phonetic.bin
%{_scim_tabledir}/Kannada-inscript.bin
%{_scim_tabledir}/Kannada-kgp.bin
%{_scim_tabledir}/Malayalam-inscript.bin
%{_scim_tabledir}/Malayalam-phonetic.bin
%{_scim_tabledir}/Punjabi-inscript.bin
%{_scim_tabledir}/Punjabi-jhelum.bin
%{_scim_tabledir}/Punjabi-phonetic.bin
%{_scim_tabledir}/Tamil-inscript.bin
%{_scim_tabledir}/Tamil-phonetic.bin
%{_scim_tabledir}/Tamil-remington.bin
%{_scim_tabledir}/Telugu-inscript.bin
%{_scim_tabledir}/Thai.bin
%{_scim_tabledir}/Translit.bin
%{_scim_tabledir}/Ukrainian-Translit.bin
%{_scim_tabledir}/Hindi-remington.bin
%{_scim_tabledir}/IPA-Kirshenbaum.bin
%{_scim_tabledir}/Marathi-remington.bin
%{_scim_tabledir}/Punjabi-remington.bin
%{_scim_tabledir}/RussianTraditional.bin
%{_scim_tabledir}/SmartCangJie6.bin
%{_scim_tabledir}/Tamil-tamil99.bin
%{_scim_tabledir}/Uyghur-Romanized.bin
%{_scim_tabledir}/Uyghur-Standard.bin
%{_scim_tabledir}/classicalhebrew.bin
%{_scim_tabledir}/greekpoly.bin
%{_scim_tabledir}/HebrewComputer.bin
%{_scim_tabledir}/RussianComputer.bin
%{_scim_icondir}/Amharic.png
%{_scim_icondir}/Arabic.png
%{_scim_icondir}/Nepali.png
%{_scim_icondir}/Yawerty.png
%{_scim_icondir}/Viqr.png
%{_scim_icondir}/IPA-X-SAMPA.png
%{_scim_icondir}/LaTeX.png
%{_scim_icondir}/Bengali-inscript.png
%{_scim_icondir}/Bengali-probhat.png
%{_scim_icondir}/Gujarati-inscript.png
%{_scim_icondir}/Gujarati-phonetic.png
%{_scim_icondir}/Hindi-inscript.png
%{_scim_icondir}/Hindi-phonetic.png
%{_scim_icondir}/Kannada-inscript.png
%{_scim_icondir}/Kannada-kgp.png
%{_scim_icondir}/Malayalam-inscript.png
%{_scim_icondir}/Malayalam-phonetic.png
%{_scim_icondir}/Punjabi-inscript.png
%{_scim_icondir}/Punjabi-jhelum.png
%{_scim_icondir}/Punjabi-phonetic.png
%{_scim_icondir}/Tamil-inscript.png
%{_scim_icondir}/Tamil-phonetic.png
%{_scim_icondir}/Tamil-remington.png
%{_scim_icondir}/Telugu-inscript.png
%{_scim_icondir}/Thai.png
%{_scim_icondir}/Hindi-remington.png
%{_scim_icondir}/Marathi-remington.png
%{_scim_icondir}/Punjabi-remington.png
%{_scim_icondir}/RussianTraditional.png
%{_scim_icondir}/SmartCangJie6.png
%{_scim_icondir}/Tamil-tamil99.png
%{_scim_icondir}/Translit.png
%{_scim_icondir}/Ukrainian-Translit.png
%{_scim_icondir}/Uyghur.png
%{_scim_icondir}/HebrewComputer.png
%{_scim_icondir}/RussianComputer.png

%files lang -f %{name}.lang
%defattr(-, root, root)

%changelog
