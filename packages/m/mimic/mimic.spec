#
# spec file for package mimic
#
# Copyright (c) 2026 SUSE LLC
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


%define _lto_cflags %{nil}
Name:           mimic
Version:        1.3.0.1
Release:        0
Summary:        Mycroft's TTS engine, based on CMU's Flite (Festival Lite)
License:        BSD-3-Clause AND MIT-CMU
Group:          Productivity/Text/Convertors
URL:            https://mimic.mycroft.ai
Source:         https://github.com/MycroftAI/mimic/archive/%{version}.tar.gz
Patch0:         mimic-HTS_Free.patch
# fix build with gcc16
Patch1:         mimic-gcc16.patch
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa) >= 1.0.11
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libpulse)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mimic is a text-to-speech engine based on Carnegie Mellon
University’s Flite (Festival-Lite) software. Mimic takes in text and
reads it out loud to create a voice.

%package -n libttsmimic0
Summary:        Core libraries of Mycroft's TTS engine
Group:          System/Libraries

%description -n libttsmimic0
Mimic is a text-to-speech engine based on Carnegie Mellon
University’s Flite (Festival-Lite) software. Mimic takes in text and
reads it out loud to create a voice.

%package devel
Summary:        Development files for mimic (Mycroft's TTS engine)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %version

%description devel
Mimic is a text-to-speech engine based on Carnegie Mellon
University’s Flite (Festival-Lite) software. Mimic takes in text and
reads it out loud to create a voice.

This package contains the headers and development libraries for mimic.

%prep
%autosetup -p1 -n %{name}1-%{version}

%build
./autogen.sh
%configure --enable-shared
make %{?_smp_mflags}

%install
%make_install
rm -fv "%{buildroot}/%{_libdir}"/*.la

%post   -n libttsmimic0 -p /sbin/ldconfig
%postun -n libttsmimic0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md ACKNOWLEDGEMENTS
%license COPYING
%{_bindir}/compile_regexes
%{_bindir}/mimic
%{_bindir}/mimic_time
%{_bindir}/mimicvox_info
%{_bindir}/t2p
%{_mandir}/man?/mimic.1.gz
%{_datadir}/mimic/
%{_datadir}/mimic/voices/
%{_datadir}/mimic/voices/cmu_us_slt_hts.htsvoice

%files -n libttsmimic0
%{_libdir}/libttsmimic.so.0*
%{_libdir}/libttsmimic_lang_all_langs.so.0*
%{_libdir}/libttsmimic_lang_all_voices.so.0*
%{_libdir}/libttsmimic_lang_cmu_grapheme_lang.so.0*
%{_libdir}/libttsmimic_lang_cmu_grapheme_lex.so.0*
%{_libdir}/libttsmimic_lang_cmu_indic_lang.so.0*
%{_libdir}/libttsmimic_lang_cmu_indic_lex.so.0*
%{_libdir}/libttsmimic_lang_cmu_time_awb.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_awb.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_kal.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_kal16.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_rms.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_slt.so.0*
%{_libdir}/libttsmimic_lang_cmulex.so.0*
%{_libdir}/libttsmimic_lang_usenglish.so.0*
%{_libdir}/libttsmimic_lang_vid_gb_ap.so.0*
%{_libdir}/libttsmimic_lang_cmu_us_slt_hts.so.0*

%files devel
%{_includedir}/ttsmimic
%{_libdir}/pkgconfig/mimic.pc
%{_libdir}/libttsmimic.so
%{_libdir}/libttsmimic_lang_all_langs.so
%{_libdir}/libttsmimic_lang_all_voices.so
%{_libdir}/libttsmimic_lang_cmu_grapheme_lang.so
%{_libdir}/libttsmimic_lang_cmu_grapheme_lex.so
%{_libdir}/libttsmimic_lang_cmu_indic_lang.so
%{_libdir}/libttsmimic_lang_cmu_indic_lex.so
%{_libdir}/libttsmimic_lang_cmu_time_awb.so
%{_libdir}/libttsmimic_lang_cmu_us_awb.so
%{_libdir}/libttsmimic_lang_cmu_us_kal.so
%{_libdir}/libttsmimic_lang_cmu_us_kal16.so
%{_libdir}/libttsmimic_lang_cmu_us_rms.so
%{_libdir}/libttsmimic_lang_cmu_us_slt.so
%{_libdir}/libttsmimic_lang_cmulex.so
%{_libdir}/libttsmimic_lang_usenglish.so
%{_libdir}/libttsmimic_lang_vid_gb_ap.so
%{_libdir}/libttsmimic_lang_cmu_us_slt_hts.so

%changelog
