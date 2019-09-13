#
# spec file for package gnu-cobol
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover   4
%define _mver   3.0
%define _over   3.0-rc1
Name:           gnu-cobol
Version:        3.0rc1
Release:        0
Summary:        A COBOL compiler
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Other
Url:            https://savannah.gnu.org/projects/gnucobol
Source0:        https://sourceforge.net/projects/open-cobol/files/gnu-cobol/%{_mver}/gnucobol-%{_over}.tar.xz
Source1:        %{name}.changes
# PATCH-FIX-OPENSUSE gnucobol-CFLAGS.patch -- fixes overreaching regex
Patch2:         gnucobol-CFLAGS.patch
BuildRequires:  db-devel
BuildRequires:  dos2unix
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       opencobol = %{version}

%description
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n libcob%{sover}
Summary:        GnuCOBOL shared library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Other

%description -n libcob%{sover}
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n libcob-devel
Summary:        Include files for the GnuCOBOL shared library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       libcob%{sover} = %{version}

%description -n libcob-devel
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%prep
%setup -q -n gnucobol-%{_over}
%patch2 -p1
# replace build date with date from changelog
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"
# fix EOL encoding
dos2unix ABOUT-NLS AUTHORS COPYING COPYING.DOC ChangeLog NEWS \
 README THANKS TODO COPYING.LESSER

%build
%configure \
	--enable-static=no
make %{?_smp_mflags}

%install
%make_install
# do not ship these
rm %{buildroot}%{_libdir}/libcob.la
%find_lang gnucobol

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%post -n libcob%{sover} -p /sbin/ldconfig
%postun -n libcob%{sover} -p /sbin/ldconfig

%files -f gnucobol.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING COPYING.DOC ChangeLog NEWS README THANKS TODO
%{_bindir}/cob-config
%{_bindir}/cobc
%{_bindir}/cobcrun
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info%{ext_info}
%{_libdir}/gnucobol
%{_mandir}/man1/cobc.1%{ext_info}
%{_mandir}/man1/cobcrun.1%{ext_info}

%files -n libcob%{sover}
%defattr(-,root,root)
%doc COPYING.LESSER
%{_libdir}/libcob.so.%{sover}*

%files -n libcob-devel
%defattr(-,root,root)
%{_includedir}/libcob.h
%{_includedir}/libcob
%{_libdir}/libcob.so

%changelog
