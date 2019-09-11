#
# spec file for package fcitx-table-extra
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


Name:           fcitx-table-extra
Version:        0.3.8
Release:        0
Summary:        Extra table for Fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-table-extra
Source:         http://download.fcitx-im.org/fcitx-table-extra/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-table-tools
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fcitx-table-extra provides extra Chinese tables for Fcitx.

%package -n fcitx-table-tw-boshiamy
Summary:        Boshiamy table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}
Provides:       locale(fcitx-table:zh_TW;)

%description -n fcitx-table-tw-boshiamy
Fcitx Boshiamy table for Traditional Chinese.

%package -n fcitx-table-tw-cangjie3
Summary:        Tsang Jei 3 table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-cangjie3
Fcitx Tsang Jei (Cang Jie) 3 table for Traditional Chinese.

%package -n fcitx-table-tw-cangjie5
Summary:        Tsang Jei 5 table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}
Provides:       locale(fcitx-table:zh_TW;)

%description -n fcitx-table-tw-cangjie5
Fcitx Tsang Jei (Cang Jie) 5 table for Traditional Chinese.

%package -n fcitx-table-tw-cangjie-large
Summary:        Tsang Jei large character set table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}
Provides:       locale(fcitx-table:zh_TW;)

%description -n fcitx-table-tw-cangjie-large
Fcitx Tsang Jei (Cang Jie) table with large character set 
for Traditional Chinese.

%package -n fcitx-table-tw-smart-cangjie6
Summary:        Smart Tsang Jei 6 table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}
Provides:       locale(fcitx-table:zh_TW;)

%description -n fcitx-table-tw-smart-cangjie6
Fcitx Smart Tsang Jei (Fast Cang Jie) 6 table for Traditional Chinese.

%package -n fcitx-table-cn-cantonese
Summary:        Standard Guongdonkwa Penkyampji table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-cn-cantonese
Fcitx Guongdonkwa Penkyampji(Cantonese Pinyin) table for Simplified Chinese.

Cantonese Pinyin is a table input method, but it's not the pinyin used 
in Mainland China, but derivative schemes used by overseas Chinese in
Hongkong, Kuala Lumpur, Sydney, Auckland, and Vancouver.
This standard is released by Education department of Canton Province 
in 1960s.

See: http://en.wikipedia.org/wiki/Guangdong_Romanization for details

If you don't know what it is, don't try.

%package -n fcitx-table-hk-cantonese
Summary:        Hong Kong Guongdonkwa Penkyampji table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-hk-cantonese
Fcitx Hong Kong Guongdonkwa Penkyampji table for Traditional Chinese.

This is Hong Kong derivative of the standard Guongdonkwa Penkyampji schemes.

See: http://en.wikipedia.org/wiki/Guangdong_Romanization for details

If you don't know what it is, don't try.

%package -n fcitx-table-hk-jyutping
Summary:        Hong Kong jyutping table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-hk-jyutping
Fcitx Hong Kong Jyutping table for Traditional Chinese.

This is the jyutping schemes released by Hong Kong government
in colony era.

It's used to convert Chinese person and road names to English,
which can be pronounced easily in International Phonetic Alphabet
and followed by a native Hongkongnese.

But people seldomly use it to type in Chinese. its pronounciation 
is hard for a native Chinese to learn. 

And it's a incomplete scheme.

See: http://en.wikipedia.org/wiki/Hong_Kong_Government_Cantonese_Romanisation  for details

If you don't know what it is, don't try.

%package -n fcitx-table-hk-stroke5
Summary:        Hong Kong 5 stroke input table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-hk-stroke5
Fcitx Hong Kong 5 stroke input table for Traditional Chinese.

%package -n fcitx-table-tw-easy-large
Summary:        Easy table with large character set for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-easy-large
Fcitx Easy (Heng Sung) table with large character set
for Traditional Chinese.

%package -n fcitx-table-tw-quick3
Summary:        Quick 3 table for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-quick3
Fcitx Quick (Cuk Sing) 3 table for Traditional Chinese.

%package -n fcitx-table-tw-quick5
Summary:        Quick 5 table for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-quick5
Fcitx Quick (Cuk Sing) 5 table for Traditional Chinese.

%package -n fcitx-table-tw-quick-classic
Summary:        Quick Classic table for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-quick-classic
Fcitx Quick (Cuk Sing) Classic table for Traditional Chinese.

%package -n fcitx-table-tw-array30
Summary:        Array 30 table for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-array30
Fcitx Array 30 (hang laat 30) table for Traditional Chinese.

%package -n fcitx-table-tw-array30-large
Summary:        Array 30 table with large character set for Traditional Chinese
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-tw-array30-large
Fcitx Array 30 (hang laat 30) table with large character set
for Traditional Chinese.

%package -n fcitx-table-cn-wubi-large
Summary:        Wubi large character set table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}
Provides:       locale(fcitx-table:zh_CN;)

%description -n fcitx-table-cn-wubi-large
Fcitx Wubi (Wu Bi Zi Xing) table with large character set
for Simplified Chinese.

Wubi in Fcitx is based on wubi x86.

%package -n fcitx-table-cn-wu
Summary:        Wu table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-cn-wu
Fcitx Wu table for Simplified Chinese.

It's not Wubi, but Shanghainese.

Wu is a dialect used in a few provinces in the south end beach of yangtse river.

If you don't know what it is, don't try.

%package -n fcitx-table-cn-zhengma
Summary:        Cheng table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-cn-zhengma
Fcitx Cheng (Zheng Ma) table for Simplified Chinese.

%package -n fcitx-table-cn-zhengma-large
Summary:        Cheng large character set table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-cn-zhengma-large
Fcitx Cheng (Zheng Ma) table with large character set 
for Simplified Chinese.

%package -n fcitx-table-t9
Summary:        T9 table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
%{fcitx_table_requires}
BuildArch:      noarch
Provides:       %{name} = %{version}

%description -n fcitx-table-t9
Fcitx T9 table.

%package lang 
Summary:        Languages for package %{name} 
License:        GPL-2.0+ and SUSE-Public-Domain
Group:          System/Localization 
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
%if 0%{?suse_version}
Supplements:    packageand(bundle-lang-other:%{name}) 
%endif
BuildArch:      noarch 

%description lang 
Provides translations to the package %{name}

%prep
%setup -q

%build
%{__mkdir} -pv build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} ..
make %{?_smp_mflags}

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang %{name}

%fdupes %{buildroot}

%files lang -f %{name}.lang
%defattr(-,root,root)
%doc COPYING

%files -n fcitx-table-tw-boshiamy
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/boshiamy.*
%{_datadir}/icons/hicolor/*/apps/fcitx-boshiamy.png
%{_fcitx_imicondir}/boshiamy.png

%files -n fcitx-table-tw-cangjie3
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/cangjie3.*

%files -n fcitx-table-tw-cangjie5
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/cangjie5.*

%files -n fcitx-table-tw-cangjie-large
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/cangjie-big.*

%files -n fcitx-table-tw-smart-cangjie6
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/scj6.*
%{_datadir}/icons/hicolor/*/apps/fcitx-scj6.png
%{_fcitx_imicondir}/scj6.png

%files -n fcitx-table-cn-cantonese
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/cantonese.*
%{_datadir}/icons/hicolor/*/apps/fcitx-cantonese.png
%{_fcitx_imicondir}/cantonese.png

%files -n fcitx-table-hk-cantonese
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/cantonhk.*
%{_datadir}/icons/hicolor/*/apps/fcitx-cantonhk.png
%{_fcitx_imicondir}/cantonhk.png

%files -n fcitx-table-hk-jyutping
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/jyutping.*
%{_datadir}/icons/hicolor/*/apps/fcitx-jyutping.png
%{_fcitx_imicondir}/jyutping.png

%files -n fcitx-table-hk-stroke5
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/stroke5.*
%{_datadir}/icons/hicolor/*/apps/fcitx-stroke5.png
%{_fcitx_imicondir}/stroke5.png

%files -n fcitx-table-tw-easy-large
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/easy-big.*
%{_datadir}/icons/hicolor/*/apps/fcitx-easy-big.png
%{_fcitx_imicondir}/easy-big.png

%files -n fcitx-table-tw-quick3
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/quick3.*
%{_datadir}/icons/hicolor/*/apps/fcitx-quick3.png
%{_fcitx_imicondir}/quick3.png

%files -n fcitx-table-tw-quick5
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/quick5.*
%{_datadir}/icons/hicolor/*/apps/fcitx-quick5.png
%{_fcitx_imicondir}/quick5.png

%files -n fcitx-table-tw-quick-classic
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/quick-classic.*
%{_datadir}/icons/hicolor/*/apps/fcitx-quick-classic.png
%{_fcitx_imicondir}/quick-classic.png

%files -n fcitx-table-tw-array30
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/array30.*
%{_datadir}/icons/hicolor/*/apps/fcitx-array30.png
%{_fcitx_imicondir}/array30.png

%files -n fcitx-table-tw-array30-large
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/array30-big.*
%{_datadir}/icons/hicolor/*/apps/fcitx-array30-big.png
%{_fcitx_imicondir}/array30-big.png

%files -n fcitx-table-cn-wubi-large
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/wubi-large.*

%files -n fcitx-table-cn-wu
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/wu.*
%{_datadir}/icons/hicolor/*/apps/fcitx-wu.png
%{_fcitx_imicondir}/wu.png

%files -n fcitx-table-cn-zhengma
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/zhengma.*
%{_datadir}/icons/hicolor/*/apps/fcitx-zhengma.png
%{_fcitx_imicondir}/zhengma.png

%files -n fcitx-table-cn-zhengma-large
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/zhengma-large.*

%files -n fcitx-table-t9
%defattr(-,root,root)
%doc COPYING
%{_fcitx_tabledir}/t9.*
%{_fcitx_imicondir}/t9.png
%{_datadir}/icons/hicolor/64x64/apps/fcitx-t9.png

%changelog
