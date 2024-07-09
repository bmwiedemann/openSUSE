#
# spec file for package brltty
#
# Copyright (c) 2024 SUSE LLC
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


%global _lto_cflags %_lto_cflags -ffat-lto-objects
%define api_version 0.8.5
%define sover 0_8
%define soname libbrlapi%{sover}
Name:           brltty
Version:        6.6
Release:        0
# FIXME libbraille driver when libbraille is in factory
Summary:        Braille display driver for Linux/Unix
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://brltty.app/

Source0:        https://brltty.app/archive/%name-%version.tar.xz
Source1:        README.SUSE
Source2:        %name.rpmlintrc
Patch0:         brltty-udev-dir.patch
Patch1:         https://github.com/brltty/brltty/commit/e6707d5e.patch

Requires(pre):  system-user-brltty = %version-%release

BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  espeak-ng-compat-devel
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gpm-devel
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  libbraille-devel
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros >= 20231101
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros > 20240101
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
%{?systemd_ordering}

%description
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

%package driver-at-spi2
Summary:        AT-SPI 2 driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and at-spi2-core)

%description driver-at-spi2
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the AT-SPI 2 screen driver.

%package driver-brlapi
Summary:        BrlAPI driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and %{soname})

%description driver-brlapi
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the BrlAPI braille driver.

%package driver-libbraille
Summary:        Libbraille driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and libbraille)

%description driver-libbraille
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the libbraille braille driver.

%package driver-espeak
Summary:        ESpeak driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and espeak-ng-compat)

%description driver-espeak
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the eSpeak speech driver.

%package driver-speech-dispatcher
Summary:        Speech Dispatcher driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and libspeechd2)

%description driver-speech-dispatcher
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the Speech Dispatcher speech driver.

%package driver-xwindow
Summary:        XWindow driver for BRLTTY
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (brltty and xorg-x11-server)

%description driver-xwindow
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the XWindow braille driver.

%package udev-generic
Summary:        BRLTTY Udev rules for braille devices that use a generic USB to serial adapter
Group:          System/Daemons
Requires:       %name = %version-%release

%description udev-generic
This package provides additional rules for managing BRLTTY via Udev.

Install this package in order to support braille devices that use a generic USB to serial adapter.

%package utils
Summary:        Braille display driver for Linux/Unix
Group:          System/Daemons
Requires:       %name = %version

%description utils
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contain various utilities related to BRLTTY.

%package -n xbrlapi
Summary:        X BrlAPI helper
Group:          System/Daemons
Requires:       %name = %version
Supplements:    (%{soname} and xorg-x11-server)

%description -n xbrlapi
The xbrlapi utility is a helper to have BrlAPI work on a X system.

%package -n %{soname}
Summary:        Library to use BRLTTY from applications
Group:          System/Daemons
Requires(post): coreutils
#!BuildIgnore:  group(brlapi)
Requires(post): group(brlapi)
Requires(post): util-linux
Recommends:     %name

%description -n %{soname}
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n brlapi-devel
Summary:        Library to use BRLTTY from applications -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %version

%description -n brlapi-devel
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n brlapi-java
Summary:        Library to use BRLTTY from applications -- Java Bindings
Group:          System/Daemons
Requires:       java
Requires:       jpackage-utils

%description -n brlapi-java
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n ocaml-brlapi
Summary:        Library to use BRLTTY from applications -- OCaml Bindings
Group:          System/Daemons
Requires:       ocaml

%description -n ocaml-brlapi
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n python3-brlapi
Summary:        Library to use BRLTTY from applications -- Python Bindings
Group:          System/Daemons

%description -n python3-brlapi
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n tcl-brlapi
Summary:        Library to use BRLTTY from applications -- Tcl Bindings
Group:          System/Daemons
Requires:       tcl

%description -n tcl-brlapi
BrlAPI is a service provided by the brltty daemon.

Its purpose is to allow programmers to write applications that take
advantage of a braille terminal in order to deliver a blind user
suitable information for his/her specific needs.

While an application communicates with the braille terminal, everything
brltty sends to the braille terminal in the application's console is
ignored, whereas each piece of data coming from the braille terminal is
sent to the application, rather than to brltty.

%package -n system-user-brltty
Summary:        System user and group named brltty
Group:          System/Base
Requires(pre):  group(pulse-access)
Requires(pre):  group(root)
Requires(pre):  group(tty)
Requires(pre):  group(dialout)
Requires(pre):  group(audio)
Requires(pre):  group(input)
BuildArch:      noarch
BuildRequires:  sysuser-tools
%?sysusers_requires

%description -n system-user-brltty
System user for the Braille display driver for Linux/Unix

%lang_package

%prep
%autosetup -p1

%build
%sysusers_generate_pre Autostart/Systemd/sysusers system-user-brltty %name.conf
cp %_sourcedir/README.SUSE .
# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' Documents/Manual-BRLTTY/Portuguese/BRLTTY.txt

modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%_sourcedir/%name.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
for i in -I%_libdir/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
export PYTHON=/usr/bin/python3
%configure CPPFLAGS="$java_inc" \
        --with-tables-directory=%_datadir/%name \
        --disable-stripping
make

%install
sed -i "s=/usr/libexec/brltty-systemd-wrapper=%_libexecdir/brltty-systemd-wrapper=" Autostart/Systemd/brltty@.service
%make_install install-systemd install-udev install-polkit INSTALL_ROOT="%buildroot"
for exe in %buildroot%_bindir/*
do
	sed -i~ '1{s@%_bindir/env[[:blank:]]\+@%_bindir/@}' "${exe}"
	diff -u "$_"~ "$_" || :
	rm -f "${exe}~"
done
%find_lang %name
sed -i "s/#api-parameters Auth=polkit/api-parameters Auth=polkit/" Documents/brltty.conf
install -D -m644 Documents/brltty.conf %buildroot%_sysconfdir/brltty.conf
# ghost brlapi.key
touch %buildroot%_sysconfdir/brlapi.key
# OCaml
%ocaml_create_file_list
#
rm %buildroot%_libdir/libbrlapi.a
rm %buildroot/etc/X11/Xsession.d/90xbrlapi # TODO: install this somewhere?
# fix missing executable bits
test ! -x %buildroot%_bindir/brltty-config.sh
chmod a+x %buildroot%_bindir/brltty-config.sh
# clean up the manuals:
rm Documents/Manual-*/*/{*.mk,Makefile*,*.sgml}
mv Documents/BrlAPIref/html Documents/BrlAPIref/BrlAPIref
# group all the documentation in a doc subdirectory:
find . \( -path ./doc -o -path ./Documents \) -prune -o \
  \( -name 'README*' -o -name '*.txt' -o -name '*.html' -o \
     -name '*.sgml' -o -name '*.patch' -o \
     \( -path './Bootdisks/*' -type f -perm /ugo=x \) \) -print |
while read file; do
   mkdir -p doc/${file%/*} && cp -rp $file doc/$file || exit 1
done

# disable xbrlapi gdm autostart, there is already orca
rm -f %buildroot%_datadir/gdm/greeter/autostart/xbrlapi.desktop

install -Dm0644 Autostart/AppStream/org.a11y.brltty.metainfo.xml \
                %buildroot%_datadir/metainfo/org.a11y.brltty.metainfo.xml

%python3_fix_shebang_path %{buildroot}%{_datadir}/brltty/Contraction/latex-access.ctb

%fdupes -s %buildroot%_mandir
%fdupes -s %buildroot

%pre -n system-user-brltty -f system-user-brltty.pre

%post -n %{soname}
if [ ! -e %_sysconfdir/brlapi.key ]; then
 mcookie > %_sysconfdir/brlapi.key
 chgrp brlapi %_sysconfdir/brlapi.key
 chmod 0640 %_sysconfdir/brlapi.key
fi
/sbin/ldconfig

%postun -n %{soname} -p /sbin/ldconfig

%pre
%service_add_pre %name.path

%post
%tmpfiles_create %_tmpfilesdir/%name.conf
%service_add_post %name.path

# Remove any messages that could've been in place about the upgrade
rm -f %_localstatedir/adm/update-messages/%name-%version-%release-something

if [ -f /usr/bin/lsusb ]; then
  lsusb 2>/dev/null |grep -q 0403:6001
  if [ $? -eq 0 ]; then
    cat >> %_localstatedir/adm/update-messages/%name-%version-%release-something << EOF

WARNING: The SUSE brltty package no longer enables certain USB
refreshable Braille displays by default, and it appears that you may have
one of these displays attached. If so, then you may need to edit
%_udevrulesdir/90-brltty-device.rules.
If your device is a standard USB-to-serial converter, rather than a
refreshable Braille display, then you can ignore this message.
See /usr/share/doc/packages/brltty/README.SUSE for more information.

EOF
  fi
fi

%preun
%service_del_preun %name.path

%postun
%service_del_postun %name.path
# Remove the /var/adm updatemsg that was hand-created and thus not on filelist
rm -f %_localstatedir/adm/update-messages/%name-%version-%release-something

%files
%license LICENSE-LGPL
%doc README README.SUSE Documents/ChangeLog Documents/CONTRIBUTORS Documents/HISTORY Documents/README.Bluetooth Documents/TODO
%doc Documents/Manual-BRLTTY/English
%config(noreplace) %_sysconfdir/brltty.conf
%_datadir/brltty/
%_bindir/brltty
%_bindir/brltty-clip
%_bindir/brltty-atb
%_bindir/brltty-cldr
%_bindir/brltty-config.sh
%_bindir/brltty-ctb
%_bindir/brltty-genkey
%_bindir/brltty-hid
%_bindir/brltty-ktb
%_bindir/brltty-lscmds
%_bindir/brltty-lsinc
%_bindir/brltty-mkuser
%_bindir/brltty-morse
%_bindir/brltty-prologue.bash
%_bindir/brltty-prologue.lua
%_bindir/brltty-prologue.tcl
%_bindir/brltty-prologue.sh
%_bindir/brltty-setcaps
%_bindir/brltty-term
%_bindir/brltty-trtxt
%_bindir/brltty-ttb
%_bindir/brltty-ttysize
%_bindir/brltty-tune
%_bindir/eutp
%dir %_datadir/metainfo
%_datadir/metainfo/org.a11y.%name.metainfo.xml
%_datadir/polkit-1/actions/org.a11y.brlapi.policy
%_datadir/polkit-1/rules.d/org.a11y.brlapi.rules
%_libdir/brltty/
%_libexecdir/brltty/
%_mandir/man1/brltty.1*
%_mandir/man1/eutp.1.gz
%_tmpfilesdir/%name.conf
%_udevrulesdir/90-%name-hid.rules
%_udevrulesdir/90-%name-uinput.rules
%_udevrulesdir/90-%name-usb-customized.rules
%_unitdir/%name.path
%_unitdir/%name@.path
%_unitdir/%name-device@.service
%_unitdir/%name@.service
%exclude %_libdir/brltty/libbrlttybba.so
%exclude %_libdir/brltty/libbrlttyblb.so
%exclude %_libdir/brltty/libbrlttybxw.so
%exclude %_libdir/brltty/libbrlttyses.so
%exclude %_libdir/brltty/libbrlttyssd.so
%exclude %_libdir/brltty/libbrlttyxa2.so
%ghost %_localstatedir/adm/update-messages/%name-%version-%release-something

%files driver-at-spi2
%_libdir/brltty/libbrlttyxa2.so

%files driver-brlapi
%doc Drivers/Braille/BrlAPI/README
%_libdir/brltty/libbrlttybba.so

%files driver-libbraille
%_libdir/brltty/libbrlttyblb.so

%files driver-espeak
%doc Drivers/Speech/eSpeak/README
%_libdir/brltty/libbrlttyses.so

%files driver-speech-dispatcher
%doc Drivers/Speech/SpeechDispatcher/README
%_libdir/brltty/libbrlttyssd.so

%files driver-xwindow
%doc Drivers/Braille/XWindow/README
%_libdir/brltty/libbrlttybxw.so

%files udev-generic
%_udevrulesdir/90-%name-usb-generic.rules

%files utils
%_bindir/vstp
%_mandir/man1/vstp.1*

%files -n xbrlapi
%_bindir/xbrlapi
%_mandir/man1/xbrlapi.1*

%files -n %{soname}
%doc Documents/Manual-BrlAPI/
%_libdir/libbrlapi.so.*
%ghost %_sysconfdir/brlapi.key

%files -n brlapi-devel
%_includedir/brltty/
%_includedir/brlapi*.h
%_libdir/libbrlapi.so
%_libdir/pkgconfig/brltty.pc
%doc %_mandir/man3/brlapi_*

%files -n brlapi-java
%{_jnidir}/libbrlapi_java.so
%{_javadir}/brlapi.jar

%files -n ocaml-brlapi -f %name.files.devel

%files -n python3-brlapi
%{python3_sitearch}/brlapi.cpython*.so
%{python3_sitearch}/Brlapi-*.egg-info

%files -n tcl-brlapi
%_libdir/tcl/brlapi-%{api_version}/

%files -n system-user-brltty
%_sysusersdir/%name.conf

%files lang -f %name.lang
%doc Documents/Manual-BRLTTY/French
%doc Documents/Manual-BRLTTY/Portuguese

%changelog
