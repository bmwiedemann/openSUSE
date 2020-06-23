#
# spec file for package autogen
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


%define         libname libopts25
Name:           autogen
Version:        5.18.16
Release:        0
Summary:        Automated Text File Generator
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://www.gnu.org/software/autogen/
Source0:        https://ftp.gnu.org/gnu/autogen/rel%{version}/%{name}-%{version}.tar.xz
Patch1:         autogen-build_ldpath.patch
# PATCH-FIX-UPSTREAM -- https://savannah.gnu.org/support/index.php?109234 boo#1021353
Patch2:         autogen-catch-race-error.patch
# PATCH-FIX-UPSTREAM don't make programs uninstallable
Patch3:         installable-programs.patch
# PATCH-FIX-UPSTREAM
Patch4:         sprintf-overflow.patch
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/autogen/bugs/193/#5844
Patch5:         gcc9-fix-wrestrict.patch
# PATCH-FIX-UPSTREAM Allow building with guile 3.0
Patch6:         guile-version.patch
BuildRequires:  fdupes
BuildRequires:  guile-devel
BuildRequires:  makeinfo
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
AutoGen is a tool designed for generating program files that contain
repetitive text with varied substitutions.  Its goal is to simplify the
maintenance of programs that contain large amounts of repetitious text.
This is especially valuable if there are several blocks of such text that
must be kept synchronized in parallel tables.

%package -n %{libname}
Summary:        Shared library libopts
Group:          System/Libraries

%description -n %{libname}
AutoOpts is a tool that virtually eliminates the hassle of processing
options and keeping man pages, info docs and usage text up to date.  This
package allows you to specify several program attributes, thousands of
option types and many option attributes.  From this, it then produces all
the code necessary to parse and handle the command line and configuration
file options, and the documentation that should go with your program as
well.

This package contains shared library libopts

%package -n autoopts
Summary:        Automated Option Processing
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}-%{release}
Requires:       autogen
Obsoletes:      %{libname}-devel < %{version}-%{release}
Provides:       autogen:/usr/bin/autoopts-config
Provides:       libopts-devel

%description -n autoopts
AutoOpts is a tool that virtually eliminates the hassle of processing
options and keeping man pages, info docs and usage text up to date.  This
package allows you to specify several program attributes, thousands of
option types and many option attributes.  From this, it then produces all
the code necessary to parse and handle the command line and configuration
file options, and the documentation that should go with your program as
well.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
touch aclocal.m4 configure Makefile.in config-h.in

%build
%configure \
	--enable-timeout=70 \
	--disable-static \
	--with-pic
make %{?_smp_mflags}

%install
export MAN_PAGE_DATE=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%s)} -I)
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_datadir}

%check
make %{?_smp_mflags} check VERBOSE=1

%post
%install_info --info-dir=%{_infodir} %{_infodir}/autogen.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autogen.info%{ext_info}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc NEWS
%license COPYING
%{_bindir}/autogen
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/xml2ag
%{_mandir}/man1/*%{ext_man}
%exclude %{_mandir}/man1/autoopts-config.1%{ext_man}
%{_infodir}/*%{ext_info}
%dir %{_datadir}/autogen
%{_datadir}/autogen/fsm-trans.tlib
%{_datadir}/autogen/fsm-macro.tlib

%files -n %{libname}
%{_libdir}/libopts.so.*

%files -n autoopts
%{_bindir}/autoopts-config
%{_libdir}/libopts.so
%{_includedir}/*
%{_mandir}/man1/autoopts-config.1%{ext_man}
%{_mandir}/man3/*%{ext_man}
%{_libdir}/autogen
%{_datadir}/aclocal/*
%{_datadir}/autogen
%exclude %{_datadir}/autogen/fsm-trans.tlib
%exclude %{_datadir}/autogen/fsm-macro.tlib
%{_libdir}/pkgconfig/*.pc

%changelog
