#
# spec file for package snd
#
# Copyright (c) 2022 SUSE LLC
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
Version:        23
Release:        0
Summary:        Sound File Editor
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://ccrma.stanford.edu/software/snd/
Source:         ftp://ccrma-ftp.stanford.edu/pub/Lisp/snd-%{version}.tar.gz
Source1:        snd.desktop
Source2:        snd.png
BuildRequires:  alsa-devel
BuildRequires:  fftw3-devel
BuildRequires:  freeglut-devel
BuildRequires:  gsl
BuildRequires:  gsl-devel
BuildRequires:  gtk3-devel
BuildRequires:  ladspa-devel
BuildRequires:  libXpm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjack-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  motif-devel
BuildRequires:  update-desktop-files
Requires:       ladspa

%description
Snd is a sound editor modelled loosely after Emacs and an old,
PDP-10 sound editor named Dpysnd. It can accommodate any
number of sounds each with any number of channels and can be customized
and extended using guile and guile-gtk.

%prep
%setup -q
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

%install
install -d -m 755 %{buildroot}/%{_bindir}
for i in snd sndplay sndinfo ; do
  install -c -m 755 $i %{buildroot}/%{_bindir}
done
mkdir -p %{buildroot}/%{_libdir}/snd/scheme
cp -a *.scm %{buildroot}/%{_libdir}/snd/scheme
mkdir -p %{buildroot}/%{_mandir}/man1
install -c -m 0644 snd.1 %{buildroot}/%{_mandir}/man1
%suse_update_desktop_file -i snd AudioVideo AudioVideoEditing
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
