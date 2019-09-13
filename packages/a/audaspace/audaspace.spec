#
# spec file for package audaspace
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


# See also http://en.opensuse.org/openSUSE:Shared_library_packaging_policy
# NOTE: sover follows version.
%define sover 1_3
%define soversion 1.3

Name:           audaspace
Version:        1.3.0
Release:        0
Summary:        A High-Level Audio Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/audaspace/audaspace/releases/tag/v%{version}
Source0:        audaspace-%{version}.tar.gz
#PATCH-FIX-UPSTREAM audaspace-gcc7.patch davejplater@gmail.com -- add missing "#include <functional>" picked up by gcc7
Patch0:         audaspace-gcc7.patch
#PATCH-FIX-UPSTREAM audaspace-plugin-build-options.patch davejplater@gmail.com -- add options for building plugins.
# See boo#1057965
Patch1:         audaspace-plugin-build-options.patch
# PATCH-FIX-UPSTREAM audaspace-support-ffmpeg4.patch -- Support ffmpeg v4
Patch2:         audaspace-support-ffmpeg4.patch
BuildRequires:  cmake > 3
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(sndfile)
#BuildRequires:  python-devel
#BuildRequires:  python3-Sphinx
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
#Requires:

%description
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library. This package contains demo binaries.

%package        plugins
Summary:        Plugins for %{name}
Group:          System/Libraries
Requires:       %{name} = %{version}

%description    plugins
Audaspace (pronounced "outer space") is a high-level audio library written
in C++ with language bindings for Python for example. It started out as the
audio engine of the 3D modelling application Blender and is now released as
a standalone library. This package contains audio plugins.

%package -n libaudaspace%{sover}
Summary:        A high-level audio library
Group:          System/Libraries

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
Requires:       %{name} = %{version}
Requires:       %{name}-plugins = %{version}
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
%patch0
%patch1
%patch2 -p1

%build
tmpflags="%{optflags}"
%ifarch ppc64le
# avoid contentions between SDL vector and gcc defines
# disable the include of altivec.h in /usr/include/SDL2/SDL_cpuinfo.h
# note that --disable-altivec not supported by gcc 4.8
tmpflags="$tmpflags -U__ALTIVEC__"
%endif
# NOTE: python3 numpy include flag (-isystem points to includes) reported upstream.
%cmake -DWITH_VERSIONED_PLUGINS:BOOL=FALSE \
      -DWITH_FFMPEG:BOOL=TRUE \
      -DCMAKE_EXE_LINKER_FLAGS:STRING="$CMAKE_EXE_LINKER_FLAGS -pie" \
      -DDEFAULT_PLUGIN_PATH:PATH=%{_libdir}/%{name}-%{soversion}/plugins \
      -DWITH_PYTHON_MODULE:BOOL=off \
      -DCMAKE_C_FLAGS:STRING="%{optflags} -isystem %{python3_sitearch}/numpy/core/include/" \
      -DCMAKE_CXX_FLAGS:STRING="${tmpflags} -isystem %{python3_sitearch}/numpy/core/include/" \
      -DDOCUMENTATION_INSTALL_PATH:PATH=%{_docdir}/%{name}
%make_jobs

%install
%cmake_install
find %{buildroot} -name '*.la' -delete
%fdupes -s %{buildroot}%{_docdir}/%{name}

%post -n libaudaspace%{sover} -p /sbin/ldconfig

%postun -n libaudaspace%{sover} -p /sbin/ldconfig

%post -n libaudaspace-c%{sover} -p /sbin/ldconfig

%postun -n libaudaspace-c%{sover} -p /sbin/ldconfig

%post -n libaudaspace-py%{sover} -p /sbin/ldconfig

%postun -n libaudaspace-py%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/*

%files plugins
%dir %{_libdir}/%{name}-%{soversion}
%dir %{_libdir}/%{name}-%{soversion}/plugins
%{_libdir}/%{name}-%{soversion}/plugins/*.so
#%%{_libdir}/%%{name}-%%{soversion}/plugins/*.so

%files -n libaudaspace%{sover}
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
