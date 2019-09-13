#
# spec file for package gnome-keyring
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


Name:           gnome-keyring
Version:        3.31.91
Release:        0
Summary:        GNOME Keyring
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
Url:            https://wiki.gnome.org/Projects/GnomeKeyring
Source0:        https://download.gnome.org/sources/gnome-keyring/3.31/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-OPENSUSE gnome-keyring-pam-auth-prompt-password.patch bnc#466732 bgo#560488 vuntz@novell.com -- Make the pam module prompt the password in auth, so we can use pam-config. This is a workaround until bnc#477488 is implemented.
Patch0:         gnome-keyring-pam-auth-prompt-password.patch
# PATCH-FEATURE-UPSTREAM gnome-keyring-bsc1039461-pam-man-page.patch bsc#1039461 bgo#784051 hpj@suse.com -- Add a man page for the PAM module
Patch1:         gnome-keyring-bsc1039461-pam-man-page.patch
## NOTE: Keep SLE-only patches at bottom (starting on 1000).
# PATCH-FIX-SLE gnome-keyring-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com
Patch1000:      gnome-keyring-bsc932232-use-libgcrypt-allocators.patch
# PATCH-FIX-SLE gnome-keyring-bsc932232-use-non-fips-md5.patch bsc#932232 hpj@suse.com
Patch1001:      gnome-keyring-bsc932232-use-non-fips-md5.patch

BuildRequires:  automake
BuildRequires:  ca-certificates
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  libcap-ng-devel
BuildRequires:  libgcrypt-devel >= 1.2.2
BuildRequires:  libselinux-devel
BuildRequires:  openssh
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gck-1) >= 3.3.4
BuildRequires:  pkgconfig(gcr-3) >= 3.27.90
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
Requires:       libgck-modules-gnome-keyring = %{version}
Recommends:     %{name}-lang
Recommends:     %{name}-pam
Provides:       dbus(org.freedesktop.secrets)
Provides:       dbus(org.gnome.keyring)
%if 0%{?BUILD_FROM_VCS}
BuildRequires:  gnome-common
%endif
#

%description
The GNOME Keyring is a daemon in the session, similar to ssh-agent,
and other applications can use it to store passwords and other
sensitive information.

The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package -n libgck-modules-gnome-keyring
Summary:        Glib wrapper library for PKCS#11 - Modules
# libgck-X-Y has a Provides for gck, just to help us with this Requires
Group:          System/GUI/GNOME
Requires:       gck
# libgp11 used to be the library providing all this. It turns out the
# modules are, as of 2.91.3, installed in the same place
Obsoletes:      libgp11-modules < %{version}
# starting with 3.3, libgck got split from gnome-keyring and so we can't use a
# generic name like libgck-modules anymore.
Obsoletes:      libgck-modules < %{version}

%description -n libgck-modules-gnome-keyring
GCK is a wrapper based on GLib implementing the PKCS#11 (Cryptoki)
interface.

This package contains various PKCS#11 modules, to expose keys and
certificates from different sources.

%package pam
Summary:        GNOME Keyring - PAM module
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         pam-config >= 0.72
PreReq:         sed
# Package was present in OpenSUSE 10.2 and 10.3:
Provides:       pam_keyring = 0.0.8
Obsoletes:      pam_keyring < 0.0.8

%description pam
The GNOME Keyring is a daemon in the session, similar to ssh-agent,
and other applications can use it to store passwords and other
sensitive information.

The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

The PAM module can be used to unlock the keyring on login.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if !0%{?is_opensuse}
%patch1000 -p1
%patch1001 -p1
%endif
translation-update-upstream

%build
autoreconf -f
%configure\
        --enable-pam \
        --with-pam-dir=/%{_lib}/security
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# XFCE team wants gnome-keyring to work by default.
for i in %{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop ; do
 desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart --add-only-show-in=XFCE $i
done
%find_lang %{name}
%suse_update_desktop_file gnome-keyring-pkcs11
%suse_update_desktop_file gnome-keyring-secrets
%suse_update_desktop_file gnome-keyring-ssh
%fdupes %{buildroot}%{_datadir}

###
# WARNING: when changing the pam-config calls in the scriptlets, please also
# update them in baselibs.conf.
# pam-config checks if the pam module is available for 32bit too if pam-32bit
# is installed, so the call here might fail until gnome-keyring-pam-32bit gets
# installed (see bnc#728586).
###

%post pam
%{_sbindir}/pam-config -a --gnome_keyring --gnome_keyring-auto_start --gnome_keyring-only_if=gdm,gdm-password,lxdm,lightdm,mdm,sddm || true
# Remove leftover from the old way, before we used pam-config. We start
# cleaning up in 11.2, so this can be removed in 12.2.
# Note: this can safely be done after pam-config, since pam-config doesn't
# touch /etc/pam.d/gdm
if test -f etc/pam.d/gdm; then
if grep -F -q pam_gnome_keyring.so etc/pam.d/gdm ; then
  sed -i '/ pam_gnome_keyring\.so/d' etc/pam.d/gdm
fi
fi

%postun pam
if [ "$1" = "0" ]; then
  %{_sbindir}/pam-config -d --gnome_keyring || true
fi

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gnome-keyring
%{_bindir}/gnome-keyring-3
%{_bindir}/gnome-keyring-daemon
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/gnome-keyring-pkcs11.so
%{_datadir}/dbus-1/services/org.freedesktop.secrets.service
%{_datadir}/dbus-1/services/org.gnome.keyring.service
%{_datadir}/p11-kit/modules/gnome-keyring.module
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.crypto.cache.convert
%{_datadir}/glib-2.0/schemas/org.gnome.crypto.cache.gschema.xml
%{_sysconfdir}/xdg/autostart/*.desktop
%{_mandir}/man1/gnome-keyring.1%{?ext_man}
%{_mandir}/man1/gnome-keyring-3.1%{?ext_man}
%{_mandir}/man1/gnome-keyring-daemon.1%{?ext_man}

%files -n libgck-modules-gnome-keyring
# Note: if modules move to %%{_libdir}/pkcs11, then we should remove
# the libgp11-modules Obsoletes tag.
%dir %{_libdir}/gnome-keyring
%dir %{_libdir}/gnome-keyring/devel
%{_libdir}/gnome-keyring/devel/gkm-gnome2-store-standalone.so
%{_libdir}/gnome-keyring/devel/gkm-secret-store-standalone.so
%{_libdir}/gnome-keyring/devel/gkm-ssh-store-standalone.so
%{_libdir}/gnome-keyring/devel/gkm-xdg-store-standalone.so

%files pam
%attr(555,root,root) /%{_lib}/security/*.so
%{_mandir}/man8/pam_gnome_keyring.8%{?ext_man}

%files lang -f %{name}.lang

%changelog
