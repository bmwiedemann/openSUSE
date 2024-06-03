#
# spec file for package lazarus
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


%define qt5_sover   1
%define qt6_sover   6
Name:           lazarus
Version:        3.4
Release:        0
# Please note that the LGPL is modified and this is not multi-licensed, but each component has a separate license chosen.
Summary:        FreePascal RAD IDE and Component Library
License:        GPL-2.0-only AND LGPL-2.0-only AND MPL-1.1
Group:          Development/Languages/Other
URL:            http://www.lazarus.freepascal.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-0.tar.gz
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
Requires:       binutils
Requires:       fpc
Requires:       fpc-src
Requires:       gcc
Requires:       gdb
Requires:       make
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel >= 5.6.0
BuildRequires:  qt6-base-common-devel >= 6.2.0
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
Requires:       %{name}-ide = %{version}
Requires:       %{name}-lcl = %{version}
Requires:       %{name}-lcl-gtk2 = %{version}
Requires:       %{name}-lcl-nogui = %{version}
Requires:       %{name}-tools = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-2.0)

%description
Lazarus is an IDE to create (graphical and console) applications with
Free Pascal, the (L)GPLed Pascal and Object Pascal compiler that runs on
Windows, Linux, Mac OS X, FreeBSD and more.

Lazarus is the missing part of the puzzle that will allow you to develop
programs for all of the above platforms in a Delphi-like environment.
The IDE is a RAD tool that includes a form designer.

Unlike Java's "write once, run anywhere" motto, Lazarus and Free Pascal
strive for "write once, compile anywhere". Since the exact same compiler
is available on all of the above platforms you don't need to do any recoding
to produce identical products for different platforms.

In short, Lazarus is a free RAD tool for Free Pascal using its
Lazarus Component Library (LCL).

%package ide
Summary:        Lazarus RAD IDE for Free Pascal
License:        GPL-2.0-or-later AND LGPL-2.0-only WITH Classpath-exception-2.0
Requires:       %{name}-lcl = %{version}
Requires:       %{name}-tools = %{version}
Recommends:     %{name}-doc = %{version}
Requires:       fpc-src
Requires:       gdb
Requires:       hicolor-icon-theme
Requires:       make

%description ide
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package provides the Lazarus RAD IDE.

%package tools
Summary:        Lazarus IDE helper programs
License:        GPL-2.0-or-later
Requires:       binutils
Requires:       fpc
Requires:       glibc-devel

%description tools
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package provides helper programs used for building Lazarus projects.

%package doc
Summary:        Lazarus IDE documentation
License:        GPL-2.0-or-later

%description doc
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains documentation and example programs for the Lazarus IDE.

%package lcl
Summary:        Lazarus Component Library
Recommends:     %{name}-lcl-gtk2 = %{version}
Recommends:     %{name}-lcl-nogui = %{version}

%description lcl
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains the common parts of the Lazarus Component Library.

%package lcl-nogui
Summary:        Lazarus Component Library - non-graphical components
Requires:       %{name}-lcl = %{version}

%description lcl-nogui
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains LCL components for developing non-graphical applications
and command-line tools.

%package lcl-gtk2
Summary:        Lazarus Component Library - GTK2 widgetset support
Requires:       %{name}-lcl = %{version}
Requires:       gtk2-devel

%description lcl-gtk2
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains LCL components for developing applications
using the GTK2 widgetset.

%package lcl-gtk3
Summary:        Lazarus Component Library - GTK2 widgetset support
Requires:       %{name}-lcl = %{version}-%{release}
Requires:       gtk3-devel >= 3.24.24

%description lcl-gtk3
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains LCL components for developing applications
using the GTK3 widgetset.

%package lcl-qt5
Summary:        Lazarus Component Library - Qt5 widgetset support
Requires:       %{name}-lcl = %{version}
Requires:       libQt5Pas-devel = %{version}

%description lcl-qt5
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains LCL components for developing applications
using the Qt5 widgetset.

%package     -n libQt5Pas%{qt5_sover}
Summary:        Free Pascal interface to Qt5
License:        LGPL-3.0-only
Group:          System/Libraries

%description -n libQt5Pas%{qt5_sover}
Qt5 bindings for Pascal from Lazarus.

%package     -n libQt5Pas-devel
Summary:        Free Pascal interface to Qt5
License:        LGPL-3.0-only
Group:          Development/Libraries/Other
Requires:       libQt5Pas%{qt5_sover} = %{version}

%description -n libQt5Pas-devel
The qt5pas-devel package contains libraries and header files for
developing applications that use qt5pas.

%package lcl-qt6
Summary:        Lazarus Component Library - Qt6 widgetset support
Requires:       %{name}-lcl = %{version}
Requires:       libQt6Pas-devel = %{version}

%description lcl-qt6
Lazarus is a cross-platform IDE and component library for Free Pascal.
This package contains LCL components for developing applications
using the Qt6 widgetset.

%package     -n libQt6Pas%{qt6_sover}
Summary:        Free Pascal interface to Qt6
License:        LGPL-3.0-only
Group:          System/Libraries

%description -n libQt6Pas%{qt6_sover}
Qt5 bindings for Pascal from Lazarus.

%package     -n libQt6Pas-devel
Summary:        Free Pascal interface to Qt6
License:        LGPL-3.0-only
Group:          Development/Libraries/Other
Requires:       libQt6Pas%{qt6_sover} = %{version}

%description -n libQt6Pas-devel
The qt6pas-devel package contains libraries and header files for
developing applications that use qt5pas.

# Instruct fpmake to build in parallel
%global fpmakeopt %{?_smp_build_ncpus:FPMAKEOPT='-T %{_smp_build_ncpus}'}

# Preferred compilation options - enable GDB debuginfo in DWARF format, plus some optimisations
%global fpcopt -g -gl -gw -O3

%prep
%autosetup -p1 -n %{name}

# remove unneeded files
rm -rf tools/install/cross_unix/debian_crosswin32/
rm -f tools/install/cross_unix/*deb.*
rm -rf tools/install/debian_*
rm -rf tools/install/freebsd_*
rm -rf tools/install/macosx/
rm -rf tools/install/slacktgz/
rm -rf tools/install/win/
rm -f tools/install/*slacktgz.*

# fix shebang
find . \( -name "*.sh" -o -name "*.pl" \) -exec sed -i '1s|#!%{_bindir}/env |#!%{_bindir}/|' {} +

# set executable bit to fix rpmlint error "non-executable-script"
chmod +x components/datetimectrls/docs/clean-files.sh
chmod +x components/datetimectrls/docs/make-archive.sh
chmod +x components/datetimectrls/docs/make-docs.sh
chmod +x components/lazcontrols/docs/make-docs.sh
chmod +x components/rtticontrols/fpdoc/clean-files.sh
chmod +x components/rtticontrols/fpdoc/make-docs.sh

# remove git ignore files to prevent them from being installed to fix rpmlint error "version-control-internal-file"
find . \( -name ".gitignore" \) -delete

%build
# Remove the files for building other packages
rm -rf debian
pushd tools
find install -depth -type d ! \( -path "install/linux/*" -o -path "install/linux" -o -path "install" \) -exec rm -rf '{}' \;
popd

# Re-create the Makefiles
export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall
pushd components
fpcmake -Tall
popd

# Compile some basic targets required by everything else
make registration %{fpmakeopt} OPT='%{fpcopt}'

# Compile lazbuild - required to build other targets
make lazbuild %{fpmakeopt} OPT='%{fpcopt}'

# Compile LCL base (Lazarus Component Library) for the "nogui" widgetset
make lcl %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM=nogui

# Compile extra tools
make tools %{fpmakeopt} OPT='%{fpcopt}'

# Compile the LCL base + extra components for GUI widgetsets
for WIDGETSET in gtk2 gtk3 qt5 qt6; do
	make lcl basecomponents bigidecomponents %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM="${WIDGETSET}"
done

# Compile the IDE itself. Default to using the gkt2 widget set.
make bigide %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM=gtk2

# Build libQt5Pas
pushd lcl/interfaces/qt5/cbindings
  %qmake5
  %make_build
popd

# Build libQt6Pas
pushd lcl/interfaces/qt6/cbindings
  %qmake6
  %make_build
popd

%install
make install INSTALL_PREFIX=%{buildroot}%{_prefix} _LIB=%{_lib}

# Remove man page for an executable that is not actually installed.
rm %{buildroot}%{_mandir}/man1/svn2revisioninc.1* || true

desktop-file-install --dir %{buildroot}%{_datadir}/applications install/%{name}.desktop

install -d %{buildroot}%{_sysconfdir}/lazarus
sed 's#__LAZARUSDIR__#%{_libdir}/%{name}#;s#__FPCSRCDIR__#%{_datadir}/fpcsrc#' \
        tools/install/linux/environmentoptions.xml \
        > %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml

chmod 755 %{buildroot}%{_libdir}/%{name}/components/lazreport/tools/localize.sh

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

pushd lcl/interfaces/qt5/cbindings
  %make_install INSTALL_ROOT=%{buildroot}
popd

pushd lcl/interfaces/qt6/cbindings
  %make_install INSTALL_ROOT=%{buildroot}
popd

# Since we provide Qt5Pas as a standalone package, remove the .so files bundled in Lazarus dir
# and replace them with symlinks to the standalone .so.
for FILEPATH in %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt5/cbindings/libQt5Pas.so* ; do
    FILENAME="$(basename "${FILEPATH}")"
    ln -sf "%{_libdir}/${FILENAME}" "${FILEPATH}"
done

# Remove hidden files to fix rpmlint warning "hidden-file-or-dir"
rm -f %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt5/cbindings/.qmake.stash
rm -f %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt6/cbindings/.qmake.stash

# Remove duplicate files
%fdupes %{buildroot}%{_libdir}/%{name}

%post -n libQt5Pas%{qt5_sover} -p /sbin/ldconfig
%postun -n libQt5Pas%{qt5_sover} -p /sbin/ldconfig
%post -n libQt6Pas%{qt6_sover} -p /sbin/ldconfig
%postun -n libQt6Pas%{qt6_sover} -p /sbin/ldconfig

%files
# No files, but we want to build the "lazarus" metapackage

%files doc
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/docs
%{_libdir}/%{name}/examples
%license COPYING.GPL.txt

%files tools
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lazbuild
%{_libdir}/%{name}/packager/
%{_libdir}/%{name}/tools/
%{_bindir}/lazbuild
%{_bindir}/lazres
%{_bindir}/lrstolfm
%{_bindir}/updatepofiles
%dir %{_sysconfdir}/lazarus
%config(noreplace) %{_sysconfdir}/lazarus/environmentoptions.xml
%license COPYING.GPL.txt
%{_mandir}/man1/lazbuild.1*
%{_mandir}/man1/lazres.1*
%{_mandir}/man1/lrstolfm.1*
%{_mandir}/man1/updatepofiles.1*

%files ide
%{_libdir}/%{name}
# Exclude -docs files
%exclude %{_libdir}/%{name}/docs
%exclude %{_libdir}/%{name}/examples
# Exclude -lcl files
%exclude %{_libdir}/%{name}/components
%exclude %{_libdir}/%{name}/lcl
# Exclude -tools files
%exclude %{_libdir}/%{name}/lazbuild
%exclude %{_libdir}/%{name}/packager
%exclude %{_libdir}/%{name}/tools
%{_bindir}/lazarus-ide
%{_bindir}/startlazarus
%{_datadir}/pixmaps/lazarus.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/mime/packages/lazarus.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%doc README.md
%license COPYING.txt
%license COPYING.LGPL.txt
%license COPYING.modifiedLGPL.txt
%{_mandir}/man1/lazarus-ide.1*
%{_mandir}/man1/startlazarus.1*

# Helper macro to reduce repetitions (lcl, basecomponents)
%define lcl_base_files(n:) %{expand:
	%{*} %{_libdir}/%{name}/components/*/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/units/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/lcl/interfaces/%{-n*}/
	%{*} %{_libdir}/%{name}/lcl/units/*/%{-n*}/
}

# Some files are not present for nogui (bigidecomponents)
%define lcl_extra_files(n:) %{expand:
	%{*} %{_libdir}/%{name}/components/*/design/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/design/units/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/include/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/include/intf/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/lib/*-linux-%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/units/%{-n*}/

	%{*} %{_libdir}/%{name}/components/chmhelp/packages/help/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/chmhelp/packages/idehelp/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/fpcunit/ide/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/jcf2/IdePlugin/lazarus/lib/*-linux/%{-n*}/
}

%files lcl
%license COPYING.txt
%license COPYING.LGPL.txt
%license COPYING.modifiedLGPL.txt
%license %{_libdir}/%{name}/lcl/interfaces/customdrawn/android/ApacheLicense2.0.txt
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/components/
%{_libdir}/%{name}/lcl/
%lcl_base_files  -n nogui %exclude
%lcl_base_files  -n gtk2 %exclude
%lcl_extra_files -n gtk2 %exclude
%lcl_base_files  -n gtk3 %exclude
%lcl_extra_files -n gtk3 %exclude
%lcl_base_files  -n qt5 %exclude
%lcl_extra_files -n qt5 %exclude
%lcl_base_files  -n qt6 %exclude
%lcl_extra_files -n qt6 %exclude

%files lcl-nogui
%lcl_base_files -n nogui

%files lcl-gtk2
%lcl_base_files -n gtk2
%lcl_extra_files -n gtk2

%files lcl-gtk3
%lcl_base_files -n gtk3
%lcl_extra_files -n gtk3

%files lcl-qt5
%lcl_base_files -n qt5
%lcl_extra_files -n qt5

%files lcl-qt6
%lcl_base_files -n qt6
%lcl_extra_files -n qt6

%files -n libQt5Pas%{qt5_sover}
%license lcl/interfaces/qt5/cbindings/COPYING.TXT
%doc lcl/interfaces/qt5/cbindings/README.TXT
%{_libdir}/libQt5Pas.so.%{qt5_sover}*

%files -n libQt5Pas-devel
%{_libdir}/libQt5Pas.so

%files -n libQt6Pas%{qt6_sover}
%license lcl/interfaces/qt6/cbindings/COPYING.TXT
%doc lcl/interfaces/qt6/cbindings/README.TXT
%{_libdir}/libQt6Pas.so.%{qt6_sover}*

%files -n libQt6Pas-devel
%{_libdir}/libQt6Pas.so

%changelog
