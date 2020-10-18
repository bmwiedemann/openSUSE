#
# spec file for package bison
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


Name:           bison
Version:        3.7.3
Release:        0
Summary:        The GNU Parser Generator
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/bison/bison.html
Source0:        ftp://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  flex
BuildRequires:  gcc-c++
Requires:       m4
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

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
  # non-parallel profiling for reproducible results https://bugzilla.opensuse.org/show_bug.cgi?id=1040589
  %make_build --jobs=1 CFLAGS="%{optflags}" check
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%check
# Tests dont work reliably in parallel
%make_build --jobs=1 check

%install
%make_install
%find_lang %{name} --all-name

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files lang -f %{name}.lang

%files
%{_docdir}/%{name}
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
