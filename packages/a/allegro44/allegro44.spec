#
# spec file for package allegro44
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           allegro44
Version:        4.4.2
Release:        0
Summary:        Cross-platform library for games and multimedia programming
# http://alleg.sourceforge.net/latestdocs/en/faq.html#The%20giftware%20licence
License:        SUSE-Permissive
Group:          System/Libraries
Url:            http://alleg.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/alleg/allegro/%{version}/allegro-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE allegro-4.4.2-shared_plugins.patch reddwarf@opensuse.org -- Compile plugins as shared libs
Patch0:         allegro-%{version}-shared_plugins.patch
# PATCH-FIX-OPENSUSE allegro-4.4.2-pkgconfig.patch reddwarf@opensuse.org -- Correct pkg-config files to reflect shared_plugins patch
Patch1:         allegro-4.4.2-pkgconfig.patch
# PATCH-FEATURE-OPENSUSE allegro-4.4.2-modules.patch reddwarf@opensuse.org -- Avoid allegro searching for modules that don't exist
Patch2:         allegro-4.4.2-modules.patch
# PATCH-FIX-OPENSUSE allegro-4.4.2-agl_no_dlopen.patch http://www.allegro.cc/forums/thread/600657 reddwarf@opensuse.org -- Link directly to libGL instead of dlopening, upstream doesn't likes it
Patch3:         allegro-4.4.2-agl_no_dlopen.patch
# PATCH-FIX-OPENSUSE allegro-4.4.2--underlinking.patch -- Add allegro to target_link_libraries
Patch4:         allegro-4.4.2-underlinking.patch
# PATCH-FIX-OPENSUSE allegro-4.4.2--no_c++.patch -- Removed CXX
Patch5:         allegro-4.4.2-no_c++.patch
# PATCH-FIX-OPENSUSE allegro-4.4.2--monotonic.patch -- Fix monotonic
Patch6:         allegro-4.4.2-monotonic.patch
# PATCH-FIX-OPENSUSE allegro4-4.4.2-src_x_xkeyboard.c.patch -- Fix include and 'XKeycodeToKeysym' is deprecated
Patch7:         allegro-4.4.2-src_x_xkeyboard.c.patch
# PATCH-FIX-OPENSUSE fix-glx.patch -- Fix issue with GLXext
Patch8:         fix-glx.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  texinfo
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  pkgconfig(xxf86vm)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

A wide range of extension packages and add-on modules are also available, which
can be found in the "Library Extensions" section of the Allegro website.

%package -n liballeg4_4
Summary:        A game programming library
Group:          System/Libraries

%description -n liballeg4_4
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%package -n liballeg44-devel
Summary:        A game programming library
Group:          Development/Languages/C and C++
Requires(pre):  %install_info_prereq
Requires:       %{name} = %{version}
Requires:       liballeg4_4 = %{version}
Provides:       allegro-devel = %{version}
Provides:       liballeg-devel = %{version}
Obsoletes:      allegro-devel < %{version}
Conflicts:      allegro-devel > %{version}
Conflicts:      liballeg-devel > %{version}

%description -n liballeg44-devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%package -n allegro44-tools
Summary:        Extra tools for the Allegro programming library
Group:          Development/Tools/Other

%description -n allegro44-tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package contains extra
tools which are useful for developing Allegro programs.

%package jack-plugin
Summary:        Allegro JACK (Jack Audio Connection Kit) plugin
Group:          System/Libraries
Requires:       %{name} = %{version}

%description jack-plugin
This package contains a plugin for Allegro which enables Allegro to playback
sound through JACK (Jack Audio Connection Kit).

%package dga2-plugin
Summary:        Allegro DGA2 (Direct Graphics Access) plugin
Group:          System/Libraries
Requires:       %{name} = %{version}

%description dga2-plugin
This package contains a DGA2 (Direct Graphics Access) driver for Allegro.

%package -n liballeggl4_4
Summary:        Allegro OpenGL bindings
Group:          System/Libraries

%description -n liballeggl4_4
This library allows to use OpenGL from Allegro.

%package -n liballeggl44-devel
Summary:        Development files for AllegroGL
Group:          Development/Languages/C and C++
Requires:       liballeggl4_4 = %{version}

%description -n liballeggl44-devel
This package is needed to build programs that use AllegroGL.

%package -n libjpgalleg4_4
Summary:        JPEG support library for Allegro
Group:          System/Libraries

%description -n libjpgalleg4_4
This library allows to load/save JPG images using standard Allegro image
handling functions.

%package -n libjpgalleg44-devel
Summary:        Development files for JPGAlleg
Group:          Development/Languages/C and C++
Requires:       libjpgalleg4_4 = %{version}
Provides:       libjpgalleg-devel = %{version}
Conflicts:      libjpgalleg-devel > %{version}

%description -n libjpgalleg44-devel
This package is needed to build programs that use JPGAlleg.

%package -n libloadpng4_4
Summary:        PNG support library for Allegro
Group:          System/Libraries

%description -n libloadpng4_4
This library allows to load/save PNG images using standard Allegro image
handling functions.

%package -n libloadpng44-devel
Summary:        Development files for Allegro's loadpng
Group:          Development/Languages/C and C++
Requires:       libloadpng4_4 = %{version}
Provides:       libloadpng-devel = %{version}
Conflicts:      libloadpng-devel > %{version}

%description -n libloadpng44-devel
This package is needed to build programs that use Allegro's loadpng.

%package -n liblogg4_4
Summary:        Ogg Vorbis support library for Allegro
Group:          System/Libraries

%description -n liblogg4_4
This library allows to use Ogg Vorbis sound files from Allegro.

%package -n liblogg44-devel
Summary:        Development files for Allegro's logg
Group:          Development/Languages/C and C++
Requires:       liblogg4_4 = %{version}
Provides:       liblogg-devel = %{version}
Conflicts:      liblogg-devel > %{version}

%description -n liblogg44-devel
This package is needed to build programs that use Allegro's logg.

%prep
%setup -q -n allegro-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8 -p1

# SED-FIX-OPENSUSE – Fix include, warning "xf86dga.h is obsolete and may be removed in the future."
sed -i 's|X11/extensions/xf86dga.h|X11/extensions/Xxf86dga.h|' src/x/xdga2.c

%build
mkdir build
cd build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
cmake -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB_SUFFIX=$(echo %{_lib} | cut -b4-) \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DDOCDIR=%{_docdir} \
      -DMANDIR=%{_mandir} \
      -DINFODIR=%{_infodir} \
      -DWANT_EXAMPLES=no \
      -DWANT_TESTS=no \
      -DWANT_OSS=no \
      ..
make %{?_smp_flags}

%install
cd build
%make_install
install -pm 0755 docs/makedoc %{buildroot}%{_bindir}/allegro-makedoc
rm -f %{buildroot}%{_includedir}/alleggl_config.h
# Since the CMakeLists.txt file is wrong install them manually
install -dm 0755 %{buildroot}%{_mandir}/man3
install -pm 0644 docs/man/*.3 %{buildroot}%{_mandir}/man3

%if 0%{?suse_version} 
    %fdupes -s %{buildroot}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n liballeg4_4 -p /sbin/ldconfig

%postun -n liballeg4_4 -p /sbin/ldconfig

%post -n liballeggl4_4 -p /sbin/ldconfig

%postun -n liballeggl4_4 -p /sbin/ldconfig

%post -n libjpgalleg4_4 -p /sbin/ldconfig

%postun -n libjpgalleg4_4 -p /sbin/ldconfig

%post -n libloadpng4_4 -p /sbin/ldconfig

%postun -n libloadpng4_4 -p /sbin/ldconfig

%post -n liblogg4_4 -p /sbin/ldconfig

%postun -n liblogg4_4 -p /sbin/ldconfig

%post -n liballeg44-devel
%install_info --info-dir=%{_infodir} %{_infodir}/allegro.info%{ext_info}

%preun -n liballeg44-devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/allegro.info%{ext_info}

%files
%defattr(0644,root,root,0755)
%{_libdir}/allegro
%exclude %{_libdir}/allegro/%{version}/alleg-jack.so
%exclude %{_libdir}/allegro/%{version}/alleg-dga2.so

%files -n liballeg4_4
%defattr(0644,root,root,0755)
%{_libdir}/liballeg.so.*

%files -n liballeg44-devel
%defattr(0644,root,root,0755)
%{_docdir}/allegro-%{version}
%attr(0755,-,-) %{_bindir}/allegro-config
%attr(0755,-,-) %{_bindir}/allegro-makedoc
%{_libdir}/liballeg.so
%{_includedir}/allegro.h
%{_includedir}/xalleg.h
%{_includedir}/allegro
%{_libdir}/pkgconfig/allegro.pc
%{_infodir}/allegro.info%{ext_info}
%{_mandir}/man3/*

%files -n allegro44-tools
%defattr(0755,root,root)
%{_bindir}/colormap
%{_bindir}/dat
%{_bindir}/dat2c
%{_bindir}/dat2s
%{_bindir}/exedat
%{_bindir}/grabber
%{_bindir}/pack
%{_bindir}/pat2dat
%{_bindir}/rgbmap
%{_bindir}/textconv

%files jack-plugin
%defattr(0644,root,root,0755)
%{_libdir}/allegro/%{version}/alleg-jack.so

%files dga2-plugin
%defattr(0644,root,root,0755)
%{_libdir}/allegro/%{version}/alleg-dga2.so

%files -n liballeggl4_4
%defattr(0644,root,root,0755)
%{_libdir}/liballeggl.so.*

%files -n liballeggl44-devel
%defattr(0644,root,root,0755)
%{_libdir}/liballeggl.so
%{_includedir}/alleggl.h
%{_includedir}/allegrogl
%{_libdir}/pkgconfig/allegrogl.pc

%files -n libjpgalleg4_4
%defattr(0644,root,root,0755)
%{_libdir}/libjpgalleg.so.*

%files -n libjpgalleg44-devel
%defattr(0644,root,root,0755)
%{_libdir}/libjpgalleg.so
%{_includedir}/jpgalleg.h
%{_libdir}/pkgconfig/jpgalleg.pc

%files -n libloadpng4_4
%defattr(0644,root,root,0755)
%{_libdir}/libloadpng.so.*

%files -n libloadpng44-devel
%defattr(0644,root,root,0755)
%{_libdir}/libloadpng.so
%{_includedir}/loadpng.h
%{_libdir}/pkgconfig/loadpng.pc

%files -n liblogg4_4
%defattr(0644,root,root,0755)
%{_libdir}/liblogg.so.*

%files -n liblogg44-devel
%defattr(0644,root,root,0755)
%{_libdir}/liblogg.so
%{_includedir}/logg.h
%{_libdir}/pkgconfig/logg.pc

%changelog
