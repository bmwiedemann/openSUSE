#
# spec file for package presage
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


%global flavor @BUILD_FLAVOR@%{nil}
%global sname presage
%if "%{flavor}" != ""
%global pname %{sname}-%{flavor}
%else
%global pname %{sname}
%endif

%define py_ver %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null || echo PYTHON-NOT-FOUND)
Name:           %pname
Version:        0.9.1
Release:        0
Summary:        Intelligent predictive text entry platform (tools and demos)
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
Url:            http://presage.sourceforge.net
Source:         http://ncu.dl.sourceforge.net/project/%{sname}/%{sname}/%{version}/%{sname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM jzheng@suse.com - fix ncurese builds in openSUSE
Patch0:         presage-0.8.9-ncurses_flag.patch
# PATCH-FIX-UPSTREAM i@marguerite.su - port to cmuclmtk
Patch1:         presage-0.8.9-port_cmuclmtk.patch
# PATCH-FIX-UPSTREAM i@marguerite.su automake 1.12 abuild patch
Patch2:         presage-0.9.1-automake-1.12.patch
# PATCH-FIX-UPSTREAM automake 1.14 starts to check subdir-objects
Patch3:         presage-0.9.1-automake-1.14.patch
Patch4:         reproducible.patch
# PATCH-FIX-UPSTREAM narrowing conversion from int to char inside {}
Patch5:         presage-0.9.1-gcc6.patch
# PATCH-FIX-UPSTREAM doxygen no longer ships with the FreeSans font
Patch6:         presage-0.9.1-doxygen-no-freesans.patch
Patch7:         presage-buildcycle.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
%if "%{flavor}" == "doc"
# Documentation Start
BuildRequires:  doxygen
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  pkgconfig
# Documentation End
%else
BuildRequires:  help2man
BuildRequires:  libcmuclmtk-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  python-atspi
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
BuildRequires:  python-xlib
BuildRequires:  swig
%if 0%{?suse_version}
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dbus-1-python-devel
BuildRequires:  libcppunit-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
%else
BuildRequires:  cppunit-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  dbus-python-devel
BuildRequires:  desktop-file-utils
BuildRequires:  sqlite-devel
%endif
%endif

%description
Presage is an intelligent predictive text entry platform.

This package contains the tools required to generate custom statistical data used by the presage predictive text engine to generate predictions.

This package also contains simple demonstration programs and simulator.

%if "%{flavor}" == ""
%package -n libpresage-devel
Summary:        Intelligent predictive text entry platform (development files)
Group:          Development/Libraries/C and C++
Requires:       libpresage1 = %{version}

%description -n libpresage-devel
Presage is an intelligent predictive text entry platform.

This package contains development files.

This package contains the header files needed to compile applications or shared objects that use libpresage.

%package -n libpresage1
Summary:        Intelligent predictive text entry platform (shared library)
Group:          System/Libraries
Requires:       presage-data = %{version}

%description -n libpresage1
Presage is an intelligent predictive text entry platform.

A predictive text entry system attempts to improve the ease and speed of textual input by predicting words. Word prediction consists in computing which word tokens or word completions are most likely to be entered next. The system analyses the text already entered and combines the information thus extracted with other information sources to calculate the set of most probable tokens.

Presage exploits redundant information embedded in natural languages to generate word predictions. The modular architecture allows its language model to be extended and customized to utilize statistical, syntactic, and semantic information sources.

This package contains the shared library.

%package -n presage-data
Summary:        Intelligent predictive text entry platform (data files)
Group:          System/Libraries
Provides:       libpresage-data = %{version}
Obsoletes:      libpresage-data < %{version}

%description -n presage-data
Presage is an intelligent predictive text entry platform.

This package contains the sample statistical data files and abbreviation files needed by presage.

%package -n python-presage
Summary:        Intelligent predictive text entry platform (Python binding)
Group:          System/Libraries
%py_requires

%description -n python-presage
Presage is an intelligent predictive text entry platform.

This package provides the Python binding for libpresage.

This package contains the Python extension module for libpresage.

%package -n dbus-1-presage
Summary:        Intelligent predictive text entry platform (dbus service)
Group:          System/Libraries

%description -n dbus-1-presage
Presage is an intelligent predictive text entry platform.

This package contains the presage D-Bus service.

This package also contains a simple demonstration program that uses the D-Bus service.

%package -n python-presagemate
Summary:        Universial predictive text companion
Group:          Productivity/Text/Utilities
Requires:       python-atspi
Requires:       python-gtk
Requires:       python-presage
Requires:       python-xlib
BuildArch:      noarch
%py_requires

%description -n python-presagemate
Pypresagemate is a universal predictive text companion. Pypresagemate works alongside any AT-SPI aware application. The Assistive Technology Service Provider Interface (AT-SPI) is a toolkit-neutral way of providing accessibility facilities in applications. Pypresagemate works in the background by tracking what keystrokes are typed and displaying predictions in its window. When a prediction is selected, text is sent to the active application.

%package -n gprompter
Summary:        Intelligent predictive GTK+ text editor
Group:          Productivity/Text/Editors

%description -n gprompter
gprompter is a cross-platform predictive text editor, based on presage, the intelligent predictive text entry platform.

gprompter displays predictions in a contextual pop-up box as each letter is typed. Predictions can be easily selected and inserted in the document.

%package -n pyprompter
Summary:        Intelligent predictive wxPython text editor
Group:          Productivity/Text/Editors
Requires:       python-presagemate
Requires:       python-wxWidgets
BuildArch:      noarch
%py_requires

%description -n pyprompter
This package contains the wxPython predictive text editor pyprompter.

pyprompter is a cross-platform predictive text editor.

pyprompter displays predictions in a contextual pop-up box as each letter is typed. Predictions can be easily selected and inserted in the document.

%else
%package -n libpresage-doc
Summary:        Intelligent predictive text entry platform (documentation)
Group:          Documentation/HTML
BuildArch:      noarch

%description -n libpresage-doc
Presage is an intelligent predictive text entry platform.

This package contains the libpresage API Documentation in HTML format.
%endif

%prep
%setup -q -n %{sname}-%{version}
find . -type f -exec sed -i  's/\r//g' "{}" \;
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
echo "[D-BUS Service]" > apps/dbus/org.gnome.presage.service.in
echo "Name=org.gnome.presage.beta" >> apps/dbus/org.gnome.presage.service.in
echo "Exec={bindir}/presage_dbus_service --start" >> apps/dbus/org.gnome.presage.service.in
echo "User=root" >> apps/dbus/org.gnome.presage.service.in

%build
autoreconf -fi
%if "%{flavor}" == "doc"
# nl -ba ./configure
%configure --disable-sqlite --disable-gprompter --disable-gpresagemate --disable-python-binding
make -C doc %{?_smp_mflags}
%else
export LIBS+="-lm -lgmodule-2.0"
%configure
make %{?_smp_mflags}
%endif

%install
%if "%{flavor}" == "doc"
make -C doc %{?_smp_mflags} DESTDIR=%{buildroot} install
%fdupes %{buildroot}/%{_datadir}

%else
make %{?_smp_mflags} DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version}

pushd %{buildroot}%{python_sitelib}/prompter/
%py_compile .
popd
pushd %{buildroot}%{python_sitearch}/
%py_compile .
popd

sed -i -e '1 s#/usr/bin/env.*python#/usr/bin/python2#' %{buildroot}%{_bindir}/presage_dbus_*

%suse_update_desktop_file gprompter Utility DesktopUtility
%suse_update_desktop_file pyprompter Utility DesktopUtility

%fdupes %{buildroot}/%{_prefix}

%else

desktop-file-install --add-category="Utility" --delete-original --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/gprompter.desktop
desktop-file-install --add-category="Utility" --delete-original --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/pyprompter.desktop

fdupes -n -q -r %{buildroot}

%endif
%endif

%if "%{flavor}" == ""
%post -n libpresage1 -p /sbin/ldconfig
%postun -n libpresage1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/presage_demo
%{_bindir}/presage_demo_text
%{_mandir}/man1/presage_demo.1%{ext_man}
%{_bindir}/presage_simulator
%{_bindir}/text2ngram
%{_mandir}/man1/presage_demo_text.1%{ext_man}
%{_mandir}/man1/presage_simulator.1%{ext_man}
%{_mandir}/man1/text2ngram.1%{ext_man}

%files -n dbus-1-presage
%{_bindir}/presage_dbus_python_demo
%{_bindir}/presage_dbus_service
%{python_sitelib}/presage_dbus_service.py
%{python_sitelib}/presage_dbus_service.pyc
%{python_sitelib}/presage_dbus_service.pyo
%{_datadir}/dbus-1/services/org.gnome.presage.service
%{_mandir}/man1/presage_dbus_python_demo.1%{ext_man}
%{_mandir}/man1/presage_dbus_service.1%{ext_man}

%files -n libpresage1
%{_libdir}/libpresage.so.1
%{_libdir}/libpresage.so.1.1.1

%files -n presage-data
%config %{_sysconfdir}/presage.xml
%{_datadir}/presage
%exclude %{_datadir}/presage/html
%exclude %{_datadir}/presage/getting_started.txt
%exclude %{_datadir}/presage/python_binding.txt

%files -n python-presagemate
%{_bindir}/pypresagemate
%{python_sitelib}/presagemate

%files -n libpresage-devel
%{_includedir}/presageCallback.h
%{_includedir}/presageException.h
%{_includedir}/presage.h
%{_libdir}/libpresage.so

%files -n python-presage
%{_bindir}/presage_python_demo
%{python_sitearch}/_presage.so
%{python_sitearch}/presage.py
%{python_sitearch}/presage.pyc
%if 0%{?fedora}
%{python_sitearch}/presage.pyo
%endif
%{_mandir}/man1/presage_python_demo.1%{ext_man}
%{python_sitearch}/python_presage-0.9.1-py%{py_ver}.egg-info

%files -n pyprompter
%{_bindir}/pyprompter
%{python_sitelib}/prompter
%{python_sitelib}/pyprompter-0.9.1-py%{py_ver}.egg-info
%{_datadir}/applications/pyprompter.desktop
%{_datadir}/icons/hicolor/scalable/apps/pyprompter.svg
%{_mandir}/man1/pyprompter.1%{ext_man}
%{_datadir}/pixmaps/pyprompter.*

%files -n gprompter
%{_bindir}/gprompter
%{_datadir}/applications/gprompter.desktop
%{_datadir}/icons/hicolor/scalable/apps/gprompter.svg
%{_mandir}/man1/gprompter.1%{ext_man}
%{_datadir}/pixmaps/gprompter.*

%else 
%files -n libpresage-doc
%dir %{_datadir}/presage
%{_datadir}/presage/html/
%{_datadir}/presage/getting_started.txt
%{_datadir}/presage/python_binding.txt
%endif

%changelog
