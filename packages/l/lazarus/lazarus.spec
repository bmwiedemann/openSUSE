#
# spec file for package lazarus
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


%define sover   1
Name:           lazarus
Version:        2.0.10
Release:        0
# Please note that the LGPL is modified and this is not multi-licensed, but each component has a separate license chosen.
Summary:        FreePascal RAD IDE and Component Library
License:        GPL-2.0-only AND LGPL-2.0-only AND MPL-1.1
Group:          Development/Languages/Other
URL:            http://www.lazarus.freepascal.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-2.tar.gz
# PATCH-FEATURE-UPSTREAM http://mantis.freepascal.org/view.php?id=31364
Source1:        https://raw.githubusercontent.com/hughsie/fedora-appstream/developerapps/appdata-extra/desktop/lazarus.appdata.xml
Source90:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE lazarus-Makefile_patch.diff -- Change installation path from /usr/share/lazarus to /usr/lib(64)/lazarus
Patch0:         %{name}-Makefile_patch.diff
# PATCH-FIX-OPENSUSE lazarus.desktop.patch -- Fix desktop file
Patch1:         lazarus.desktop.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  fpc >= 3.0.0
BuildRequires:  fpc-src >= 3.0.0
Requires:       fpc
Requires:       fpc-src
Requires:       gdb
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
%if 0%{?suse_version} > 1210
BuildRequires:  desktop-file-utils
%else
BuildRequires:  update-desktop-files
%endif
%if 0%{?suse_version} >= 1140
BuildRequires:  hicolor-icon-theme
%endif
%if 0%{?sles_version} == 11
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
%else
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
BuildRequires:  libqt5-qtbase-common-devel >= 5.6.0
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
%endif
%if 0%{?sles_version} == 11
Requires:       glib2-devel
Requires:       gtk2-devel
%else
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-2.0)
%endif

%description
Lazarus is a Rapid Application Development
tool for the FreePascal compiler using the Lazarus component
library - LCL. The LCL is included in this package.

%package     -n libQt5Pas%{sover}
Summary:        Free Pascal interface to Qt5
License:        LGPL-3.0-only
Group:          System/Libraries

%description -n libQt5Pas%{sover}
Library that allows to use Qt5 with Free Pascal

%package     -n libQt5Pas-devel
Summary:        Free Pascal interface to Qt5
License:        LGPL-3.0-only
Group:          Development/Libraries/Other
Requires:       libQt5Pas%{sover} = %{version}

%description -n libQt5Pas-devel
Development files for Free Pascal interface to Qt5.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

# remove unneeded files
rm -rf debian
rm -rf tools/install/cross_unix/debian_crosswin32/
rm -f tools/install/cross_unix/*deb.*
rm -rf tools/install/debian_*
rm -rf tools/install/freebsd_*
rm -rf tools/install/macosx/
rm -rf tools/install/slacktgz/
rm -rf tools/install/win/
rm -f tools/install/*slacktgz.*

# remove scripts vulnerable to symlink-attacks (bug 460642)
rm tools/install/build_fpc_snaphot_rpm.sh
rm tools/install/check_fpc_dependencies.sh
rm tools/install/create_fpc_deb.sh
rm tools/install/create_fpc_export_tgz.sh
rm tools/install/create_fpc_rpm.sh
rm tools/install/create_fpc-src_rpm.sh
rm tools/install/create_fpc_tgz_from_local_dir.sh
rm tools/install/create_lazarus_export_tgz.sh

# fix lineencodings
dos2unix examples/trayicon/frmtest.*
dos2unix examples/trayicon/wndtray.*

# fix rpmlint error "spurious-executable-perm"
chmod 644 docs/booth/ProdProgEntwMitOpenSourceSystems2007.odp
if [ -n "$SOURCE_DATE_EPOCH" ] ; then
  datestr=$(date -u "-d@$SOURCE_DATE_EPOCH" +%Y/%m/%d)
  sed -i -e 's!{\$I %%date%%}!'"'$datestr'"'!' \
    ide/ideinfodlg.pas ide/aboutfrm.pas ide/idefpcinfo.pas
  touch -d@"$SOURCE_DATE_EPOCH" ide/ideinfodlg.pas ide/aboutfrm.pas ide/idefpcinfo.pas # reset source timestamps because they are embedded in compiled files
fi

# fix shebang
find . \( -name "*.sh" -o -name "*.pl" \) -exec sed -i '1s|#!%{_bindir}/env|%{_bindir}/|' {} +

%build
# Don't use -gs (use explicitly "stabs" debuginfo) for compiling lhelp but -g (use the default debuginfo type "dwarf") as in the rest of package's Makefiles
# Fixes the "Stabs debuginfo not supported" error when extracting debug info from the package
sed -i "s/\-gs/\-g/" components/chmhelp/lhelp/Makefile

export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall

MAKEOPTS="-gl -Fl/usr/%{_lib}"
make bigide OPT="$MAKEOPTS"

export LCL_PLATFORM=

# build Qt4 interface
make -C lcl/interfaces/qt all LCL_PLATFORM=qt OPT="-dQT_NATIVE_DIALOGS"

%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
# build Qt5 interface
make -C lcl/interfaces/qt5 all LCL_PLATFORM=qt5 OPT="-dQT_NATIVE_DIALOGS"

# build libQt5Pas
pushd lcl/interfaces/qt5/cbindings
%qmake5
make %{?_smp_mflags}
popd
%endif

%install
make install \
    INSTALL_PREFIX=%{buildroot}%{_prefix} \
    INSTALL_LIBDIR=%{buildroot}%{_libdir} \
    INSTALL_BINDIR=%{buildroot}%{_bindir} \
    LAZARUS_INSTALL_DIR=%{buildroot}%{_libdir}/%{name} \
    _LIB=%{_lib}

%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
pushd lcl/interfaces/qt5/cbindings
%qmake5_install
install -Dpm 0644 qt5.pas %{buildroot}%{_datadir}/fpcsrc/packages/qt5/qt5.pas
popd
%endif

# convenience links
for f in lazarus lazbuild startlazarus; do
    rm -f %{buildroot}%{_bindir}/$f
    ln -sf ../%{_lib}/%{name}/$f %{buildroot}%{_bindir}/$f
done
rm -f %{buildroot}%{_bindir}/lazarus-ide
ln -sf ../%{_lib}/%{name}/lazarus %{buildroot}%{_bindir}/lazarus-ide
for f in lazres lrstolfm updatepofiles; do
    ln -sf ../%{_lib}/%{name}/tools/$f %{buildroot}%{_bindir}/$f
    cat %{buildroot}%{_libdir}/%{name}/install/man/man1/${f}.1 | gzip >%{buildroot}%{_mandir}/man1/${f}.1.gz
done

# collect docs and samples
install -dm 755 %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{_libdir}/%{name}/examples %{buildroot}%{_defaultdocdir}/%{name}
ln -s %{_defaultdocdir}/%{name}/examples %{buildroot}%{_libdir}/%{name}/examples
mv %{buildroot}%{_libdir}/%{name}/docs %{buildroot}%{_defaultdocdir}/%{name}
ln -s %{_defaultdocdir}/%{name}/docs %{buildroot}%{_libdir}/%{name}/docs
mv %{buildroot}%{_libdir}/%{name}/COPYING* %{buildroot}%{_libdir}/%{name}/README* %{buildroot}%{_defaultdocdir}/%{name}

# icons
for f in 16 32 48 64 128 256; do
    install -Dpm 0644 images/icons/lazarus${f}x${f}.png %{buildroot}%{_datadir}/icons/hicolor/${f}x${f}/apps/%{name}.png
done

# menu-entry
%if 0%{?suse_version} > 1210
desktop-file-install install/lazarus.desktop
%else
install -Dpm 0644 install/lazarus.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -n %{name} Development IDE
%endif

# mime info
install -Dpm 0644 install/%{name}-mime.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# software gallery metadata
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# configs
install -dm 0755 %{buildroot}%{_sysconfdir}/%{name}
sed <tools/install/linux/environmentoptions.xml -e "s#__LAZARUSDIR__#%{_libdir}/%{name}/#" -e "s#__FPCSRCDIR__#%{_datadir}/fpcsrc/#" > %{buildroot}%{_sysconfdir}/%{name}/environmentoptions.xml

# cleanup
rm -rf %{buildroot}%{_libdir}/%{name}/install/man
rm -f %{buildroot}%{_libdir}/%{name}/Makefile.fpc.orig
rm -rf %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt5/cbindings
%fdupes -s %{buildroot}

%if 0%{?suse_version} <= 1320
%post
%if 0%{?suse_version} >= 1140
%mime_database_post
%icon_theme_cache_post
%desktop_database_post
%else
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :
%endif

%postun
%if 0%{?suse_version} >= 1140
%mime_database_postun
%icon_theme_cache_postun
%desktop_database_postun
%else
%{_bindir}/update-mime-database %{_datadir}/mime &> /dev/null || :
%endif
%endif

%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
%post -n libQt5Pas%{sover} -p /sbin/ldconfig

%postun -n libQt5Pas%{sover} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%{_mandir}/man1/*
%doc %{_defaultdocdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/environmentoptions.xml
%{_bindir}/%{name}
%{_bindir}/%{name}-ide
%{_bindir}/lazbuild
%{_bindir}/startlazarus
%{_bindir}/lazres
%{_bindir}/lrstolfm
%{_bindir}/updatepofiles
%{_libdir}/%{name}/
# license is problematic
%exclude %{_libdir}/%{name}/components/aggpas/gpc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/pixmaps/lazarus.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
%files -n libQt5Pas%{sover}
%defattr(-,root,root,-)
%license lcl/interfaces/qt5/cbindings/COPYING.TXT
%{_libdir}/libQt5Pas.so.%{sover}*

%files -n libQt5Pas-devel
%defattr(-,root,root,-)
%license lcl/interfaces/qt5/cbindings/COPYING.TXT
%dir %{_datadir}/fpcsrc
%dir %{_datadir}/fpcsrc/packages
%dir %{_datadir}/fpcsrc/packages/qt5
%{_datadir}/fpcsrc/packages/qt5/qt5.pas
%{_libdir}/libQt5Pas.so
%endif

%changelog
