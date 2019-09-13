#
# spec file for package snack
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           snack
BuildRequires:  alsa-devel
BuildRequires:  libvorbis-devel
BuildRequires:  python
BuildRequires:  tk-devel
BuildRequires:  xorg-x11-devel
Summary:        Sound Extension for Tcl/Tk and Python
License:        GPL-2.0+
Group:          Development/Libraries/Tcl
Version:        2.2.10
Release:        0
Requires:       tcl
Requires:       tk
%{py_requires}
Url:            http://www.speech.kth.se/snack
Source0:        %{name}%{version}.tar.bz2
Source1:        snack-rpmlintrc
Patch0:         snack.patch
Patch1:         snack-alsa.patch
Patch2:         snack-CVE-2012-6303.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Snack provides commands to play, record, process, and visualize sound.
It supports various file formats such as WAV, AU, AIFF, and MP3.

With Snack, you can easily create sound applications with Tcl/Tk or
Python or extend existing programs with sound capabilities.

The documentation is located under /usr/share/doc/packages/snack There
is also a 'demos' subdirectory which contains examples for Tcl/Tk and
Python.



Authors:
--------
    Kåre Sjölander <kare@speech.kth.se>

%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q -n %{name}%{version}
%patch0
%patch1
%patch2 -p 1
chmod 644 BSD.txt changes README COPYING doc/* ext/*
chmod 755 ext/configure

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-unused-variable -Wno-unused-but-set-variable"
cd unix
./configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --with-tcl=%_libdir \
    --with-tk=%_libdir \
    --with-ogg-include=%_includedir \
    --with-ogg-lib=%_libdir \
    --enable-alsa
make OPTFLAGS="$CFLAGS"

%install
%{INSTALL_DIR} %buildroot%py_sitedir
%{INSTALL_DATA} python/tkSnack.py %buildroot%py_sitedir
cd unix
make  install \
	DESTDIR=%buildroot \
	SNACK_INSTALL_PATH=%tclscriptdir
# We don't install the headers, so we don't need the stubs lib
rm -f %buildroot/%_libdir/libsnack*.a

%clean
rm -rf %buildroot

%files
%defattr(-, root, root,-)
%_libdir/lib*
%defattr(644, root, root, 755)
%doc BSD.txt changes README COPYING doc/* ext
%tclscriptdir/*
%py_sitedir/*

%changelog
