#
# spec file for package pspp
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2008 Matj Cepl <mcepl@redhat.com>
# Copyright (c) 2008 D. Steuer <steuer@hsuhh.de>
# Copyright (c) 2018 <astieger@suse.com>
# Copyright (c) 2010-2024 <opensuse.lietuviu.kalba@gmail.com>
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


%if 0%{?mandriva_version}
%define _disable_ld_no_undefined 1
#Next line is needed for Mandriva build
%define _disable_ld_as_needed 1
%endif
Name:           pspp
Version:        2.0.1
Release:        0
Summary:        A program for statistical analysis of sampled data
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/pspp/
Source0:        https://ftp.gnu.org/pub/gnu/pspp/pspp-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/pspp/pspp-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=245#/%{name}.keyring

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?fedora} 
BuildRequires:  atlas
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
PreReq:         %install_info_prereq
%endif
%if 0%{?is_opensuse}
# Next package only for "make check", but "free-ttf-fonts" exist only in openSUSE, not in SUSE
BuildRequires:  free-ttf-fonts
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext >= 0.20
BuildRequires:  gsl-devel >= 1.12
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  gtksourceview4-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  m4
BuildRequires:  pango-devel
BuildRequires:  perl(Text::Diff)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream)
BuildRequires:  postgresql-devel
BuildRequires:  python3-devel >= 3.4
BuildRequires:  readline-devel
BuildRequires:  spread-sheet-widget-devel >= 0.6
BuildRequires:  texinfo
BuildRequires:  zlib-devel
AutoReqProv:    Yes
Recommends:     %{name}-doc = %{version}

%description
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

PSPP development is ongoing. It already supports a large subset of
SPSS's syntax. Its statistical procedure support is currently
limited, but growing. At your option, PSPP will produce statistical
reports in ASCII, PostScript, PDF, HTML, SVG, or OpenDocument formats.


%if 0%{?suse_version}
%lang_package
%else
%package lang
Summary:        Translations for package pspp
License:        GPL-3.0-or-later

%description lang
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

This subpackage provides translations for PSPP.
%endif


%package devel
Summary:        Development files for PSPP, a statistical analysis program
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       cairo-devel
Requires:       glib2-devel
Requires:       glibc-devel
Requires:       gsl-devel
Requires:       harfbuzz-devel
Requires:       libxml2-devel
Requires:       pango-devel
Requires:       postgresql-devel
Requires:       zlib-devel
%if 0%{?suse_version} 
Requires:       xz-devel
%endif
Recommends:     %{name}-devel-doc = %{version}

%description devel
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

This subpackage contains libraries and header files for developing
applications that want to build pspp plugins.


%package doc
Summary:        Manual for PSPP
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

This subpackage contains documentation for PSPP.


%package devel-doc
Summary:        PSPP Developers Guide
License:        GPL-3.0-or-later
BuildArch:      noarch

%description devel-doc
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

This subpackage contains development documentation for PSPP.


%prep
%setup -q -n pspp-%{version}

%build
export SUSE_ASNEEDED=0
export CFLAGS="%{optflags} -fgnu89-inline -fcommon"
%configure \
             --disable-relocatable --disable-static --disable-rpath \
             --without-libreadline-prefix

%if 0%{?suse_version} >= 1500 
%make_build
%else
make
%endif
make html

%install
%make_install
%if 0%{?suse_version}
%suse_update_desktop_file -r org.gnu.%{name} Education Math
%endif

# Use help in HTML
mv ./doc/pspp.html/ ./doc/pspp-dev.html/ %{buildroot}%{_datadir}/doc/pspp/
# don't need xml since we have html
rm -f %{buildroot}/%{_datadir}/doc/pspp/pspp.xml
# screenshots directory contains *.png, *.eps and *.grab, but only *.png is sufficient
rm -f %{buildroot}/%{_datadir}/doc/pspp/pspp.html/pspp-figures/*.{eps,grab}
# don't need pspp-figures directory because 
# * sps, html tables are already incorporated in html documentation
# * texi, txt, spv tables are redundant
# * png has very bad quality
[ -d %{buildroot}/%{_infodir}/pspp-figures ] && rm -fr %{buildroot}/%{_infodir}/pspp-figures
[ -d %{buildroot}%{_datadir}/doc/pspp/pspp.html/pspp-figures ] && rm -fr %{buildroot}%{_datadir}/doc/pspp/pspp.html/pspp-figures
# screenshots must not be in /usr/share/info, but in /usr/share/doc/pspp/pspp.html/
[ -d %{buildroot}/%{_infodir}/screenshots ] && mv %{buildroot}/%{_infodir}/screenshots/  %{buildroot}%{_datadir}/doc/pspp/pspp.html/
# don't own /usr/share/info/dir if it exist
[ -f %{buildroot}/%{_infodir}/dir ] && rm %{buildroot}/%{_infodir}/dir
# PSPP 2.0 no longer installs /usr/bin/pspp-dump-sav by default, thus its man is not needed
[ -f %{buildroot}/%{_mandir}/man1/pspp-dump-sav.1 ] && rm -f %{buildroot}/%{_mandir}/man1/pspp-dump-sav.1
# don't own /usr/share/info/dir if it exist
[ -f %{buildroot}/%{_infodir}/dir ] && rm %{buildroot}/%{_infodir}/dir

#Config for ld
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >%{buildroot}%{_sysconfdir}/ld.so.conf.d/pspp.conf <<EOF
%{_libdir}/pspp
EOF

# AppData
mv $RPM_BUILD_ROOT/%{_datadir}/metainfo $RPM_BUILD_ROOT/%{_datadir}/appdata

%if 0%{?suse_version}
%fdupes -s %{buildroot}/%{_datadir}
%endif

# localization
%find_lang pspp

%check
export TESTSUITEFLAGS='-v -j128'
%make_build check || /bin/true
# just look into test results, don't need to package them
[ -f ./tests/testsuite.log ] && cat ./tests/testsuite.log

%post
/sbin/ldconfig
%install_info  --info-dir=%{_infodir}  %{_infodir}/pspp.info
%desktop_database_post

%preun
if [ $1 = 0 ] ; then
   %install_info_delete --info-dir=%{_infodir} %{_infodir}/pspp.info*
fi

%postun
/sbin/ldconfig
%desktop_database_postun

%files
%license COPYING
%doc README THANKS AUTHORS
%exclude %dir %{_datadir}/doc/pspp/
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/pspp.conf
%{_bindir}/pspp
%{_bindir}/psppire
%{_bindir}/pspp-convert
%{_bindir}/pspp-output
%defattr(644,root,root,755)
%{_infodir}/pspp*info*
%dir %{_libdir}/pspp/
%{_libdir}/pspp/*.so
%{_datadir}/pspp
%exclude %dir %{_datadir}/pspp/tests
%exclude %{_datadir}/pspp/tests/testsuite.log
%{_datadir}/icons/hicolor/scalable/apps/org.gnu.pspp.svg
%{_datadir}/icons/hicolor/16x16/apps/org.gnu.pspp.png
%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-spss-*.png
%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-spss-*.png
%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-spss-*.png
%{_datadir}/icons/hicolor/256x256/apps/org.gnu.pspp.png
%{_datadir}/icons/hicolor/256x256/mimetypes/application-x-spss-*.png
%{_datadir}/icons/hicolor/32x32/apps/org.gnu.pspp.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-spss-*.png
%{_datadir}/icons/hicolor/48x48/apps/org.gnu.pspp.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-spss-*.png
%{_datadir}/mime/packages/org.gnu.pspp.xml
%{_datadir}/applications/org.gnu.pspp.desktop
%{_datadir}/appdata/org.gnu.pspp.metainfo.xml
%if 0%{?mandriva_version} 
%doc %{_mandir}/man1/pspp.1.xz
%doc %{_mandir}/man1/psppire.1.xz
%doc %{_mandir}/man1/pspp-convert.1.xz
%doc %{_mandir}/man1/pspp-output.1.xz
%else
%doc %{_mandir}/man1/pspp.1.gz
%doc %{_mandir}/man1/psppire.1.gz
%doc %{_mandir}/man1/pspp-convert.1.gz
%doc %{_mandir}/man1/pspp-output.1.gz
%endif

%files lang -f %{name}.lang

%files devel
%dir %{_libdir}/pspp/
%{_libdir}/pspp/libpspp-core.la
%{_libdir}/pspp/libpspp.la

%files doc
%defattr(-, root, root)
%dir %{_datadir}/doc/pspp/
%dir %{_datadir}/doc/pspp/pspp.html/
%doc %{_datadir}/doc/pspp/pspp.html/*.html
%dir %{_datadir}/doc/pspp/pspp.html/screenshots/
%{_datadir}/doc/pspp/pspp.html/screenshots/*.png
%exclude %dir %{_datadir}/doc/pspp/pspp-dev.html/

%files devel-doc
%defattr(-, root, root)
%dir %{_datadir}/doc/pspp/pspp-dev.html/
%doc %{_datadir}/doc/pspp/pspp-dev.html/*.html


%changelog

