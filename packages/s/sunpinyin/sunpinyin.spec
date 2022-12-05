#
# spec file for package sunpinyin
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


Name:           sunpinyin
Version:        2.0.99.2
Release:        0
Summary:        A Statistical Language Model Based Chinese Input Method
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/sunpinyin/sunpinyin
Source:         https://github.com/sunpinyin/sunpinyin/archive/v3.0.0-rc2/%{name}-3.0.0-rc2.tar.gz
# https://sourceforge.net/projects/open-gram
Source1:        http://jaist.dl.sourceforge.net/project/open-gram/lm_sc.3gm.arpa-20140820.tar.bz2
Source2:        http://jaist.dl.sourceforge.net/project/open-gram/dict.utf8-20131214.tar.bz2
Source3:        sunpinyin-dictgen-local.mk.in
# PATCH-FIX-OPENSUSE marguerite@opensuse.org do not download online
Patch1:         no-download.patch
# PATCH-FIX-UPSTREAM bmwiedemann@opensuse.org make build reproducible
# Patch2:         reproducible.patch
# PATCH-FIx-UPSTREAM sunpinyin-scons-on-py3.patch dimstar@opensuse.org -- Fix build with scons using python3 as interpreter
# Patch3:         sunpinyin-scons-on-py3.patch
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  scons
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(sqlite3)
Provides:       locale(ibus:zh_CN;zh_SG)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sunpinyin is a statistical language model based Chinese input method engine. to
model the Chinese language, it use a backoff bigram and trigram language model.

%package -n lib%{name}3
Summary:        Libraries for Sunpinyin
Group:          System/Libraries
Requires:       %{name}-data >= %{version}

%description -n lib%{name}3
Sunpinyin is a statistical language model based Chinese input method engine. to
model the Chinese language, it use a backoff bigram and trigram language model.

%package data
Summary:        Data files for Sunpinyin
Group:          System/I18n/Chinese

%description data
Sunpinyin is a statistical language model based Chinese input method engine. to
model the Chinese language, it use a backoff bigram and trigram language model.

This package provides data files needed by it.

%package tools
Summary:        Dictionary tools for Sunpinyin
Group:          System/I18n/Chinese

%description tools
Sunpinyin is a statistical language model based Chinese input method engine. to
model the Chinese language, it use a backoff bigram and trigram language model.

This package provides dictionary tools needed by it.

%package devel
Summary:        Development Files for Sunpinyin
Group:          Development/Libraries/C and C++
Requires:       lib%{name}3 = %{version}
Requires:       sunpinyin-tools = %{version}
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}

%description devel
Sunpinyin is a statistical language model based Chinese input method engine. to
model the Chinese language, it use a backoff bigram and trigram language model.

This package provides development headers for it.

%prep
%autosetup -p1 -n %{name}-3.0.0-rc2
cp -r %{SOURCE1} .
cp -r %{SOURCE2} .
cp -r %{SOURCE3} src

%build
export CXXFLAGS+="%{optflags}"
scons --prefix=%{_prefix}

%install
scons --prefix=%{_prefix} \
      --libdir=%{_libdir} \
      --install-sandbox=%{buildroot} \
      install

# make dicts
src/sunpinyin-dictgen-local
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 lm_sc.t3g %{buildroot}%{_datadir}/%{name}
install -m 0644 pydict_sc.bin %{buildroot}%{_datadir}/%{name}

# fix doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%post -n lib%{name}3 -p /sbin/ldconfig

%postun -n lib%{name}3 -p /sbin/ldconfig

%files -n lib%{name}3
%defattr(-,root,root)
%doc AUTHORS NEWS README.md TODO
%license COPYING LGPL.LICENSE OPENSOLARIS.LICENSE
%{_libdir}/lib%{name}.so.*

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lm_sc.t3g
%{_datadir}/%{name}/pydict_sc.bin

%files tools
%defattr(-,root,root)
%{_bindir}/genpyt
%{_bindir}/getwordfreq
%{_bindir}/idngram_merge
%{_bindir}/ids2ngram
%{_bindir}/mmseg
%{_bindir}/slmbuild
%{_bindir}/slminfo
%{_bindir}/slmpack
%{_bindir}/slmprune
%{_bindir}/slmseg
%{_bindir}/slmthread
%{_bindir}/%{name}-dictgen
%{_bindir}/tslmendian
%{_bindir}/tslminfo
%{_mandir}/man1/genpyt.1.gz
%{_mandir}/man1/getwordfreq.1.gz
%{_mandir}/man1/idngram_merge.1.gz
%{_mandir}/man1/ids2ngram.1.gz
%{_mandir}/man1/mmseg.1.gz
%{_mandir}/man1/slmbuild.1.gz
%{_mandir}/man1/slminfo.1.gz
%{_mandir}/man1/slmpack.1.gz
%{_mandir}/man1/slmprune.1.gz
%{_mandir}/man1/slmseg.1.gz
%{_mandir}/man1/slmthread.1.gz
%{_mandir}/man1/tslmendian.1.gz
%{_mandir}/man1/tslminfo.1.gz

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}-2.0/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%changelog
