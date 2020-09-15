#
# spec file for package python-qtwebengine-qt5
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-qtwebengine-qt5
Version:        5.15.1
Release:        0
Summary:        Python bindings for the Qt5 WebEngine framework
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtwebengine/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 4.19.4}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5WebEngine)
Requires:       python-qt5
Requires:       python-sip(api) = %{python_sip_api_ver}

%python_subpackages

%description
PyQtWebEngine is a set of Python bindings for the Qt5 WebEngine
framework. The framework provides the ability to embed web
content in applications.

%package     -n %{name}-api
Summary:        Eric API files for %{name}
Group:          Development/Tools/IDE
Provides:       %{python_module qtwebengine-qt5-api = %{version}}
Supplements:    packageand(eric:%{python2_prefix}-qtwebengine-qt5)
Supplements:    packageand(eric:python3-qtwebengine-qt5)
BuildArch:      noarch

%description -n %{name}-api
This package provides Qt5 WebEngine framework API files for the Eric
IDE.

%package     -n %{name}-sip
Summary:        Sip files for %{name} 
Group:          Development/Libraries/Python
Provides:       %{python_module qtwebengine-qt5-sip = %{version}}
Supplements:    packageand(%{python2_prefix}-sip:%{python2_prefix}-qtwebengine-qt5)
Supplements:    packageand(python3-sip:python3-qtwebengine-qt5)
BuildArch:      noarch

%description -n %{name}-sip
This package contains sip files used to generate
bindings to the Qt5 WebEngine framework.

%prep
%autosetup -p1 -n PyQtWebEngine-%{version}
%{python_expand mkdir build_%{$python_bin_suffix}
cp *.py build_%{$python_bin_suffix}
cp -r sip build_%{$python_bin_suffix}
}

%build
%{python_expand pushd build_%{$python_bin_suffix}
$python configure.py \
    --no-dist-info \
    --qmake=%{_bindir}/qmake-qt5

make %{?_smp_mflags}
popd
}

%install
%{python_expand pushd build_%{$python_bin_suffix}
%make_install INSTALL_ROOT=%{buildroot}
popd
}

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{python_sitearch}/PyQt5/QtWebEngine.*
%{python_sitearch}/PyQt5/QtWebEngineCore.*
%{python_sitearch}/PyQt5/QtWebEngineWidgets.*

%files -n %{name}-api
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python/
%{_datadir}/qt5/qsci/api/python/PyQtWebEngine.api

%files -n %{name}-sip
%license LICENSE
%{_datadir}/sip/PyQt5/QtWebEngine/
%{_datadir}/sip/PyQt5/QtWebEngineCore/
%{_datadir}/sip/PyQt5/QtWebEngineWidgets/

%changelog
