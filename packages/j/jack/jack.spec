#
# spec file for package jack
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


%define buildoc 1
%define debug_package_requires %{name} = %{version}-%{release}
# Switch the --dbus on and off, on = 1
%define wdbus 1
%define sonum 0
BuildRequires:  pkgconfig(libffado) >= 2.0.1.2040
Name:           jack
Version:        1.9.12
Release:        0
#to_be_filled_by_service
Summary:        Jack-Audio Connection Kit
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Sound Daemons
Url:            http://jackaudio.org/
Source0:        https://github.com/jackaudio/jack2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         jack-waf2.patch
Patch1:         fix-mmap-return-value-check.patch
Patch2:         0001-Make-jack_control-python2-3-compatible.patch
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(alsa)
#BuildRequires:  readline-devel
# NOTE: somebody changed libiec61883 to libiec61883-0 after Leap was released and didn't note it in the changes file.
%if 0%{suse_version} <= 1320
#!BuildIgnore:  libiec61883
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
Provides:       jack-audio-connection-kit
Provides:       jack2 = %{version}
Obsoletes:      jack2 < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
JACK is system for handling real-time, low latency audio
(and MIDI). It runs on GNU/Linux, Solaris, FreeBSD, OS X and
Windows (and can be ported to other POSIX-conformant
platforms). It can connect a number of different
applications to an audio device, as well as allowing them to
share audio between themselves. Its clients can run in their
own processes (ie. as normal applications), or can they can
run within the JACK server (ie. as a "plugin"). JACK also
has support for distributing audio processing across a
network, both fast & reliable LANs as well as slower, less
reliable WANs.

%package -n libjack%{sonum}
Summary:        Jack Audio Connection Kit Library
Group:          System/Libraries
Provides:       libjack = %{version}
Obsoletes:      libjack < %{version}
Provides:       libjack2

%description -n libjack%{sonum}
This package contains the library to access JACK
(Jack Audio ConnectionKit).

%package -n libjacknet%{sonum}
Summary:        Jack Audio Connection Kit Library
# libjacknet was packaged with libjack prior to 1.9.12
# libjacknet is not a compatible replacerment for libjack0
Group:          System/Libraries
Obsoletes:      libjack%{sonum} < 1.9.12

%description -n libjacknet%{sonum}
This package contains the library to access JACK
(Jack Audio ConnectionKit) network functions.

%package -n libjackserver%{sonum}
Summary:        Jack Audio Connection Kit Library
# libjackserver was packaged with libjack prior to 1.9.12
# libjacknet is not a compatible replacerment for libjack0
Group:          System/Libraries
Obsoletes:      libjack%{sonum} < 1.9.12

%description -n libjackserver%{sonum}
This package contains the library to access JACK
(Jack Audio ConnectionKit) server functions.

%package -n libjack-devel
Summary:        Development package for jack
Group:          Development/Libraries/C and C++
Requires:       libjack%{sonum} = %{version}
Requires:       libjacknet%{sonum} = %{version}
Requires:       libjackserver%{sonum} = %{version}
Requires:       pkgconfig
Provides:       jack-audio-connection-kit-devel
Provides:       jack-devel
Provides:       libjack2-devel = %{version}
Obsoletes:      libjack2-devel < %{version}

%description -n libjack-devel
This package contains the files needed to compile programs that
communicate with jack clients/servers.

%prep
%setup -q -n %{name}2-%{version}
%autopatch -p1

#Change python script headers to python3
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -ggdb -fPIC"
export CXXFLAGS="$CFLAGS"

./waf -v %{_smp_mflags} \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --classic \
%if 0%{?wdbus} == 1
  --dbus \
%endif
  --firewire \
%if %{buildoc} == 1
  --doxygen \
%endif
  --alsa \
  --ports=1024 \
  --enable-pkg-config-dbus-service-dir \
  --mandir=%{_mandir}/man1 \
  configure

# build is too heavy, so don't spawn more than one process or the build hangs
./waf -v %{_smp_mflags} build

%install
export SOURCE_DATE_EPOCH=1411299887
%if %{buildoc} == 1
# This is a workaround because the doc build looks for build/default/html but there isn't one.
mkdir -p build/default
pushd build/default/
ln -s ../../html html
popd
%endif

./waf -j1 install --destdir=%{buildroot}
mkdir -p %{buildroot}%{_docdir}/%{name}
%if %{buildoc} == 1
mv %{buildroot}%{_datadir}/jack-audio-connection-kit %{buildroot}%{_docdir}
%endif

dos2unix -k ChangeLog
dos2unix -k README
dos2unix -k TODO
cp ChangeLog README* TODO %{buildroot}%{_docdir}/%{name}/

# Fix wrong-file-end-of-line-encoding
dos2unix -k %{buildroot}%{_docdir}/%{name}/ChangeLog
dos2unix -k %{buildroot}%{_docdir}/%{name}/README
dos2unix -k %{buildroot}%{_docdir}/%{name}/TODO
%fdupes -s %{_docdir}/jack-audio-connection-kit/

%post -n libjack%{sonum} -p /sbin/ldconfig
%postun -n libjack%{sonum} -p /sbin/ldconfig

%post -n libjacknet%{sonum} -p /sbin/ldconfig
%postun -n libjacknet%{sonum} -p /sbin/ldconfig

%post -n libjackserver%{sonum} -p /sbin/ldconfig
%postun -n libjackserver%{sonum} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/ChangeLog
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/TODO
%license windows/Setup/src/COPYING
%{_mandir}/man1/*
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/inprocess.so
%{_libdir}/%{name}/%{name}_alsa.so
%{_libdir}/%{name}/%{name}_dummy.so
%{_libdir}/%{name}/%{name}_net.so
%{_libdir}/%{name}/netmanager.so*
%{_libdir}/%{name}/profiler.so*
%{_libdir}/%{name}/netadapter.so*
%{_libdir}/%{name}/audioadapter.so*
%{_libdir}/%{name}/%{name}_loopback.so*
%{_libdir}/%{name}/%{name}_netone.so*
%{_libdir}/%{name}/jack_alsarawmidi.so
%{_libdir}/%{name}/%{name}_firewire.so
%{_libdir}/%{name}/%{name}_proxy.so
%if 0%{?wdbus} == 1
%{_datadir}/dbus-1/services/org.jackaudio.service
%endif

%files -n libjack%{sonum}
%defattr(-, root, root)
%{_libdir}/libjack.so.%{sonum}*

%files -n libjacknet%{sonum}
%defattr(-, root, root)
%{_libdir}/libjacknet.so.%{sonum}*

%files -n libjackserver%{sonum}
%defattr(-, root, root)
%{_libdir}/libjackserver.so.%{sonum}*

%files -n libjack-devel
%defattr(-, root, root)
%doc %dir %{_docdir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}
%if %{buildoc} == 1
%dir %{_docdir}/jack-audio-connection-kit
%doc %{_docdir}/jack-audio-connection-kit/*
%endif

%changelog
