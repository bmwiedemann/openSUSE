#
# spec file for package kakasi
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           kakasi
Version:        2.3.6
Release:        0
Summary:        Filter to Convert Kanji Characters to Hiragana, Katakana, or Romaji
License:        GPL-2.0-or-later
Group:          Productivity/Text/Convertors
URL:            http://kakasi.namazu.org/
Source:         http://kakasi.namazu.org/stable/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM marguerite@opensuse.org
Patch0:         kakasi-2.3.6-no-return-in-nonvoid-function.patch
BuildRequires:  automake
Requires:       kakasi-dict = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KAKASI is the language processing filter to convert Kanji characters to
Hiragana, Katakana, or Romaji(1) and may be helpful for reading
Japanese documents. The word-splitting patch is merged from version
2.3.0.

The name "KAKASI" is the abbreviation of "kanji kana simple inverter"
and the inverse of SKK "simple kana kanji converter" developed by
Masahiko Sato at Tohoku University. Most entries of the kakasi
dictionary are derived from the SKK dictionaries. If interested  in the
naming of KAKASI, consult a Japanese-English dictionary.

(1) "Romaji" is an alphabetical description of Japanese pronunciation.

%package devel
Summary:        Header file and libraries of KAKASI
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       kakaside = %{version}
Obsoletes:      kakaside < %{version}

%description devel
header file and libraries of KAKASI

%package dict
Summary:        The base dictionary of KAKASI
Group:          Productivity/Text/Convertors
Provides:       kakasidi = %{version}
Obsoletes:      kakasidi < %{version}

%description dict
The base dictionary of KAKASI

%prep
%autosetup -p1

# w: version-control-internal-file
rm -rf doc/CVS
# non-linux-readme
rm -rf doc/README.*OS*

%build
cp %{_datadir}/automake*/config.{guess,sub} .
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ONEWS README* THANKS TODO ChangeLog
%doc ./doc/*
%{_bindir}/atoc_conv
%{_bindir}/kakasi
%{_bindir}/kakasi-config
%{_bindir}/mkkanwa
%{_bindir}/rdic_conv
%{_bindir}/wx2_conv
%{_libdir}/libkakasi.so.2
%{_libdir}/libkakasi.so.2.1.0
%dir %{_datadir}/kakasi
%{_datadir}/kakasi/itaijidict
%{_mandir}/man1/kakasi.1.gz
%{_mandir}/man1/kakasi-config.1.gz

%files devel
%defattr(-,root,root)
%{_includedir}/libkakasi.h
%{_libdir}/libkakasi.so

%files dict
%defattr(-,root,root)
%{_datadir}/kakasi/kanwadict

%changelog
