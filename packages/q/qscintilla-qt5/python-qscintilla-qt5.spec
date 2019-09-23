#
# spec file for package python-qscintilla-qt5
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-qscintilla-qt5
Version:        2.11.2
Release:        0
Summary:        Python  Bindings for the C++ Editor Class Library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.riverbankcomputing.co.uk/qscintilla
Source:         https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_gpl-%{version}.tar.gz
#PATCH-FIX-OPENSUSE: Rename qscintilla2 to qscintilla2-qt5:
Patch0:         python-config.diff
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 4.19.8}
BuildRequires:  libqscintilla_qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       %{name}-sip = %{version}
Requires:       python-sip(api) = %{python_sip_api_ver}
%requires_ge    python-qt5
%ifpython2
%requires_ge    python2-qt5
%endif
%python_subpackages

%description
QScintilla is a Qt port of Neil Hodgson's Scintilla C++ editor class.

This is a Qt port from the original Scintilla class
(http://www.scintilla.org/).

This package is mainly used by eric, the Python IDE.

%package -n %{name}-sip
Summary:        Sip files for PyQScintilla
Group:          Development/Libraries/Python
Provides:       %{python_module qscintilla-qt5-sip = %{version}}

%description -n %{name}-sip
This package is needed to avoid conflicts between python-qscintilla and
python3-qscintilla packages. It contains sip files  used to generate
bindings to QScintilla

%prep
%setup -q -n QScintilla_gpl-%{version}
%patch0 -p1

%build
%{python_expand cp -r Python Python_%{$python_bin_suffix}
pushd Python_%{$python_bin_suffix}

$python configure.py \
  --pyqt=PyQt5 \
  --sip=%{_bindir}/sip-%{$python_bin_suffix} \
  --pyqt-sipdir=%{_datadir}/sip/PyQt5 \
  --qsci-incdir=%{_libqt5_includedir} \
  --qmake=%{_bindir}/qmake-qt5 \
  --no-dist-info \
  --no-stubs \
  --no-qsci-api

make %{?_smp_mflags}

popd

}

%install
%{python_expand pushd Python_%{$python_bin_suffix}

%make_install INSTALL_ROOT=%{buildroot}

popd

}

%files %{python_files}
%license LICENSE
%doc NEWS README
%{python_sitearch}/PyQt5/Qsci.so

%files -n %{name}-sip
%license LICENSE
%{_datadir}/sip/PyQt5/Qsci

%changelog
