#
# spec file for package qcustomplot
#
# Copyright (c) 2022 SUSE LLC
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


Name:           qcustomplot
Version:        2.1.1
%define sover   2
Release:        0
Summary:        Qt widget for plotting and data visualization
License:        GPL-3.0-or-later
URL:            https://www.qcustomplot.com/
Group:          Development/Libraries/C and C++
Source0:        https://www.qcustomplot.com/release/%{version}fixed/QCustomPlot.tar.gz
Source1:        https://www.qcustomplot.com/release/%{version}fixed/QCustomPlot-sharedlib.tar.gz
# PATCH-FIX-OPENSUSE relwithdebug.diff -- build with debug symbols
Patch1:         relwithdebug.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.6.4
BuildRequires:  gdb
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

%package     -n lib%{name}%{sover}
Summary:        Qt widget for plotting and data visualization
Group:          System/Libraries
Provides:       %{name} = %{version}
Provides:       lib%{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       %{name}-qt5 = %{version}
Obsoletes:      %{name}-qt5 < %{version}
# Earlier misnamed packages
Provides:       lib%{name}-%{sover} = %{version}
Obsoletes:      lib%{name}-%{sover} < %{version}

%description -n lib%{name}%{sover}
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

%package        devel
Summary:        Development files for QCustomPlot
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
# Last used 2018 with version 2.0.0
Provides:       %{name}-qt5-devel = %{version}
Obsoletes:      %{name}-qt5-devel < %{version}

%description    devel
This package contains libraries and header files for
developing applications that use QCustomPlot.

%package        doc
Summary:        Documentation and examples for QCustomPlot
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
This package contains the documentation and examples for QCustomPlot.

%prep
%setup -q -n %{name} -a 1 %{name}-sharedlib
%patch -P 1 -p1

%build
mkdir %{name}-sharedlib/sharedlib-compilation/build
pushd %{name}-sharedlib/sharedlib-compilation/build
export SOVERSION=%{version}
%qmake5 ../sharedlib-compilation.pro
%make_jobs
popd

%install
pushd %{name}-sharedlib/sharedlib-compilation/build
install -Dm 755 -t %{buildroot}%{_libdir} libqcustomplot*.so*
popd

install -Dm 644 qcustomplot.h %{buildroot}%{_includedir}/qcustomplot.h

# pkg-config files
install -d %{buildroot}%{_libdir}/pkgconfig/

cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}

Name:           %{name}
Version:        %{version}
Description: %{summary}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot
EOF

install -Dm 0644 -t %{buildroot}%{_docdir}/%{name}/ changelog.txt documentation/qcustomplot.qch
cp -r documentation/html/ %{buildroot}%{_docdir}/%{name}/
cp -r examples %{buildroot}%{_docdir}/%{name}/
find %{buildroot}%{_docdir}/%{name}/ -type f -exec chmod 0644 \{\} +
%fdupes %{buildroot}/%{_prefix}

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license GPL.txt
%{_libdir}/libqcustomplot.so.*

%files devel
%{_includedir}/qcustomplot.h
%{_libdir}/libqcustomplot.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/qcustomplot.qch
%{_docdir}/%{name}/changelog.txt
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/examples/

%changelog
