#
# spec file for package kdelibs4
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


# bypass https://bugzilla.opensuse.org/show_bug.cgi?id=1143249
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

# a hack for building apidoc, currently unused and unneeded (rev.312)
%bcond_with gendoxygen
Name:           kdelibs4
Version:        4.14.38
Release:        0
Summary:        KDE Base Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source0:        kdelibs-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        hidden.desktop
Source3:        ycp.xml
Source4:        kde4rc
Patch1:         default-useragent.diff
Patch2:         add-suse-translations.diff
Patch3:         clever-menu.diff
Patch4:         kdesu-settings.diff
Patch5:         desktop-translations.diff
Patch6:         kjs-mark-register-stack.diff
Patch7:         flash-player-non-oss.diff
Patch8:         plasma-libs.diff
Patch9:         ignore-inline-menu.diff
Patch10:        ksuseinstall.diff
# PATCH-FIX-OPENSUSE exclude-qtuitools-symbols-from-public-libraries.patch -- We are using -Bsymbolic-functions link flags in kde4 macros,
# this patch exlcudes qtuitools symbols from libs that link to qtuitools, as otherwise users of
# those libs are crashing(bnc#819437, kde#303576, kde#231077, qtbug#437)
Patch11:        exclude-qtuitools-symbols-from-public-libraries.patch
# PATCH-FIX-OPENSUSE 0001-Ommit-Solid-s-qDebug-and-qWarning-messages.patch -- we don't need verbosity here
Patch12:        0001-Ommit-Solid-s-qDebug-and-qWarning-messages.patch
# PATCH-FIX-OPENSUSE 0001-Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch -- Nepomuk is only used in a private header, browserrun_p.h,
# thus it is not needed as KParts public dependancy, makes it possible to drop libsoprano-devel from libkde4-devel Requires
Patch15:        0001-Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch
# PATCH-FIX-OPENSUSE gcc6-fix-errors.patch -- Fix errors spotted by GCC6.
Patch17:        gcc6-fix-errors.patch
# PATCH-FIX-OPENSUSE
Patch18:        Skip-qtwebkit-parts.patch
# PATCH-FIX-OPENSUSE
Patch19:        0001-Make-kssl-compile-against-OpenSSL-1.1.0.patch
# PATCH-FIX-OPENSUSE 0001-Fix-the-smbclient-4.9-check.patch -- Fix a CMake test failure in kdebase4-runtime when using Samba 4.9
Patch20:        0001-Fix-the-smbclient-4.9-check.patch
# PATCH-FIX-UPSTREAM
Patch21:        0001-Security-remove-support-for-.-in-config-keys-with-e-.patch
BuildRequires:  OpenEXR-devel
BuildRequires:  automoc4
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.9
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  enchant-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  giflib-devel
BuildRequires:  help2man
#Remove herqq support as this causes frequent crashes (bnc#768368)
#BuildRequires:  herqq-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kde4-filesystem
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libattica-devel >= 0.4.2
BuildRequires:  libattr-devel
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libgssglue-devel
BuildRequires:  libjasper-devel
BuildRequires:  libpolkit-qt-1-devel
BuildRequires:  libqt4-devel >= 4.8.0
BuildRequires:  libudev-devel
BuildRequires:  libxslt-devel
BuildRequires:  pcre-devel
BuildRequires:  phonon-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  utempter-devel
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(bzip2)
Requires:       %{name}-branding = %{_kde_branding_version}
Requires:       kdelibs4-core = %{version}
Requires:       libkde4 = %{version}
Requires:       udisks2
Requires:       libattica0_4 >= %( echo `rpm -q --queryformat '%%{VERSION}' libattica-devel`)
%requires_ge    libqt4-x11
%requires_ge    shared-mime-info
Requires(pre):  permissions
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     media-player-info

%description
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%package branding-upstream
Summary:        KDE Base Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
Supplements:    packageand(kdelibs4:branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{_kde_branding_version}

%description branding-upstream
This package contains the basic packages for a K Desktop Environment
branding.

# KDE	292715 	292723 292725 292764 292765
# kconfig_compiler pending upstream <URL: ?l=kde-doc-english&m=132791095310563&w=2 >
%define kde_auto_man kde4-config kunittestmodrunner meinproc4

%prep
%setup -q -n kdelibs-%{version}
%patch1
%patch2
%patch3 -p1
%patch4
%patch5 -p1
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11 -p1
%patch12 -p1
%patch15 -p1
%patch17
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
  EXTRA_FLAGS="-DLIB_INSTALL_DIR=%{_kde4_libdir} \
        -DCONFIG_INSTALL_DIR=%{_kde4_configdir} \
        -DDATA_INSTALL_DIR=%{_kde4_appsdir} \
        -DKCFG_INSTALL_DIR=%{_kde4_configkcfgdir} \
        -DMIME_INSTALL_DIR=/nogo \
        -DKDE4_ENABLE_FPIE=1 \
        -DTEMPLATES_INSTALL_DIR=%{_kde4_sharedir}/templates \
        -DHTML_INSTALL_DIR=%{_kde4_htmldir} \
        -DWITH_SOLID_UDISKS2=TRUE \
        -DKIO_NO_SOPRANO=ON \
        -DKIO_NO_STRIGI=TRUE \
        -DKDE_DEFAULT_HOME=.kde4 -DSYSCONF_INSTALL_DIR=%{_sysconfdir}"
  %cmake_kde4 -d build -- -DKDE_DISTRIBUTION_TEXT="%{distribution}" $EXTRA_FLAGS
  %make_jobs
  mkdir man1
  for f in %{kde_auto_man}
  do o="man1/$f.1"
# no pipe: abort on fail
  help2man>"$o" "bin/$f.shell"
  gzip "$o"
  done

%install
  %kde4_makeinstall -C build
  chmod +x %{buildroot}%{_kde4_appsdir}/kconf_update/ksslcertificatemanager.upd.sh
  # these unmaintained certs are probably unused anyway, remove them to be sure
  rm -f %{buildroot}%{_kde4_appsdir}/kssl/ca-bundle.crt
  pushd build
  %create_subdir_filelist -d kdecore -v kdecore.devel
  %create_subdir_filelist -d kpty -f kdecore -v kdecore.devel
  install -ma=r '-t%{buildroot}%{_kde4_mandir}/man1/' man1/*.1.gz
  popd
  %create_exclude_filelist
  %if %{with gendoxygen}
  install -p -D doc/api/doxygen.sh %{buildroot}%{_kde4_bindir}/kde4-doxygen.sh
  %endif
  mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
  mv %{buildroot}%{_sysconfdir}/xdg/menus/applications.menu \
     %{buildroot}%{_sysconfdir}/xdg/menus/applications.menu.kde4
  : rm %{buildroot}%{_mandir}/man1/checkXML.1
  mv %{buildroot}%{_mandir}/man7/kdeoptions.7 \
     %{buildroot}%{_mandir}/man7/kde4options.7
  mv %{buildroot}%{_mandir}/man7/qtoptions.7 \
     %{buildroot}%{_mandir}/man7/qt4options.7
  mkdir -p %{buildroot}%{_datadir}/autostart/
  install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/autostart/panel.desktop
  install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/autostart/ktip.desktop
  install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/autostart/kdesktop.desktop
  install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/
  mkdir -p %{buildroot}/%{_kde4_libdir}/kconf_update_bin
  %kde_post_install
  %fdupes -s %{buildroot}

%post
/sbin/ldconfig
%mime_database_post

%set_permissions %{_kde4_libexecdir}/start_kdeinit

%postun
/sbin/ldconfig
%mime_database_postun

%verifyscript
%verify_permissions -e %{_kde4_libexecdir}/start_kdeinit

%package doc
%define regcat %{_bindir}/sgml-register-catalog
Summary:        Documentation for KDE Base Libraries
License:        LGPL-2.1-or-later AND GFDL-1.2-or-later
Group:          System/GUI/KDE
Requires:       sgml-skel
Requires(pre):  %{_bindir}/edit-xml-catalog
Requires(pre):  %{_bindir}/xmlcatalog
Requires(pre):  %{regcat}
Requires(pre):  awk
Requires(pre):  grep
Requires(pre):  sed

%description doc
This package contains the core environment and templates for the KDE
help system.

%files doc
%doc %lang(en) %{_kde4_htmldir}/en/kioslave
%{_kde4_appsdir}/ksgmltools2
%{_kde4_bindir}/meinproc4
%{_kde4_bindir}/meinproc4_simple
%license COPYING.LIB COPYING.DOC
%doc %{_kde4_mandir}/man1/meinproc4.1.gz

%if %{with gendoxygen}
%{_kde4_bindir}/kde4-doxygen.sh
%doc %{_kde4_mandir}/man1/kde4-doxygen.sh.1.gz
%endif

%package -n libkdecore4
Summary:        KDE Core Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
%requires_ge    libqt4

%description -n libkdecore4
This package contains the core libraries of the K Desktop Environment.

This package is absolutely necessary for using KDE applications.

%post -n libkdecore4 -p /sbin/ldconfig
%postun -n libkdecore4 -p /sbin/ldconfig

%files -n libkdecore4
%license COPYING COPYING.DOC COPYING.LIB
%doc README
%{_kde4_libdir}/libkdecore.so.*
%{_kde4_libdir}/libkdefakes.so.*
%{_kde4_libdir}/libkpty.so.*

%package -n kdelibs4-core
Summary:        KDE Base Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
Requires:       kde4-filesystem >= 4.14
Requires:       libkdecore4 = %{version}
%requires_ge    libpolkit-qt-1-1

%description -n kdelibs4-core
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%files -n kdelibs4-core -f filelists/kdecore
%license COPYING.LIB
%{_kde4_configdir}/kdebug.areas
%{_kde4_configdir}/kdebugrc
%config %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.auth.conf
%config %{_kde4_sysconfdir}/kde4rc

%dir %{_kde4_libdir}/kde4
%dir %{_kde4_sharedir}/servicetypes

%exclude %{_datadir}/locale/all_languages
%exclude %{_kde4_bindir}/kconfig_compiler
%exclude %{_kde4_libdir}/libkdecore.so.*
%exclude %{_kde4_libdir}/libkdefakes.so.*
%exclude %{_kde4_libdir}/libkpty.so.*

%doc %{_kde4_mandir}/man1/kde4-config.1.gz

%package -n libkdecore4-devel
Summary:        KDE Core Libraries: Build Environment
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       automoc4
Requires:       cmake
Requires:       kdelibs4-core = %{version}
Requires:       libkdecore4 = %{version}
Requires:       libqt4-devel >= 4.8.0

%description -n libkdecore4-devel
This package contains all necessary include files and libraries needed
to develop non-graphical KDE applications.

%files -n libkdecore4-devel -f filelists/kdecore.devel
%license COPYING.LIB
%doc README
%{_kde4_bindir}/kconfig_compiler
%{_kde4_includedir}/kdemacros.h
%doc %{_kde4_mandir}/man1/kconfig_compiler.1.gz

%package -n libkde4
Summary:        KDE Base Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
%requires_ge    libqt4-x11

%description -n libkde4
This package contains the basic packages of the K Desktop Environment.
It contains the necessary libraries for the KDE desktop.

This package is absolutely necessary for using graphical KDE
applications.

%post -n libkde4 -p /sbin/ldconfig
%postun -n libkde4 -p /sbin/ldconfig

%files branding-upstream
%license COPYING.LIB
%{_kde4_appsdir}/kdeui/about

%files -n libkde4
%license COPYING.LIB
%{_datadir}/locale/all_languages
%{_kde4_libdir}/libkcmutils.so.*
%{_kde4_libdir}/libkde3support.so.*
%{_kde4_libdir}/libkdeclarative.so.*
%{_kde4_libdir}/libkdesu.so.*
%{_kde4_libdir}/libkdeui.so.*
%{_kde4_libdir}/libkdnssd.so.*
%{_kde4_libdir}/libkemoticons.so.*
%{_kde4_libdir}/libkfile.so.*
%{_kde4_libdir}/libkhtml.so.*
%{_kde4_libdir}/libkidletime.so.*
%{_kde4_libdir}/libkimproxy.so.*
%{_kde4_libdir}/libkio.so.*
%{_kde4_libdir}/libkjs.so.*
%{_kde4_libdir}/libkjsapi.so.*
%{_kde4_libdir}/libkjsembed.so.*
%{_kde4_libdir}/libkmediaplayer.so.*
%{_kde4_libdir}/libknewstuff2.so.*
%{_kde4_libdir}/libknewstuff3.so.*
%{_kde4_libdir}/libknotifyconfig.so.*
%{_kde4_libdir}/libkntlm.so.*
%{_kde4_libdir}/libkparts.so.*
%{_kde4_libdir}/libkprintutils.so.*
%{_kde4_libdir}/libkrosscore.so.*
%{_kde4_libdir}/libkrossui.so.*
%{_kde4_libdir}/libktexteditor.so.*
%{_kde4_libdir}/libkunitconversion.so.*
%{_kde4_libdir}/libkunittest.so.*
%{_kde4_libdir}/libkutils.so.*
%{_kde4_libdir}/libplasma.so.*
%{_kde4_libdir}/libsolid.so.*
%{_kde4_libdir}/libthreadweaver.so.*

%package -n libkde4-devel
Summary:        KDE Base Libraries: Build Environment
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       docbook-xsl-stylesheets
Requires:       kdelibs4 = %{version}
Requires:       kdelibs4-doc = %{version}
Requires:       libkde4 = %{version}
Requires:       libkdecore4-devel = %{version}
Requires:       phonon-devel
Requires:       update-desktop-files

%description -n libkde4-devel
This package contains all necessary include files and libraries needed
to develop KDE applications.

%files -n libkde4-devel -f filelists/exclude
%exclude %{_kde4_includedir}/ksuseinstall*
%exclude %{_kde4_includedir}/kdemacros.h
%exclude %{_kde4_libdir}/libkdeinit4_*.so
%exclude %{_kde4_libdir}/libksuseinstall.so

%{_kde4_appsdir}/cmake
%{_kde4_includedir}/*
%{_kde4_libdir}/*.so
%{_kde4_libdir}/cmake
%{_kde4_libdir}/kde4/plugins/script/libkrossqtsplugin.so

%license COPYING.LIB
%doc README

%files -f filelists/exclude
%verify(not mode caps) %attr(4755,root,root) %{_kde4_libexecdir}/start_kdeinit
%{_kde4_configdir}/*
%config %{_kde4_sysconfdir}/xdg/menus/applications.menu.kde4

%dir %{_datadir}/autostart
%dir %{_datadir}/doc/kde
%doc %dir %{_kde4_docdir}/HTML
%doc %dir %{_kde4_htmldir}/en
%doc %dir %{_kde4_htmldir}/en/common
%dir %{_kde4_libdir}/kconf_update_bin
%dir %{_kde4_libdir}/kde4
%dir %{_kde4_sharedir}/servicetypes
%dir %{_kde4_sysconfdir}/xdg/menus

%doc %lang(en) %{_kde4_htmldir}/en/sonnet

%exclude %{_kde4_appsdir}/cmake
%exclude %{_kde4_appsdir}/kdeui/about
%exclude %{_kde4_appsdir}/ksgmltools2
%exclude %{_kde4_bindir}/meinproc4
%exclude %{_kde4_bindir}/meinproc4_simple
%exclude %{_kde4_libdir}/kde4/plugins/script/libkrossqtsplugin.so

%{_datadir}/autostart/kdesktop.desktop
%{_datadir}/autostart/ktip.desktop
%{_datadir}/autostart/panel.desktop
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/mime/packages/kde.xml

%{_kde4_applicationsdir}/kmailservice.desktop
%{_kde4_applicationsdir}/ktelnetservice.desktop
%{_kde4_appsdir}/*
%{_kde4_bindir}/*
%doc %{_kde4_htmldir}/en/common/*
%{_kde4_iconsdir}/hicolor/*/actions/presence_away.*
%{_kde4_iconsdir}/hicolor/*/actions/presence_offline.*
%{_kde4_iconsdir}/hicolor/*/actions/presence_online.*
%{_kde4_iconsdir}/hicolor/*/actions/presence_unknown.*
%{_kde4_libdir}/libkdeinit4_*.so

%doc %{_kde4_mandir}/man*/*
%exclude %{_kde4_mandir}/man1/kde4-config.1.gz
%exclude %{_kde4_mandir}/man1/meinproc4.1.gz
%exclude %{_kde4_mandir}/man1/kconfig_compiler.1.gz

%{_kde4_modulesdir}/*
%{_kde4_servicesdir}/*
%{_kde4_servicetypesdir}/*
%{_kde4_sysconfdir}/xdg/menus/applications.menu.kde4

%if %{with gendoxygen}
%exclude %{_kde4_mandir}/man1/kde4-doxygen.sh.1.gz
%exclude %{_kde4_bindir}/kde4-doxygen.sh
%endif

# IMPORTANT: When this is obsolete, do not just remove this, but create
# a separate package (for backwards compatibility).

%package -n libksuseinstall1
Summary:        On-demand installation of packages
License:        MIT
Group:          Development/Libraries/KDE
Requires:       yast2-packager >= 2.19.7
Requires:       zypper
%requires_ge    libqt4-x11
Recommends:     ptools

%description -n libksuseinstall1
This library implements private API to install additional packages for KDE.

%package -n libksuseinstall-devel
Summary:        On-demand installation of packages
License:        MIT
Group:          Development/Libraries/KDE
Requires:       libkde4-devel
Requires:       libksuseinstall1 = %{version}

%description -n libksuseinstall-devel
This library implements private API to install additional packages for KDE.

%post -n libksuseinstall1 -p /sbin/ldconfig
%postun -n libksuseinstall1 -p /sbin/ldconfig

%files -n libksuseinstall1
%{_kde4_libdir}/libksuseinstall.so.*

%files -n libksuseinstall-devel
%{_kde4_includedir}/ksuseinstall.h
%{_kde4_includedir}/ksuseinstall_export.h
%{_kde4_libdir}/libksuseinstall.so

%changelog
