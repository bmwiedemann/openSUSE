#
# spec file for package projectM
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


%define _libver 3
Name:           projectM
Version:        3.1.0
Release:        0
Summary:        A Music Visualizer
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Visualization
Url:            http://projectm.sourceforge.net
Source0:        https://github.com/projectM-visualizer/projectm/archive/v%{version}.tar.gz#/projectm-%{version}.tar.gz
# PATCH-FIX-OPENSUSE projectM-disable_native_plugins.patch
Patch4:         projectM-disable_native_plugins.patch
# PATCH-FIX-UPSTREAM projectM-increase_soversion.patch
Patch5:         projectM-increase_soversion.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(pthread-stubs)
Recommends:     %{name}-data = %{version}
Obsoletes:      %{name}-qt5 < %{version}
Provides:       %{name}-qt5 = %{version}

%description
projectM is a music visualizer.

%package     -n lib%{name}%{_libver}
Summary:        Run-time library for projectM
Group:          System/Libraries
Obsoletes:      lib%{name}-qt5-%{_libver} < %{version}
Provides:       lib%{name}-qt5-%{_libver} = %{version}

%description -n lib%{name}%{_libver}
projectM is a music visualizer.
This package contains its runtime library.

%package        data
Summary:        Data files for projectM
Group:          Productivity/Multimedia/Sound/Visualization
Requires:       %{name} = %{version}
Requires:       dejavu
Obsoletes:      %{name}-qt5-data < %{version}
Provides:       %{name}-qt5-data = %{version}

%description    data
projectM is a music visualizer.
This package contains its data: config, presets, shaders.

%package        devel
Summary:        Development Files for projectM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-data = %{version}
Requires:       lib%{name}%{_libver} = %{version}
Obsoletes:      %{name}-qt5-devel < %{version}
Provides:       %{name}-qt5-devel = %{version}

%description    devel
projectM is a music visualizer.
This package contains its development files.

%prep
%setup -q -n projectm-%{version}
chmod -x LICENSE.txt
%patch4 -p1
%patch5 -p1

%build
autoreconf -fiv
%configure --disable-static --disable-rpath --enable-qt
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name *.la -delete
%suse_update_desktop_file -r projectM-pulseaudio AudioVideo Audio Mixer
%fdupes -s %{buildroot}

%post -n lib%{name}%{_libver} -p /sbin/ldconfig
%postun -n lib%{name}%{_libver} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}-pulseaudio
%{_datadir}/applications/%{name}-pulseaudio.desktop
%{_datadir}/pixmaps/prjm16-transparent.svg
%{_mandir}/man1/%{name}-pulseaudio.1%{ext_man}

%files -n lib%{name}%{_libver}
%{_libdir}/lib%{name}.so.%{_libver}*

%files data
%{_datadir}/%{name}

%files devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
