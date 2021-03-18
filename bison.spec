#
# spec file for package bison
#
# Copyright (c) 2021 SUSE LLC
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


Name:           bison
Version:        3.7.6
Release:        0
Summary:        The GNU Parser Generator
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/bison/bison.html
Source0:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  flex
BuildRequires:  gcc-c++
Requires:       m4

%description
Bison is a parser generator similar to yacc(1).

%lang_package

%prep
%autosetup

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure \
  --disable-silent-rules \
  --disable-rpath \
  --enable-nls \
  --docdir=%{_docdir}/%{name} \
  gl_cv_func_printf_directive_n=yes \
  gl_cv_func_printf_infinite_long_double=yes
%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  %make_build CFLAGS="%{optflags}" check
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%check
%make_build check

%install
%make_install
%find_lang %{name} --all-name

%files lang -f %{name}.lang

%files
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%exclude %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/examples
%dir %{_datadir}/aclocal
%{_bindir}/bison
%{_bindir}/yacc
%{_libdir}/liby.a
%{_datadir}/bison
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/bison-i18n.m4
%{_infodir}/bison.info*.gz
%{_mandir}/man1/bison.1%{?ext_man}
%{_mandir}/man1/yacc.1%{?ext_man}

%changelog
