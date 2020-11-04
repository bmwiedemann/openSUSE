#
# spec file for package scim
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


Name:           scim
Version:        1.4.18
Release:        0
Summary:        Smart Chinese/Common Input Method platform
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/scim-im/scim
Source:         %{name}-%{version}.tar.xz
Source1:        xim.d-scim
Source2:        scim.config
Source3:        macros.scim
Source99:       baselibs.conf
Patch1:         configs.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  x11-tools
BuildRequires:  xz
%if 0%{?suse_version} <= 1500
BuildRequires:  libqt4-devel
%endif
Requires:       scim-gtk = %{version}
Recommends:     scim-lang = %{version}
%if 0%{?suse_version} <= 1500
Requires:       scim-qt4 = %{version}
%endif
# not SLE_12
%if 0%{?suse_version} >= 1310 && 0%{?suse_version} != 1315
BuildRequires:  libpng-tools
%endif
%if 0%{?suse_version} > 1130
BuildRequires:  gtk3-devel
Requires:       scim-gtk3 = %{version}
%endif

%description
SCIM is a developing platform to significantly reduce the difficulty of
input method development.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package gtk
Summary:        SCIM im module for gtk2
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Supplements:    packageand(scim:gtk2)
%if 0%{?sles_version} && 0%{?suse_version} != 1315
Requires(post): gtk2
Requires(postun): gtk2
%else
%{gtk2_immodule_requires}
%endif

%description gtk
This package contains SCIM im module for gtk2

%if 0%{?suse_version} > 1130
%package gtk3
Summary:        SCIM im module for gtk3
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Supplements:    packageand(scim:gtk3)
%{gtk3_immodule_requires}

%description gtk3
This package contains SCIM im module for gtk3
%endif

%if 0%{?suse_version} <= 1500
%package qt4
Summary:        SCIM im module for qt4
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}
Supplements:    packageand(scim:libqt4)

%description qt4
This package contains SCIM im module for qt4
%endif

%lang_package

%prep
%setup -q
%patch1 -p1
UTF_8_LOCALES=$(locale -a | grep utf8 | perl -p -e "s/utf8/UTF-8/; s/\n/,/; " | perl -p -e "s/,$//")
perl -pi -e "s/\/SupportedUnicodeLocales =.*/\/SupportedUnicodeLocales = $UTF_8_LOCALES/"  configs/global
# hack to fix incompatibility of gtk-query-immodules-2.0 (bnc#845860)
%if 0%{?suse_version} < 1310
sed -i \
    -e's@\(gtk-query-immodules-2.0-64\) --update-cache@\1 > <prefix>%{_sysconfdir}/gtk-2.0/gtk64.immodules@g' \
    -e's@\(gtk-query-immodules-2.0\) --update-cache@\1 > <prefix>%{_sysconfdir}/gtk-2.0/gtk.immodules@g' \
    %{_sourcedir}/baselibs.conf
%endif

%build
./bootstrap
%configure\
	--libexecdir=%{_libexecdir}/scim-1.0\
%if 0%{?suse_version} > 1130
        --with-gtk3-im-module-dir=%{_libdir}/gtk-3.0/3.0.0/immodules\
        --with-gtk-version=3\
%endif
	--enable-gtk2-immodule\
%if 0%{?suse_version} <= 1500
        --enable-qt4-immodule\
%endif
	--disable-static\
	--enable-debug\
	--enable-ld-version-script
make %{?_smp_mflags} top_builddir=$(pwd)
# build documentation:
make %{?_smp_mflags} -C docs html

%install
make DESTDIR=%{buildroot} top_builddir=$(pwd) install
find %{buildroot} -type f -name "*.la" -delete -print

# install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xim.d/scim

# install symlinks in /etc/X11/xim.d/$lang for all languages
# where SCIM might be useful:
PRIORITY=50
pushd %{buildroot}%{_sysconfdir}/X11/xim.d/
    for lang in am ar as bn el fa gu he hi hr ja ka kk kn ko lo ml my \
		pa ru sk vi zh_TW zh_CN zh_HK zh_SG \
		de fr it es nl cs pl da nn nb fi en sv
    do
        mkdir $lang
	pushd $lang
            ln -s ../scim $PRIORITY-scim
	popd
    done
popd

install -m 755 %{SOURCE2} %{buildroot}%{_datadir}/scim
%find_lang scim
%suse_update_desktop_file scim-setup System SystemSetup

# own _scim_tabledir
install -d %{buildroot}%{_datadir}/scim/tables

# install macro.scim
mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rpm/

# not SLE_12
%if 0%{?suse_version} >= 1310 && 0%{?suse_version} != 1315
%png_fix %{buildroot}%{_datadir}/%{name}/icons/menu.png
%endif

%fdupes %{buildroot}

%post
/sbin/ldconfig
# Update KeyboardLayout
%{_datadir}/scim/scim.config

%postun -p /sbin/ldconfig
%post gtk
/sbin/ldconfig
%if 0%{?sles_version} && 0%{?suse_version} != 1315
%if "%{_lib}" == "lib64"
	%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk-2.0/gtk64.immodules
%else
	%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif
%else
%{gtk2_immodule_post}
%endif

%postun gtk
/sbin/ldconfig
%if 0%{?sles_version} && 0%{?suse_version} != 1315
if [ $1 -eq 0 ] ; then
%if "%{_lib}" == "lib64"
	%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk-2.0/gtk64.immodules
%else
	%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif
fi
%else
%{gtk2_immodule_postun}
%endif

%if 0%{?suse_version} > 1130
%post gtk3
#Add icons to gnome3 panel
TARGET="%{_datadir}/gnome-shell/js/ui/statusIconDispatcher.js"
if [ -f $TARGET ] && [ ! -f $TARGET-scim ] ; then
mv $TARGET $TARGET-scim
sed "/^const STANDARD_TRAY_ICON_IMPLEMENTATIONS/a \    'scim-panel-gtk': 'input-method'," $TARGET-scim > $TARGET
fi
%{gtk3_immodule_post}

%postun gtk3
/sbin/ldconfig
%{gtk3_immodule_postun}
%endif

%files
%license COPYING
%doc AUTHORS README ChangeLog TODO
%config %{_sysconfdir}/X11/xim.d/*
%config %{_sysconfdir}/rpm/macros.scim
%dir %{_sysconfdir}/scim
%config %{_sysconfdir}/scim/config
%config %{_sysconfdir}/scim/global
%{_bindir}/scim
%{_bindir}/scim-config-agent
%{_bindir}/scim-im-agent
%{_bindir}/scim-setup
%{_libdir}/scim-1.0/scim-helper-launcher
%{_libdir}/scim-1.0/scim-helper-manager
%{_libdir}/scim-1.0/scim-launcher
%{_libdir}/scim-1.0/scim-panel-gtk
%{_datadir}/scim
%dir %{_datadir}/scim/tables
%{_datadir}/pixmaps/scim-setup.png
%{_datadir}/applications/scim-setup.desktop
%{_datadir}/control-center-2.0
%{_libdir}/libscim-1.0.so.8
%{_libdir}/libscim-1.0.so.8.2.6
%{_libdir}/libscim-gtkutils-1.0.so.8
%{_libdir}/libscim-gtkutils-1.0.so.8.2.6
%{_libdir}/libscim-x11utils-1.0.so.8
%{_libdir}/libscim-x11utils-1.0.so.8.2.6
%dir %{_libdir}/scim-1.0
%dir %{_libdir}/scim-1.0/1.4.0
%dir %{_libdir}/scim-1.0/1.4.0/Config
%dir %{_libdir}/scim-1.0/1.4.0/Filter
%dir %{_libdir}/scim-1.0/1.4.0/FrontEnd
%dir %{_libdir}/scim-1.0/1.4.0/Helper
%dir %{_libdir}/scim-1.0/1.4.0/IMEngine
%dir %{_libdir}/scim-1.0/1.4.0/SetupUI
%{_libdir}/scim-1.0/1.4.0/Config/simple.so
%{_libdir}/scim-1.0/1.4.0/Config/socket.so
%{_libdir}/scim-1.0/1.4.0/Filter/sctc.so
%{_libdir}/scim-1.0/1.4.0/FrontEnd/socket.so
%{_libdir}/scim-1.0/1.4.0/FrontEnd/x11.so
%{_libdir}/scim-1.0/1.4.0/Helper/setup.so
%{_libdir}/scim-1.0/1.4.0/IMEngine/rawcode.so
%{_libdir}/scim-1.0/1.4.0/IMEngine/socket.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/aaa-frontend-setup.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/aaa-imengine-setup.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/panel-gtk-setup.so

%files gtk
%{_libdir}/gtk-2.0/2.10.0/immodules/im-scim.so

%if 0%{?suse_version} > 1130
%files gtk3
%{_libdir}/gtk-3.0/3.0.0/immodules/im-scim.so
%endif

%if 0%{?suse_version} <= 1500
%files qt4
%{_libdir}/qt4/plugins/inputmethods/im-scim.so
%endif

%files devel
%doc docs/html
%doc docs/developers
%{_libdir}/libscim-1.0.so
%{_libdir}/libscim-gtkutils-1.0.so
%{_libdir}/libscim-x11utils-1.0.so
%{_libdir}/pkgconfig/scim.pc
%{_libdir}/pkgconfig/scim-gtkutils.pc
%{_libdir}/pkgconfig/scim-x11utils.pc
%{_includedir}/scim-1.0

%files lang -f %{name}.lang

%changelog
