#
# spec file for package global
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           global
Version:        6.6.13
Release:        0
Summary:        Common source code tag system
License:        GPL-3.0-only
Group:          Development/Tools/Navigators
URL:            https://www.gnu.org/software/global/
Source0:        ftp://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=250#/%{name}.keyring
Patch0:         global-5.7.diff
# PATCH-FIX-UPSTREAM fix_paths.patch bnc#977967
Patch1:         fix_paths.patch
BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
BuildRequires:  emacs-nox
BuildRequires:  fdupes
BuildRequires:  idutils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
Requires:       python3-Pygments
Recommends:     idutils
Recommends:     universal-ctags >= 6.0.0

%description
GLOBAL is a common source code tag system for C, C++, Yacc, and Java.
You can locate the specified function in source files and move there
easily. It is useful to hack a large project containing many
subdirectories or many main() functions like MH, X, or Linux kernel.

%prep
%autosetup -p1

%build
autoreconf -fiv
export CPPFLAGS="-fno-common"
%configure \
  --with-python-interpreter=%{_bindir}/python3 \
  --disable-static \
  --with-sqlite3 \
  --without-included-ltdl \
  --with-universal-ctags=%{_bindir}/ctags \
  %{nil}
%make_build

%install
%make_install
install -d -m 755 %{buildroot}/{usr/share/emacs/site-lisp,etc}
mv %{buildroot}/%{_docdir}/%{name}/gtags.el %{buildroot}%{_datadir}/emacs/site-lisp/
mv %{buildroot}/%{_docdir}/%{name}/gtags.conf %{buildroot}%{_sysconfdir}/
rm -rf %{buildroot}/%{_docdir}/%{name}/INSTALL

# installed via %%license
rm -v %{buildroot}/%{_docdir}/%{name}/COPYING*
rm -v %{buildroot}/%{_docdir}/%{name}/LICENSE

%if 0%{?suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_datadir}/gtags/script/pygments_parser.py
%endif

# Do not use env
sed -i "s|env perl|perl|g" \
  %{buildroot}%{_datadir}/gtags/script/maps2conf.pl

%fdupes -s %{buildroot}

%check
%make_build check

%files
%license COPYING COPYING.LIB LICENSE
%{_bindir}/global
%{_bindir}/globash
%{_bindir}/gozilla
%{_bindir}/gtags
%{_bindir}/gtags-cscope
%{_bindir}/htags
%{_bindir}/htags-server
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%config(noreplace) %{_sysconfdir}/gtags.conf
%doc %{_docdir}/%{name}
%{_mandir}/man*/*%{?ext_man}
%{_infodir}/global.info%{?ext_info}
%{_datadir}/emacs/site-lisp/gtags.el
%{_datadir}/gtags
%{_libdir}/gtags

%changelog
