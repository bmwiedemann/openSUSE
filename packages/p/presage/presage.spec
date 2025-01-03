#
# spec file for package presage
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


%global flavor @BUILD_FLAVOR@%{nil}
%global sname presage
%if "%{flavor}" != ""
%global pname %{sname}-%{flavor}
%else
%global pname %{sname}
%endif

Name:           %{pname}
Version:        0.9.1
Release:        0
Summary:        Intelligent predictive text entry platform (tools and demos)
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://presage.sourceforge.net
Source:         https://master.dl.sourceforge.net/project/%{sname}/%{sname}/%{version}/%{sname}-%{version}.tar.gz
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
# PATCH-FIX-UPSTREAM port python binding to python3
Patch8:         presage-0.9.1-python3.patch
# PATCH-FIX-UPSTREAM fix ISO C++17 does not allow dynamic exception specifications
Patch9:         presage-0.9.1-gcc11.patch
# PATCH-FIX-UPSTREAM Fix installation of python bindings with recent setuptools
Patch10:        presage-setuptools.patch
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
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  help2man
BuildRequires:  libcmuclmtk-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  python3-atspi
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-xlib
BuildRequires:  swig
%if 0%{?suse_version}
BuildRequires:  dbus-1-glib-devel
BuildRequires:  libcppunit-devel
BuildRequires:  python3-dbus-python
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
Requires:       presage-data

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

%package -n python3-presage
Summary:        Intelligent predictive text entry platform (Python binding)
Group:          Development/Languages/Python
Provides:       python-presage = %{version}-%{release}
Obsoletes:      python-presage < %{version}-%{release}

%description -n python3-presage
Presage is an intelligent predictive text entry platform.

This package provides the Python binding for libpresage.

This package contains the Python extension module for libpresage.

%package -n python3-dbus-presage
Summary:        Intelligent predictive text entry platform (dbus service)
Group:          Development/Languages/Python
Requires:       python3-dbus-python
Requires:       python3-presage
Provides:       dbus-1-presage = %{version}-%{release}
Obsoletes:      dbus-1-presage < %{version}-%{release}

%description -n python3-dbus-presage
Presage is an intelligent predictive text entry platform.

This package contains the presage D-Bus service.

This package also contains a simple demonstration program that uses the D-Bus service.

%package -n python3-presagemate
Summary:        Universial predictive text companion
Group:          Productivity/Text/Utilities
Requires:       python3-atspi
Requires:       python3-gobject
Requires:       python3-presage
Requires:       python3-xlib
Provides:       python-presagemate = %{version}-%{release}
Obsoletes:      python-presagemate < %{version}-%{release}
BuildArch:      noarch

%description -n python3-presagemate
Pypresagemate is a universal predictive text companion. Pypresagemate works alongside any AT-SPI aware application. The Assistive Technology Service Provider Interface (AT-SPI) is a toolkit-neutral way of providing accessibility facilities in applications. Pypresagemate works in the background by tracking what keystrokes are typed and displaying predictions in its window. When a prediction is selected, text is sent to the active application.

%package -n gprompter
Summary:        Intelligent predictive GTK+ text editor
Group:          Productivity/Text/Editors

%description -n gprompter
gprompter is a cross-platform predictive text editor, based on presage, the intelligent predictive text entry platform.

gprompter displays predictions in a contextual pop-up box as each letter is typed. Predictions can be easily selected and inserted in the document.

%package -n python3-pyprompter
Summary:        Intelligent predictive wxPython text editor
Group:          Productivity/Text/Editors
Requires:       python3-presage
Requires:       python3-wxPython
Provides:       pyprompter = %{version}-%{release}
Obsoletes:      pyprompter < %{version}-%{release}
BuildArch:      noarch

%description -n python3-pyprompter
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
%autosetup -p1 -n %{sname}-%{version}

find . -type f \( \! -name '*.png' -a \! -name 'presage_python_demo.1' \) -exec sed -i  's/\r//g' "{}" \;
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
export PYTHON="/usr/bin/python3"
export CFLAGS="%{optflags} $(python3-config --includes)"
export CXXFLAGS="%{optflags} $(python3-config --includes)"
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

pushd %{buildroot}%{python3_sitelib}/prompter/
%py3_compile -O .
popd
pushd %{buildroot}%{python3_sitearch}/
%py3_compile -O .
popd

sed -i -e '1 s#/usr/bin/env.*python#/usr/bin/python3#' %{buildroot}%{_bindir}/presage_dbus_*

%suse_update_desktop_file gprompter Utility DesktopUtility
%suse_update_desktop_file pyprompter Utility DesktopUtility

%fdupes %{buildroot}/%{_prefix}
%python3_fix_shebang

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

%files -n python3-dbus-presage
%dir %{python3_sitelib}/__pycache__/
%{_bindir}/presage_dbus_python_demo
%{_bindir}/presage_dbus_service
%{python3_sitelib}/presage_dbus_service.py
%{python3_sitelib}/__pycache__/presage_dbus_service.*.pyc
#%{python3_sitelib}/__pycache__/presage_dbus_service.*.pyo
%{_datadir}/dbus-1/services/org.gnome.presage.service
%{_mandir}/man1/presage_dbus_python_demo.1%{ext_man}
%{_mandir}/man1/presage_dbus_service.1%{ext_man}

%files -n libpresage1
%{_libdir}/libpresage.so.1
%{_libdir}/libpresage.so.1.1.1

%files -n presage-data
%config %{_sysconfdir}/presage.xml
%{_datadir}/presage
#%exclude %{_datadir}/presage/html
%exclude %{_datadir}/presage/getting_started.txt
%exclude %{_datadir}/presage/python_binding.txt

%files -n python3-presagemate
%{_bindir}/pypresagemate
%{python3_sitelib}/presagemate

%files -n libpresage-devel
%{_includedir}/presageCallback.h
%{_includedir}/presageException.h
%{_includedir}/presage.h
%{_libdir}/libpresage.so

%files -n python3-presage
%dir %{python3_sitearch}/__pycache__/
%{_bindir}/presage_python_demo
%{python3_sitearch}/_presage*.so
%{python3_sitearch}/presage.py
%{python3_sitearch}/__pycache__/presage.*.pyc
%if 0%{?fedora}
%{python3_sitearch}/__pycache__/presage.*.pyo
%endif
%{_mandir}/man1/presage_python_demo.1%{ext_man}
%{python3_sitearch}/python_presage-0.9.1-py%{py3_ver}.egg-info

%files -n python3-pyprompter
%{_bindir}/pyprompter
%{python3_sitelib}/prompter
%{python3_sitelib}/pyprompter-0.9.1-py%{py3_ver}.egg-info
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
