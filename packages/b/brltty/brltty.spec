#
# spec file for package brltty
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


%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl/tcl%{tcl_version}}
%define api_version 0.8.0
%define sover 0_8
%define soname libbrlapi%{sover}

%define with_polkit 1

%if 0%{?suse_version} >= 1500
%define espeak    espeak-ng-compat
%define espeakdev espeak-ng-compat-devel
%else
%define espeak    espeak
%define espeakdev espeak-devel
%endif

Name:           brltty
Version:        6.1
Release:        0
# FIXME libbraille driver when libbraille is in factory
Summary:        Braille display driver for Linux/Unix
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://brltty.app/

Source0:        https://brltty.app/archive/%{name}-%{version}.tar.xz
Source1:        README.SUSE
Patch0:         brltty-5.5-systemd-install.patch
Patch1:         brltty-gcc10.patch

BuildRequires:  %{espeakdev}
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gpm-devel
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  libbraille-devel
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
%if %{?with_polkit}
BuildRequires:  pkgconfig(polkit-gobject-1)
%endif
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
%{?systemd_ordering}
%define _udevdir %(pkg-config --variable udevdir udev)

%description
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

%package driver-at-spi2
Summary:        AT-SPI 2 driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:at-spi2-core)

%description driver-at-spi2
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the AT-SPI 2 screen driver.

%package driver-brlapi
Summary:        BrlAPI driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:%{soname})

%description driver-brlapi
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the BrlAPI braille driver.

%package driver-libbraille
Summary:        Libbraille driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:libbraille)

%description driver-libbraille
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the libbraille braille driver.

%package driver-espeak
Summary:        ESpeak driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:%{espeak})

%description driver-espeak
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the eSpeak speech driver.

%package driver-speech-dispatcher
Summary:        Speech Dispatcher driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:libspeechd2)

%description driver-speech-dispatcher
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the Speech Dispatcher speech driver.

%package driver-xwindow
Summary:        XWindow driver for BRLTTY
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(brltty:xorg-x11-server)

%description driver-xwindow
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contains the XWindow braille driver.

%package utils
Summary:        Braille display driver for Linux/Unix
Group:          System/Daemons
Requires:       %{name} = %{version}

%description utils
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable braille display. It drives the braille display and provides
complete screen review functionality.

This package contain various utilities related to BRLTTY.

%package -n xbrlapi
Summary:        X BrlAPI helper
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(%{soname}:xorg-x11-server)

%description -n xbrlapi
The xbrlapi utility is a helper to have BrlAPI work on a X system.

%package -n %{soname}
Summary:        Library to use BRLTTY from applications
Group:          System/Daemons
Requires(post): coreutils
Requires(post): shadow
Requires(post): util-linux
Recommends:     %{name}

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
Requires:       %{soname} = %{version}

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

%lang_package

%prep
%autosetup -p1

%build
cp %{_sourcedir}/README.SUSE .
# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' Documents/Manual-BRLTTY/Portuguese/BRLTTY.txt

sed -i 's:/usr/bin/python:/usr/bin/python3:' ./Tables/Contraction/latex-access.ctb

modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
for i in -I%{_libdir}/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
export PYTHON=/usr/bin/python3
%configure CPPFLAGS="$java_inc" \
        --with-install-root="%{buildroot}" \
        --libexecdir=%_libexecdir \
        --disable-stripping
make -j1 # not parallel build safe

%install
sed -i "s=/usr/libexec/brltty-systemd-wrapper=%_libexecdir/brltty-systemd-wrapper=" Autostart/Systemd/brltty@.service
make install install-systemd DESTDIR="%buildroot"
%find_lang %{name}
%if %{?with_polkit}
sed -i "s/#api-parameters Auth=polkit/api-parameters Auth=polkit/" Documents/brltty.conf
%endif
install -D -m644 Documents/brltty.conf %{buildroot}%{_sysconfdir}/brltty.conf
# ghost brlapi.key
touch %{buildroot}%{_sysconfdir}/brlapi.key
# Don't include source files in binary package
rm -f %{buildroot}%{_libdir}/ocaml/brlapi/brlapi.{mli,cmxa}
# Don't claim generic USB serial adapters (boo#1007652)
sed -i \
  -e 's/^ENV{PRODUCT}=="403\/6001\/\*"/#ENV{PRODUCT}=="403\/6001\/\*"/' \
  -e 's/^ENV{PRODUCT}=="10c4\/ea60\/\*"/#ENV{PRODUCT}=="10c4\/ea60\/\*"/' \
  -e 's/^ENV{PRODUCT}=="10c4\/ea80\/\*"/#ENV{PRODUCT}=="10c4\/ea80\/\*"/' \
  Autostart/Udev/rules
mkdir -p %{buildroot}%{_udevdir}/rules.d
install -m644 Autostart/Udev/rules %{buildroot}%{_udevdir}/rules.d/69-%{name}.rules
%if %{?with_polkit}
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
install -m 644 Authorization/Polkit/org.a11y.brlapi.policy %{buildroot}%{_datadir}/polkit-1/actions
%endif
rm %{buildroot}%{_libdir}/libbrlapi.a
rm %{buildroot}%{_libdir}/ocaml/brlapi/libbrlapi_stubs.a
rm %{buildroot}/etc/X11/Xsession.d/90xbrlapi # TODO: install this somewhere?
# fix missing executable bits
test ! -x %{buildroot}%{_bindir}/brltty-config
chmod a+x %{buildroot}%{_bindir}/brltty-config
# clean up the manuals:
rm Documents/Manual-*/*/{*.mk,*.made,Makefile*,*.sgml,*-[0-9]*.html}
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
rm -f %{buildroot}%{_datadir}/gdm/greeter/autostart/xbrlapi.desktop

install -Dm0644 Autostart/AppStream/org.a11y.brltty.metainfo.xml \
                %{buildroot}%{_datadir}/metainfo/org.a11y.brltty.metainfo.xml

%fdupes -s %{buildroot}%{_mandir}
%fdupes -s %{buildroot}

# fix brp-tcl wrong location for Tcl files
mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/brlapi-%{api_version} %{buildroot}%{tcl_sitearch}/

%pre -n %{soname}
getent group brlapi >/dev/null || groupadd -r brlapi >/dev/null

%post -n %{soname}
if [ ! -e %{_sysconfdir}/brlapi.key ]; then
 mcookie > %{_sysconfdir}/brlapi.key
 chgrp brlapi %{_sysconfdir}/brlapi.key
 chmod 0640 %{_sysconfdir}/brlapi.key
fi
/sbin/ldconfig

%postun -n %{soname} -p /sbin/ldconfig

%pre
%service_add_pre %{name}.path

%post
%service_add_post %{name}.path

# Remove any messages that could've been in place about the upgrade
rm -f %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something

if [ -f /usr/bin/lsusb ]; then
  lsusb 2>/dev/null |grep -q 0403:6001
  if [ $? -eq 0 ]; then
    cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

WARNING: The SUSE brltty package no longer enables certain USB
refreshable Braille displays by default, and it appears that you may have
one of these displays attached. If so, then you may need to edit
/usr/lib/udev/rules.d/69-brltty.rules.
If your device is a standard USB-to-serial converter, rather than a
refreshable Braille display, then you can ignore this message.
See /usr/share/doc/packages/brltty/README.SUSE for more information.

EOF
  fi
fi

%preun
%service_del_preun %{name}.path

%postun
%service_del_postun %{name}.path
# Remove the /var/adm updatemsg that was hand-created and thus not on filelist
rm -f %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something

%files
%defattr(-, root, root)
%doc LICENSE-LGPL README README.SUSE Documents/ChangeLog Documents/CONTRIBUTORS Documents/HISTORY Documents/README.Bluetooth Documents/TODO
%doc Documents/Manual-BRLTTY/English
%config(noreplace) %{_sysconfdir}/brltty.conf
%{_sysconfdir}/brltty/
%{_bindir}/brltty
%{_bindir}/brltty-clip
%{_bindir}/brltty-atb
%{_bindir}/brltty-cldr
%{_bindir}/brltty-config
%{_bindir}/brltty-ctb
%{_bindir}/brltty-ktb
%{_bindir}/brltty-lscmds
%{_bindir}/brltty-lsinc
%{_bindir}/brltty-morse
%{_bindir}/brltty-trtxt
%{_bindir}/brltty-ttb
%{_bindir}/brltty-tune
%{_bindir}/eutp
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.a11y.%{name}.metainfo.xml
%if %{?with_polkit}
%{_datadir}/polkit-1/actions/org.a11y.brlapi.policy
%endif
%{_libdir}/brltty/
%{_prefix}/lib/brltty/
%{_prefix}/lib/%{name}/systemd-wrapper
%{_mandir}/man1/brltty.1*
%{_mandir}/man1/eutp.1.gz
%{_udevdir}/rules.d/69-%{name}.rules
%{_unitdir}/%{name}.path
%{_unitdir}/%{name}@.path
%{_unitdir}/%{name}@.service
%exclude %{_libdir}/brltty/libbrlttybba.so
%exclude %{_libdir}/brltty/libbrlttyblb.so
%exclude %{_libdir}/brltty/libbrlttybxw.so
%exclude %{_libdir}/brltty/libbrlttyses.so
%exclude %{_libdir}/brltty/libbrlttyssd.so
%exclude %{_libdir}/brltty/libbrlttyxa2.so
%ghost %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something

%files driver-at-spi2
%defattr(-, root, root)
%{_libdir}/brltty/libbrlttyxa2.so

%files driver-brlapi
%defattr(-, root, root)
%doc Drivers/Braille/BrlAPI/README
%{_libdir}/brltty/libbrlttybba.so

%files driver-libbraille
%defattr(-, root, root)
%{_libdir}/brltty/libbrlttyblb.so

%files driver-espeak
%defattr(-, root, root)
%doc Drivers/Speech/eSpeak/README
%{_libdir}/brltty/libbrlttyses.so

%files driver-speech-dispatcher
%defattr(-, root, root)
%doc Drivers/Speech/SpeechDispatcher/README
%{_libdir}/brltty/libbrlttyssd.so

%files driver-xwindow
%defattr(-, root, root)
%doc Drivers/Braille/XWindow/README
%{_libdir}/brltty/libbrlttybxw.so

%files utils
%defattr(-, root, root)
%{_bindir}/vstp
%{_mandir}/man1/vstp.1*

%files -n xbrlapi
%defattr(-, root, root)
%{_bindir}/xbrlapi
%{_mandir}/man1/xbrlapi.1*

%files -n %{soname}
%defattr(-, root, root)
%doc Documents/Manual-BrlAPI/
%{_libdir}/libbrlapi.so.*
%ghost %{_sysconfdir}/brlapi.key

%files -n brlapi-devel
%defattr(-, root, root)
%doc Documents/BrlAPIref/BrlAPIref/
%{_includedir}/brltty/
%{_includedir}/brlapi*.h
%{_libdir}/libbrlapi.so
%doc %{_mandir}/man3/brlapi_*

%files -n brlapi-java
%defattr(-, root, root)
%{_jnidir}/libbrlapi_java.so
%{_javadir}/brlapi.jar

%files -n ocaml-brlapi
%defattr(-, root, root)
%{_libdir}/ocaml/brlapi/
%{_libdir}/ocaml/stublibs/dllbrlapi_stubs.so*

%files -n python3-brlapi
%defattr(-, root, root)
%{python3_sitearch}/brlapi.cpython*.so
%{python3_sitearch}/Brlapi-*.egg-info

%files -n tcl-brlapi
%defattr(-, root, root)
%{tcl_sitearch}/brlapi-%{api_version}/

%files lang -f %{name}.lang
%defattr(-, root, root)
%doc Documents/Manual-BRLTTY/French
%doc Documents/Manual-BRLTTY/Portuguese

%changelog
