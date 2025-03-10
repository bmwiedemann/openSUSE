#
# spec file for package liboggplay
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 2
Name:           liboggplay
Version:        0.3.0
Release:        0
Summary:        Library for playing Ogg multimedia
License:        BSD-3-Clause
URL:            https://wiki.xiph.org/index.php/OggPlay
Source:         https://downloads.xiph.org/releases/liboggplay/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(fishsound) >= 0.9.1
BuildRequires:  pkgconfig(kate)
BuildRequires:  pkgconfig(oggz) >= 0.9.8
BuildRequires:  pkgconfig(theora)

%description
OggPlay is a library designed to allow drop-in playback of Xiph.Org media
in an application.

%package -n %{name}%{sover}
Summary:        Library for playing Ogg multimedia

%description -n %{name}%{sover}
OggPlay is a library designed to allow drop-in playback of Xiph.Org media in an
application.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
OggPlay is a library designed to allow drop-in playback of Xiph.Org media in an
application.

This package contains the files needed to build with %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_docdir}/%{name}/latex

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%{_bindir}/oggplay-info
%{_libdir}/liboggplay.so.%{sover}
%{_libdir}/liboggplay.so.%{sover}.*

%files devel
%doc README AUTHORS ChangeLog
%license COPYING
%{_includedir}/oggplay
%{_libdir}/liboggplay.so
%{_libdir}/pkgconfig/oggplay.pc
%{_libdir}/pkgconfig/oggplay-uninstalled.pc
%{_docdir}/%{name}

%changelog
