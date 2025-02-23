#
# spec file for package gnuastro
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 21
%bcond_with     tests
Name:           gnuastro
Version:        0.23
Release:        0
Summary:        GNU Astronomy Utilities
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gnuastro/
Source:         https://ftp.gnu.org/pub/gnu/gnuastro/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/gnuastro/%{name}-%{version}.tar.gz.sig
Source3:        https://akhlaghi.org/public-pgp-key.txt#/%{name}.keyring
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(wcslib)
Recommends:     %{name}-doc
Recommends:     curl
Recommends:     ghostscript_any >= 9.10
BuildRequires:  ghostscript_any

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

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}

%prep
%autosetup -p1

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
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions
mv -v %{buildroot}/%{_datadir}/%{name}/completion.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{name}

%check
%if %{with tests}
%make_build check
%endif

%ldconfig_scriptlets -n libgnuastro%{sover}

%files
%license COPYING*
%doc ChangeLog README NEWS THANKS AUTHORS
%dir %{_sysconfdir}/gnuastro
%config %{_sysconfdir}/gnuastro/*
%{_bindir}/*
%{_datadir}/gnuastro
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
%license COPYING*
%{_infodir}/gnuastro.info*.gz
%{_infodir}/gnuastro-figures

%files bash-completion
%license COPYING*
%{_datadir}/bash-completion/completions/%{name}

%changelog
