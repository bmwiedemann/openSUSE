#
# spec file for package enlightenment
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define efl_version	1.18.0
%define systemd_present (0%{?suse_version} >= 1230 || 0%{?fedora} >= 18)
%define enable_wayland (0%{?suse_version} > 1320)
%define generate_manpages 0
Name:           enlightenment
Version:        0.22.4
Release:        0
Summary:        The window manager
License:        BSD-2-Clause
Group:          System/X11/Displaymanagers
Url:            http://enlightenment.org/
Source:         http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Source2:        enlightenment.pam
# PATCH-FEATURE_OPENSUSE feature-network-manager-wizard.patch simon@simotek.net adds nm-applet to startup apps if its present,
# this will be maybe upstreamed when upstream network manager applet supports app indicator - (1.1.0)
Source3:        network_manager_wizard.c
# PATCH-FIX-OPENSUSE - enlightenment-0.16.999.65256-dont_require_suidbit.patch sleep_walker@opensuse.org -- upstream insist on having suidbit
Patch0:         enlightenment-0.16.999.65256-dont_require_suidbit.patch
# PATCH-FEATURE-OPENSUSE dont_offer_updates.patch -- don't offer updates, that's up to package manager -- sleep_walker@opensuse.org
Patch1:         dont_offer_updates.patch
# PATCH-FEATURE-OPENSUSE as we use Network Manager rather then connman offline mode doesn't do anything so Hide the menu option
Patch2:         feature-suse-disable-offline-menu.patch
# boo#1003939 don't ask for language if we can use the current system one
Patch3:         feature-wizard-auto-lang.patch
Patch4:         feature-wizard-keylayout-from-sys.patch
Patch5:         feature-qt-apps-gtk2-theme.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  edje >= %{efl_version}
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# configure scripts looks for Xwayland binary
%if %{enable_wayland}
BuildRequires:  xorg-x11-server-wayland
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ecore) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-con) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-evas) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-file) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-ipc) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-x) >= %{efl_version}
BuildRequires:  pkgconfig(eet) >= %{efl_version}
BuildRequires:  pkgconfig(efreet) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-mime) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-trash) >= %{efl_version}
BuildRequires:  pkgconfig(eina) >= %{efl_version}
BuildRequires:  pkgconfig(eio) >= %{efl_version}
BuildRequires:  pkgconfig(eldbus) >= %{efl_version}
BuildRequires:  pkgconfig(elementary) >= %{efl_version}
BuildRequires:  pkgconfig(emotion) >= %{efl_version}
BuildRequires:  pkgconfig(evas) >= %{efl_version}
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
# you'll need dbus-1 for default actions set in sysactions.conf
Requires:       dbus-1
Requires:       edje
Requires:       efl
Requires:       elementary
Requires:       enlightenment-branding = 0.1
Requires:       evas-generic-loaders
# Require a Icon theme that will be detected by enlghtenment
Requires:       oxygen-icon-theme
# We use xdg-terminal, xdg-open and xdg-su in various places
Requires:       xdg-utils
Conflicts:      e17 > 0.17.3
# lets not have users complain about theme incompat
Conflicts:      e17-theme
Provides:       e_module-notification = 0.2.1
Obsoletes:      e_module-notification < 0.2.1
# Obsolete 12.3 and 13.1 users using e17.0 and e17.3 but not 13.2 users using e17.6 as they will
# have chosen e17 over e18 and later manually
# according to DimStar, obsoleting all will allow a smooth upgrade, only providing 0.17.4 or less will mean that
# older e17.3 users will update but anyone who manually installs e17.6 will stay
Obsoletes:      e17
Provides:       e17 > 0.17.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
%if %{enable_wayland}
BuildRequires:  pkgconfig(ecore-wl2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
%endif
%if %{systemd_present}
BuildRequires:  systemd-devel
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
%if 0%{?fedora} >= 18
Requires:       systemd
%endif
%if 0%{?suse_version}
Recommends:     NetworkManager-appindicator
Recommends:     alsa-plugins-pulse
# Recommended to make NetworkManager Intergration work
Recommends:     gnome-keyring
# Recommended to make audio work out of the box boo#972912
Recommends:     pulseaudio
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-jack
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
# Recommend sni-qt to make Qt4/kde4 apps work with systray
Recommends:     sni-qt
# to have working automounting we need udisks
Recommends:     udisks
%endif

%description
Enlightenment window manager and desktop environment is really fast, configurable and beautiful.
This package will provide the latest released version of enlightenment, as opposed to e16 or e17.

%package devel
Summary:        Enightenment development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       efl-devel
Requires:       elementary-devel
Requires:       freetype2-devel >= 2.1.7
Requires:       pam-devel
Requires:       pkgconfig
Requires:       xorg-x11-libXext-devel
Requires:       pkgconfig(dbus-1)
Conflicts:      e17-devel > 0.17.3
Obsoletes:      e17-devel < 0.17.3
Provides:       e17-devel = 0.17.3

%description devel
Development files of Enlightenment package.

%package branding-upstream
Summary:        Enlightenment files for upstream branding
# this uses elementary version number not enlightenment
Group:          System/GUI/Other
Requires:       enlightenment-theme-upstream
Conflicts:      terminology-theme-openSUSE
Provides:       enlightenment-branding = 0.1
%if 0%{?suse_version}
Supplements:    packageand(enlightenment:branding-upstream)
Conflicts:      otherproviders(e17-branding)
Conflicts:      otherproviders(enlightenment-branding)
%endif

%description branding-upstream
Various files for Enlightenment provided by upstream but altered by openSUSE or Petite Linux.

%package doc-html
Summary:        HTML documentation of Enlightenment
Group:          Documentation/HTML
Conflicts:      e17-doc-html

%description doc-html
Documentation of Enlightenment in form of HTML pages.

%if %{generate_manpages}
%package doc-man
Summary:        Man documentation of Enlightenment
Group:          Documentation/Man

%description doc-man
Documentation of Enlightenment in form of man pages.
%endif

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Copy In new Network Wizard
rm src/modules/wizard/page_110.c
cp -v %{SOURCE3} src/modules/wizard/page_110.c

%build
# fake time used for documentation
FAKE_DOCDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y')
FAKE_DOCYEAR=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%Y')
FAKE_DOCDATETIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y %{T}')
sed -i "s/\$datetime/$FAKE_DOCDATETIME/g;s/\$date/$FAKE_DOCDATE/g;s/\$year/$FAKEDOCYEAR/g" doc/*.html

%configure \
%if %{enable_wayland}
	   --enable-wayland \
	   --enable-wayland-egl \
	   --enable-xwayland \
	   --enable-wl-desktop-shell \
	   --enable-wl-x11 \
	   --enable-wl-fb \
	   --enable-wl-drm \
	   --enable-wl-text-input \
	   --disable-wl-weekeyboard \
%endif
	   --disable-static \
	   --disable-silent-rules
make %{?_smp_mflags}
make %{?_smp_mflags} doc

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%if %{enable_wayland}
%if 0%{?suse_version} >= 1550
# gdm doesn't show 2 desktop files with the same name
rm %{buildroot}%{_datadir}/wayland-sessions/enlightenment.desktop
cp %{buildroot}%{_datadir}/xsessions/enlightenment.desktop \
 %{buildroot}%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%else
# for now don't ship a desktop file for Leap - wayland is not stably tested
rm %{buildroot}%{_datadir}/wayland-sessions/enlightenment.desktop
%endif
%endif

# copy documentation manually
echo "Copying HTML documentation"
mkdir -p %{buildroot}%{_docdir}/%{name}
/bin/cp -vr doc/html %{buildroot}%{_docdir}/%{name}

%if %{generate_manpages}
echo "Copying MAN pages"
/bin/cp -vr doc/man/ %{buildroot}%{_mandir}/
%endif

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang enlightenment
%if 0%{?suse_version}
# remove setuid bits, enlightenment_backlight requires eeze-devel, which is not available for SLE
# enlightenment_ckpasswd only needs suid bit on bsd's
chmod -s %{buildroot}%{_libdir}/enlightenment/utils/enlightenment_backlight \
		 %{buildroot}%{_libdir}/enlightenment/utils/enlightenment_ckpasswd \
		 %{buildroot}%{_libdir}/enlightenment/utils/enlightenment_sys \
		 %{buildroot}%{_libdir}/enlightenment/modules/sysinfo/*/cpuclock_sysfs \
         %{buildroot}%{_libdir}/enlightenment/modules/cpufreq/*/freqset
%endif

# copy PAM profile
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/enlightenment

%if 0%{?suse_version}
%suse_update_desktop_file -r -G mixer emixer "AudioVideo;Mixer;"
%if 0%{?suse_version} >= 1550
%suse_update_desktop_file -N "Unstable: Enlightenment (Wayland)" -G "Unstable: Enlightenment (Wayland)"  %{buildroot}%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif
# fdupes needs to be called after desktop files have been made unique
%fdupes -s %{buildroot}
%endif

# Remove unwanted wizard pages
# /usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-ver-autocannoli-0.20/page_010.so

# Remove language / keyboard pages
# rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_011.so
# Remove connman page
rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_110.so
# Don't remove Updates 170 (We have a patch to ensure its disabled)
# Remove tasks page, with our profile its not needed
rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_180.so

# remove files from not wanted place
rm %{buildroot}%{_datadir}/enlightenment/{COPYING,AUTHORS}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/enlightenment.desktop 20

%postun
if [ ! -f %{_datadir}/xsessions/enlightenment.desktop ] ; then
  %{_sbindir}/update-alternatives  --remove default-xsession.desktop %{_datadir}/xsessions/enlightenment.desktop
fi

%files -f enlightenment.lang
%defattr(-,root,root)
%doc COPYING README AUTHORS
%exclude %{_docdir}/%{name}/html
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/xsessions/default.desktop
%if %{enable_wayland} && 0%{?suse_version} >= 1550
# This should be owned by something else
%{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_datadir}/enlightenment/
%{_datadir}/applications/*.desktop
%{_libdir}/enlightenment
%config(noreplace) %{_sysconfdir}/enlightenment
%config(noreplace) %{_sysconfdir}/pam.d/enlightenment
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/e-applications.menu
%{_bindir}/enlightenment*
%{_bindir}/emixer
%{_datadir}/pixmaps/emixer.png
%{_datadir}/pixmaps/enlightenment-askpass.png

%if %{systemd_present}
%{_prefix}/lib/systemd/user/enlightenment.service
%endif
# excluded to be branded
%exclude %{_libdir}/enlightenment/modules/wizard/def-ibar.txt

%files branding-upstream
%defattr(-, root, root)
%{_libdir}/enlightenment/modules/wizard/def-ibar.txt

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/enlightenment

%files doc-html
%defattr(-, root, root)
%{_docdir}/%{name}
%if 0%{?centos_version} || 0%{?fedora_version} == 16
%exclude %{_docdir}/%{name}-%{version}/COPYING
%exclude %{_docdir}/%{name}-%{version}/README
%exclude %{_docdir}/%{name}-%{version}/AUTHORS
%else
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/README
%exclude %{_docdir}/%{name}/AUTHORS
%endif

%if %{generate_manpages}
%files doc-man
%defattr(-, root, root)
%{_mandir}/*/*
%endif

%changelog
