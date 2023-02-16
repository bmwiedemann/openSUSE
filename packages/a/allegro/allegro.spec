#
# spec file for package allegro
#
# Copyright (c) 2023 SUSE LLC
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


%define pack_descr Allegro is a cross-platform library mainly aimed at \
video game and multimedia programming. It handles common, low-level \
tasks such as creating windows, accepting user input, loading data, \
drawing images, playing sounds, etc. and generally abstracting away \
the underlying platform. However, Allegro is not a game engine: \
developers are free to design and structure the program as desired.
%define allegro_so_nr 5_2
%define dot_allegro_so_nr %(echo %{allegro_so_nr} | sed s/_/./)
Name:           allegro
Version:        5.2.8.0
Release:        0
Summary:        A game programming library
License:        BSD-3-Clause AND Zlib
Group:          Development/Libraries/C and C++
URL:            https://liballeg.org
Source0:        https://github.com/liballeg/allegro5/releases/download/%{version}/allegro-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libphysfs-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dumb) >= 2.0
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%description
%{pack_descr}

%package -n liballegro%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro%{allegro_so_nr}
%{pack_descr}

%package -n liballegro%{allegro_so_nr}-devel
Summary:        Development files for liballegro
Group:          Development/Libraries/C and C++
Requires:       liballegro%{allegro_so_nr} = %{version}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)

%description -n liballegro%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro.

%package -n liballegro_acodec%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_acodec%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_acodec%{allegro_so_nr}-devel
Summary:        Development files for liballegro_acodec
Group:          Development/Libraries/C and C++
Requires:       liballegro_acodec%{allegro_so_nr} = %{version}

%description -n liballegro_acodec%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_acodec.

%package -n liballegro_audio%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_audio%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_audio%{allegro_so_nr}-devel
Summary:        Development files for liballegro_audio
Group:          Development/Libraries/C and C++
Requires:       liballegro_audio%{allegro_so_nr} = %{version}

%description -n liballegro_audio%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_audio.

%package -n liballegro_color%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_color%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_color%{allegro_so_nr}-devel
Summary:        Development files for liballegro_color
Group:          Development/Libraries/C and C++
Requires:       liballegro_color%{allegro_so_nr} = %{version}

%description -n liballegro_color%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_color.

%package -n liballegro_dialog%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_dialog%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_dialog%{allegro_so_nr}-devel
Summary:        Development files for liballegro_dialog
Group:          Development/Libraries/C and C++
Requires:       liballegro_dialog%{allegro_so_nr} = %{version}

%description -n liballegro_dialog%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_dialog.

%package -n liballegro_font%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_font%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_font%{allegro_so_nr}-devel
Summary:        Development files for liballegro_font
Group:          Development/Libraries/C and C++
Requires:       liballegro_font%{allegro_so_nr} = %{version}

%description -n liballegro_font%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_font.

%package -n liballegro_image%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_image%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_image%{allegro_so_nr}-devel
Summary:        Development files for liballegro_image
Group:          Development/Libraries/C and C++
Requires:       liballegro_image%{allegro_so_nr} = %{version}

%description -n liballegro_image%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_image.

%package -n liballegro_main%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_main%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_main%{allegro_so_nr}-devel
Summary:        Development files for liballegro_main
Group:          Development/Libraries/C and C++
Requires:       liballegro_main%{allegro_so_nr} = %{version}

%description -n liballegro_main%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_main.

%package -n liballegro_memfile%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_memfile%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_memfile%{allegro_so_nr}-devel
Summary:        Development files for liballegro_memfile
Group:          Development/Libraries/C and C++
Requires:       liballegro_memfile%{allegro_so_nr} = %{version}

%description -n liballegro_memfile%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_memfile.

%package -n liballegro_physfs%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_physfs%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_physfs%{allegro_so_nr}-devel
Summary:        Development files for liballegro_physfs
Group:          Development/Libraries/C and C++
Requires:       liballegro_physfs%{allegro_so_nr} = %{version}

%description -n liballegro_physfs%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_physfs.

%package -n liballegro_primitives%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_primitives%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_primitives%{allegro_so_nr}-devel
Summary:        Development files for liballegro_primitives
Group:          Development/Libraries/C and C++
Requires:       liballegro_primitives%{allegro_so_nr} = %{version}

%description -n liballegro_primitives%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_primitives.

%package -n liballegro_ttf%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_ttf%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_ttf%{allegro_so_nr}-devel
Summary:        Development files for liballegro_ttf
Group:          Development/Libraries/C and C++
Requires:       liballegro_ttf%{allegro_so_nr} = %{version}

%description -n liballegro_ttf%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_ttf.

%package -n liballegro_video%{allegro_so_nr}
Summary:        A game programming library
Group:          System/Libraries

%description -n liballegro_video%{allegro_so_nr}
%{pack_descr}

%package -n liballegro_video%{allegro_so_nr}-devel
Summary:        Development files for liballegro_video
Group:          Development/Libraries/C and C++
Requires:       liballegro_video%{allegro_so_nr} = %{version}

%description -n liballegro_video%{allegro_so_nr}-devel
Development files needed to build applications which use liballegro_video.

%package -n liballegro-doc
Summary:        Allegro Documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description -n liballegro-doc
Allegro HTML documentation and man pages.

%prep
%setup -q

%build
# Tests require a graphics card
%cmake \
      -DCMAKE_C_FLAGS="%{optflags} -fPIC -D_FILE_OFFSET_BITS=64" \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DWANT_EXAMPLES=NO \
      -DWANT_TESTS=NO \
      -DWANT_DEMO=NO ..
%make_build

%install
%cmake_install
install -D -m 644 allegro5.cfg %{buildroot}%{_sysconfdir}/allegro5rc
install -d -D %{buildroot}%{_mandir}/man3
cp docs/man/*.3 %{buildroot}%{_mandir}/man3
%fdupes -s %{buildroot}%{_mandir}/man3
install -d -D %{buildroot}%{_datadir}/doc/%{name}
cp -r docs/html/refman/* %{buildroot}%{_datadir}/doc/%{name}

%post -n liballegro_video%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_ttf%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_primitives%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_physfs%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_memfile%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_main%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_image%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_font%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_dialog%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_color%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_audio%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro_acodec%{allegro_so_nr} -p /sbin/ldconfig
%post -n liballegro%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_acodec%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_audio%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_color%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_dialog%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_font%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_image%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_main%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_memfile%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_physfs%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_primitives%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_ttf%{allegro_so_nr} -p /sbin/ldconfig
%postun -n liballegro_video%{allegro_so_nr} -p /sbin/ldconfig

%files -n liballegro%{allegro_so_nr}
%license LICENSE.txt
%doc CHANGES-5.?.txt CONTRIBUTORS.txt README.txt
%{_libdir}/liballegro.so.%{dot_allegro_so_nr}*
%config(noreplace) %{_sysconfdir}/allegro5rc

%files -n liballegro%{allegro_so_nr}-devel
%{_libdir}/liballegro.so
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_color.h
%exclude %{_includedir}/allegro5/allegro_native_dialog.h
%exclude %{_includedir}/allegro5/allegro_font.h
%exclude %{_includedir}/allegro5/allegro_image.h
%exclude %{_includedir}/allegro5/allegro_memfile.h
%exclude %{_includedir}/allegro5/allegro_physfs.h
%exclude %{_includedir}/allegro5/allegro_primitives.h
%exclude %{_includedir}/allegro5/allegro_ttf.h
%exclude %{_includedir}/allegro5/allegro_video.h
%{_libdir}/pkgconfig/allegro-5.pc

%files -n liballegro-doc
%{_datadir}/doc/%{name}/
%{_mandir}/man3/*

%files -n liballegro_primitives%{allegro_so_nr}
%{_libdir}/liballegro_primitives.so.%{dot_allegro_so_nr}*

%files -n liballegro_primitives%{allegro_so_nr}-devel
%{_libdir}/liballegro_primitives.so
%{_includedir}/allegro5/allegro_primitives.h
%{_libdir}/pkgconfig/allegro_primitives-5.pc

%files -n liballegro_acodec%{allegro_so_nr}
%{_libdir}/liballegro_acodec.so.%{dot_allegro_so_nr}*

%files -n liballegro_acodec%{allegro_so_nr}-devel
%{_libdir}/liballegro_acodec.so
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/pkgconfig/allegro_acodec-5.pc

%files -n liballegro_audio%{allegro_so_nr}
%{_libdir}/liballegro_audio.so.%{dot_allegro_so_nr}*

%files -n liballegro_audio%{allegro_so_nr}-devel
%{_libdir}/liballegro_audio.so
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/pkgconfig/allegro_audio-5.pc

%files -n liballegro_color%{allegro_so_nr}
%{_libdir}/liballegro_color.so.%{dot_allegro_so_nr}*

%files -n liballegro_color%{allegro_so_nr}-devel
%{_libdir}/liballegro_color.so
%{_includedir}/allegro5/allegro_color.h
%{_libdir}/pkgconfig/allegro_color-5.pc

%files -n liballegro_dialog%{allegro_so_nr}
%{_libdir}/liballegro_dialog.so.%{dot_allegro_so_nr}*

%files -n liballegro_dialog%{allegro_so_nr}-devel
%{_libdir}/liballegro_dialog.so
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/pkgconfig/allegro_dialog-5.pc

%files -n liballegro_font%{allegro_so_nr}
%{_libdir}/liballegro_font.so.%{dot_allegro_so_nr}*

%files -n liballegro_font%{allegro_so_nr}-devel
%{_libdir}/liballegro_font.so
%{_includedir}/allegro5/allegro_font.h
%{_libdir}/pkgconfig/allegro_font-5.pc

%files -n liballegro_image%{allegro_so_nr}
%{_libdir}/liballegro_image.so.%{dot_allegro_so_nr}*

%files -n liballegro_image%{allegro_so_nr}-devel
%{_libdir}/liballegro_image.so
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/pkgconfig/allegro_image-5.pc

%files -n liballegro_main%{allegro_so_nr}
%{_libdir}/liballegro_main.so.%{dot_allegro_so_nr}*

%files -n liballegro_main%{allegro_so_nr}-devel
%{_libdir}/liballegro_main.so
%{_libdir}/pkgconfig/allegro_main-5.pc

%files -n liballegro_memfile%{allegro_so_nr}
%{_libdir}/liballegro_memfile.so.%{dot_allegro_so_nr}*

%files -n liballegro_memfile%{allegro_so_nr}-devel
%{_libdir}/liballegro_memfile.so
%{_includedir}/allegro5/allegro_memfile.h
%{_libdir}/pkgconfig/allegro_memfile-5.pc

%files -n liballegro_physfs%{allegro_so_nr}
%{_libdir}/liballegro_physfs.so.%{dot_allegro_so_nr}*

%files -n liballegro_physfs%{allegro_so_nr}-devel
%{_libdir}/liballegro_physfs.so
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/pkgconfig/allegro_physfs-5.pc

%files -n liballegro_ttf%{allegro_so_nr}
%{_libdir}/liballegro_ttf.so.%{dot_allegro_so_nr}*

%files -n liballegro_ttf%{allegro_so_nr}-devel
%{_libdir}/liballegro_ttf.so
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/pkgconfig/allegro_ttf-5.pc

%files -n liballegro_video%{allegro_so_nr}
%{_libdir}/liballegro_video.so.%{dot_allegro_so_nr}*

%files -n liballegro_video%{allegro_so_nr}-devel
%{_libdir}/liballegro_video.so
%{_includedir}/allegro5/allegro_video.h
%{_libdir}/pkgconfig/allegro_video-5.pc

%changelog
