#
# spec file for package python-dbus-python
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


%{?!python_module:%define python_module() python3-%{**}}
# expand separate from Provides/Obsoletes tags, because these are later duplicated by the python_subpackages macro
%define python_add_provides %{python_provides}
Name:           python-dbus-python
Version:        1.3.2
Release:        0
Summary:        Python bindings for D-Bus
License:        MIT
Group:          Development/Libraries/Python
URL:            https://www.freedesktop.org/wiki/Software/DBusBindings/
Source:         https://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
Source2:        https://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz.asc
Source99:       python-dbus-python-rpmlintrc
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(dbus-1) >= 1.8.0
BuildRequires:  pkgconfig(dbus-glib-1)
Requires:       python-gobject
Requires:       python-xml
%requires_ge    dbus-1
Provides:       dbus-1-%{python_flavor} = %{version}
Obsoletes:      dbus-1-%{python_flavor} < %{version}
%if "%{?python_provides}" != ""
# additional provider for python2 --> python and python38 --> python3
Provides:       dbus-1-%{python_add_provides} = %{version}
Obsoletes:      dbus-1-%{python_add_provides} < %{version}
%endif
%python_subpackages

%description
D-Bus python bindings for use with python programs.

%package devel
Summary:        Python bindings for D-Bus -- development files
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel
%requires_ge    dbus-1
%requires_ge    dbus-1-devel
Provides:       dbus-1-%{python_flavor}-devel = %{version}
Obsoletes:      dbus-1-%{python_flavor}-devel < %{version}
%if "%{?python_provides}" != ""
# additional provider for python2 --> python and python38 --> python3
Provides:       dbus-1-%{python_add_provides}-devel = %{version}
Obsoletes:      dbus-1-%{python_add_provides}-devel < %{version}
%endif

%description devel
D-Bus python bindings for use with python programs.

This package contains the development files for
Python bindings for D-Bus.

%package -n %{name}-common-devel
Summary:        Python bindings for D-Bus -- shared development files
Group:          Development/Libraries/Python
Requires:       dbus-1-devel
Requires:       pkgconfig(dbus-1) >= 1.6.0
Requires:       pkgconfig(dbus-glib-1)
Provides:       %{python_module dbus-python-common-devel = %{version}}

%description -n %{name}-common-devel
D-Bus python bindings for use with python programs.

This package contains development files shared between
the Python2 and Python3 versions of the bindings.

%prep
%setup -q -n dbus-python-%{version}
# Remove Makefile* (fix rpmlint warning "makefile-junk")
rm -f examples/Makefile*
# Remove shebang from examples
sed -i '1 {\|^#!%{_bindir}/env| d}' examples/*.py

%build
export CFLAGS="%{optflags} -fstack-protector -fno-strict-aliasing -fPIC"
%define _configure ../configure

%{python_expand mkdir build_%{$python_bin_suffix}
pushd build_%{$python_bin_suffix}

%configure PYTHON=%{_bindir}/$python
%make_build

popd

}

%check
%{python_expand pushd build_%{$python_bin_suffix}

make check

popd
}

%install
%{python_expand pushd build_%{$python_bin_suffix}

%make_install

popd

# Remove libtool config files
rm -f %{buildroot}%{$python_sitearch}/*.la

#avoid conflicts with multiple Python flavors
cp %{buildroot}%{_includedir}/dbus-1.0/dbus/dbus-python.h \
   %{buildroot}%{_includedir}/dbus-1.0/dbus/dbus-python-%{$python_bin_suffix}.h
cp %{buildroot}%{_libdir}/pkgconfig/dbus-python.pc \
   %{buildroot}%{_libdir}/pkgconfig/dbus-python-%{$python_bin_suffix}.pc
}

%{python_expand # Check to make sure all Python flavor versions of the header file and pkgconfig file are the same
if [ ! cmp --silent %{buildroot}%{_includedir}/dbus-1.0/dbus/dbus-python{,-%{$python_bin_suffix}}.h ] ; then
    echo "pkgconfig files are different between python flavors"
    exit 1
fi
if [ ! cmp --silent %{buildroot}%{_libdir}/pkgconfig/dbus-python{,-%{$python_bin_suffix}}.pc ] ; then
    echo "pkgconfig files are different between python flavors"
    exit 1
fi
}

%{python_expand # link all to the same file
mv %{buildroot}%{_includedir}/dbus-1.0/dbus/dbus-python{-%{$python_bin_suffix},}.h
mv %{buildroot}%{_libdir}/pkgconfig/dbus-python{-%{$python_bin_suffix},}.pc

ln -s %{_includedir}/dbus-1.0/dbus/dbus-python.h \
      %{buildroot}%{_includedir}/dbus-1.0/dbus/dbus-python-%{$python_bin_suffix}.h
ln -s %{_libdir}/pkgconfig/dbus-python.pc \
      %{buildroot}%{_libdir}/pkgconfig/dbus-python-%{$python_bin_suffix}.pc
}

%fdupes %{buildroot}

%files %{python_files}
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{python_sitelib}/dbus/
%{python_sitearch}/_dbus_bindings.so
%{python_sitearch}/_dbus_glib_bindings.so

%files %{python_files devel}
%license COPYING
%doc AUTHORS
%{_includedir}/dbus-1.0/dbus/dbus-python-%{python_bin_suffix}.h
%{_libdir}/pkgconfig/dbus-python-%{python_bin_suffix}.pc

%files -n %{name}-common-devel
%license COPYING
%doc AUTHORS
%doc doc/ examples/
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
