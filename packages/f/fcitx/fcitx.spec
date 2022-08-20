#
# spec file for package fcitx
#
# Copyright (c) 2022 SUSE LLC
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


%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif

Name:           fcitx
Version:        4.2.9.9
Release:        0
Summary:        Flexible Context-aware Input Tool with eXtension
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx
Source:         https://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz
Source1:        xim.d-fcitx
Source2:        fcitx-README.suse
Source3:        xim.fcitx.suse.template
Source8:        openSUSE-themes.tar.gz
Source9:        macros.%{name}
Source10:       %{name}.keyring
Source99:       baselibs.conf
Source100:      https://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz.sig
# PATCH-FIX-OPENSUSE fcitx-autostart-check-INPUT_METHOD.patch boo#947576
Patch2:         fcitx-autostart-check-INPUT_METHOD.patch
# PATCH-FIX-OPENSUSE downgrade cmake requirement to 3.1 again
Patch3:         fcitx-cmake-3.1.patch
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  iso-codes-devel
BuildRequires:  libicu-devel
BuildRequires:  libpresage-devel
# Only for leap < 15.2
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
BuildRequires:  libqt4-devel
%endif
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  opencc-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xkbfile)
Requires:       %{name}-branding = %{version}
Recommends:     %{name}-pinyin = %{version}-%{release}
Recommends:     %{name}-table = %{version}-%{release}
# These libraries are dlopen-ed in fcitx at runtime
# for spell-checking for keyboard users. ld can't find
# them, so explicitly recommends.
Recommends:     libenchant1
Recommends:     libopencc1_1
Recommends:     libpresage1
Provides:       locale(ko;zh_CN;zh_SG)

%description
Fcitx is a CJK input method framework. It supports Table,
Pinyin and QuWei input methods. It's flexible and fast.

%package -n libfcitx-core0
Summary:        Core library of fcitx
Group:          System/Libraries
Provides:       libfcitx-4_2_9 = %{version}
Obsoletes:      libfcitx-4_2_9 <= %{version}

%description -n libfcitx-core0
Core library of fcitx.

%package -n libfcitx-gclient1
Summary:        GClient library of fcitx
Group:          System/Libraries

%description -n libfcitx-gclient1
GClient library of fcitx

%package -n libfcitx-utils0
Summary:        Util library of fcitx
Group:          System/Libraries

%description -n libfcitx-utils0
Util library of fcitx

%package -n libfcitx-config4
Summary:        Config library of fcitx4
Group:          System/Libraries

%description -n libfcitx-config4
Config library of fcitx

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libfcitx-config4 = %{version}
Requires:       libfcitx-core0 = %{version}
Requires:       libfcitx-gclient1 = %{version}
Requires:       libfcitx-utils0 = %{version}

%description devel
Development header files for Fcitx input method framework.

%package gtk2
Summary:        Gtk2 IM module for %{name}
Group:          System/I18n/Chinese
Supplements:    (fcitx and libgtk-2_0-0)
%{gtk2_immodule_requires}

%description gtk2
GTK+ version 2 input module for Fcitx input method rfamework.

%package gtk3
Summary:        Gtk3 IM module for %{name}
Group:          System/I18n/Chinese
Supplements:    (fcitx and libgtk-3-0)
%{gtk3_immodule_requires}

%description gtk3
GTK+ version 3 input module for Fcitx input method framework.

%package -n typelib-1_0-Fcitx-1_0
Summary:        The Flexible Context-aware Input Tool with eXtension -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Fcitx-1_0
Fcitx is a CJK input method framework. It supports Table,
Pinyin and QuWei input methods. It's flexible and fast.

This package provides the GObject Introspection bindings for Fcitx.

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%package qt4
Summary:        Qt4 IM module for %{name}
Group:          System/I18n/Chinese
Supplements:    (fcitx and libqt4)

%description qt4
QT4 input module for Fcitx input method framework.
%endif

%package quwei
Summary:        Chinese Zone-bit(QuWei) engine for %{name}
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}

%description quwei
Chinese Zone-bit(QuWei) engine for Fcitx input method framework.

%package pinyin
Summary:        Chinese Pinyin engine for %{name}
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}

%description pinyin
Chinese Pinyin engine for Fcitx input method framework.

%package table
Summary:        Table engine for %{name}
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}

%description table
Table engine for Fcitx input method framework.

It's the basic component for other users except some Chinese.

%package table-cn-cangjie
Summary:        Simplified Chinese Tsang-Jei(Cangjie) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-cangjie
Fcitx Tsang Jei (Cang Jie) input tables for Simplified Chinese.

%package table-cn-dianbao
Summary:        Telegram(Dianbao) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-dianbao
Fcitx Telegram (Dian Bao) input tables for Simplified Chinese.

%package table-cn-erbi
Summary:        Two stroke(Erbi) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-erbi
Fcitx Two Stroke (Er Bi) input tables for Simplified Chinese.

%package table-cn-bingchan
Summary:        Icefrog Holography(QXM) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-bingchan
Fcitx Icefrog Holography (Bing Chan Quan Xi, or QXM) input tables for Simplified Chinese.

%package table-cn-wanfeng
Summary:        Evening Breeze(Wanfeng) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-wanfeng
Fcitx Evening Breeze (Wan feng) input tables for Simplified Chinese.

%package table-cn-wubi-pinyin
Summary:        Wubi and pinyin(wubi-pinyin) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
Provides:       locale(fcitx-table:zh_CN;)
BuildArch:      noarch

%description table-cn-wubi-pinyin
Fcitx Wubi (Wu Bi Zi Xing) and Pinyin mixed input tables for Simplified Chinese.

Wubi in Fcitx is based on wubi x86.

%package table-cn-wubi
Summary:        Wubi table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
Provides:       locale(fcitx-table:zh_CN;)
BuildArch:      noarch

%description table-cn-wubi
Fcitx Wubi (Wu Bi Zi Xing) input tables for Simplified Chinese.

Wubi in Fcitx is based on wubi x86.

%package table-cn-ziran
Summary:        Nature(Ziran) table for %{name}
Group:          System/I18n/Chinese
Requires:       %{name}-table = %{version}-%{release}
BuildArch:      noarch

%description table-cn-ziran
Fcitx Nature (Zi Ran Ma) input tables for Simplified Chinese.

%package table-tools
Summary:        Fcitx tools to make tables
Group:          System/I18n/Chinese

%description table-tools
Tools to convert txt word sheets to fcitx tables.

see manpage for details

%package pinyin-tools
Summary:        Fcitx tools to make pinyin match list
Group:          System/I18n/Chinese

%description pinyin-tools
Tools to convert txt or scel(sougou pinyin data format) pinyin sheets to fcitx match lists.

%package branding-openSUSE
Summary:        openSUSE default Skins for Fcitx
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and branding-openSUSE)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-openSUSE
openSUSE default skins for Fcitx

You can either use this package or download from kde-look.org using knewstaff in fcitx-config-kde4.

%package skin-new-air
Summary:        New Air skin for Fcitx
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
BuildArch:      noarch

%description skin-new-air
New Air skin for Fcitx, inspired by KDE Air theme.

You can either use this package or download from kde-look.org using knewstaff in
fcitx-config-kde4.

%package skin-classic
Summary:        Fcitx Classic Skin
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description skin-classic
Fcitx classic skin.

You can either use this package or download from kde-look.org using knewstaff in fcitx-config-kde4.

%package skin-dark
Summary:        Fcitx Dark Skin
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description skin-dark
Fcitx dark skin.

You can either use this package for download from kde-look.org using knewstaff in fcitx-config-kde4.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

%build
mkdir build
cd build

# fix dlopen-ed library name
cmake .. \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_VERBOSE_MAKEFILE=On \
        -DCMAKE_BUILD_TYPE=Release \
        -DOPENCC_LIBRARY_FILENAME=libopencc.so.2 \
        -DENCHANT_LIBRARY_FILENAME=libenchant.so.1 \
        -DPRESAGE_LIBRARY_FILENAME=libpresage.so.1 \
        -DENABLE_GTK3_IM_MODULE=On \
%if 0%{?sles_version} || 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
        -DENABLE_QT=Off \
        -DENABLE_QT_IM_MODULE=off \
%endif
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DLIB_INSTALL_DIR=%{_libdir} \
        -DSYSCONFDIR=%{_sysconfdir} \
        -DENABLE_LUA=On

# fix gobject-introspection build
export SUSE_ASNEEDED=0
%make_build

%install
%cmake_install

# install openSUSE skins
tar -xzf %{SOURCE8}
mv openSUSE-themes/Harlequin %{buildroot}%{_datadir}/%{name}/skin/
mv openSUSE-themes/Dartmouth %{buildroot}%{_datadir}/%{name}/skin/
mv openSUSE-themes/NewAir %{buildroot}%{_datadir}/%{name}/skin/

%suse_update_desktop_file fcitx Utility DesktopUtility
%suse_update_desktop_file fcitx-skin-installer Utility DesktopUtility
%suse_update_desktop_file fcitx-configtool Settings DesktopSettings

# fix doc
mkdir -p %{buildroot}%{_docdir}/
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/
cp -r %{SOURCE2} %{buildroot}%{_docdir}/%{name}/
cp -r %{SOURCE3} %{buildroot}%{_docdir}/%{name}/
cp -r AUTHORS %{buildroot}%{_docdir}/%{name}/
cp -r ChangeLog %{buildroot}%{_docdir}/%{name}/

# create autostart
mkdir -p %{buildroot}%{_distconfdir}/X11/xim.d/
install -m 644 %{SOURCE1} %{buildroot}%{_distconfdir}/X11/xim.d/fcitx

priority=30
pushd  %{buildroot}%{_distconfdir}/X11/xim.d/
    for lang in am ar as bn el fa gu he hi hr ja ka kk kn ko lo ml my \
                pa ru sk vi zh_TW zh_CN zh_HK zh_SG \
                de fr it es nl cs pl da nn nb fi en sv ; do
        mkdir $lang
        pushd $lang
            ln -s ../fcitx $priority-fcitx
        popd
    done
popd

# install rpm macros
install -D -m644 %{SOURCE9} %{buildroot}%{_rpmmacrodir}/macros.%{name}

# remove *.la
rm -rf %{buildroot}%{_libdir}/lib%{name}-config.la

# fix scripts
for script in $(ls %{buildroot}%{_datadir}/cmake/fcitx/*.sh) ; do
  sed -i "s/\/usr\/bin\/env bash/\/usr\/bin\/bash/" $script;
  chmod +x $script;
done
sed -i "s/\/usr\/bin\/env bash/\/usr\/bin\/bash/" %{buildroot}%{_bindir}/fcitx-diagnose

%find_lang %{name}

%fdupes %{buildroot}

%post gtk2
%{gtk2_immodule_post}

%postun gtk2
%{gtk2_immodule_postun}

%post gtk3
%{gtk3_immodule_post}

# Add fcitx icons to gnome3 panel
TARGET="%{_datadir}/gnome-shell/js/ui/statusIconDispatcher.js"
if [ -f $TARGET ] && [ ! -f $TARGET-fcitx ] ; then
mv $TARGET $TARGET-fcitx
sed "/^const STANDARD_TRAY_ICON_IMPLEMENTATIONS/a \    'fcitx': 'input-method'," $TARGET-fcitx > $TARGET
fi

%postun gtk3
%{gtk3_immodule_postun}

%post
%desktop_database_post
%icon_theme_cache_post
exit 0

%postun
%desktop_database_postun
%icon_theme_cache_postun
exit 0

%post -n libfcitx-core0 -p /sbin/ldconfig
%post -n libfcitx-gclient1 -p /sbin/ldconfig
%post -n libfcitx-utils0 -p /sbin/ldconfig
%post -n libfcitx-config4 -p /sbin/ldconfig
%postun -n libfcitx-core0 -p /sbin/ldconfig
%postun -n libfcitx-gclient1 -p /sbin/ldconfig
%postun -n libfcitx-utils0 -p /sbin/ldconfig
%postun -n libfcitx-config4 -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-autostart
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-skin-installer
%{_bindir}/%{name}-dbus-watcher
%{_bindir}/%{name}-diagnose
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/mime/packages/*
%{_datadir}/dbus-1/services/org.fcitx.Fcitx.service
%{_mandir}/man1/fcitx.1%{?ext_man}
%{_mandir}/man1/fcitx-remote.1%{?ext_man}
%{_libdir}/%{name}/
%{_sysconfdir}/xdg/autostart/%{name}*.desktop
%{_distconfdir}/X11/xim.d
%doc %{_docdir}/%{name}/

# excludes
%exclude %{_datadir}/%{name}/pinyin
%exclude %{_datadir}/%{name}/table/*
%exclude %{_datadir}/%{name}/imicon/*
%exclude %{_datadir}/%{name}/inputmethod/*
%exclude %{_datadir}/%{name}/addon/%{name}-pinyin.conf
%exclude %{_datadir}/%{name}/addon/%{name}-table.conf
%exclude %{_datadir}/%{name}/addon/%{name}-qw.conf
%exclude %{_datadir}/%{name}/configdesc/%{name}-pinyin.desc
%exclude %{_datadir}/%{name}/configdesc/table.desc
%exclude %{_libdir}/%{name}/fcitx-pinyin.so
%exclude %{_libdir}/%{name}/fcitx-table.so
%exclude %{_libdir}/%{name}/fcitx-qw.so
%exclude %{_libdir}/%{name}/libexec/comp-spell-dict
%exclude %{_libdir}/%{name}/libexec/fcitx-po-parser
%exclude %{_libdir}/%{name}/libexec/fcitx-scanner
%exclude %{_datadir}/%{name}/skin/Harlequin
%exclude %{_datadir}/%{name}/skin/Dartmouth
%exclude %{_datadir}/%{name}/skin/NewAir
%exclude %{_datadir}/%{name}/skin/classic
%exclude %{_datadir}/%{name}/skin/dark

%files -n libfcitx-core0
%{_libdir}/libfcitx-core.so.0
%{_libdir}/libfcitx-core.so.0.3

%files -n libfcitx-gclient1
%{_libdir}/libfcitx-gclient.so.1
%{_libdir}/libfcitx-gclient.so.0.2

%files -n libfcitx-utils0
%{_libdir}/libfcitx-utils.so.0
%{_libdir}/libfcitx-utils.so.0.1

%files -n libfcitx-config4
%{_libdir}/libfcitx-config.so.4
%{_libdir}/libfcitx-config.so.4.1

%files gtk2
%{_libdir}/gtk-2.0/*

%files gtk3
%{_libdir}/gtk-3.0/*

%files -n typelib-1_0-Fcitx-1_0
%{_libdir}/girepository-1.0/Fcitx-1.0.typelib

%files quwei
%{_libdir}/%{name}/%{name}-qw.so
%{_datadir}/%{name}/inputmethod/qw.conf
%{_datadir}/%{name}/addon/%{name}-qw.conf

%files pinyin
%{_libdir}/%{name}/%{name}-pinyin.so
%{_datadir}/%{name}/pinyin/
%{_datadir}/%{name}/inputmethod/pinyin.conf
%{_datadir}/%{name}/inputmethod/shuangpin.conf
%{_datadir}/%{name}/addon/%{name}-pinyin.conf
%{_datadir}/%{name}/imicon/pinyin.png
%{_datadir}/%{name}/imicon/shuangpin.png
%{_datadir}/%{name}/configdesc/%{name}-pinyin.desc

%files table
%{_libdir}/%{name}/%{name}-table.so
%{_datadir}/%{name}/addon/%{name}-table.conf
%{_datadir}/%{name}/configdesc/table.desc

%files table-cn-cangjie
%{_datadir}/%{name}/table/cangjie.*
%{_datadir}/%{name}/imicon/cangjie.png

%files table-cn-dianbao
%{_datadir}/%{name}/table/db.*

%files table-cn-erbi
%{_datadir}/%{name}/table/erbi.*
%{_datadir}/%{name}/imicon/erbi.png

%files table-cn-bingchan
%{_datadir}/%{name}/table/qxm.*

%files table-cn-wanfeng
%{_datadir}/%{name}/table/wanfeng.*

%files table-cn-wubi-pinyin
%{_datadir}/%{name}/table/wbpy.*
%{_datadir}/%{name}/imicon/wbpy.png

%files table-cn-wubi
%{_datadir}/%{name}/table/wbx.*
%{_datadir}/%{name}/imicon/wubi.png

%files table-cn-ziran
%{_datadir}/%{name}/table/zrm.*
%{_datadir}/%{name}/imicon/ziranma.png

%files table-tools
%{_bindir}/mb2txt
%{_bindir}/txt2mb
%{_mandir}/man1/mb2txt.1%{?ext_man}
%{_mandir}/man1/txt2mb.1%{?ext_man}

%files pinyin-tools
%{_bindir}/createPYMB
%{_bindir}/readPYMB
%{_bindir}/readPYBase
%{_bindir}/mb2org
%{_bindir}/scel2org
%{_mandir}/man1/createPYMB.1%{?ext_man}
%{_mandir}/man1/readPYMB.1%{?ext_man}
%{_mandir}/man1/readPYBase.1%{?ext_man}
%{_mandir}/man1/mb2org.1%{?ext_man}
%{_mandir}/man1/scel2org.1%{?ext_man}

%files branding-openSUSE
%{_datadir}/%{name}/skin/Harlequin
%{_datadir}/%{name}/skin/Dartmouth

%files skin-new-air
%{_datadir}/%{name}/skin/NewAir

%files skin-classic
%{_datadir}/%{name}/skin/classic

%files skin-dark
%{_datadir}/%{name}/skin/dark

%files devel
%{_rpmmacrodir}/macros.%{name}
%{_includedir}/*
%{_bindir}/%{name}4-config
%{_libdir}/%{name}/libexec/comp-spell-dict
%{_libdir}/%{name}/libexec/fcitx-po-parser
%{_libdir}/%{name}/libexec/fcitx-scanner
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/
%{_datadir}/gir-1.0/Fcitx-1.0.gir
%{_libdir}/libfcitx-config.so
%{_libdir}/libfcitx-core.so
%{_libdir}/libfcitx-utils.so
%{_libdir}/libfcitx-gclient.so

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%files qt4
%{_libdir}/qt4/*
%endif

%changelog
