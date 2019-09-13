#
# spec file for package python-pyotherside
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without test
%define skip_python2 1
%define srcname pyotherside
Name:           python-pyotherside
Version:        1.5.4.git.1549621936.ebe2845
Release:        0
Summary:        Asynchronous Python 3 Bindings for Qt 5
License:        ISC
Group:          Development/Languages/Python
Url:            http://thp.io/2011/pyotherside/
Source:         %{srcname}-%{version}.tar.xz
Provides:       pyotherside = %{version}-%{release}
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  Mesa-dri
BuildRequires:  xvfb-run
%endif
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(python3)
%python_subpackages

%description
A QML Plugin that provides access to a Python 3 interpreter from QML.

%prep
%setup -q -n %{srcname}-%{version}
# disable qtquicktests
sed -i 's| qtquicktests||' pyotherside.pro

%build
qmake-qt5 PYTHON_CONFIG=python%{python_version}-config QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true";
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%if %{with test}
%check
xvfb-run -s '-screen 0, 1280x1024x24' -a  ./tests/tests
%endif

%files %{python_files}
%doc README
%license LICENSE
%dir %{_libqt5_archdatadir}/qml/io/
%dir %{_libqt5_archdatadir}/qml/io/thp/
%{_libqt5_archdatadir}/qml/io/thp/pyotherside

%changelog
