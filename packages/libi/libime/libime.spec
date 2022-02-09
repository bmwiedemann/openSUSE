#
# spec file for package libime
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


Name:           libime
Version:        1.0.11
Release:        0
Summary:        Generic input method implementation
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/libime
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/data/dict.utf8-20211021.tar.xz
Source2:        https://download.fcitx-im.org/data/lm_sc.3gm.arpa-20140820.tar.bz2
Source3:        https://download.fcitx-im.org/data/table.tar.gz
Patch0:         libime-no-download.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_filesystem-devel

%description
This is a library to support generic input method implementation.

%package devel
Summary:        Development files for libime
Group:          Development/Libraries/C and C++
Requires:       libIMECore0 = %{version}
Requires:       libIMEPinyin0 = %{version}
Requires:       libIMETable0 = %{version}

%description devel
This package provides development files for libime.

%package tools
Summary:        Toolkit for libime
Group:          System/I18n/Chinese

%description tools
This package provides toolkit for libime.

%package -n libIMECore0
Summary:        Core library for libime
Group:          System/Libraries
Requires:       libime-tools

%description -n libIMECore0
This package provides core library for libime.

%package -n libIMEPinyin0
Summary:        Pinyin library for libime
Group:          System/Libraries
Requires:       libime-dicts

%description -n libIMEPinyin0
This package provides pinyin library for libime.

%package -n libIMETable0
Summary:        Table library for libime
Group:          System/Libraries
Requires:       libime-dicts

%description -n libIMETable0
This package provides table library for libime.

%package dicts
Summary:        Dictionary files for libime
Group:          System/I18n/Chinese

%description dicts
This package provides dictionary files for libime.

%prep
%setup -q
%autopatch -p1
cp -r %{SOURCE1} data/
cp -r %{SOURCE2} data/
cp -r %{SOURCE3} data/

%build
export LANG=en_US.UTF-8
%cmake -DCMAKE_SKIP_RPATH=OFF
%make_build

%install
%cmake_install
%fdupes %{buildroot}

%post -n libIMECore0 -p /sbin/ldconfig
%post -n libIMEPinyin0 -p /sbin/ldconfig
%post -n libIMETable0 -p /sbin/ldconfig
%postun -n libIMECore0 -p /sbin/ldconfig
%postun -n libIMEPinyin0 -p /sbin/ldconfig
%postun -n libIMETable0 -p /sbin/ldconfig

%files tools
%{_bindir}/libime_history
%{_bindir}/libime_prediction
%{_bindir}/libime_slm_build_binary
%{_bindir}/libime_migrate_fcitx4_pinyin
%{_bindir}/libime_migrate_fcitx4_table
%{_bindir}/libime_pinyindict
%{_bindir}/libime_tabledict

%files -n libIMECore0
%{_libdir}/libIMECore.so.0
%{_libdir}/libIMECore.so.%{version}
%{_libdir}/libime

%files -n libIMEPinyin0
%{_libdir}/libIMEPinyin.so.0
%{_libdir}/libIMEPinyin.so.%{version}

%files -n libIMETable0
%{_libdir}/libIMETable.so.0
%{_libdir}/libIMETable.so.%{version}

%files devel
%license LICENSES
%doc README.md
%{_includedir}/LibIME
%{_libdir}/cmake/LibIME*
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so

%files dicts
%{_datadir}/libime

%changelog
