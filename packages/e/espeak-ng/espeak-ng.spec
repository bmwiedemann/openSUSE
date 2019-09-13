#
# spec file for package espeak-ng
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           espeak-ng
Version:        1.49.2
Release:        0
Summary:        Software speech synthesizer (text-to-speech)
License:        GPL-3.0-or-later AND BSD-2-Clause AND Apache-2.0 AND Unicode-DFS-2015
Group:          Productivity/Multimedia/Other
Url:            https://github.com/espeak-ng/espeak-ng
Source0:        https://github.com/espeak-ng/espeak-ng/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM espeak-ng-1.49.2-fix_no_return_nonvoid.patch aloisio@gmx.com -- addresses rpmlint complaint
Patch0:         espeak-ng-1.49.2-fix_no_return_nonvoid.patch
Patch1:         espeak-ng-1.49.2-fix_no_return_nonvoid-in-configure.patch
BuildRequires:  fdupes
BuildRequires:  libtool >= 2.4.2
BuildRequires:  pcaudiolib-devel
BuildRequires:  pkgconfig

%description
The eSpeak NG (Next Generation) Text-to-Speech program is a speech
synthesizer that supports 100 languages and accents. It is based
on the eSpeak engine created by Jonathan Duddington. It uses
spectral formant synthesis by default which sounds robotic, but can
be configured to use Klatt formant synthesis or MBROLA to give it a
more natural sound.

%package        devel
Summary:        Development files for espeak-ng
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
This package contains development files for espeak-ng.

%package        compat
Summary:        Executables compatible with the original espeak
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Conflicts:      espeak

%description    compat
This package contains executables compatible with the original espeak.

%package        compat-devel
Summary:        Development files for espeak-ng compatible with espeak
Group:          Development/Languages/C and C++
Requires:       %{name}-compat = %{version}
Requires:       espeak-ng-devel = %{version}
Conflicts:      espeak-devel

%description    compat-devel
This package contains development files for espeak-ng
compatible with the original espeak.

%package     -n lib%{name}%{sover}
Summary:        Software speech synthesizer (text-to-speech)
Group:          System/Libraries

%description -n lib%{name}%{sover}
Software speech synthesizer (text-to-speech), support
library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# let's have a versioned data dir
sed -i '/^DATADIR/s/data/data-%{version}/' Makefile.am

%build
./autogen.sh
%configure \
   --with-extdict-ru \
   --with-extdict-zh \
   --with-extdict-zhy
# build is not parallel-safe
make V=1

%install
%make_install
find %{buildroot} \( -name *.a -o -name *.la -o -name libespeak-ng-test* \) -delete
pushd %{buildroot}%{_libdir}
ln -s lib%{name}.so.%{sover} libespeak.so
popd
%fdupes -s %{buildroot}

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc CHANGELOG.md README.md
%license COPYING COPYING.APACHE COPYING.BSD2 COPYING.IEEE COPYING.UCD
%{_bindir}/espeak-ng
%{_bindir}/speak-ng
%{_datadir}/vim

%files devel
%exclude %{_includedir}/espeak
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files compat
%{_bindir}/espeak
%{_bindir}/speak

%files compat-devel
%{_includedir}/espeak
%{_libdir}/libespeak.so

%files -n lib%{name}%{sover}
%{_datadir}/espeak-ng-data-%{version}
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
