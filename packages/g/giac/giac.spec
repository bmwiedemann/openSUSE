#
# spec file for package giac
#
# Copyright (c) 2020 SUSE LLC.
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


%bcond_with cocoa
Name:           giac
%define tarver  1.5.0-85
Version:        %( echo %{tarver} | sed 's/-/./' ) 
%define mainver %( echo %{tarver} | sed 's/-.*//' )
%define soname  0
Release:        0
Summary:        Computer algebra system
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
Source:         http://www-fourier.ujf-grenoble.fr/~parisse/debian/dists/stable/main/source/giac_%{tarver}.tar.gz
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  gmp-ecm-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  lapack-devel
BuildRequires:  latex2html
BuildRequires:  libjpeg-devel
BuildRequires:  mpfi-devel
BuildRequires:  mpfr-devel
BuildRequires:  nauty-devel
BuildRequires:  ntl-devel
BuildRequires:  pari-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  shared-mime-info
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%if !%{with cocoa}
BuildRequires:  pkgconfig(ao)
%endif

%description
A computer algebra system, compatible with existing CAS, as a C++
library with various user interfaces (GUI with formal spreadsheet and exact
dynamic geometry, on-line, readline, emacs, texmacs...).

%package     -n xcas
Summary:        Computer algebra interface
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n xcas
Xcas is an interface to perform computer algebra, function graphs,
interactive geometry (2-d and 3-d), spreadsheet and statistics
programmation. It may be used as a replacement for graphic calculators
for example on netbooks.

%package     -n lib%{name}%{soname}
Summary:        The core library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{soname}
A computer algebra system, compatible with existing CAS, as a C++
library with various user interfaces (GUI with formal spreadsheet and exact
dynamic geometry, on-line, readline, emacs, texmacs...).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       fltk-devel
Requires:       lib%{name}%{soname} = %{version}
Requires:       mpfi-devel
Requires:       mpfr-devel
Requires:       ntl-devel
Requires:       pkgconfig(gsl)

%description    devel
This package contains header files and libraries needed to develop
application that use the GIAC computer algebra system.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
This document describes the basic structure and provides information on
usage of giac, a computer algebra system.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{mainver}

# remove all hidden files
find . -type f -iname '.*' -delete

%build
%configure \
    --enable-gui \
    --enable-static=no
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

# use the freedesktop standard
rm -rf %{buildroot}%{_datadir}/application-registry
# install man page
find debian -type f -name \*.1 | while read i; do
	install -Dm 0644 $i "%{buildroot}/%{_mandir}/man1/${i##*/}"
done
# install mimeinfo
install -Dm 0644 debian/%{name}.sharedmimeinfo %{buildroot}%{_datadir}/mime/packages/%{name}.xml
# remove makefiles from %%doc
find %{buildroot}%{_datadir}/%{name}/doc -type f -iname "Makefile*" -delete
# remove zero-length
find %{buildroot}%{_datadir}/%{name}/doc -type f -empty -delete
# fix non-executable-script
chmod a+x %{buildroot}%{_datadir}/%{name}/doc/pari/gphtml
# fix script-without-shebang
chmod a-x %{buildroot}%{_datadir}/%{name}/examples/Exemples/*/*.xws
chmod a-x %{buildroot}%{_datadir}/%{name}/examples/geo/*.cas
chmod a-x %{buildroot}%{_datadir}/%{name}/examples/lewisw/fermat_gcd_1var
chmod a-x %{buildroot}%{_datadir}/%{name}/examples/lewisw/fermat_gcd_mod_1var
# fix spurious-executable-perm
chmod a-x %{buildroot}%{_datadir}/%{name}/examples/tortue/*.cxx
# put docs in correct directory
if [ "%{_docdir}" != "%{_datadir}/doc" ]; then
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
fi

rm %{buildroot}%{_docdir}/giac/Makefile.am

%find_lang %{name}

%fdupes -s %{buildroot}%{_datadir}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}_es.info%{ext_info}
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}_us.info%{ext_info}

%preun
if [ $1 -eq 0 ]; then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}_es.info%{ext_info}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}_us.info%{ext_info}
fi

%post   -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_docdir}/giac/README
%{_bindir}/giac
%{_bindir}/hevea2mml
%{_bindir}/icas
%{_bindir}/pgiac
%{_bindir}/cas_help
%{_bindir}/en_cas_help
%{_bindir}/es_cas_help
%{_bindir}/fr_cas_help
%{_datadir}/giac/
%{_datadir}/mime/packages/giac.xml
%{_infodir}/giac_es.info%{?ext_info}
%{_infodir}/giac_us.info%{?ext_info}
%{_mandir}/man1/cas_help.1%{ext_info}
%{_mandir}/man1/fr_cas_help.1%{ext_info}
%{_mandir}/man1/giac.1%{ext_info}
%{_mandir}/man1/icas.1%{ext_info}
%{_mandir}/man1/pgiac.1%{ext_info}
%exclude %{_datadir}/giac/doc/
%exclude %{_datadir}/giac/aide_cas
%exclude %{_datadir}/giac/examples/
%exclude %{_docdir}/giac/index.html
%exclude %{_docdir}/giac/*/

%files -n xcas
%license COPYING
%{_bindir}/xcas
%{_bindir}/xcasnew
%{_mandir}/man1/xcas.1%{ext_info}
%{_datadir}/icons/hicolor/*/apps/*xcas.png
%{_datadir}/icons/hicolor/*/mimetypes/*xcas.png
%{_datadir}/pixmaps/xcas.xpm
%{_datadir}/applications/xcas.desktop

%files -n lib%{name}%{soname}
%license COPYING
%{_libdir}/libgiac.so.*

%files devel
%license COPYING
%{_includedir}/giac/
%{_libdir}/libgiac.so

%files doc
%license COPYING
%{_datadir}/giac/doc/
%{_datadir}/giac/aide_cas
%{_datadir}/giac/examples/
%{_docdir}/giac/index.html
%{_docdir}/giac/*/

%files lang -f %{name}.lang
%license COPYING

%changelog
