#
# spec file for package jconvolver
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jconvolver
Version:        1.0.3
Release:        0
Summary:        Convolution engine for JACK
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch:          jconvolver-build-fixes.diff
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zita-convolver-devel >= 4.0.0
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)

%description
Jconvolver is a Convolution Engine for JACK, based on FFT convolution and using
non-uniform partition sizes: small ones at the start of the IR and building up
to the most efficient size further on. It can perform zero-delay processing with
moderate CPU load.

Main features:
  * Any matrix of convolutions between up to up 64 inputs and 64 outputs, as
    long as your CPU(s) can handle it.
  * Allows trading off CPU load to processing delay, and remains efficient even
    when configured for zero delay.
  * Sparse and diagonal matrices are handled as efficiently as dense ones.
    No CPU cycles or memory resources are wasted on empty cells in the matrix,
    nor on empty partitions if IRs are of different length.

%package examples
Summary:        Configuration examples for jconvolver
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}

%description examples
This package contains configuration examples for jconvolver, a convolution
engine for JACK.

%prep
%setup -q
%patch -p1

%build
CXXFLAGS="%{optflags}" make -C source %{?_smp_mflags}

%install
%make_install -C source PREFIX=%{_prefix}
install -d %{buildroot}%{_docdir}/%{name}
cp -r config-files %{buildroot}%{_docdir}/%{name}

%files
%doc README README.CONFIG
%license COPYING
%{_bindir}/jconvolver
%{_bindir}/fconvolver
%{_bindir}/makemulti

%files examples
%{_docdir}/%{name}/config-files

%changelog
