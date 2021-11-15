#
# spec file for package broadvoice32
#
# Copyright (c) 2021 SUSE LLC
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


%define static 0
%define shared 1
%define tools  1

Name:           broadvoice32
Version:        1.2
Release:        0
Summary:        BroadVoice 32 Speech Codec
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.broadcom.com/site-search?q=broadvoice
Source0:        BroadVoice32OpenSource.v%{version}.zip
Source1:        COPYING
Source2:        README
Source3:        README.SUSE
Source4:        meson_options.txt
Source5:        meson.build
Source6:        baselibs.conf
BuildRequires:  meson
BuildRequires:  unzip

%description
BroadVoice is a family of speech coding algorithms created by
Broadcom and standardized by CableLabs, SCTE, and ANSI for Voice over
IP applications in cable telephony. BroadVoice is also part of the
ITU-T Recommendations J.161 and J.361.

%package devel
Summary:        BroadVoice 32 development files
Group:          Development/Libraries/C and C++
%if !0%{?static}
Requires:       %{name}
%endif

%description devel
Header files for the libbv32 library.
%if 0%{?static}
This package also includes the static library.
%endif

%prep
%autosetup -n BroadVoice32

%build
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .
cp %{SOURCE4} %{SOURCE5} FloatingPoint
cd FloatingPoint
%meson \
%if 0%{?static}
  -Dstatic_libs=true \
%endif
%if !0%{?shared}
  -Dshared_libs=false \
%endif
%if !0%{?tools}
  -Dbuild_tools=false \
%endif

%meson_build

%install
cd FloatingPoint
%meson_install
%if !0%{?static} && !0%{?shared}
rm -r %{buildroot}%{_includedir}/bv32-floatingpoint
%endif

%check
%if 0%{?tools}
%ifarch s390x ppc ppc64 %sparc %sparc64
%define endianness BigEndian
%else
%define endianness LittleEndian
%endif
cd FloatingPoint/process
#return failure if TestBroadVoice32 fails
echo 'exit $checksum' >>TestBroadVoice32
#TestBroadVoice32 is setup for compilation with DG192BITSTREAM=1
#remove some tests for compilation with DG192BITSTREAM=0
grep -qF DG192BITSTREAM=0 ../meson.build && \
  sed -i '/cmp tv.bv32 tv.bv32.ref/,/fi/d' TestBroadVoice32 && \
  sed -i '/cmp tv.bv32.bfe10.raw tv.bv32.bfe10.ref.raw/,/fi/d' TestBroadVoice32 && \
  sed -i '/cmp tvbe.bv32 tvbe.bv32.ref/,/fi/d' TestBroadVoice32 && \
  sed -i '/cmp tvbe.bv32.bfe10.raw tvbe.bv32.bfe10.ref.raw/,/fi/d' TestBroadVoice32
PATH=%{buildroot}%{_bindir}:$PATH LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
  bash TestBroadVoice32 %endianness
%endif

%if 0%{?shared}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%files
%license COPYING
%doc README README.SUSE BroadVoice32.doc
%if 0%{?tools}
%{_bindir}/BroadVoice32
%endif
%if 0%{?shared}
%{_libdir}/*.so
%endif

%if 0%{?static} || 0%{?shared}
%files devel
%dir %{_includedir}/bv32-floatingpoint
%dir %{_includedir}/bv32-floatingpoint/*
%{_includedir}/*/*/*.h
%if 0%{?static}
%{_libdir}/*.a
%endif
%endif

%changelog
