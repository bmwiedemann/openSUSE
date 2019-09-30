#
# spec file for package timidity
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           timidity
Summary:        Software Synthesizer and MIDI Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Version:        2.14.0
Release:        0
Url:            http://timidity.sourceforge.net/
%define my_provides /tmp/my-provides
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  flac-devel
BuildRequires:  gtk2-devel
BuildRequires:  libao-devel
BuildRequires:  libjack-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ncurses-devel
BuildRequires:  slang-devel
BuildRequires:  speex-devel
BuildRequires:  update-desktop-files
BuildRequires:  xaw3d
BuildRequires:  xorg-x11
Recommends:     fluid-soundfont-gm fluid-soundfont-gs
BuildRequires:  fdupes
BuildRequires:  systemd
BuildRequires:  xaw3d-devel
%{?systemd_requires}
PreReq:         %fillup_prereq
Source:         TiMidity++-%{version}.tar.xz
Source1:        timidity-patches.tar.bz2
Source2:        %name.desktop
Source3:        timidity.png
Source4:        timidity.cfg
Source5:        %{name}.service
Source6:        %{name}.sysconf
Source7:        README.SUSE
Patch2:         0002-Fix-alsaseq-polling-at-idle-time.patch
Patch100:       timidity-no_date.patch
Patch101:       timidity-add_fluid_cfgs.patch
Patch200:       timidity-readmidi-zero-division-fix.patch
Patch201:       timidity-resample-frac-overflow-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TiMidity plays MIDI files without external MIDI instruments and
converts MIDI files to WAV using GUS/patch and SoundFont for voice
data.


%prep
%setup -q -n TiMidity++-%{version} -a 1
%patch2 -p1
%patch100
%patch101
%patch200 -p1
%patch201 -p1
for f in ./utils/bitset.c ./utils/bitset.h ./utils/nkflib.c; do
	iconv -f EUC-JISX0213 -t UTF-8 $f > $f.utf8 && mv $f.utf8 $f
done

%build
# disable LTO for avoiding segfaults with ALSA backend (boo#1149461)
%define _lto_cflags %{nil}
echo >> autoconf/arts.m4
autoreconf --force --install
%configure \
	--enable-dynamic=ncurses,emacs,slang,vt100,xskin,gtk,alsaseq,server \
	--enable-audio=alsa,oss,vorbis,jack,ao,flac,speex \
	--with-default-output=alsa \
	--enable-network \
	--enable-spectrogram \
	--enable-wrd \
	--with-module-dir=%{_libdir}/timidity \
	--with-default-path=/etc
make %{?_smp_mflags} WISH=tclsh CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall WISH=tclsh
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/
cp interface/TiMidity.ad $RPM_BUILD_ROOT/usr/share/X11/app-defaults/TiMidity
# for japanese locale
# UTF-8 version
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/{ja,ja_JP.UTF-8,ja_JP.eucJP,ja_JP.ujis}/app-defaults
iconv -feuc-jp -tutf-8 interface/TiMidity-uj.ad > $RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/TiMidity
ln -s ../../ja/app-defaults/TiMidity $RPM_BUILD_ROOT%{_datadir}/X11/ja_JP.UTF-8/app-defaults/TiMidity
# EUC-jp version
cp interface/TiMidity-uj.ad $RPM_BUILD_ROOT%{_datadir}/X11/ja_JP.eucJP/app-defaults/TiMidity
ln -s ../../ja_JP.eucJP/app-defaults/TiMidity $RPM_BUILD_ROOT%{_datadir}/X11/ja_JP.ujis/app-defaults/TiMidity
# copy documents
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp AUTHORS COPYING ChangeLog* NEWS README TODO \
  $RPM_BUILD_ROOT%{_docdir}/%{name}
cp %{SOURCE7} $RPM_BUILD_ROOT%{_docdir}/%{name}
for i in *.ja; do
  iconv -f euc-jp -t utf8 $i > $RPM_BUILD_ROOT%{_docdir}/%{name}/$i
done
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/en
(cd doc/C
  for i in * ; do
    case $i in
    Makefile*|*.[1-9])
      ;;
    *)
      cp $i $RPM_BUILD_ROOT%{_docdir}/%{name}/en
      ;;
    esac
  done
)
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/ja_JP
(cd doc/ja_JP.eucJP
  for i in * ; do
    case $i in
    Makefile*|*.[1-9])
      ;;
    *)
      iconv -f euc-jp -t utf8 $i > $RPM_BUILD_ROOT%{_docdir}/%{name}/ja_JP/$i
      ;;
    esac
  done
)
# copy sample patches and config file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/timidity
cp -a timidity-patches/* $RPM_BUILD_ROOT%{_datadir}/timidity
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xemacs/site-lisp/lisp
cp interface/timidity.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
cp interface/timidity.el $RPM_BUILD_ROOT%{_datadir}/xemacs/site-lisp/lisp
%suse_update_desktop_file -i -u %name AudioVideo Midi
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT/etc
install -c -m 644 %{SOURCE4} $RPM_BUILD_ROOT/etc

# boot scripts
#
%__install -m 644 -D %{S:6} %{buildroot}%{_fillupdir}/sysconfig.timidity
%__install -Dm 644 %{S:5} %{buildroot}%{_unitdir}/%{name}.service
%__install -d %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

# exclude plugins from the provide-list
cat << EOF > %{my_provides}
grep -v $RPM_BUILD_ROOT%{_libdir}/timidity | %{__find_provides}
EOF
chmod 755 %{my_provides}
%define __find_provides %{my_provides}
%fdupes -s %{buildroot}

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%{_docdir}
%{_libdir}/timidity
%{_datadir}/timidity
%config(noreplace) %{_datadir}/timidity/timidity.cfg
%{_bindir}/timidity
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%config /etc/timidity.cfg
%doc %{_mandir}/man*/*
%{_datadir}/X11/app-defaults/TiMidity
%{_datadir}/X11/ja*
%{_datadir}/emacs
%{_datadir}/xemacs
%{_unitdir}/timidity.service
%{_sbindir}/rctimidity
%{_fillupdir}/sysconfig.timidity

%changelog
