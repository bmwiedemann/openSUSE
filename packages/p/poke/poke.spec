#
# spec file for package poke
#
# Copyright (c) 2023 SUSE LLC
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


%define sover   1
Name:           poke
Version:        4.1
Release:        0
Summary:        An interactive, extensible editor for binary data
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/poke/
Source0:        https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=217829#/%{name}.keyring
BuildRequires:  dejagnu
BuildRequires:  gawk
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(libnbd)
Recommends:     mimehandler(x-scheme-handler/app)
%if 0%{?suse_version} > 1500
BuildRequires:  libtextstyle-devel
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif

%description
GNU poke is an interactive, extensible editor for binary data. Not limited to
editing basic entities such as bits and bytes, it provides a full-fledged
procedural, interactive programming language designed to describe data
structures and to operate on them.

%package devel
Summary:        Devel package for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
Development package for %{name}.

%package -n lib%{name}%{sover}
Summary:        Support library for %{name}

%description -n lib%{name}%{sover}
Contains support library for %{name}.

%package -n emacs-%{name}
Summary:        Emacs support for %{name}
Requires:       %{name} = %{version}
Requires:       emacs
Supplements:    (emacs and %{name})
BuildArch:      noarch

%description -n emacs-%{name}
Provides Emacs support for %{name}.

%package -n vim-%{name}
Summary:        Vim support for %{name}
Requires:       %{name} = %{version}
Requires:       vim
Supplements:    (vim and %{name})
BuildArch:      noarch

%description -n vim-poke
Provides Vim support for %{name}.

%prep
%autosetup -p1

%build
# jitter fails to build with LTO, disable it for now
%define _lto_cflags %{nil}
%configure \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING
%doc README AUTHORS NEWS
%{_bindir}/%{name}
%{_bindir}/pk-bin2poke
%{_bindir}/pk-jojopatch
%{_bindir}/pk-strings
%{_bindir}/poked
%{_bindir}/pokefmt
%{_datadir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_infodir}/%{name}.info-1%{?ext_info}
%{_infodir}/%{name}.info-2%{?ext_info}
%{_infodir}/%{name}.info-3%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/pokefmt.1%{?ext_man}
%{_mandir}/man1/poked.1%{?ext_man}
%{_datadir}/poke/pickles/

%files devel
%license COPYING
%{_datadir}/aclocal/poke.m4
%{_includedir}/libpoke.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/poke.pc

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files -n emacs-%{name}
%license COPYING
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/poke-map-mode.el
%{_datadir}/emacs/site-lisp/poke-ras-mode.el

%files -n vim-%{name}
%license COPYING
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/ftdetect
%{_datadir}/vim/vimfiles/ftdetect/poke.vim
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/poke.vim

%changelog
