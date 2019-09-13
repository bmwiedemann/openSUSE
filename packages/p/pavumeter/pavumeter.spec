#
# spec file for package pavumeter
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pavumeter
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libpulse-devel
BuildRequires:  update-desktop-files
%if %suse_version > 1010
BuildRequires:  gtkmm2-devel
%else
BuildRequires:  gtkmm24-devel
%endif
Summary:        PulseAudio Volume Meter
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Visualization
Version:        0.9.3
Release:        0
Url:            http://0pointer.de/lennart/projects/pavumeter/
Source:         %{name}-%{version}.tar.bz2
Source1:        pavumeter.png
Patch:          pavumeter-desktop-fix.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PulseAudio Volume Meter (pavumeter) is a simple GTK volume meter for
the PulseAudio sound server.

%prep
%setup -q
%patch

%build
autoreconf -fi
%configure --disable-lynx
make

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%suse_update_desktop_file %{name} AudioVideo Mixer
%suse_update_desktop_file %{name}-record AudioVideo Mixer

%clean
test "$RPM_BUILD_ROOT" != "/" -a -d "$RPM_BUILD_ROOT" && rm -rf $RPM_BUILD_ROOT

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc doc/README doc/README.html
%doc LICENSE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
