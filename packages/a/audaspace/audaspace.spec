#
# spec file for package audaspace
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


# See also http://en.opensuse.org/openSUSE:Shared_library_packaging_policy
# NOTE: sover follows version.
%define sover 1_4
%define soversion 1.4

Name:           audaspace
Version:        1.4.0
Release:        0
Summary:        A High-Level Audio Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://audaspace.github.io/
Source0:        https://github.com/audaspace/audaspace/archive/refs/tags/v%{version}.tar.gz#/audaspace-%{version}.tar.gz
BuildRequires:  cmake > 3
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)

%description
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library. This package contains demo binaries.

%package        plugin-ffmpeg
Summary:        FFmpeg plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-fileplugin
Supplements:    libaudaspace%{sover}

%description    plugin-ffmpeg
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the FFmpeg plugin

%package        plugin-jack
Summary:        JACK plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-deviceplugin

%description    plugin-jack
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the JACK plugin

%package        plugin-openal
Summary:        OpenAL plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-deviceplugin

%description    plugin-openal
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the OpenAL plugin

%package        plugin-pulse
Summary:        Pulseaudio plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-deviceplugin
Supplements:    (libaudaspace%{sover} and (pulseaudio or pulseaudio-pipewire))

%description    plugin-pulse
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the Pulseaudio plugin

%package        plugin-sdl2
Summary:        SDL2 plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-deviceplugin

%description    plugin-sdl2
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the SDL2 plugin

%package        plugin-sndfile
Summary:        Sndfile plugin for %{name}
Group:          System/Libraries
Provides:       audaspace-fileplugin

%description    plugin-sndfile
Audaspace (pronounced "outer space") is a high-level audio library.
This package contains the Sndfile plugin

%package -n libaudaspace%{sover}
Summary:        A high-level audio library
Group:          System/Libraries
Recommends:     audaspace-deviceplugin
Recommends:     audaspace-fileplugin

%description -n libaudaspace%{sover}
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library.

%package -n libaudaspace-c%{sover}
Summary:        C bindings for %{name}
Group:          System/Libraries

%description -n libaudaspace-c%{sover}
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library.

%package -n libaudaspace-py%{sover}
Summary:        Python Bindings for %{name}
Group:          System/Libraries

%description -n libaudaspace-py%{sover}
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libaudaspace%{sover} = %{version}
Requires:       libaudaspace-c%{sover} = %{version}
Requires:       libaudaspace-py%{sover} = %{version}
Recommends:     %{name}-doc = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Recommends:     %{name}-devel = %{version}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for
developing applications that use %{name}.

%prep
%setup -n audaspace-%{version} -q

%build
%cmake \
    -DWITH_VERSIONED_PLUGINS:BOOL=FALSE \
    -DWITH_FFMPEG:BOOL=TRUE \
    -DDEFAULT_PLUGIN_PATH:PATH=%{_libdir}/%{name}-%{soversion} \
    -DWITH_PYTHON_MODULE:BOOL=off \
    -DDOCUMENTATION_INSTALL_PATH:PATH=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_docdir}/%{name}

%post -n libaudaspace%{sover} -p /sbin/ldconfig

%postun -n libaudaspace%{sover} -p /sbin/ldconfig

%post -n libaudaspace-c%{sover} -p /sbin/ldconfig

%postun -n libaudaspace-c%{sover} -p /sbin/ldconfig

%post -n libaudaspace-py%{sover} -p /sbin/ldconfig

%postun -n libaudaspace-py%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/*

%files plugin-ffmpeg
%{_libdir}/%{name}-%{soversion}/libaudffmpeg.so

%files plugin-jack
%{_libdir}/%{name}-%{soversion}/libaudjack.so

%files plugin-openal
%{_libdir}/%{name}-%{soversion}/libaudopenal.so

%files plugin-pulse
%{_libdir}/%{name}-%{soversion}/libaudpulseaudio.so

%files plugin-sdl2
%{_libdir}/%{name}-%{soversion}/libaudsdl.so

%files plugin-sndfile
%{_libdir}/%{name}-%{soversion}/libaudlibsndfile.so

%files -n libaudaspace%{sover}
%dir %{_libdir}/%{name}-%{soversion}
%{_libdir}/libaudaspace.so.%{soversion}

%files -n libaudaspace-c%{sover}
%{_libdir}/libaudaspace-c.so.%{soversion}

%files -n libaudaspace-py%{sover}
%{_libdir}/libaudaspace-py.so.%{soversion}

%files doc
%doc AUTHORS CHANGES README.md
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so

%changelog
