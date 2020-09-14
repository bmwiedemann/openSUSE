#
# spec file for package pcsx2
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


Name:           pcsx2
Version:        1.6.0
Release:        0
Summary:        Sony PlayStation 2 Emulator
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only
URL:            http://pcsx2.net/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  i586

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
BuildRequires:  libpcap-devel-static
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

%description
Sony PlayStation 2 emulator. Requires a BIOS image in %{_libdir}/%{name}/bios
or in .%{name}/bios in your HOME directory (will be created when you first run
PCSX2). Check http://www.pcsx2.net/guide.php#Bios for details on which files
you need and how to obtain them.

%package     -n %{name}-lang-ar
Summary:        Arabic translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ar)
BuildArch:      noarch

%description -n %{name}-lang-ar
This package contains Arabic translations for PCSX2

%package     -n %{name}-lang-ca
Summary:        Catalan translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ca)
BuildArch:      noarch

%description -n %{name}-lang-ca
This package contains Catalan translations for PCSX2

%package     -n %{name}-lang-cs
Summary:        Czech translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:cs)
BuildArch:      noarch

%description -n %{name}-lang-cs
This package contains Czech translations for PCSX2

%package     -n %{name}-lang-da
Summary:        Danish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:da)
BuildArch:      noarch

%description -n %{name}-lang-da
This package contains Danish translations for PCSX2

%package     -n %{name}-lang-de
Summary:        German translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:de)
BuildArch:      noarch

%description -n %{name}-lang-de
This package contains German translations for PCSX2

%package     -n %{name}-lang-es
Summary:        Spanish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:es)
BuildArch:      noarch

%description -n %{name}-lang-es
This package contains Spanish translations for PCSX2

%package     -n %{name}-lang-fi
Summary:        Finnish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:fi)
BuildArch:      noarch

%description -n %{name}-lang-fi
This package contains Finnish translations for PCSX2

%package     -n %{name}-lang-fr
Summary:        French translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:fr)
BuildArch:      noarch

%description -n %{name}-lang-fr
This package contains French translations for PCSX2

%package     -n %{name}-lang-hr
Summary:        Croatian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:hr)
BuildArch:      noarch

%description -n %{name}-lang-hr
This package contains Croatian translations for PCSX2

%package     -n %{name}-lang-hu
Summary:        Hungarian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:hu)
BuildArch:      noarch

%description -n %{name}-lang-hu
This package contains Hungarian translations for PCSX2

%package     -n %{name}-lang-id
Summary:        Indonesian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:id)
BuildArch:      noarch

%description -n %{name}-lang-id
This package contains Indonesian translations for PCSX2

%package     -n %{name}-lang-it
Summary:        Italian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:it)
BuildArch:      noarch

%description -n %{name}-lang-it
This package contains Italian translations for PCSX2

%package     -n %{name}-lang-ja
Summary:        Japanese translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ja)
BuildArch:      noarch

%description -n %{name}-lang-ja
This package contains Japanese translations for PCSX2

%package     -n %{name}-lang-ko
Summary:        Korean translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ko)
BuildArch:      noarch

%description -n %{name}-lang-ko
This package contains Korean translations for PCSX2

%package     -n %{name}-lang-lt
Summary:        Lithuanian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:lt)
BuildArch:      noarch

%description -n %{name}-lang-lt
This package contains Lithuanian translations for PCSX2

%package     -n %{name}-lang-nb
Summary:        Norwegian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:nb)
BuildArch:      noarch

%description -n %{name}-lang-nb
This package contains Norwegian translations for PCSX2

%package     -n %{name}-lang-nl
Summary:        Dutch translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:nl)
BuildArch:      noarch

%description -n %{name}-lang-nl
This package contains Dutch translations for PCSX2

%package     -n %{name}-lang-pl
Summary:        Polish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:pl)
BuildArch:      noarch

%description -n %{name}-lang-pl
This package contains Polish translations for PCSX2

%package     -n %{name}-lang-pt_BR
Summary:        Brazilian Portuguese translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:pt_BR)
BuildArch:      noarch

%description -n %{name}-lang-pt_BR
This package contains Brazilian Portuguese translations for PCSX2

%package     -n %{name}-lang-ru
Summary:        Russian translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ru)
BuildArch:      noarch

%description -n %{name}-lang-ru
This package contains Russian translations for PCSX2

%package     -n %{name}-lang-sv
Summary:        Swedish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:sv)
BuildArch:      noarch

%description -n %{name}-lang-sv
This package contains Swedish translations for PCSX2

%package     -n %{name}-lang-th
Summary:        Thai translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:th)
BuildArch:      noarch

%description -n %{name}-lang-th
This package contains Thai translations for PCSX2

%package     -n %{name}-lang-tr
Summary:        Turkish translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:tr)
BuildArch:      noarch

%description -n %{name}-lang-tr
This package contains Turkish translations for PCSX2

%package     -n %{name}-lang-zh_CN
Summary:        Simplified Chinese translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:zh_CN)
BuildArch:      noarch

%description -n %{name}-lang-zh_CN
This package contains Simplified Chinese translations for PCSX2

%package     -n %{name}-lang-zh_TW
Summary:        Traditional Chinese translations for PCSX2
Requires:       %{name} = %{version}
Provides:       locale(%{name}:zh_TW)
BuildArch:      noarch

%description -n %{name}-lang-zh_TW
This package contains Traditional Chinese translations for PCSX2

%prep
%setup -q

%build
# -DUSER_CMAKE_C_FLAGS="-Wno-narrowing": build fails otherwise
# -DUSER_CMAKE_CXX_FLAGS="-Wno-narrowing": build fails otherwise
# -DDISABLE_ADVANCE_SIMD=ON: the name of this option is misleading. it actually
# build multiple binary for different instruction sets. it is more compatible
# to both old and new CPU.
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSER_CMAKE_C_FLAGS="-Wno-narrowing" \
  -DUSER_CMAKE_CXX_FLAGS="-Wno-narrowing" \
  -DXDG_STD=ON \
  -DPACKAGE_MODE=ON \
  -DDISABLE_ADVANCE_SIMD=ON \
  -DPLUGIN_DIR="%{_libdir}/%{name}" \
  -DGAMEINDEX_DIR="%{_datadir}/%{name}" \
  -DGLSL_SHADER_DIR="%{_datadir}/%{name}" \
  -DDOC_DIR="%{_datadir}/doc/%{name}"

%cmake_build

%install
%cmake_install

# add executable bit
chmod +x %{buildroot}%{_bindir}/PCSX2-linux.sh

# move translations to main language dir if there isn't a sublang or delete
# translations not supported by distro at all
for i in $(ls %{buildroot}%{_datadir}/locale | grep _); do
  new=$(echo $i | sed "s:_.*::g")
  if [ ! -d %{_datadir}/locale/$i ]; then
    if [ -d %{_datadir}/locale/$new ]; then
      mv %{buildroot}%{_datadir}/locale/$i %{buildroot}%{_datadir}/locale/$new
    else
      rm -rf %{buildroot}%{_datadir}/locale/$i
    fi
  fi
done

# shorten language code
mv %{buildroot}%{_datadir}/locale/cs_CZ %{buildroot}%{_datadir}/locale/cs
mv %{buildroot}%{_datadir}/locale/de_DE %{buildroot}%{_datadir}/locale/de
mv %{buildroot}%{_datadir}/locale/es_ES %{buildroot}%{_datadir}/locale/es
mv %{buildroot}%{_datadir}/locale/fi_FI %{buildroot}%{_datadir}/locale/fi
mv %{buildroot}%{_datadir}/locale/fr_FR %{buildroot}%{_datadir}/locale/fr
mv %{buildroot}%{_datadir}/locale/it_IT %{buildroot}%{_datadir}/locale/it
mv %{buildroot}%{_datadir}/locale/nb_NO %{buildroot}%{_datadir}/locale/nb
mv %{buildroot}%{_datadir}/locale/pl_PL %{buildroot}%{_datadir}/locale/pl
mv %{buildroot}%{_datadir}/locale/ru_RU %{buildroot}%{_datadir}/locale/ru
mv %{buildroot}%{_datadir}/locale/tr_TR %{buildroot}%{_datadir}/locale/tr

%fdupes -s %{buildroot}

%check
%ctest

%files
%doc README.md
%license COPYING.LGPLv2.1 COPYING.LGPLv3 COPYING.GPLv2 COPYING.GPLv3
%{_bindir}/PCSX2
%{_bindir}/PCSX2-linux.sh
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/applications/PCSX2.desktop
%{_datadir}/pixmaps/PCSX2.xpm
%{_mandir}/man1/PCSX2.1%{?ext_man}

%files -n %{name}-lang-ar
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*.mo

%files -n %{name}-lang-ca
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*.mo

%files -n %{name}-lang-cs
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*.mo

%files -n %{name}-lang-da
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*.mo

%files -n %{name}-lang-de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*.mo

%files -n %{name}-lang-es
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*.mo

%files -n %{name}-lang-fi
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*.mo

%files -n %{name}-lang-fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*.mo

%files -n %{name}-lang-hr
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*.mo

%files -n %{name}-lang-hu
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*.mo

%files -n %{name}-lang-id
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*.mo

%files -n %{name}-lang-it
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*.mo

%files -n %{name}-lang-ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*.mo

%files -n %{name}-lang-ko
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*.mo

%files -n %{name}-lang-lt
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*.mo

%files -n %{name}-lang-nb
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*.mo

%files -n %{name}-lang-nl
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*.mo

%files -n %{name}-lang-pl
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*.mo

%files -n %{name}-lang-pt_BR
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*.mo

%files -n %{name}-lang-ru
%lang(ru_RU) %{_datadir}/locale/ru/LC_MESSAGES/*.mo

%files -n %{name}-lang-sv
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*.mo

%files -n %{name}-lang-th
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*.mo

%files -n %{name}-lang-tr
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*.mo

%files -n %{name}-lang-zh_CN
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*.mo

%files -n %{name}-lang-zh_TW
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*.mo

%changelog
