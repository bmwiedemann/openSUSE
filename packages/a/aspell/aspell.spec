#
# spec file for package aspell
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


Name:           aspell
Version:        0.60.8
Release:        0
Summary:        A Spell Checker
License:        GFDL-1.1-or-later AND LGPL-2.1-only AND HPND AND SUSE-BSD-Mark-Modifications
Group:          Productivity/Text/Spell
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source100:      baselibs.conf
# PATCH-FIX-OPENSUSE aspell-strict-aliasing.patch pnemec@suse.cz -- Fix gcc strict aliasing warnings
Patch0:         aspell-strict-aliasing.patch
# PATCH-FIX-OPENSUSE aspell-quotes.patch lmichnovic@suse.cz -- Fix command execution in script "run-with-aspell"
Patch1:         aspell-quotes.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
Requires(post): info
Requires(preun): info
Recommends:     aspell-en
Suggests:       aspell-ispell
Suggests:       aspell-spell
Provides:       pspell = %{version}
Obsoletes:      pspell < %{version}

%description
GNU Aspell is a spell checker planned to eventually replace Ispell. It
can be used as a library or as an independent spell checker.

Its main feature is an improved method for finding possible
suggestions for the English language, arguably surpassing Ispell and
Microsoft Word. It also has many other technical enhancements over
Ispell, such as using shared memory for dictionaries and
intelligently handling personal dictionaries when more than one
Aspell process is open at once.

%package devel
Summary:        Include Files and Libraries Mandatory for Development with aspell
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libaspell15 = %{version}
Requires:       libpspell15 = %{version}
Requires(post): info
Requires(preun): info
Provides:       pspell-devel = %{version}
Obsoletes:      pspell-devel < %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require aspell.

%package ispell
Summary:        GNU Aspell - Ispell compatibility
Group:          Productivity/Text/Spell
Requires:       %{name} = %{version}
Conflicts:      ispell

%description ispell
GNU Aspell is a spell checker planned to eventually replace Ispell. It
can be used as a library or as an independent spell checker.

This package contains an ispell script for compatibility reasons so that
programs that expect the "ispell" command will work correctly.

%package spell
Summary:        GNU Aspell - Spell compatibility
Group:          Productivity/Text/Spell
Requires:       %{name} = %{version}
Provides:       spell

%description spell
GNU Aspell is a spell checker planned to eventually replace Ispell. It
can be used as a library or as an independent spell checker.

This package contains a spell script for compatibility reasons so that programs
that expect the "spell" command will work correctly.

%package -n libaspell15
Summary:        GNU Aspell Library
Group:          System/Libraries

%description -n libaspell15
GNU Aspell is a spell checker planned to eventually replace Ispell. It
can be used as a library or as an independent spell checker.

This package contains the aspell library.

%package -n libpspell15
Summary:        GNU Aspell - Pspell Compatibility Library
Group:          System/Libraries
Recommends:     aspell-en

%description -n libpspell15
GNU Aspell is a spell checker planned to eventually replace Ispell. It
can be used as a library or as an independent spell checker.

This package contains the pspell compatibility library.

%prep
%autosetup -p0

%build
autoreconf -fiv
export CXXFLAGS="%{optflags} `ncursesw6-config --cflags`"
#this is an ugly kludge , don't look :-)
export LDFLAGS="`ncursesw6-config --libs`"
%configure \
  --enable-curses="-lncursesw" \
  --disable-rpath

%make_build

%install
%make_install
# Links for compatibility reasons (ispell and spell)
ln -s %{_libdir}/aspell-0.60/ispell %{buildroot}%{_bindir}
ln -s %{_libdir}/aspell-0.60/spell %{buildroot}%{_bindir}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}

%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}-dev.info%{ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}-dev.info%{ext_info}

%post -n libaspell15 -p /sbin/ldconfig

%postun -n libaspell15 -p /sbin/ldconfig

%post -n libpspell15 -p /sbin/ldconfig

%postun -n libpspell15 -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc README TODO
%doc manual/aspell.html/
%{_bindir}/aspell
%{_bindir}/aspell-import
%{_bindir}/pre*
%{_bindir}/run-with-aspell
%{_bindir}/word-list-compress
%{_infodir}/%{name}.info%{ext_info}
%{_mandir}/man1/*.1%{ext_man}
%exclude %{_mandir}/man1/pspell-config.1%{ext_man}

%files devel
%doc manual/aspell-dev.html/
%{_bindir}/pspell-config
%{_includedir}/pspell/
%{_includedir}/*.h
%{_libdir}/libaspell.so
%{_libdir}/libpspell.so
%{_infodir}/%{name}-dev.info%{ext_info}
%{_mandir}/man1/pspell-config.1%{ext_man}

%files ispell
%{_bindir}/ispell

%files spell
%{_bindir}/spell

%files -n libaspell15
%{_libdir}/aspell-0.60/
%{_libdir}/libaspell.so.15*

%files -n libpspell15
%{_libdir}/libpspell.so.15*

%changelog
