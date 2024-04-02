#
# spec file for package libextractor
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2013 Marguerite Su <marguerite@opensuse.org>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soname	        3
%define common_soname   1
Name:           libextractor
Version:        1.13
Release:        0
Summary:        Library to Extract Metadata from Files
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.gnu.org/software/libextractor/
Source:         https://ftp.gnu.org/gnu/libextractor/libextractor-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/libextractor/libextractor-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=libextractor&download=1#/%{name}.keyring
Source4:        %{name}-rpmlintrc
Recommends:     %{name}-plugins
%lang_package
# SECTION general dependencies
BuildRequires:  c++_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libapparmor)
BuildRequires:  pkgconfig(zlib)
# /SECTION
# SECTION file format dependencies
# Unfortunately OBS cannot parse this from macros, so this is repeated in
# subpackages
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmpeg2)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(vorbis)
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(tidy)
%else
BuildRequires:  file-devel
BuildRequires:  libtidy-devel
%endif
# /SECTION

%description
GNU Libextractor is a library for extracting meta data from various files types.

The '%{name}' package contains the 'extract' command. Install '%{name}-plugins'
to install all available file format plugins, or select individual packages
from '%{name}-plugins*' as needed.

# Macro that generates a plugin package definition
%define pluginpkg(B:) \
%package plugins-%{1} \
Summary:         The '%{1}' libextractor plugin \
Supplements:     %{name}-plugins = %{version} \
BuildRequires:   %{-B*} \
\
%description plugins-%{1} \
This package ships the '%{1}' plugin for libextractor. \
\
%files plugins-%{1} \
%%license COPYING \
%{_libdir}/%{name}/%{name}_%{1}.so \
%{nil}
#
# These packages are split out for the following reasons:
# 0. Give the user control over which file formats to parse. Media format
#    libraries are notorious for security issues, especially when parsing
#    content from potentially untrusted sources.
# 1. Give the user the option for a reduced dependency installation.
%pluginpkg archive      -B pkgconfig(libarchive)
%pluginpkg exiv2        -B pkgconfig(exiv2)
%pluginpkg flac         -B pkgconfig(flac)
%pluginpkg gif          -B giflib-devel
%pluginpkg gstreamer    -B pkgconfig(gstreamer-plugins-base-1.0)
%pluginpkg jpeg         -B pkgconfig(libjpeg)
%pluginpkg mpeg         -B pkgconfig(libmpeg2)
%pluginpkg ogg          -B pkgconfig(vorbis)
%pluginpkg ole2         -B pkgconfig(libgsf-1)
%pluginpkg rpm          -B pkgconfig(rpm)
%pluginpkg thumbnailgtk -B pkgconfig(gdk-pixbuf-2.0)
%pluginpkg tiff         -B pkgconfig(libtiff-4)
%if 0%{?suse_version} > 1600
%pluginpkg mime         -B pkgconfig(libmagic)
%pluginpkg html         -B pkgconfig(tidy)
%else
%pluginpkg mime         -B file-devel
%pluginpkg html         -B libtidy-devel
%endif

%package -n %{name}%{soname}
Summary:        Shared libraries for libextractor
Recommends:     %{name}-plugins

%description -n %{name}%{soname}
GNU Libextractor is a library for extracting meta data from various files types.

This package contains the shared libraries for %{name}.

%package -n     %{name}_common%{common_soname}
Summary:        Shared libraries (common) for libextractor

%description -n %{name}_common%{common_soname}
GNU Libextractor is a library for extracting meta data from various files types.

This package contains the shared libraries for %{name}.

%package        plugins
Summary:        Installs all plugins for %{name}
Requires:       %{name}-plugins-archive = %{version}
Requires:       %{name}-plugins-base = %{version}
Requires:       %{name}-plugins-exiv2 = %{version}
Requires:       %{name}-plugins-flac = %{version}
Requires:       %{name}-plugins-gif = %{version}
Requires:       %{name}-plugins-gstreamer = %{version}
Requires:       %{name}-plugins-html = %{version}
Requires:       %{name}-plugins-jpeg = %{version}
Requires:       %{name}-plugins-mime = %{version}
Requires:       %{name}-plugins-mpeg = %{version}
Requires:       %{name}-plugins-ogg = %{version}
Requires:       %{name}-plugins-ole2 = %{version}
Requires:       %{name}-plugins-rpm = %{version}
Requires:       %{name}-plugins-thumbnailgtk = %{version}
Requires:       %{name}-plugins-tiff = %{version}
BuildArch:      noarch

%description    plugins
GNU Libextractor is a library for extracting meta data from various files types.

This package triggers the installation of all available file format plugins.

%package        plugins-base
Summary:        Base pugins for %{name}

%description    plugins-base
GNU Libextractor is a library for extracting meta data from various files types.

This package contains file format plugins for %{name} that do not add extra
dependencies.

%package devel
Summary:        Include Files and Libraries mandatory for Development with libextractor
Group:          Development/Languages/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       %{name}_common%{common_soname} = %{version}

%description devel
GNU Libextractor is a library for extracting meta data from various files types.

This package contains all necessary include files and libraries needed to
develop applications that require these.

%prep
%autosetup -p1

%build
%configure \
    --disable-static

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# generate a list of plugins that do not introduce additional dependencies
for i in %{buildroot}%{_libdir}/%{name}/*.so; do
    readelf -a "$i" | \
    sed '/(NEEDED)/s!.*\[\(.*\)\].*!\1!p;d' | {
        target=base
        fname=${i##%{buildroot}}
        while read lib; do
            lib=${lib%%.so*}
            case $lib in
                (libgcc_s|ld-linux*)                ;;
                (libz|libdl)                        ;;
                (libextractor|libextractor_common)  ;;
                (libc|libm|libpthread)              ;;
                (libstdc++)                         ;;
                (*)
                    target=other
                    echo "$fname -> $lib"
                    ;;
            esac
        done
        case $target in
            (base)    echo "$fname" >> filelists.base;;
        esac
    }
done
%find_lang %{name}

%check
# failing: text_exiv2
# flakey: test_ipc
# export LD_LIBRARY_PATH=%%{buildroot}%%{_libdir}
# export LIBEXTRACTOR_PREFIX=%%{buildroot}%%{_libdir}/libextractor
# %%make_build check

%ldconfig_scriptlets -n %{name}%{soname}
%ldconfig_scriptlets -n %{name}_common%{common_soname}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/extract
%{_mandir}/man1/extract.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%files plugins
%license COPYING

%files plugins-base -f filelists.base
%license COPYING

%files -n %{name}%{soname}
%license COPYING
%{_libdir}/libextractor.so.%{soname}
%{_libdir}/libextractor.so.%{soname}.*
%dir %{_libdir}/%{name}

%files -n %{name}_common%{common_soname}
%license COPYING
%{_libdir}/%{name}_common.so.%{common_soname}
%{_libdir}/%{name}_common.so.%{common_soname}.*

%files devel
%license COPYING
%{_includedir}/*.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}_common.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man?/libextractor.?%{ext_man}
%{_infodir}/%{name}.info%{?ext_info}

%changelog
