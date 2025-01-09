#
# spec file for package espeak-ng
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1.52.0
Release:        0
Summary:        Software speech synthesizer (text-to-speech)
License:        Apache-2.0 AND BSD-2-Clause AND GPL-3.0-or-later AND Unicode-DFS-2015
URL:            https://github.com/espeak-ng/espeak-ng
Source0:        https://github.com/espeak-ng/espeak-ng/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool >= 2.4.2
BuildRequires:  pcaudiolib-devel
BuildRequires:  pkgconfig
BuildRequires:  rubygem(kramdown)
#SECTION docs
BuildRequires:  /usr/bin/ronn
#/SECTION

%description
The eSpeak NG (Next Generation) Text-to-Speech program is a speech
synthesizer that supports 100 languages and accents. It is based
on the eSpeak engine created by Jonathan Duddington. It uses
spectral formant synthesis by default which sounds robotic, but can
be configured to use Klatt formant synthesis or MBROLA to give it a
more natural sound.

%package        devel
Summary:        Development files for espeak-ng
Requires:       lib%{name}%{sover} = %{version}

%description    devel
This package contains development files for espeak-ng.

%package        compat
Summary:        Executables compatible with the original espeak
Requires:       %{name} = %{version}
Conflicts:      espeak
BuildArch:      noarch

%description    compat
This package contains executables compatible with the original espeak.

%package        compat-devel
Summary:        Development files for espeak-ng compatible with espeak
Requires:       %{name}-compat = %{version}
Requires:       espeak-ng-devel = %{version}
Requires:       libespeak-ng%{sover} = %{version}
Conflicts:      espeak-devel

%description    compat-devel
This package contains development files for espeak-ng
compatible with the original espeak.

%package     -n lib%{name}%{sover}
Summary:        Software speech synthesizer (text-to-speech)

%description -n lib%{name}%{sover}
Software speech synthesizer (text-to-speech), support
library.

%package vim
Summary:        Vim syntax highlighting for espeak-ng data files
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and vim)
BuildArch:      noarch

%description vim
Optional files for syntax highlighting for espeak-ng data files in vim.

%prep
%autosetup -p1
# let's have a versioned data dir
sed -i '/^DATADIR/s/data/data-%{version}/' Makefile.am
# remove spurious executable flag
chmod -x espeak-ng-data/lang/tai/shn

%build
./autogen.sh
%configure
# build is not parallel-safe
%make_build
LC_ALL=C.UTF-8 make docs

%install
%make_install
find %{buildroot} \( -name *.a -o -name *.la -o -name libespeak-ng-test* \) -delete
pushd %{buildroot}%{_libdir}
ln -s lib%{name}.so.%{sover} libespeak.so
popd
mv %{buildroot}%{_datadir}/vim/addons %{buildroot}%{_datadir}/vim/vimfiles
rm -vrf %{buildroot}%{_datadir}/vim/registry
%fdupes %{buildroot}

%check
ESPEAK_DATA_PATH=`pwd` LD_LIBRARY_PATH=src:${LD_LIBRARY_PATH} src/espeak-ng ...

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc ChangeLog.md README.md
%license COPYING COPYING.APACHE COPYING.BSD2 COPYING.UCD
%{_bindir}/espeak-ng
%{_bindir}/speak-ng
%{_mandir}/man1/speak-ng.1%{?ext_man}
%{_mandir}/man1/espeak-ng.1%{?ext_man}

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

%files vim
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/ftdetect/espeakfiletype.vim
%{_datadir}/vim/vimfiles/syntax/espeaklist.vim
%{_datadir}/vim/vimfiles/syntax/espeakrules.vim

%changelog
