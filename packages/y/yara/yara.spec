#
# spec file for package yara
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


%define soname 4
Name:           yara
Version:        4.0.2
Release:        0
Summary:        A malware identification and classification tool
License:        Apache-2.0
Group:          System/Filesystems
URL:            https://plusvic.github.io/yara/
Source:         https://github.com/VirusTotal/yara/archive/v%{version}.tar.gz
#PATCH-FIX-UPSTREAM - https://github.com/VirusTotal/yara/pull/1352
Patch1:         yara-fix-arm.patch
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpcre16)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libpcreposix)

%description
YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%package -n libyara%{soname}
Summary:        Library to support the yara malware identification tool
Group:          System/Libraries

%description -n libyara%{soname}
YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%package -n libyara-devel
Summary:        Development files to support the yara malware identification tool
Group:          Development/Libraries/C and C++
Requires:       libyara%{soname} = %{version}-%{release}

%description -n libyara-devel
YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%package doc
Summary:        Documentation files to support the YARA malware identification tool
Group:          Development/Libraries/C and C++
Requires:       libyara%{soname} = %{version}-%{release}

%description doc
Documentation and guideslines to support YARA.

YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fvi
%configure \
  --disable-silent-rules \
  --enable-magic \
  --enable-cuckoo
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_libdir}/libyara.a

%check
%make_build check

%post   -n libyara%{soname} -p /sbin/ldconfig
%postun -n libyara%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md CONTRIBUTORS AUTHORS
%{_bindir}/yara
%{_bindir}/yarac
%{_mandir}/man1/yara.1%{?ext_man}
%{_mandir}/man1/yarac.1%{?ext_man}

%files -n libyara%{soname}
%license COPYING
%doc README.md CONTRIBUTORS AUTHORS
%{_libdir}/libyara.so.%{soname}
%{_libdir}/libyara.so.%{version}

%files -n libyara-devel
%license COPYING
%doc README.md CONTRIBUTORS AUTHORS
%{_includedir}/yara.h
%{_includedir}/yara
%{_libdir}/libyara.so
%{_libdir}/pkgconfig/yara.pc

%files doc
%doc docs

%changelog
