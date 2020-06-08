#
# spec file for package gcin
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


%define build_qt4 0%{?is_opensuse} && 0%{?suse_version} < 1550

Name:           gcin
Version:        2.9.0
Release:        0
Summary:        Chinese input method server
License:        LGPL-2.1-only
Group:          System/I18n/Chinese
URL:            http://hyperrate.com/dir.php?eid=67
Source:         http://hyperrate.com/gcin-source/%{name}-%{version}.tar.xz
Source1:        xim.d-gcin
Source2:        gcin-README.suse
Source3:        xim.gcin.suse.template
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM glin@suse.com - just install the _only_ icon to pixmaps
Patch1:         icon_path.diff
# PATCH-FIX-UPSTREAM swyear@opensuse.org - fix qt3 detection in configure
Patch2:         gcin-libdir.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix gtk2/3 immodules install path
Patch3:         gcin-2.8.1-gtk_immodules_path.patch
# PATCH-FIX-UPSTREAM swyear@opensuse.org - fix doc path (used to open doc from gcin-tools)
Patch4:         doc_dir.diff
# PATCH-FIX-UPSTREAM glin@suse.com - keep the debug symbols
Patch5:         gcin-keep-debug-symbols.patch
# PATCH-FIX-UPSTREAM glin@suse.com - fix the Makefile dependency for parallel compiling
Patch7:         gcin-parallel-compiling.patch
# PATCH-FIX-OPENSUSE mlin@suse.com - improve build with pkgconfig and add private headers at moc period
Patch8:         gcin-improve-build-with-pkgconfig.patch
# PATCH-FIX-UPSTREAM boo#951750 glin@suse.com - fix the qt5 iid
Patch9:         gcin-fix-qt5-iid.patch
# PATCH-FIX-OPENSUSE glin@suse.com - Don't copy gcin-qt5.h.in since we already patched gcin-qt5.h
Patch10:        gcin-dont-copy-gcin-qt5-header.patch
# PATCH-FIX-UPSTREAM gcin-remove-dead-code.patch - remove the dead code to avoid the warning
Patch11:        gcin-remove-dead-code.patch
BuildRequires:  anthy-devel
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-devel-static
BuildRequires:  libXtst-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
%if %{build_qt4}
BuildRequires:  libqt4-devel
%endif
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  xz
Requires:       %{name}-branding
Requires:       %{name}-gtk2 = %{version}
Requires:       %{name}-gtk3 = %{version}
%if %{build_qt4}
Requires:       %{name}-qt4 = %{version}
%endif
Requires:       %{name}-qt5 = %{version}
Requires:       libgcin-im-client1 = %{version}
Recommends:     libreoffice-gnome
Provides:       locale(zh_TW;zh_HK;zh_MO)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
gcin is a Chinese input method server for traditional Chinese.
It features a better GTK user interface.

%package branding-upstream
Summary:        Upstream branding of gcin
License:        LGPL-2.1-only
Group:          System/I18n/Chinese
Requires:       gcin = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}

%description branding-upstream
This package provides upstream look and feel for gcin

%package -n libgcin-im-client1
Summary:        Share libraries of gcin
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n libgcin-im-client1
This package provides runtime libraries for gcin.

%package gtk2
Summary:        Gcin gtk2 immodule
License:        LGPL-2.1-only
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       %{name}-gtk2-immodule = %{version}
Obsoletes:      %{name}-gtk2-immodule <= 2.8.4-77.16
%{gtk2_immodule_requires}

%description gtk2
gcin gtk2 immodule, support gtk2-based applications

%if %{build_qt4}
%package qt4
Summary:        Gcin qt4 immodule
License:        GPL-2.0-only
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       %{name}-qt4-immodule = %{version}
Obsoletes:      %{name}-qt4-immodule <= 2.8.4-77.16

%description qt4
gcin qt4 immodule, support Qt4-based applications
%endif

%package qt5
Summary:        Gcin qt5 immodule
License:        GPL-2.0-only
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       %{name}-qt5-immodule = %{version}
Obsoletes:      %{name}-qt5-immodule <= 2.8.4-77.16

%description qt5
gcin qt5 immodule, support Qt5-based applications

%package anthy
Summary:        Gcin anthy module
License:        LGPL-2.1-only
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
Provides:       %{name}-anthy-module = %{version}
Obsoletes:      %{name}-anthy-module <= 2.8.4-77.16

%description anthy
gcin anthy module, try this to input Japanese with libanthy

%package gtk3
Summary:        Gcin gtk3 immodule
License:        LGPL-2.1-only
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Provides:       %{name}-gtk3-immodule = %{version}
Obsoletes:      %{name}-gtk3-immodule <= 2.8.4-77.16
%{gtk3_immodule_requires}

%description gtk3
gcin gtk3 immodule, support gtk3-based applications

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
cp -r %{SOURCE2} .
cp -r %{SOURCE3} .

# scripts/modify-XIM is mainly for Fedora/Mandriva and Qt3, obsoleted
rm -rf scripts/modify-XIM
sed -i "s/modify-XIM//" scripts/Makefile

%build
%if %{_lib} == lib64
sed -e "s,^LIB='lib',LIB=lib64," -i configure
%endif
CFLAGS="%{optflags}" %configure --prefix=/usr --use_i18n=Y \
--use_anthy=Y --doc_version_dir=N

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xim.d/gcin

rm -rf %{buildroot}%{_datadir}/doc

%suse_update_desktop_file -r -G "Set Up your inputmethod" gcin-tools Settings System SystemSetup

PRIORITY=30
pushd  %{buildroot}%{_sysconfdir}/X11/xim.d/
    for lang in en zh_TW zh_HK zh_MO ; do
        mkdir $lang
  pushd $lang
            ln -s ../gcin $PRIORITY-gcin
  popd
    done
popd

%find_lang %{name}
%fdupes %{buildroot}

%post -n libgcin-im-client1 -p /sbin/ldconfig

%postun -n libgcin-im-client1 -p /sbin/ldconfig

%post anthy -p /sbin/ldconfig

%postun anthy -p /sbin/ldconfig

%post gtk2
/sbin/ldconfig
%{gtk2_immodule_post}

%postun gtk2
/sbin/ldconfig
%{gtk2_immodule_postun}

%post gtk3
/sbin/ldconfig
#Add icons to gnome3 panel
TARGET="%{_datadir}/gnome-shell/js/ui/statusIconDispatcher.js"
if [ -f $TARGET ] ; then
 if [ -z "`grep gcin $TARGET`" ] ; then
   mv $TARGET $TARGET-gcin
   # add gcin string to the file
   sed "/^const STANDARD_TRAY_ICON_IMPLEMENTATIONS/a \    'gcin': 'input-method'," $TARGET-gcin > $TARGET
 fi
fi

%{gtk3_immodule_post}

%postun gtk3
/sbin/ldconfig
%{gtk3_immodule_postun}

%if %{build_qt4}
%post qt4 -p /sbin/ldconfig
%postun qt4 -p /sbin/ldconfig
%endif
%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%license COPYING
%doc README.html Changelog.html AUTHORS gcin-README.suse xim.gcin.suse.template
%config %{_sysconfdir}/X11/xim.d/
%{_bindir}/*
%{_datadir}/gcin/
%{_datadir}/pixmaps/gcin.png
%{_datadir}/applications/*
%dir %{_datadir}/icons/gcin/

%files -n libgcin-im-client1
%defattr(-,root,root)
%dir %{_libdir}/gcin
%{_libdir}/gcin/libgcin-im-client.so
%{_libdir}/gcin/libgcin-im-client.so.1
%{_libdir}/gcin/libgcin-im-client.so.1.2.5
%{_libdir}/gcin/gcin1.so
%{_libdir}/gcin/gcin2.so
%{_libdir}/gcin/intcode-module.so

%files branding-upstream
%defattr(-,root,root)
%{_datadir}/icons/gcin/*

%files gtk2
%defattr(-,root,root)
%{_libdir}/gtk-2.0/2.10.0/immodules/im-gcin.so

%if %{build_qt4}
%files qt4
%defattr(-,root,root)
%{_libdir}/qt4/plugins/inputmethods/im-gcin.so
%endif

%files qt5
%defattr(-,root,root)
%{_libdir}/qt5/plugins/platforminputcontexts/libgcinplatforminputcontextplugin.so

%files anthy
%defattr(-,root,root)
%{_libdir}/gcin/anthy-module.so

%files gtk3
%defattr(-,root,root)
%{_libdir}/gtk-3.0/3.0.0/immodules/im-gcin.so

%changelog
