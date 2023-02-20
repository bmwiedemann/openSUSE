#
# spec file for package python-sip4
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} < 1550
# Build the PyQt4.sip module only for older distros.
%bcond_without pyqt4_module
%else
%bcond_with pyqt4_module
%endif

# The python-qt5-sip provides the correct PyQt5 module for sip5 enabled distros,
# including SLE/Leap build targets now
%bcond_with pyqt5_module

%define python_sip_api 12.7
%define mname sip
%define pname sip4
# Note about package names:
# pythonX-sip4 contains the SIP module(s)
# pythonX-sip4-devel contains the tools to build SIP modules
# where X is the python flavor
# python-sip4-doc and python-sip4-common are flavorless
%define oldpython python
%define skip_python311 1

Name:           python-%{pname}
Version:        4.19.25
Release:        0
Summary:        SIP tool to use python sip bindings - legacy version 4
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        https://www.riverbankcomputing.com/static/Downloads/sip/%{version}/sip-%{version}.tar.gz
# PATCH-FIX-OPENSUSE disable-rpaths.diff -- Disable rpaths
Patch0:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE disable-strip.diff -- Disable stripping
Patch1:         disable-strip.diff
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{name}-common = %{version}
Provides:       python-%{mname} = %{version}-%{release}
Provides:       python-sip(api) = %{python_sip_api}
Obsoletes:      python-%{mname} < %{version}
%ifpython2
Provides:       %{oldpython}-%{mname} = %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname} < %{version}
%endif
%if %{with pyqt5_module}
Conflicts:      python-qt5-sip
%endif
%python_subpackages

%description
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package provides the legacy version 4 of the SIP tool

%package devel
Summary:        SIP tool to create python bindings
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{name}-common = %{version}
Requires:       c++_compiler
Requires:       python-devel
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-%{mname}-bin = %{version}-%{release}
Provides:       python-%{mname}-devel = %{version}-%{release}
Obsoletes:      python-%{mname}-bin < %{version}
Obsoletes:      python-%{mname}-devel < %{version}
%ifpython2
Provides:       %{oldpython}-%{mname}-bin = %{version}-%{release}
Provides:       %{oldpython}-%{mname}-devel = %{version}-%{release}
Obsoletes:      %{oldpython}-%{mname}-bin < %{version}
Obsoletes:      %{oldpython}-%{mname}-devel < %{version}
%endif

%description devel
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains all the developer tools you need to create your
own sip bindings.

%package -n python-%{pname}-doc
Summary:        SIP tool to create python bindings -- common documentation
Group:          Development/Libraries/Python
Provides:       %{python_module %{pname}-doc = %{version}-%{release}}
BuildArch:      noarch

%description -n python-%{pname}-doc
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains common documentation files shared between python2
and python3 versions of sip.

%package -n python-%{pname}-common
Summary:        SIP tool to create python bindings -- common files
Group:          Development/Libraries/Python
Provides:       %{python_module %{pname}-common = %{version}-%{release}}
BuildArch:      noarch

%description -n python-%{pname}-common
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains common files shared between python2 and python3
versions of sip.

%prep
%setup -q -n sip-%{version}
%autopatch -p1

sip_major=$(grep "define SIP_API_MAJOR_NR" siplib/sip.h | awk '{print $3}')
sip_minor=$(grep "define SIP_API_MINOR_NR" siplib/sip.h | awk '{print $3}')

if test "%{python_sip_api}" != "$sip_major.$sip_minor"; then
    echo "API version was changed to $sip_major.$sip_minor"
    exit 1
fi

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%{python_expand mkdir build_%{$python_bin_suffix}
pushd build_%{$python_bin_suffix}

# Link against libpython (fixes bnc#756282 and bnc#721280)
ldlibrary=`$python -c "import sysconfig as s;print(s.get_config_var('LDLIBRARY')[3:-3])"`
$python ../configure.py --debug \
    CFLAGS+="%{optflags}" \
    CXXFLAGS+="%{optflags}" \
    LIBS+="-l$ldlibrary" \
    -d %{$python_sitearch}

make %{?_smp_mflags}

# Point to the correct location for the documentation files
cp ../README ./
sed -i 's/"doc" directory/"doc" directory of package %{$python_prefix}-sip-devel/' README

popd
}

for P in \
%if %{with pyqt4_module}
PyQt4 \
%endif
%if %{with pyqt5_module}
PyQt5 \
%endif
; do
%{python_expand mkdir build_${P}_%{$python_bin_suffix}
pushd build_${P}_%{$python_bin_suffix}

# Link against libpython
ldlibrary=`$python -c "import sysconfig as s;print(s.get_config_var('LDLIBRARY')[3:-3])"`
$python ../configure.py --debug \
  --sip-module=${P}.sip \
  CFLAGS+="%{optflags}" \
  CXXFLAGS+="%{optflags}" \
  LIBS+="-l$ldlibrary" \
  --no-dist-info \
  -d %{$python_sitearch}

make %{?_smp_mflags}

popd
}
done

%install

%{python_expand pushd build_%{$python_bin_suffix}
%make_install
popd

# Make sure the correct sip executable is picked
sed -i 's,%{_bindir}/sip,%{_bindir}/sip-%{$python_bin_suffix},' %{buildroot}%{$python_sitearch}/sipconfig.py
}

for P in \
%if %{with pyqt4_module}
PyQt4 \
%endif
%if %{with pyqt5_module}
PyQt5 \
%endif
; do
%{python_expand pushd build_${P}_%{$python_bin_suffix}/siplib
%make_install
popd
}
done

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d

echo "%%python_sip_api_ver %{python_sip_api}" > %{buildroot}%{_rpmconfigdir}/macros.d/macros.python_all-sip4

%{python_expand # flavor specific macros
echo "%%requires_$python_sip_api Requires: %{$python_prefix}-sip(api) = %%python_sip_api_ver" \
    > %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{$python_prefix}-sip4
}
# macro for old python2 name
%if 0%{?have_python2} && ! 0%{?skip_python2}
echo "%%requires_python_sip_api Requires: %{python2_prefix}-sip(api) = %%python_sip_api_ver"  \
    >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{python2_prefix}-sip4
%endif
# additional: default python3 in case of multiple python3 flavors
%if 0%{?have_python3} && ! 0%{?skip_python3}
grep '%%requires_%{python3_prefix}_sip_api'  %{buildroot}%{_rpmconfigdir}/macros.d/macros.*-sip4 || \
  echo "%%requires_%{python3_prefix}_sip_api Requires: %{python_prefix}-sip(api) = %%python_sip_api_ver" >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.python_all-sip4
%endif
%{?python_compileall}
%{?!python_compileall:%python_exec -m compileall %{buildroot}%{$python_sitearch}}
%{?!python_compileall:%python_exec -O -m compileall %{buildroot}%{$python_sitearch}}
%python_clone -a %{buildroot}/%{_bindir}/sip
%python_expand %fdupes %{buildroot}%{$python_sitearch}
mkdir -p %{buildroot}%{_datadir}/sip

%post devel
%python_install_alternative sip

%postun devel
%python_uninstall_alternative sip

%files %{python_files}
%license LICENSE*
%doc ChangeLog NEWS
%doc build_%{python_bin_suffix}/README
%{python_sitearch}/sip.so
%if %{with pyqt4_module}
%dir %{python_sitearch}/PyQt4
%{python_sitearch}/PyQt4/sip.so
%endif
%if %{with pyqt5_module}
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/sip.so
%endif
%{python_sitearch}/sip-%{version}.dist-info/

%files %{python_files devel}
%license LICENSE*
%{_rpmconfigdir}/macros.d/macros.%{python_prefix}-sip4
%python_alternative %{_bindir}/sip
%if %{with pyqt4_module}
%dir %{python_sitearch}/PyQt4
%{python_sitearch}/PyQt4/sip.pyi
%endif
%if %{with pyqt5_module}
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/sip.pyi
%endif
%{_includedir}/python%{python_bin_suffix}*/sip.h
%{python_sitearch}/sipconfig.py*
%{python_sitearch}/sipdistutils.py*
%{python_sitearch}/sip.pyi
%pycache_only %{python_sitearch}/__pycache__/sipconfig.*.py*
%pycache_only %{python_sitearch}/__pycache__/sipdistutils.*.py*

%files -n python-%{pname}-doc
%license LICENSE*
%doc doc/

%files -n python-%{pname}-common
%license LICENSE*
%{_rpmconfigdir}/macros.d/macros.python_all-sip4
%dir %{_datadir}/sip/

%changelog
