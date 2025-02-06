#
# spec file for package fcitx5-chinese-addons
#
# Copyright (c) 2025 SUSE LLC
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


%define build_qt5 1
%define build_qt6 1
Name:           fcitx5-chinese-addons
Version:        5.1.8
Release:        0
Summary:        Pinyin and Table IM support for fcitx5
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-chinese-addons
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-lua-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libcurl-devel
BuildRequires:  libime-devel >= 1.0.12
BuildRequires:  opencc-devel
BuildRequires:  pkgconfig
BuildRequires:  zstd
%if %{build_qt6}
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-dbus-devel
BuildRequires:  qt6-webenginewidgets-devel
BuildRequires:  qt6-widgets-devel
%endif
%if %{build_qt5}
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libQt5DBus-devel
BuildRequires:  libqt5-qtwebengine-devel
%endif
Supplements:    fcitx5
Conflicts:      fcitx <= 4.2.9.8
Provides:       fcitx-cloudpinyin = %{version}
Provides:       fcitx-googlepinyin = %{version}
Provides:       fcitx-libpinyin = %{version}
Provides:       fcitx-pinyin = %{version}
Provides:       fcitx-sunpinyin = %{version}
Provides:       fcitx-table = %{version}
Provides:       fcitx-table-cn-bingchan = %{version}
Provides:       fcitx-table-cn-cangjie = %{version}
Provides:       fcitx-table-cn-dianbao = %{version}
Provides:       fcitx-table-cn-erbi = %{version}
Provides:       fcitx-table-cn-wanfeng = %{version}
Provides:       fcitx-table-cn-wubi = %{version}
Provides:       fcitx-table-cn-wubi-pinyin = %{version}
Provides:       fcitx-table-cn-ziran = %{version}
Obsoletes:      fcitx-cloudpinyin <= 0.3.7
Obsoletes:      fcitx-googlepinyin <= 0.1.6
Obsoletes:      fcitx-libpinyin <= 0.5.3
Obsoletes:      fcitx-pinyin <= 4.2.9.6
Obsoletes:      fcitx-sunpinyin <= 0.4.2
Obsoletes:      fcitx-table <= 4.2.9.6
Obsoletes:      fcitx-table-cn-bingchan < 4.2.9.6
Obsoletes:      fcitx-table-cn-cangjie < 4.2.9.6
Obsoletes:      fcitx-table-cn-dianbao < 4.2.9.6
Obsoletes:      fcitx-table-cn-erbi < 4.2.9.6
Obsoletes:      fcitx-table-cn-wanfeng < 4.2.9.6
Obsoletes:      fcitx-table-cn-wubi < 4.2.9.6
Obsoletes:      fcitx-table-cn-wubi-pinyin < 4.2.9.6
Obsoletes:      fcitx-table-cn-ziran < 4.2.9.6
%if 0%{?suse_version} == 1500
BuildRequires:  gcc8
BuildRequires:  gcc8-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
This provides pinyin and table input method support for fcitx5.

%if %{build_qt5}
%package -n fcitx5-pinyindictmanager
Summary:        Fcitx5 Pinyin dictionary manager library
Group:          System/Libraries
Supplements:    (fcitx5-chinese-addons and plasma5-workspace)

%description -n fcitx5-pinyindictmanager
Fcitx5 Pinyin dictionary manager library.

%package -n fcitx5-customphraseeditor
Summary:        Fcitx5 Custom Phrase editor library
Group:          System/Libraries
Supplements:    (fcitx5-chinese-addons and plasma5-workspace)

%description -n fcitx5-customphraseeditor
Fcitx5 Custom Phrase editor library.
%endif

%if %{build_qt6}
%package -n fcitx5-pinyindictmanager6
Summary:        Fcitx5 Pinyin dictionary manager library
Group:          System/Libraries
Supplements:    (fcitx5-chinese-addons and plasma6-workspace)

%description -n fcitx5-pinyindictmanager6
Fcitx5 Pinyin dictionary manager library.

%package -n fcitx5-customphraseeditor6
Summary:        Fcitx5 Custom Phrase editor library
Group:          System/Libraries
Supplements:    (fcitx5-chinese-addons and plasma6-workspace)

%description -n fcitx5-customphraseeditor6
Fcitx5 Custom Phrase editor library.
%endif

%package devel
Summary:        Development files for fcitx5-chinese-addons
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{build_qt5}
Requires:       fcitx5-customphraseeditor = %{version}
Requires:       fcitx5-pinyindictmanager = %{version}
%endif
%if %{build_qt6}
Requires:       fcitx5-customphraseeditor6 = %{version}
Requires:       fcitx5-pinyindictmanager6 = %{version}
%endif

%description devel
This package provides development files for fcitx5-chinese-addons.

%prep
%setup -q
%if %{build_qt6}
mkdir -p %{_builddir}/qt6_build
cp -r . %{_builddir}/qt6_build
%endif

%build
%if 0%{?suse_version} == 1500
export CC=gcc-8
export CXX=g++-8
%endif
%if %{build_qt5}
%cmake -DUSE_WEBKIT=OFF -DUSE_QT6=OFF
%make_build
%endif

%if %{build_qt6}
pushd %{_builddir}/qt6_build
%cmake -DUSE_WEBKIT=OFF
%make_build
popd
%endif

%install
%if %{build_qt5}
%cmake_install
%endif

%if %{build_qt6}
pushd %{_builddir}/qt6_build
%cmake_install
popd
%endif
%find_lang %{name}
%fdupes %{buildroot}

%if %{build_qt5}
%files -n fcitx5-pinyindictmanager
%{_fcitx5_qt5dir}/libpinyindictmanager.so

%files -n fcitx5-customphraseeditor
%{_fcitx5_qt5dir}/libcustomphraseeditor.so
%endif

%if %{build_qt6}
%files -n fcitx5-pinyindictmanager6
%{_fcitx5_qt6dir}/libpinyindictmanager.so

%files -n fcitx5-customphraseeditor6
%{_fcitx5_qt6dir}/libcustomphraseeditor.so
%endif

%files -f %{name}.lang
%doc README.md
%license LICENSES
%dir %{_fcitx5_datadir}/pinyinhelper
%dir %{_fcitx5_datadir}/punctuation
%dir %{_fcitx5_datadir}/lua
%dir %{_fcitx5_datadir}/lua/imeapi
%dir %{_fcitx5_datadir}/lua/imeapi/extensions
%dir %{_fcitx5_datadir}/pinyin
%dir %{_fcitx5_datadir}/chttrans
%{_bindir}/scel2org5
%{_fcitx5_libdir}/libchttrans.so
%{_fcitx5_libdir}/libcloudpinyin.so
%{_fcitx5_libdir}/libfullwidth.so
%{_fcitx5_libdir}/libpinyin.so
%{_fcitx5_libdir}/libpinyinhelper.so
%{_fcitx5_libdir}/libpunctuation.so
%{_fcitx5_libdir}/libtable.so
%{_fcitx5_addondir}/chttrans.conf
%{_fcitx5_addondir}/cloudpinyin.conf
%{_fcitx5_addondir}/fullwidth.conf
%{_fcitx5_addondir}/pinyin.conf
%{_fcitx5_addondir}/pinyinhelper.conf
%{_fcitx5_addondir}/punctuation.conf
%{_fcitx5_addondir}/table.conf
%{_fcitx5_datadir}/chttrans/gbks2t.tab
%{_fcitx5_imconfdir}/cangjie.conf
%{_fcitx5_imconfdir}/db.conf
%{_fcitx5_imconfdir}/erbi.conf
%{_fcitx5_imconfdir}/pinyin.conf
%{_fcitx5_imconfdir}/qxm.conf
%{_fcitx5_imconfdir}/shuangpin.conf
%{_fcitx5_imconfdir}/wanfeng.conf
%{_fcitx5_imconfdir}/wbpy.conf
%{_fcitx5_imconfdir}/wbx.conf
%{_fcitx5_imconfdir}/zrm.conf
%{_fcitx5_datadir}/pinyinhelper/py_stroke.mb
%{_fcitx5_datadir}/pinyinhelper/py_table.mb
%{_fcitx5_datadir}/punctuation/punc.mb.*
%{_fcitx5_datadir}/lua/imeapi/extensions/pinyin.lua
%{_fcitx5_datadir}/pinyin/chaizi.dict
%{_fcitx5_datadir}/pinyin/symbols
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-*
%{_datadir}/icons/hicolor/*/apps/fcitx-*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module
%{_libdir}/cmake/Fcitx5ModuleCloudPinyin
%{_libdir}/cmake/Fcitx5ModulePinyinHelper
%{_libdir}/cmake/Fcitx5ModulePunctuation

%changelog
