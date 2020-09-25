#
# spec file for package gnuastro
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


%define sover 11
%bcond_with     tests
Name:           gnuastro
Version:        0.13
Release:        0
Summary:        GNU Astronomy Utilities
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gnuastro/
Source:         https://ftp.gnu.org/pub/gnu/gnuastro/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/gnuastro/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=gnuastro&download=1#/%{name}.keyring
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(wcslib)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-doc
Recommends:     ghostscript_any >= 9.10
%if %{with tests}
BuildRequires:  ghostscript_any
%endif

%description
The GNU Astronomy Utilities (Gnuastro) contains various programs and
library functions for the manipulation and analysis of astronomical
data.

%package -n libgnuastro%{sover}
Summary:        Libraries for the GNU Astronomy Utilities

%description -n libgnuastro%{sover}
Libraries for the manipulation and analysis of astronomical data,
part of the GNU Astronomy Utilities (Gnuastro).

%package devel
Summary:        Development files for gnuastro
Requires:       libgnuastro%{sover} = %{version}

%description devel
Development files required for development with GNU Astronomy
Utilities (Gnuastro).

%package doc
Summary:        Documentation for the GNU Astromomy Utilities
BuildArch:      noarch

%description doc
Additional documentation for the GNU Astromomy Utilities.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	--disable-static \
	--disable-rpath \
	CPPFLAGS="$(pkg-config cfitsio --cflags)"
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if %{with tests}
%make_build check
%endif

%post -n libgnuastro%{sover} -p /sbin/ldconfig
%postun -n libgnuastro%{sover} -p /sbin/ldconfig
%post doc
for infoname in %{name}.info %{name}.info-{1..6}; do
%install_info --info-dir=%{_infodir} %{_infodir}/${infoname}.gz
done

%preun doc
for infoname in %{name}.info %{name}.info-{1..6}; do
%install_info_delete --info-dir=%{_infodir} %{_infodir}/${infoname}.gz
done

%files
%license COPYING*
%doc ChangeLog README NEWS THANKS AUTHORS
%config %{_sysconfdir}/*.conf
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files -n libgnuastro%{sover}
%license COPYING
%{_libdir}/libgnuastro.so.*

%files devel
%license COPYING*
%{_includedir}/gnuastro
%{_libdir}/libgnuastro.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_infodir}/gnuastro.info*.gz
%{_infodir}/gnuastro-figures

%changelog
