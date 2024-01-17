#
# spec file for package scim-pinyin
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


Name:           scim-pinyin
Version:        0.5.92
Release:        0
Summary:        Smart pinyin IM engine for SCIM platform
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/scim-im/scim-pinyin
Source:         https://github.com/scim-im/%{name}/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  scim-devel
Obsoletes:      %{name}-skim <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Smart pinyin IM engine for SCIM platform.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
./bootstrap
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure --disable-static \
	   --enable-debug \
	   --disable-skim-support \
	   --enable-tools
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang scim-pinyin

%files -f scim-pinyin.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README ChangeLog
%{_scim_enginedir}/pinyin.so
%if 0%{?suse_version} >= 1310
%{_scim_uidir}/pinyin-imengine-setup.so
%endif
%dir %{_scim_datadir}/pinyin/
%{_scim_datadir}/pinyin/phrase_lib
%{_scim_datadir}/pinyin/pinyin_phrase_index
%{_scim_datadir}/pinyin/pinyin_phrase_lib
%{_scim_datadir}/pinyin/pinyin_table
%{_scim_datadir}/pinyin/special_table
%{_scim_icondir}/smart-pinyin.png

%changelog
