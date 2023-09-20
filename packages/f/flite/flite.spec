#
# spec file for package flite
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


Name:           flite
Version:        2.2
Release:        0
Summary:        Small, fast speech synthesis engine (text-to-speech)
License:        BSD-3-Clause-Modification
Group:          Productivity/Multimedia/Other
URL:            https://github.com/festvox/flite
Source:         https://github.com/festvox/flite/archive/refs/tags/v%{version}.tar.gz
Patch0:         flite-2.2-lto.patch
Patch1:         flite-2.2-texinfo-7.0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ed
BuildRequires:  libpulse-devel
BuildRequires:  libtool
BuildRequires:  texi2html
BuildRequires:  texinfo

%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine
developed at CMU and primarily designed for small embedded machines and/or
large servers. Flite is designed as an alternative synthesis engine to
Festival for voices built using the FestVox suite of voice building tools.

%package -n libflite1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite1

%package -n libflite_cmu_grapheme_lang1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_grapheme_lang1

%package -n libflite_cmu_grapheme_lex1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_grapheme_lex1

%package -n libflite_cmu_indic_lang1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_indic_lang1

%package -n libflite_cmu_indic_lex1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_indic_lex1

%package -n libflite_cmu_time_awb1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_time_awb1

%package -n libflite_cmu_us_awb1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_us_awb1

%package -n libflite_cmu_us_kal1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_us_kal1

%package -n libflite_cmu_us_kal16-1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_us_kal16-1

%package -n libflite_cmu_us_rms1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_us_rms1

%package -n libflite_cmu_us_slt1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmu_us_slt1

%package -n libflite_cmulex1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_cmulex1

%package -n libflite_usenglish1
Summary:        Small, fast speech synthesis engine (libraries)
Group:          System/Libraries

%description -n libflite_usenglish1

%package devel
Summary:        Development files for flite
Group:          Development/Libraries/C and C++
Requires:       flite = %{version}

%description devel
Development files for Flite, a small, fast speech synthesis engine.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
    --enable-shared \
    --disable-static \
    --with-audio=pulseaudio

# This package fails to build with parallel make
%make_build -j1
# Build documentation
cd doc
%make_build flite.html

%install
make install INSTALLBINDIR="%{buildroot}/%{_bindir}" \
	INSTALLLIBDIR="%{buildroot}/%{_libdir}" \
	INSTALLINCDIR="%{buildroot}/%{_includedir}/flite"
rm -f "%{buildroot}/%{_libdir}"/*.a

%post   -n libflite1 -p /sbin/ldconfig
%postun -n libflite1 -p /sbin/ldconfig
%post   -n libflite_cmu_grapheme_lang1 -p /sbin/ldconfig
%postun -n libflite_cmu_grapheme_lang1 -p /sbin/ldconfig
%post   -n libflite_cmu_grapheme_lex1 -p /sbin/ldconfig
%postun -n libflite_cmu_grapheme_lex1 -p /sbin/ldconfig
%post   -n libflite_cmu_indic_lang1 -p /sbin/ldconfig
%postun -n libflite_cmu_indic_lang1 -p /sbin/ldconfig
%post   -n libflite_cmu_indic_lex1 -p /sbin/ldconfig
%postun -n libflite_cmu_indic_lex1 -p /sbin/ldconfig
%post   -n libflite_cmu_time_awb1 -p /sbin/ldconfig
%postun -n libflite_cmu_time_awb1 -p /sbin/ldconfig
%post   -n libflite_cmu_us_awb1 -p /sbin/ldconfig
%postun -n libflite_cmu_us_awb1 -p /sbin/ldconfig
%post   -n libflite_cmu_us_kal1 -p /sbin/ldconfig
%postun -n libflite_cmu_us_kal1 -p /sbin/ldconfig
%post   -n libflite_cmu_us_kal16-1 -p /sbin/ldconfig
%postun -n libflite_cmu_us_kal16-1 -p /sbin/ldconfig
%post   -n libflite_cmu_us_rms1 -p /sbin/ldconfig
%postun -n libflite_cmu_us_rms1 -p /sbin/ldconfig
%post   -n libflite_cmu_us_slt1 -p /sbin/ldconfig
%postun -n libflite_cmu_us_slt1 -p /sbin/ldconfig
%post   -n libflite_cmulex1 -p /sbin/ldconfig
%postun -n libflite_cmulex1 -p /sbin/ldconfig
%post   -n libflite_usenglish1 -p /sbin/ldconfig
%postun -n libflite_usenglish1 -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n libflite1
%{_libdir}/libflite.so.*

%files -n libflite_cmu_grapheme_lang1
%{_libdir}/libflite_cmu_grapheme_lang.so.*

%files -n libflite_cmu_grapheme_lex1
%{_libdir}/libflite_cmu_grapheme_lex.so.*

%files -n libflite_cmu_indic_lang1
%{_libdir}/libflite_cmu_indic_lang.so.*

%files -n libflite_cmu_indic_lex1
%{_libdir}/libflite_cmu_indic_lex.so.*

%files -n libflite_cmu_time_awb1
%{_libdir}/libflite_cmu_time_awb.so.*

%files -n libflite_cmu_us_awb1
%{_libdir}/libflite_cmu_us_awb.so.*

%files -n libflite_cmu_us_kal1
%{_libdir}/libflite_cmu_us_kal.so.*

%files -n libflite_cmu_us_kal16-1
%{_libdir}/libflite_cmu_us_kal16.so.*

%files -n libflite_cmu_us_rms1
%{_libdir}/libflite_cmu_us_rms.so.*

%files -n libflite_cmu_us_slt1
%{_libdir}/libflite_cmu_us_slt.so.*

%files -n libflite_cmulex1
%{_libdir}/libflite_cmulex.so.*

%files -n libflite_usenglish1
%{_libdir}/libflite_usenglish.so.*

%files devel
%{_includedir}/flite/
%{_libdir}/*.so
%license COPYING
%doc ACKNOWLEDGEMENTS README.md doc/html

%changelog
