#
# spec file for package jq
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 SUSE LLC and contributors
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


%define jq_sover 1
Name:           jq
Version:        1.8.1
Release:        0
Summary:        A lightweight and flexible command-line JSON processor
License:        CC-BY-3.0 AND MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/jqlang
Source:         https://github.com/jqlang/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         CVE-2026-33948.patch
Patch1:         CVE-2026-32316.patch
Patch2:         CVE-2026-33947.patch
Patch3:         CVE-2026-39956.patch
Patch4:         CVE-2026-39979.patch
Patch5:         CVE-2026-40164.patch
Patch6:         CVE-2026-40612.patch
Patch7:         CVE-2026-41256.patch
Patch8:         CVE-2026-41257.patch
Patch9:         CVE-2026-43894.patch
Patch10:        CVE-2026-43895.patch
Patch11:        CVE-2026-43896.patch
Patch12:        CVE-2026-44777_0.patch
Patch13:        CVE-2026-44777_1.patch
BuildRequires:  chrpath
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(oniguruma)
# https://github.com/stedolan/jq/issues/1904
Requires:       libjq%{jq_sover} = %{version}
%ifarch aarch64 x86_64 ppc64le s390x riscv64
BuildRequires:  valgrind
%endif

%description
A lightweight and flexible command-line JSON processor. jq is like sed for
JSON data – you can use it to slice and filter and map and transform
structured data with the same ease that sed, awk, grep and friends let
you play with text.

%package -n libjq%{jq_sover}
Summary:        Library for a lightweight and flexible command-line JSON processor
Group:          System/Libraries

%description -n libjq%{jq_sover}
Library for a lightweight and flexible command-line JSON processor.

%package -n libjq-devel
Summary:        Development files for jq
Group:          Development/Languages/C and C++
Requires:       libjq%{jq_sover} = %{version}

%description -n libjq-devel
Development files (headers and libraries for jq).

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
%ifarch aarch64 x86_64 ppc64le s390x riscv64
  --enable-valgrind \
%else
  --disable-valgrind \
%endif
%{nil}
%make_build

%install
%make_install

# RPATH contains the builddir yucks!
chrpath -d %{buildroot}%{_bindir}/jq

# No static stuff
rm %{buildroot}%{_libdir}/libjq.la

# we install the documentation in a separate location using the doc macro
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
%if "%{qemu_user_space_build}" == "0"
%make_build check
%endif

%ldconfig_scriptlets -n libjq%{jq_sover}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libjq%{jq_sover}
%license COPYING
%{_libdir}/libjq.so.%{jq_sover}*

%files -n libjq-devel
%license COPYING
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so
%{_libdir}/pkgconfig/libjq.pc

%changelog
