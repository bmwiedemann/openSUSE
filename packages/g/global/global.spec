#
# spec file for package global
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


Name:           global
Version:        6.6.4
Release:        0
Summary:        Common source code tag system
License:        GPL-3.0-only
Group:          Development/Tools/Navigators
URL:            http://www.gnu.org/software/global/
Source0:        ftp://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch0:         global-5.7.diff
# PATCH-FIX-UPSTREAM fix_paths.patch bnc#977967
Patch1:         fix_paths.patch
Patch2:         global-gcc10.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  emacs-nox
BuildRequires:  fdupes
BuildRequires:  idutils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(python3)
Requires:       python3-Pygments
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     ctags
Recommends:     idutils

%description
GLOBAL is a common source code tag system for C, C++, Yacc, and Java.
You can locate the specified function in source files and move there
easily. It is useful to hack a large project containing many
subdirectories or many main() functions like MH, X, or Linux kernel.

%prep
%setup -q
%patch0
%patch1
%patch2 -p1

%build
autoreconf -fiv
export CPPFLAGS="-fno-common"
%configure \
  --disable-static \
  --without-included-ltdl \
  --with-exuberant-ctags=%{_bindir}/ctags \
  PYTHON=python3
make %{?_smp_mflags}

%install
%make_install
install -d -m 755 %{buildroot}/{usr/share/emacs/site-lisp,etc}
mv %{buildroot}/%{_docdir}/%{name}/gtags.el %{buildroot}%{_datadir}/emacs/site-lisp/
mv %{buildroot}/%{_docdir}/%{name}/gtags.conf %{buildroot}%{_sysconfdir}/
rm -rf %{buildroot}/%{_docdir}/%{name}/INSTALL

# use python3 by default
sed -i "s|env python|python3|g" \
  %{buildroot}%{_datadir}/gtags/script/pygments_parser.py

# Do not use env
sed -i "s|env perl|perl|g" \
  %{buildroot}%{_datadir}/gtags/script/maps2conf.pl

%fdupes -s %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%config(noreplace) %{_sysconfdir}/gtags.conf
%{_bindir}/global
%{_bindir}/globash
%{_bindir}/gozilla
%{_bindir}/gtags
%{_bindir}/gtags-cscope
%{_bindir}/htags
%{_bindir}/htags-server
%doc %{_docdir}/%{name}
%{_mandir}/man1/global.1%{?ext_man}
%{_mandir}/man1/globash.1%{?ext_man}
%{_mandir}/man1/gozilla.1%{?ext_man}
%{_mandir}/man1/gtags-cscope.1%{?ext_man}
%{_mandir}/man1/gtags.1%{?ext_man}
%{_mandir}/man1/htags-server.1%{?ext_man}
%{_mandir}/man1/htags.1%{?ext_man}
%{_mandir}/man5/gtags.conf.5%{?ext_man}
%{_infodir}/global.info%{?ext_info}
%{_datadir}/emacs/site-lisp/gtags.el
%{_datadir}/gtags
%{_libdir}/gtags

%changelog
