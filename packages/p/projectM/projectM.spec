#
# spec file for package projectM
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


%define _libver 3
Name:           projectM
Version:        3.1.3
Release:        0
Summary:        A Music Visualizer
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Visualization
URL:            http://projectm.sourceforge.net
Source0:        https://github.com/projectM-visualizer/projectm/archive/v%{version}.tar.gz#/projectm-%{version}.tar.gz
# PATCH-FIX-OPENSUSE projectM-disable_native_plugins.patch
Patch0:         projectM-disable_native_plugins.patch
# PATCH-FIX-UPSTREAM 0001-Reduce-dependencies.patch
Patch1:         0001-Reduce-dependencies.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glm-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
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
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv

perl -pi -e 's#2>/dev/null##g' configure
%configure --disable-static --disable-rpath --enable-qt
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -r projectM-pulseaudio AudioVideo Audio Mixer
%fdupes -s %{buildroot}

%post -n lib%{name}%{_libver} -p /sbin/ldconfig
%postun -n lib%{name}%{_libver} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}-pulseaudio
%{_datadir}/applications/%{name}-pulseaudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/projectM.svg
%{_mandir}/man1/%{name}-pulseaudio.1%{?ext_man}

%files -n lib%{name}%{_libver}
%{_libdir}/lib%{name}.so.%{_libver}*

%files data
%{_datadir}/%{name}

%files devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
