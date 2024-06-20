#
# spec file for package python-pyotherside
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


%define srcname pyotherside
%bcond_without test
Name:           python-pyotherside
Version:        1.6.1
Release:        0
Summary:        Asynchronous Python 3 Bindings for Qt 5
License:        ISC
URL:            https://thp.io/2011/pyotherside/
Source:         https://github.com/thp/pyotherside/archive/%{version}.tar.gz
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(python3)
Provides:       pyotherside = %{version}-%{release}
Provides:       python3-pyotherside = %{version}-%{release}
Obsoletes:      python3-pyotherside < %{version}-%{release}
%if %{with test}
BuildRequires:  Mesa-dri
BuildRequires:  xvfb-run
%endif

%description
A QML Plugin that provides access to a Python 3 interpreter from QML.

%prep
%setup -q -n %{srcname}-%{version}
# disable qtquicktests
sed -i 's| qtquicktests||' pyotherside.pro

%build
%qmake5 PYTHON_CONFIG=python%{python3_version}-config QMAKE_STRIP="/bin/true";
%make_build

%install
make INSTALL_ROOT=%{buildroot} install

%if %{with test}
%check
xvfb-run -s '-screen 0, 1280x1024x24' -a  ./tests/tests
%endif

%files
%doc README.md
%license LICENSE
%dir %{_libqt5_archdatadir}/qml/io/
%dir %{_libqt5_archdatadir}/qml/io/thp/
%{_libqt5_archdatadir}/qml/io/thp/pyotherside

%changelog
