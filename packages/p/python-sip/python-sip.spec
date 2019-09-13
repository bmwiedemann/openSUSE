#
# spec file for package python-sip
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


%define python_sip_api 12.6
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sip
Version:        4.19.18
Release:        0
Summary:        SIP tool to use python sip bindings
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        https://www.riverbankcomputing.com/static/Downloads/sip/%{version}/sip-%{version}.tar.gz
# PATCH-FIX-OPENSUSE disable-rpaths.diff -- Disable rpaths
Patch0:         disable-rpaths.diff
# PATCH-FIX-OPENSUSE disable-strip.diff -- Disable stripping
Patch1:         disable-strip.diff
BuildRequires:  %{python_module devel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{name}-common = %{version}
Provides:       python-sip(api) = %{python_sip_api}
%python_subpackages

%description
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

%package devel
Summary:        SIP tool to create python bindings
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{name}-common = %{version}
Requires:       c++_compiler
Requires:       python-devel
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-bin = %{version}
Obsoletes:      %{name}-bin < %{version}

%description devel
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains all the developer tools you need to create your
own sip bindings.

%package -n %{name}-doc
Summary:        SIP tool to create python bindings -- common documentation
Group:          Development/Libraries/Python
Provides:       %{python_module sip-doc = %{version}}

%description  -n %{name}-doc
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains common documentation files shared between python2
and python3 versions of sip.

%package -n %{name}-common
Summary:        SIP tool to create python bindings -- common files
Group:          Development/Libraries/Python
Provides:       %{python_module sip-common = %{version}}

%description  -n %{name}-common
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
    LIBS+="-l$ldlibrary"

make %{?_smp_mflags}

# Point to the correct location for the documentation files
cp ../README ./
sed -i 's/"doc" directory/"doc" directory of package %{$python_prefix}-sip-devel/' README

popd
}

# Now build the PyQt4 sip module
%{python_expand mkdir build_PyQt4_%{$python_bin_suffix}
pushd build_PyQt4_%{$python_bin_suffix}

# Link against libpython
ldlibrary=`$python -c "import sysconfig as s;print(s.get_config_var('LDLIBRARY')[3:-3])"`
$python ../configure.py --debug \
  --sip-module=PyQt4.sip \
  CFLAGS+="%{optflags}" \
  CXXFLAGS+="%{optflags}" \
  LIBS+="-l$ldlibrary" \
  --no-dist-info

make %{?_smp_mflags}

popd
}

# Now build the PyQt5 sip module
%{python_expand mkdir build_PyQt5_%{$python_bin_suffix}
pushd build_PyQt5_%{$python_bin_suffix}

# Link against libpython (fixes bnc#756282 and bnc#721280)
ldlibrary=`$python -c "import sysconfig as s;print(s.get_config_var('LDLIBRARY')[3:-3])"`
$python ../configure.py --debug \
  --sip-module=PyQt5.sip \
  CFLAGS+="%{optflags}" \
  CXXFLAGS+="%{optflags}" \
  LIBS+="-l$ldlibrary" \
  --no-dist-info

make %{?_smp_mflags}

popd
}

%install
mkdir -p %{buildroot}%{_sysconfdir}/alternatives

%{python_expand pushd build_%{$python_bin_suffix}
%make_install
popd

# Prepare for update-alternatives usage
mv %{buildroot}%{_bindir}/sip %{buildroot}%{_bindir}/sip-%{$python_bin_suffix}
# Make sure the correct sip executable is picked
sed -i 's,%{_bindir}/sip,%{_bindir}/sip-%{$python_bin_suffix},' %{buildroot}%{python_sitearch}/sipconfig.py
}

%{python_expand pushd build_PyQt4_%{$python_bin_suffix}
%make_install
popd
}

%{python_expand pushd build_PyQt5_%{$python_bin_suffix}
%make_install
popd

%fdupes %{buildroot}%{python_sitearch}
}

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d

echo "%%python_sip_api_ver %{python_sip_api}" > %{buildroot}%{_rpmconfigdir}/macros.d/macros.python_all-sip

%if 0%{?have_python2}
echo "%%requires_python2_sip_api Requires: %{python2_prefix}-sip(api) = %%python_sip_api_ver" > %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{python2_prefix}-sip
echo "%%requires_python_sip_api Requires: %{python2_prefix}-sip(api) = %%python_sip_api_ver" >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{python2_prefix}-sip

%py_compile %{buildroot}%{python2_sitearch}
%endif

%if 0%{?have_python3}
echo "%%requires_python3_sip_api Requires: %{python3_prefix}-sip(api) = %%python_sip_api_ver" > %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{python3_prefix}-sip

%py3_compile %{buildroot}%{python3_sitearch}
%endif

%prepare_alternative sip
mkdir -p %{buildroot}%{_datadir}/sip

%post devel
%{python_install_alternative sip}

%postun devel
%python_uninstall_alternative sip

%files %{python_files}
%license LICENSE*
%doc ChangeLog NEWS
%doc build_%{python_bin_suffix}/README
%{python_sitearch}/sip.so
%dir %{python_sitearch}/PyQt4
%{python_sitearch}/PyQt4/sip.so
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/sip.so
%{python_sitearch}/sip-%{version}.dist-info/

%files %{python_files devel}
%license LICENSE*
%{_rpmconfigdir}/macros.d/macros.%{python_prefix}-sip
%python_alternative %{_bindir}/sip
%dir %{python_sitearch}/PyQt4
%{python_sitearch}/PyQt4/sip.pyi
%dir %{python_sitearch}/PyQt5
%{python_sitearch}/PyQt5/sip.pyi
%{_includedir}/python%{python_version}*/sip.h
%{python_sitearch}/sipconfig.py*
%{python_sitearch}/sipdistutils.py*
%{python_sitearch}/sip.pyi
%pycache_only %{python_sitearch}/__pycache__/sipconfig.*.py*
%pycache_only %{python_sitearch}/__pycache__/sipdistutils.*.py*

%files -n python-sip-doc
%license LICENSE*
%doc doc/

%files -n python-sip-common
%license LICENSE*
%{_rpmconfigdir}/macros.d/macros.python_all-sip
%{_datadir}/sip/

%changelog
