#
# spec file for package librubberband
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define library_name librubberband2
Name:           librubberband
Version:        1.8.1
Release:        0
Summary:        Audio time-stretching and pitch-shifting library
License:        GPL-2.0+
Group:          System/Libraries
Url:            http://www.breakfastquay.com/rubberband/
Source:         http://code.breakfastquay.com/attachments/download/34/rubberband-%{version}.tar.bz2
Source1:        baselibs.conf
Patch1:         rubberband-mk.patch
BuildRequires:  dos2unix
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  ladspa-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkg-config
BuildRequires:  vamp-plugin-sdk-devel
Requires:       ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n     %{library_name}
Summary:        Audio time-stretching and pitch-shifting library
Group:          System/Libraries
Url:            http://www.breakfastquay.com/rubberband/

%description -n %{library_name}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n     rubberband-cli
Summary:        Command line interface for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{library_name} = %{version}

%description -n rubberband-cli
Package rubberband-cli contains a command-line utility that can be used to exploit
Rubber Band's capabilities.

%package -n     rubberband-ladspa
Summary:        LADSPA plugin for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{library_name} = %{version}

%description -n rubberband-ladspa
Package rubberband-ladspa is LADSPA plugin that can change the pitch of a sound in real-time.

%package -n     rubberband-vamp
Summary:        Vamp plugins for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{library_name} = %{version}

%description -n rubberband-vamp
This package contains the following Vamp plugins:
 * increments (Output Increments): Output time increment for each
   input step
 * aggregate_increments (Accumulated Output Increments): Accumulated
   output time increments
 * divergence (Divergence from Linear): Difference between actual
   output time and the output time for a theoretical linear stretch
 * phaseresetdf (Phase Reset Detection Function): Curve whose peaks
   are used to identify transients for phase reset points
 * smoothedphaseresetdf (Smoothed Phase Reset Detection Function):
   Phase reset curve smoothed for peak picking
 * phaseresetpoints (Phase Reset Points): Points estimated as
   transients at which phase reset occurs
 * timesyncpoints (Time Sync Points): Salient points which stretcher
   aims to place with strictly correct timing

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n rubberband-%{version}
%patch1
# Fix README EOL encoding
dos2unix -o README.txt
mv README.txt README

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/*.a

%if 0%{?suse_version} > 1140
mkdir -p %{buildroot}%{_mandir}/man1
pushd %{buildroot}%{_mandir}/man1
cp -v %{buildroot}%{_bindir}/rubberband ./
help2man --no-discard-stderr \
	-N -o rubberband.1 ./rubberband
rm rubberband
popd
%endif

%post -n %{library_name} -p /sbin/ldconfig

%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc

%files -n rubberband-cli
%defattr(-,root,root,-)
%{_bindir}/rubberband
%if 0%{?suse_version} > 1140
%{_mandir}/man1/rubberband.1.gz
%endif

%files -n rubberband-ladspa
%defattr(-,root,root,-)
%dir %{_libdir}/ladspa
%dir %{_datadir}/ladspa
%dir %{_datadir}/ladspa/rdf
%{_libdir}/ladspa/ladspa-rubberband.*
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf

%files -n rubberband-vamp
%defattr(-,root,root,-)
%dir %{_libdir}/vamp
%{_libdir}/vamp/vamp-rubberband.*

%changelog
