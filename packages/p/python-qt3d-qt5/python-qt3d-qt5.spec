#
# spec file for package python-qt3d-qt5
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


# This definition is for projects which include the PyQt5 packages in recent
# versions but use default (old) Qt libraries e.g. from Leap, which does not
# have Qt >= 5.10. In that case, no Qt3DAnimation module will be built per
# sip %%If directives in the sip/Qt3DAnimation/*.sip files
%if %{pkg_vcmp libQt53DAnimation-devel >= 5.10}
%define have_qt3danimation 1
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-qt3d-qt5
Version:        5.15.1
Release:        0
Summary:        Python bindings for the Qt5 3D framework
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/pyqtchart/intro
Source:         https://files.pythonhosted.org/packages/source/P/PyQt3D/PyQt3D-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel >= 4.19.4}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt53DAnimation)
BuildRequires:  pkgconfig(Qt53DCore)
BuildRequires:  pkgconfig(Qt53DExtras)
BuildRequires:  pkgconfig(Qt53DInput)
BuildRequires:  pkgconfig(Qt53DLogic)
BuildRequires:  pkgconfig(Qt53DRender)
Requires:       python-qt5
Requires:       python-sip(api) = %{python_sip_api_ver}

%python_subpackages

%description
PyQt3D is a set of Python bindings for the Qt 3D framework.

%package     -n %{name}-api
Summary:        Eric API files for %{name}
Group:          Development/Tools/IDE
Provides:       %{python_module qt3d-qt5-api = %{version}}
Supplements:    packageand(eric:%{python2_prefix}-qt3d-qt5)
Supplements:    packageand(eric:python3-qt3d-qt5)
BuildArch:      noarch

%description -n %{name}-api
This package provides Qt5 3D framework API files for the Eric IDE.

%package     -n %{name}-sip
Summary:        Sip files for %{name}
Group:          Development/Libraries/Python
Provides:       %{python_module qt3d-qt5-sip = %{version}}
Supplements:    packageand(%{python2_prefix}-sip:%{python2_prefix}-qt3d-qt5)
Supplements:    packageand(python3-sip:python3-qt3d-qt5)
BuildArch:      noarch

%description -n %{name}-sip
This package contains sip files used to generate
bindings to the Qt5 3D framework.

%package     -n %{name}-examples
Summary:        Examples for %{name}
Group:          Documentation/Other
Provides:       %{python_module qt3d-qt5-examples = %{version}}
BuildArch:      noarch

%description -n %{name}-examples
This package provides %{name} examples.

%prep
%setup -q -n PyQt3D-%{version}
%{python_expand mkdir build_%{$python_bin_suffix}
cp *.py build_%{$python_bin_suffix}
cp -r sip build_%{$python_bin_suffix}
}

%build
%{python_expand pushd build_%{$python_bin_suffix}
$python configure.py \
    -w \
    --no-dist-info \
    --no-stubs \
    --qmake=%{_bindir}/qmake-qt5

make %{?_smp_mflags}
popd
}

%install
%{python_expand pushd build_%{$python_bin_suffix}
%make_install INSTALL_ROOT=%{buildroot}
popd
}
mkdir -p %{buildroot}%{_docdir}/%{name}
find examples -type f -executable -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)3\?=#!%{_bindir}/python3=' {} +
cp -r examples %{buildroot}%{_docdir}/%{name}

%files %{python_files}
%license LICENSE
%doc NEWS README
%dir %{python_sitearch}/PyQt5/
%{?have_qt3danimation:%{python_sitearch}/PyQt5/Qt3DAnimation.so}
%{python_sitearch}/PyQt5/Qt3DCore.so
%{python_sitearch}/PyQt5/Qt3DExtras.so
%{python_sitearch}/PyQt5/Qt3DInput.so
%{python_sitearch}/PyQt5/Qt3DLogic.so
%{python_sitearch}/PyQt5/Qt3DRender.so
%exclude %{_docdir}/%{name}/examples/

%files -n %{name}-api
%license LICENSE
%dir %{_datadir}/qt5/qsci/api/python/
%{_datadir}/qt5/qsci/api/python/PyQt3D.api

%files -n %{name}-sip
%license LICENSE
%{?have_qt3danimation:%{_datadir}/sip/PyQt5/Qt3DAnimation/}
%{_datadir}/sip/PyQt5/Qt3DCore/
%{_datadir}/sip/PyQt5/Qt3DExtras/
%{_datadir}/sip/PyQt5/Qt3DInput/
%{_datadir}/sip/PyQt5/Qt3DLogic/
%{_datadir}/sip/PyQt5/Qt3DRender/

%files -n %{name}-examples
%license LICENSE
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/examples/

%changelog
