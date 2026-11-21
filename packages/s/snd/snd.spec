#
# spec file for package snd
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%ifarch aarch64
%define _lto_cflags %{nil}
%endif
%ifarch %{ix86} x86_64 %{ppc} ppc64 ppc64le
# The jack support has some inline assembly, but only for x86/ppc
%bcond_without jack
%else
%bcond_with jack
%endif
Name:           snd
Version:        26.8
Release:        0
Summary:        Sound File Editor
License:        LGPL-2.1-or-later
URL:            https://ccrma.stanford.edu/software/snd/
Source0:        https://ccrma.stanford.edu/software/snd/snd-%{version}.tar.gz
Source1:        snd.desktop.in
Source2:        snd.png
BuildRequires:  gsl
BuildRequires:  ladspa-devel
BuildRequires:  motif-devel
BuildRequires:  pkgconfig
BuildRequires:  translate-suse-desktop
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(xpm)
Requires:       ladspa

%description
Snd is a sound editor modelled loosely after Emacs and an old,
PDP-10 sound editor named Dpysnd. It can accommodate any
number of sounds each with any number of channels and can be customized
and extended using guile and guile-gtk.

%prep
%autosetup
cp -a %{SOURCE1} .
find -name "*~" -type f -print -delete
find -name "*.png" -type f -exec chmod 0644 "{}" "+"

%build
%configure \
  --with-gui \
  --with-alsa \
  --with-ladspa \
  --with-gl \
  %{?with_jack:--with-jack} \
# feel free to improve following change and please notify upstream
sed -i "s:\(^LIBS =.*\):\1 -lX11 -ldl:" makefile
%make_build
%make_build sndplay sndinfo
%translate_suse_desktop snd.desktop

%install
install -d -m 755 %{buildroot}/%{_bindir}
for i in snd sndplay sndinfo ; do
  install -c -m 755 $i %{buildroot}/%{_bindir}
done
mkdir -p %{buildroot}/%{_libdir}/snd/scheme
cp -a *.scm %{buildroot}/%{_libdir}/snd/scheme
mkdir -p %{buildroot}/%{_mandir}/man1
install -c -m 0644 snd.1 %{buildroot}/%{_mandir}/man1
install -D -m 0644 snd.desktop %{buildroot}%{_datadir}/applications/snd.desktop
mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps

%files
%license COPYING
%doc *.Snd *.html pix
%{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/snd
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
