#
# spec file for package libTMCG
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Andreas Stieger <andreas.stieger@gmx.de>
# Copyright (c) 2007 pc2pus <toni@links2linux.de>
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


%define sover 18
Name:           libTMCG
Version:        1.3.18
Release:        0
Summary:        C++ library for creating secure and fair online card games
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.nongnu.org/libtmcg/
Source:         https://download.savannah.gnu.org/releases/libtmcg/%{name}-%{version}.tar.gz
Source2:        https://download.savannah.gnu.org/releases/libtmcg/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=libtmcg&download=1#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  libgcrypt-devel >= 1.7.0
BuildRequires:  libgpg-error-devel >= 0.5
BuildRequires:  pkgconfig
Requires:       gmp >= 4.2

%description
LibTMCG is a C++ library for creating secure and fair online card
games. The library contains classes, algorithms, and high-level
protocols to support an application programmer in writing such
software.

%package -n libTMCG%{sover}
Summary:        C++ library for creating secure and fair online card games
Group:          System/Libraries

%description -n libTMCG%{sover}
LibTMCG is a C++ library for creating secure and fair online card
games. The library contains classes, algorithms, and high-level
protocols to support an application programmer in writing such
software. Neither a trusted third party (TTP), i.e. a central game
server, nor trusted hardware components are necessary. With the
library, there is no need for an independent referee, because the
applied protocols provide a basic level of confidentiality and
fairness by itself. The library is suited for peer-to-peer (P2P)
environments where no TTP is available.

It cannot be avoided that malicious players share information about
their private cards, but the protocols ensure that the shuffle of the
deck is performed randomly (presumed that at least one player is
honest) and thus the cards will be distributed uniformly among the
players. Further, no coalition can learn the private cards of a
player against his will (except for trivial conclusions). The
corresponding cryptographic problemis called Mental Poker, and
LibTMCG provides an implementation of such protocols.

The implementation relies on cryptographic techniques---the so-called
zero-knowledge proofs. Using these building blocks, the high-level
protocols minimize the effect of coalitions and preserve the
confidentiality of the players' strategy, i.e. the players are not
required to reveal their cards at the end of the game to show that
they did not cheat.

%package devel
Summary:        Libraries and headers to develop with libTMCG library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
Libraries and headers to develop with the libTMCG library.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -n libTMCG%{sover} -p /sbin/ldconfig
%postun -n libTMCG%{sover} -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -n libTMCG%{sover}
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS PATENTS THANKS TODO README
%{_libdir}/lib*.so.*

%files devel
%doc AUTHORS BUGS ChangeLog NEWS PATENTS THANKS TODO README
%license COPYING
%{_bindir}/%{name}-config
%{_libdir}/lib*.so
%{_includedir}/*.h*
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info%{?ext_info}

%changelog
