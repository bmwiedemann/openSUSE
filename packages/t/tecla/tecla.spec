#
# spec file for package tecla
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define _lto_cflags %{nil}

%define sover  1
%define libname lib%{name}_r%{sover}
Name:           tecla
Version:        1.6.3
Release:        0
Summary:        Interactive command line editing library
License:        X11
Group:          Development/Libraries/C and C++
Url:            http://www.astro.caltech.edu/~mcs/tecla/
Source:         http://www.astro.caltech.edu/~mcs/tecla/libtecla-%{version}.tar.gz
Patch0:         libtecla_add-destdir.patch
Patch1:         libtecla-makefiles-rules-no-rpath.diff
Patch2:         tecla-cppflags.diff
Patch3:         tecla-only-reentrant.diff
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  ncurses-devel

%description
The tecla library provides programs with interactive command line
editing facilities, similar to those of the tcsh shell.
In addition to simple command-line editing, it supports recall of
previously entered command lines, TAB completion of file names or
other tokens, and in-line wild-card expansion of filenames. The
internal functions which perform file-name completion and wild-card
expansion are also available externally for optional use by programs.

%package -n %{libname}
Summary:        Interactive command line editing library
Group:          System/Libraries

%description -n %{libname}
The tecla library provides programs with interactive command line
editing facilities, similar to those of the tcsh shell.
In addition to simple command-line editing, it supports recall of
previously entered command lines, TAB completion of file names or
other tokens, and in-line wild-card expansion of filenames. The
internal functions which perform file-name completion and wild-card
expansion are also available externally for optional use by programs.

%package devel
Summary:        Development files for tecla, an interactive command line editing library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The tecla library provides programs with interactive command line
editing facilities, similar to those of the tcsh shell.

%prep
%setup -q -n libtecla
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf # patch3
%configure CPPFLAGS=-Wno-cpp
make #%{?_smp_mflags} # parallel build is broken

%install
%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.a" -delete
rm -f "%{buildroot}/%{_libdir}"/libtecla.so*
ln -fsv libtecla_r.so "%{buildroot}/%{_libdir}/libtecla.so"
ln -s enhance_r %{buildroot}/%{_bindir}/enhance
%fdupes %{buildroot}/%{_mandir}/man3/

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGES README RELEASE.NOTES LICENSE.TERMS
%{_bindir}/enhance
%{_bindir}/enhance_r
%{_mandir}/man1/enhance.1%{ext_man}
%{_mandir}/man5/teclarc.5%{ext_man}
%{_mandir}/man7/tecla.7%{ext_man}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libtecla_r.so.*

%files devel
%defattr(-,root,root)
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/libtecla.h
%{_libdir}/libtecla.so
%{_libdir}/libtecla_r.so

%changelog
