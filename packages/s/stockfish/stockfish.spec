#
# spec file for package stockfish
#
# Copyright (c) 2022 SUSE LLC
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


# See evaluate.h > EvalFileDefaultName
%define nnuenet nn-ad9b42354671.nnue
Name:           stockfish
Version:        15.1
Release:        0
Summary:        Chess engine
License:        GPL-3.0-or-later
URL:            https://stockfishchess.org
Source0:        https://github.com/official-stockfish/Stockfish/archive/sf_%{version}.tar.gz#/Stockfish-sf_%{version}.tar.gz
Source1:        https://tests.stockfishchess.org/api/nn/%{nnuenet}
# steal some documentation from ubuntu
Source10:       %{name}-interface.txt
Source11:       %{name}.6-20091204230329-yljoyxocuxhxg1ot-76/%{name}.6
# If 'Version' is not set it will display the date as version number. We dont want __DATE__ and Version is set anyways.
Patch0:         date.patch
# Don't try to download file. We already have it.
Patch1:         stockfish-remove-net.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  xz
Recommends:     xboard
Provides:       chess_backend
ExclusiveArch:  %{power64} %{ix86} x86_64 armv7l armv7hl armv7hnl
%ifarch %{power64}
BuildRequires:  gcc-c++-32bit
%endif

%description
Stockfish is a UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard with
PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in
order to be used comfortably. Read the documentation for your GUI of choice for
information about how to use Stockfish with your GUI.

%prep
%setup -q -n Stockfish-sf_%{version}
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} src/
cp -p %{SOURCE10} %{SOURCE11} .

dos2unix %{name}-interface.txt
dos2unix Copying.txt

%build
cd src
%ifarch x86_64
make %{?_smp_mflags} build ARCH=x86-64
%else
%ifarch %{power_64}
make %{?_smp_mflags} build ARCH=ppc-64
%else
%ifarch armv7l armv7hl armv7hnl
make %{?_smp_mflags} build ARCH=armv7
%else
#ix86
make %{?_smp_mflags} build ARCH=general-32
%endif
%endif
%endif

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p src/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
cp -p %{name}.6 %{buildroot}%{_mandir}/man6

%files
%license Copying.txt
%doc AUTHORS %{name}-interface.txt README.md
%{_mandir}/man*/%{name}.*
%{_bindir}/%{name}

%changelog
