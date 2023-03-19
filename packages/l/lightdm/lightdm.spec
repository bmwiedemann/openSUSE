#
# spec file for package lightdm
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011 Guido Berhoerster.
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


%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%define build_qt4 0
%else
%define build_qt4 1
%endif

%define ver_master      1.24
%define gobject_libname lightdm-gobject-1
%define gobject_lib     lib%{gobject_libname}-0
%define qt4_libname     lightdm-qt-3
%define qt4_lib         lib%{qt4_libname}-0
%define qt5_libname     lightdm-qt5-3
%define qt5_lib         lib%{qt5_libname}-0
%define typelibname     typelib-1_0-LightDM-1
%define rundir          /run
Name:           lightdm
Version:        1.32.0
Release:        0
Summary:        Lightweight, Cross-desktop Display Manager
License:        GPL-3.0-or-later
Group:          System/X11/Displaymanagers
URL:            https://freedesktop.org/wiki/Software/LightDM
Source:         https://github.com/CanonicalLtd/lightdm/releases/download/%{version}/%{name}-%{version}.tar.xz
#Source1:        https://github.com/CanonicalLtd/lightdm/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        %{name}-greeter.pamd
Source4:        X11-displaymanagers-%{name}
Source5:        gdmflexiserver
Source6:        50-suse-defaults.conf
Source7:        users.conf
Source8:        lightdm.pam
Source9:        lightdm-autologin.pam
Source10:       lightdm.sysusers
# PATCH-FEATURE-OPENSUSE lightdm-sysconfig-support.patch gber@opensuse.org -- Adds support for reading configuration options from /etc/sysconfig/displaymanager and /etc/sysconfig/windowmanager
Patch0:         lightdm-sysconfig-support.patch
# PATCH-FEATURE-OPENSUSE lightdm-xauthlocalhostname-support.patch boo#796230 gber@opensuse.org -- Set XAUTHLOCALHOSTNAME to the hostname for local logins to avoid issues in the session in case the hostname changes
Patch1:         lightdm-xauthlocalhostname-support.patch
# PATCH-FEATURE-OPENSUSE lightdm-set-gdmflexiserver-envvar.patch gber@opensuse.org -- Sets the GDMFLEXISERVER environment variable for the gdmflexiserver wrapper
Patch2:         lightdm-set-gdmflexiserver-envvar.patch
# PATCH-FIX-OPENSUSE lightdm-disable-utmp-handling.patch gber@opensuse.org -- Disable utmp handling since this is handled in the Xstartup/Xreset scripts
Patch3:         lightdm-disable-utmp-handling.patch
# PATCH-FIX-OPENSUSE lightdm-use-run-dir.patch gber@opensuse.org -- Use /run instead of /var/run
Patch4:         lightdm-use-run-dir.patch
# PATCH-FIX-OPENSUSE ignore-known-symlink-sessions.patch boo#1030873 -- Ignore known synlink sessions.
Patch5:         lightdm-ignore-known-symlink-sessions.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  vala
BuildRequires:  xdm
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
%if %{build_qt4}
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
%endif
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xdmcp)
Requires:       gdmflexiserver
# 3rd party greeters don't have to follow
# the same versioning of lightdm.
Requires:       lightdm-greeter
# Uses pam configuration and relies on scripts provided by xdm.
Requires:       xdm
%sysusers_requires
Recommends:     %{name}-lang
# Migrate users from lxdm to lightdm - we only obsolete up to version 0.5.
Obsoletes:      lxdm < 0.5
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(audit)
%endif

%description
LightDM is a lightweight, cross-desktop display manager. Its main
features are a well-defined greeter API allowing multiple GUIs,
support for all display manager use cases, with plugins where
appropriate, low code complexity, and fast performance. Due to its
cross-platform nature greeters can be written in several toolkits
such as Qt and GTK+.

%lang_package

%package -n %{gobject_lib}
Summary:        LightDM GObject-based Client Library
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          System/Libraries
Recommends:     accountsservice

%description -n %{gobject_lib}
A GObject-based library for LightDM clients to use to interface
with LightDM.

%package gobject-devel
Summary:        Development Files for %{gobject_lib}
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       %{gobject_lib} = %{version}

%description gobject-devel
This package contains development files needed for developing
GObject-based LightDM clients.

%package -n %{typelibname}
Summary:        GObject Introspection Bindings for the LightDM Client Library
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          System/Libraries

%description -n %{typelibname}
This package contains the GObject Introspection bindings for the
LightDM client library.

%if %{build_qt4}
%package -n %{qt4_lib}
Summary:        LightDM Qt4-based Client Library
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          System/Libraries

%description -n %{qt4_lib}
A Qt4-based library for LightDM clients to use to interface with
LightDM.

%package qt-devel
Summary:        Development Files for %{qt4_lib}
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       %{qt4_lib} = %{version}

%description qt-devel
This package contains development files needed for developing
Qt4-based LightDM clients.
%endif

%package -n %{qt5_lib}
Summary:        LightDM Qt5-based Client Library
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          System/Libraries
%if !%{build_qt4}
Provides:       %{qt4_lib} = %{version}
Obsoletes:      %{qt4_lib} < %{version}
%endif

%description -n %{qt5_lib}
A Qt5-based library for LightDM clients to use to interface with
LightDM.

%package qt5-devel
Summary:        Development Files for %{qt5_lib}
License:        LGPL-2.0-only OR LGPL-3.0-only
Group:          Development/Libraries/C and C++
Requires:       %{qt5_lib} = %{version}
%if !%{build_qt4}
Provides:       %{name}-qt-devel = %{version}
Obsoletes:      %{name}-qt-devel < %{version}
%endif

%description qt5-devel
This package contains development files needed for developing
Qt5-based LightDM clients.

%package bash-completion
Summary:        Bash completion for lightdm
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
bash command line completion support for lightdm.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE10} lightdm lightdm.conf
export MOC4='%{_bindir}/moc'
export MOC5='%{_libqt5_bindir}/moc'
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static \
  --enable-gtk-doc \
  --with-user-session=default \
  --with-greeter-session=lightdm-default-greeter \
  --with-greeter-user=lightdm
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

# Configuration is delivered in %%{_datadir}/lightdm/lightdm.conf.d
rm %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf

# upstart configuration is not needed.
rm -rf %{buildroot}%{_sysconfdir}/init/

# There is no guest session support in openSUSE.
rm -rf %{buildroot}%{_sysconfdir}/apparmor.d/
rm -rf %{buildroot}%{_libexecdir}/lightdm-guest-session

# These are useless stubs for now.
rm -rf %{buildroot}%{_datadir}/help/

# xdm and xdm-np are used instead.
rm %{buildroot}%{_sysconfdir}/pam.d/lightdm \
   %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin \
   %{buildroot}%{_sysconfdir}/pam.d/lightdm-greeter
%if 0%{?suse_version} >= 1550
  mkdir -p %{buildroot}%{_pam_vendordir}
  install %{SOURCE8} %{buildroot}%{_pam_vendordir}/lightdm
  install %{SOURCE9} %{buildroot}%{_pam_vendordir}/lightdm-autologin
  install -Dpm 0644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/lightdm-greeter
%else
  install %{SOURCE8} %{buildroot}%{_sysconfdir}/pam.d/lightdm
  install %{SOURCE9} %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin
  install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/lightdm-greeter
%endif

ln data/lightdm.conf data/lightdm.conf.example

install -d %{buildroot}%{_sysconfdir}/xdg/lightdm/lightdm.conf.d
install -d %{buildroot}%{_datadir}/lightdm/greeters
install -d %{buildroot}%{_datadir}/lightdm/lightdm.conf.d
install -d %{buildroot}%{_datadir}/lightdm/remote-sessions
install -d %{buildroot}%{_datadir}/lightdm/sessions
install -d %{buildroot}%{_datadir}/xgreeters
install -d %{buildroot}%{_localstatedir}/cache/lightdm
install -d %{buildroot}%{_localstatedir}/lib/lightdm
install -d %{buildroot}%{_localstatedir}/lib/lightdm-data
install -d %{buildroot}%{_localstatedir}/log/lightdm
install -d %{buildroot}%{rundir}/lightdm

install -Dpm 0644 %{SOURCE4} %{buildroot}%{_prefix}/lib/X11/displaymanagers/lightdm
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_prefix}/lib/X11/displaymanagers/default-displaymanager

install -Dpm 0755 %{SOURCE5} %{buildroot}%{_libexecdir}/lightdm/gdmflexiserver

install -Dpm 0644 %{SOURCE6} %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/50-suse-defaults.conf
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/lightdm/users.conf

%if !%{defined _distconfdir} || 0%{?suse_version} < 1550
sed -e 's-/usr/etc-%{_sysconfdir}-g' -i %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/50-suse-defaults.conf
%endif

install -Dm0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/lightdm.conf

%find_lang %{name} %{?no_lang_C}

%pre -f lightdm.pre
for i in pam.d/lightdm pam.d/lightdm-autologin pam.d/lightdm-greeter; do
  test -f /etc/${i}.rpmsave && mv -v /etc/${i}.rpmsave /etc/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in pam.d/lightdm pam.d/lightdm-autologin pam.d/lightdm-greeter; do
  test -f /etc/${i}.rpmsave && mv -v /etc/${i}.rpmsave /etc/${i} ||:
done

%post
# Special trick: migrate users from lxdm to lightdm
# see https://lists.opensuse.org/opensuse-factory/2016-07/msg00417.html
. %{_sysconfdir}/sysconfig/displaymanager
if [ -z "$DISPLAYMANAGER" -o "$DISPLAYMANAGER" = "lxdm" ] ; then
    sed -i 's/^DISPLAYMANAGER=".*"/DISPLAYMANAGER="lightdm"/' %{_sysconfdir}/sysconfig/displaymanager
fi
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/lightdm 15

%postun
if [ "$1" -eq 0 ]; then
    . %{_sysconfdir}/sysconfig/displaymanager
    if [ "$DISPLAYMANAGER" == "lightdm" ] ; then
        sed -i 's/^DISPLAYMANAGER="lightdm"/DISPLAYMANAGER=""/' %{_sysconfdir}/sysconfig/displaymanager
    fi
fi
[ -f %{_prefix}/lib/X11/displaymanagers/lightdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/lightdm

%post -n %{gobject_lib} -p /sbin/ldconfig

%postun -n %{gobject_lib} -p /sbin/ldconfig

%if %{build_qt4}
%post -n %{qt4_lib} -p /sbin/ldconfig

%postun -n %{qt4_lib} -p /sbin/ldconfig
%endif

%post -n %{qt5_lib} -p /sbin/ldconfig

%postun -n %{qt5_lib} -p /sbin/ldconfig

%files
%license COPYING.GPL3
%doc NEWS data/lightdm.conf.example
%{_bindir}/dm-tool
%{_sbindir}/lightdm
%dir %{_libexecdir}/lightdm/
%{_libexecdir}/%{name}/gdmflexiserver
%dir %{_sysconfdir}/xdg/lightdm/
%dir %{_sysconfdir}/xdg/lightdm/lightdm.conf.d/
%dir %{_sysconfdir}/lightdm/
%config(noreplace) %{_sysconfdir}/lightdm/users.conf
%config(noreplace) %{_sysconfdir}/lightdm/keys.conf
%if 0%{?suse_version} >= 1550
%{_pam_vendordir}/lightdm
%{_pam_vendordir}/lightdm-autologin
%{_pam_vendordir}/lightdm-greeter
%else
%config %{_sysconfdir}/pam.d/lightdm
%config %{_sysconfdir}/pam.d/lightdm-autologin
%config %{_sysconfdir}/pam.d/lightdm-greeter
%endif
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%dir %{_prefix}/lib/X11/displaymanagers/
%{_prefix}/lib/X11/displaymanagers/lightdm
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_datadir}/lightdm/
%dir %{_datadir}/accountsservice/
%dir %{_datadir}/accountsservice/interfaces/
%{_datadir}/accountsservice/interfaces/org.freedesktop.DisplayManager.AccountsService.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.DisplayManager.AccountsService.xml
%{_datadir}/polkit-1/actions/org.freedesktop.DisplayManager.AccountsService.policy
%dir %{_datadir}/xgreeters/
%ghost %attr(711,lightdm,lightdm) %dir %{rundir}/lightdm/
%attr(750,lightdm,lightdm) %dir %{_localstatedir}/log/lightdm/
%attr(750,lightdm,lightdm) %dir %{_localstatedir}/lib/lightdm/
%attr(750,lightdm,lightdm) %dir %{_localstatedir}/lib/lightdm-data/
%attr(711,root,root) %dir %{_localstatedir}/cache/lightdm/
%{_mandir}/man1/lightdm.1%{?ext_man}
%{_mandir}/man1/dm-tool.1%{?ext_man}
%{_sysusersdir}/lightdm.conf

%files lang -f %{name}.lang

%files -n %{gobject_lib}
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/lib%{gobject_libname}.so.*

%files gobject-devel
%{_libdir}/lib%{gobject_libname}.so
%{_libdir}/pkgconfig/lib%{gobject_libname}.pc
%{_includedir}/%{gobject_libname}/
%{_datadir}/gir-1.0/LightDM-1.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/lib%{gobject_libname}.*
%doc %{_datadir}/gtk-doc/html/%{gobject_libname}/

%files -n %{typelibname}
%{_libdir}/girepository-1.0/LightDM-1.typelib

%if %{build_qt4}
%files -n %{qt4_lib}
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/lib%{qt4_libname}.so.*

%files qt-devel
%{_libdir}/lib%{qt4_libname}.so
%{_libdir}/pkgconfig/lib%{qt4_libname}.pc
%{_includedir}/%{qt4_libname}/
%endif

%files -n %{qt5_lib}
%license COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/lib%{qt5_libname}.so.*

%files qt5-devel
%{_libdir}/lib%{qt5_libname}.so
%{_libdir}/pkgconfig/lib%{qt5_libname}.pc
%{_includedir}/%{qt5_libname}/

%files bash-completion
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/dm-tool
%{_datadir}/bash-completion/completions/lightdm

%changelog
