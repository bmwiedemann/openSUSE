#
# spec file for package fairymax
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fairymax
Version:        5.0b
Release:        0
Summary:        A xboard compatible chess and chess-variant engine
License:        SUSE-Public-Domain
Group:          Amusements/Games/Board/Chess
Url:            http://home.hccnet.nl/h.g.muller/CVfairy.html
# downloaded from: http://hgm.nubati.net/cgi-bin/gitweb.cgi?p=fairymax.git;a=snapshot;h=refs/tags/%{version};sf=tgz
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fairymax-makefile.patch
Patch0:         fairymax-makefile.patch
# PATCH-FIX-UPSTREAM fairymax-fix-return.patch
Patch1:         fairymax-fix-return.patch
BuildRequires:  fdupes
Provides:       chess_backend

%description
Fairymax is a program that plays chess and chess variants. It uses
the xboard/winboard chess-engine protocol to communicate. Apart from
'regular' chess (also known as the Mad-Queen variant), it can play
Capablanca chess, gothic chess, knightmate, cylinder chess, berolina
chess, superchess and courier chess.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%doc copyright changelog README CVfairy.html
%{_bindir}/fairymax
%{_bindir}/maxqi
%{_bindir}/shamax
%{_datadir}/games/fairymax
%{_datadir}/games/plugins
%{_mandir}/man6/fairymax.6%{ext_man}

%changelog
