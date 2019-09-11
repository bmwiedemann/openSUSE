#
# spec file for package jq
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jq
Version:        1.6
Release:        0
Summary:        A lightweight and flexible command-line JSON processor
License:        MIT AND CC-BY-3.0
Group:          Productivity/Text/Utilities
URL:            http://stedolan.github.io/jq/
Source:         https://github.com/stedolan/jq/releases/download/jq-%{version}/jq-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  oniguruma-devel
BuildRequires:  valgrind

%description
A lightweight and flexible command-line JSON processor. jq is like sed for
JSON data – you can use it to slice and filter and map and transform
structured data with the same ease that sed, awk, grep and friends let
you play with text.

%package -n libjq1
Summary:        Library for a lightweight and flexible command-line JSON processor
Group:          System/Libraries

%description -n libjq1
Library for a lightweight and flexible command-line JSON processor.

%package -n libjq-devel
Summary:        Development files for jq
Group:          Development/Languages/C and C++
Requires:       libjq1 = %{version}

%description -n libjq-devel
Development files (headers and libraries for jq).

%prep
%setup -q

%build
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

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
make %{?_smp_mflags} check
%endif

%post -n libjq1 -p /sbin/ldconfig
%postun -n libjq1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libjq1
%{_libdir}/libjq.so.1*

%files -n libjq-devel
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so

%changelog
