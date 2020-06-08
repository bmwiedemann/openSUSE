#
# spec file for package pspp
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2008 Matj Cepl <mcepl@redhat.com>
# Copyright (c) 2008 D. Steuer <steuer@hsuhh.de>
# Copyright (c) 2018 <astieger@suse.com>
# Copyright (c) 2010-2019 <opensuse.lietuviu.kalba@gmail.com>
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
Version:        1.2.0
Release:        0
Summary:        A program for statistical analysis of sampled data
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/pspp/
Source0:        ftp://ftp.gnu.org/pub/gnu/pspp/pspp-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/pub/gnu/pspp/pspp-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=245#/%{name}.keyring
# PATCH-FIX-UPSTREAM CVE-2018-20230.patch bnc#1120061 CVE-2018-20230
Patch0:         CVE-2018-20230.patch
# PATCH-FIX-UPSTREAM CVE-2019-9211.patch boo#1127343 CVE-2019-9211
Patch1:         CVE-2019-9211.patch
# Fix build with Texinfo 4.13 for openSUSE Leap 42.*
Patch2:         avoid_old_Texinfo_4.13.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gsl-devel >= 1.12
BuildRequires:  gtk3-devel >= 3.14.5
BuildRequires:  libglade2-devel
BuildRequires:  libxml2-devel
BuildRequires:  m4
BuildRequires:  pango-devel
BuildRequires:  postgresql-devel
BuildRequires:  readline-devel
BuildRequires:  spread-sheet-widget-devel >= 0.3
BuildRequires:  texinfo
BuildRequires:  zlib-devel
Requires:       yelp
%if 0%{?centos_version}
BuildRequires:  gtksourceview3-devel
BuildRequires:  perl
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  pkgconfig
%endif
%if 0%{?fedora}
BuildRequires:  atlas
BuildRequires:  gtksourceview3-devel
BuildRequires:  perl
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  pkgconfig
%endif
%if 0%{?mandriva_version}
BuildRequires:  gtksourceview-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  perl-base
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
%endif
%if  0%{?suse_version}
BuildRequires:  gtksourceview-devel >= 3.18.0
%endif
%if 0%{?suse_version}
#Next package only for "make check"
BuildRequires:  free-ttf-fonts
%endif
%if  0%{?suse_version} <= 1310
BuildRequires:  postgresql-libs
%else
# BuildRequires:  postgresql93-libs
%endif
%if 0%{?suse_version} <= 1320
BuildRequires:  libtool
%endif

%description
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

PSPP development is ongoing. It already supports a large subset of
SPSS's syntax. Its statistical procedure support is currently
limited, but growing. At your option, PSPP will produce statistical
reports in ASCII, PostScript, PDF, HTML, SVG, or OpenDocument formats.

%package devel
Summary:        Development files for pspp, a statistical analysis program
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       gsl-devel
Requires:       libxml2-devel
Requires:       postgresql-devel
Requires:       zlib-devel

%description devel
PSPP is a program for statistical analysis of sampled data. It
is a free replacement for the proprietary program SPSS.

This subpackage contains libraries and header files for developing
applications that want to build pspp plugins.

%prep
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?mandriva_version}
%setup -q -n pspp-%{version}
%else
%setup -q -n pspp-%{version}
%endif

%patch0 -p1
%patch1 -p1
%if 0%{?suse_version} <= 1320
%patch2 -p1
%endif

%build
export SUSE_ASNEEDED=0
export CFLAGS="%{optflags} -fgnu89-inline -fcommon"
%if 0%{?suse_version} <= 1320
autoreconf -f -i
%endif
%configure \
             --disable-relocatable --disable-static --disable-rpath \
             --enable-debug --without-libreadline-prefix

#Fix "File is compiled without RPM_OPT_FLAGS"
%make_build

%install
%make_install
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} Education Math
%endif

%if 0%{?mandriva_version}
# do nothing
%else
# don't own /usr/share/info/dir if it exist
[ -d %{buildroot}/%{_infodir}/dir ] && rm %{buildroot}/%{_infodir}/dir
%endif

#Config for ld
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >%{buildroot}%{_sysconfdir}/ld.so.conf.d/pspp.conf <<EOF
%if 0%{?suse_version} > 1120
%{_libdir}/pspp
%endif
EOF

%if 0%{?suse_version}
%fdupes -s %{buildroot}/%{_datadir}
%endif

# localization
%find_lang pspp

%check
%make_build check || /bin/true

%post
/sbin/ldconfig
%install_info  --info-dir=%{_infodir}/dir  %{_infodir}/pspp.info
%if 0%{?suse_version} >= 1140
%desktop_database_post
%endif

%preun
if [ $1 = 0 ] ; then
   %install_info_delete --info-dir=%{_infodir}/dir %{_infodir}/pspp.info*
fi

%postun
/sbin/ldconfig
%if 0%{?suse_version} >= 1140
%desktop_database_postun
%endif

%files -f pspp.lang
%license COPYING
%doc README THANKS AUTHORS
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/pspp.conf
%{_bindir}/pspp
%{_bindir}/psppire
%{_bindir}/pspp-dump-sav
%{_bindir}/pspp-convert
%defattr(644,root,root,755)
%{_infodir}/pspp*
%dir %{_libdir}/pspp/
%{_libdir}/pspp/*.so
%{_datadir}/pspp
%doc %{_datadir}/doc/pspp
%{_datadir}/icons/hicolor/scalable/apps/pspp.svg
%{_datadir}/icons/hicolor/16x16/apps/pspp.png
%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/16x16/mimetypes/application-x-spss-zsav.png
%{_datadir}/icons/hicolor/22x22/apps/pspp.png
%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/22x22/mimetypes/application-x-spss-zsav.png
%{_datadir}/icons/hicolor/24x24/apps/pspp.png
%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/24x24/mimetypes/application-x-spss-zsav.png
%{_datadir}/icons/hicolor/256x256/apps/pspp.png
%{_datadir}/icons/hicolor/256x256/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/256x256/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/256x256/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/256x256/mimetypes/application-x-spss-zsav.png
%{_datadir}/icons/hicolor/32x32/apps/pspp.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-spss-zsav.png
%{_datadir}/icons/hicolor/48x48/apps/pspp.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-spss-por.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-spss-sav.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-spss-sps.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-spss-zsav.png
%{_datadir}/applications/pspp.desktop
%if 0%{?mandriva_version}
%{_mandir}/man1/pspp.1.xz
%{_mandir}/man1/psppire.1.xz
%{_mandir}/man1/pspp-dump-sav.1.xz
%{_mandir}/man1/pspp-convert.1.xz
%else
%{_mandir}/man1/pspp.1%{?ext_man}
%{_mandir}/man1/psppire.1%{?ext_man}
%{_mandir}/man1/pspp-dump-sav.1%{?ext_man}
%{_mandir}/man1/pspp-convert.1%{?ext_man}
%endif
%dir %{_datadir}/appdata/
%{_datadir}/appdata/pspp.appdata.xml

%files devel
%dir %{_libdir}/pspp/
%{_libdir}/pspp/libpspp-core.la
%{_libdir}/pspp/libpspp.la

%changelog
