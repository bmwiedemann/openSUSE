#
# spec file for package libunity
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


%define sover   9
%define typelib typelib-1_0-Unity-7_0
%define typelib_extras typelib-1_0-UnityExtras-7_0
%define _version 7.1.4+19.04.20190319
Name:           libunity
Version:        7.1.4+bzr20190319
Release:        0
Summary:        Library for the Unity shell
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://launchpad.net/libunity
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE libunity-protocol-private-install.patch i@marguerite.su -- Unity can't find /usr/lib(64)/libunity/.
Patch0:         libunity-protocol-private-install.patch
# PATCH-FIX-UPSTREAM 0001-Fix-FTB-with-recent-vala-requiring-non-public-abstra.patch vala 0.46.1+ doesn't allow creation method of abstract class to be public
Patch1:         0001-Fix-FTB-with-recent-vala-requiring-non-public-abstra.patch
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python3
BuildRequires:  vala >= 0.22
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.3.93
BuildRequires:  pkgconfig(dee-1.0) >= 1.2.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.1
BuildRequires:  pkgconfig(lttng-ust)
%glib2_gsettings_schema_requires

%description
LibUnity is library for instrumenting and integrating with
all aspects of the Unity shell. This is not a library used
in the implementation of the Unity shell itself, but a
library to be consumed by clients that wants to do deep
integration with the Unity shell.

%package tools
Summary:        Unity tools
Group:          System/GUI/Other
Requires:       python3-%{name} = %{version}

%description tools
Tools for Unity instrumenting and integration library.

%package -n %{name}%{sover}
Summary:        Unity shared libraries
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{name}%{sover}
Shared libraries for Unity instrumenting and integration library.

%package -n %{typelib}
Summary:        Introspection bindings for the Unity shell library
Group:          System/Libraries

%description -n %{typelib}
This package provides the GObject Introspection bindings for libunity.

%package -n %{typelib_extras}
Summary:        Introspection bindings for the Unity shell library
Group:          System/Libraries

%description -n %{typelib_extras}
This package provides the GObject Introspection bindings for libunity.

%if 0%{?suse_version} >= 1500
%package -n python2-%{name}
%else
%package -n python-%{name}
%endif
Summary:        Python bindings for libunity
Group:          Development/Languages/Python
%if 0%{?suse_version} >= 1500
# python-libunity was last used in openSUSE Leap 42.3.
Provides:       python-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < %{version}-%{release}

%description -n python2-%{name}
%else

%description -n python-%{name}
%endif
Python bindings for Unity instrumenting and integration library.

%package -n python3-%{name}
Summary:        Python bindings for libunity
Group:          Development/Languages/Python

%description -n python3-%{name}
Python bindings for Unity instrumenting and integration library.

%package devel
Summary:        Development Headers for libunity
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       %{typelib_extras} = %{version}
Requires:       %{typelib} = %{version}

%description devel
This package provides development headers for libunity.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
for py in python python3; do
    dir="../%{name}-%{version}-$py/"
    mkdir -p "$dir"
    cp -aT . "$dir"
    pushd "$dir"
    export PYTHON="$py"
    %configure \
      --disable-static         \
      --disable-headless-tests
    make %{?_smp_mflags} V=1
    popd
done

%install
%make_install -C ../%{name}-%{version}-python
%make_install -C ../%{name}-%{version}-python3

# Ask for one specific Python version in unity-scopes/.
pushd %{buildroot}%{_datadir}/unity-scopes/
rm -rf *.pyc *.pyo __pycache__/
chmod a+x *
sed -i '1s|^#!.*$|#!%{_bindir}/python3|' *.py
%py3_compile .
popd

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}/
%fdupes %{buildroot}%{python3_sitearch}/
%fdupes %{buildroot}%{python_sitearch}/

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post tools
%glib2_gsettings_schema_post

%postun tools
%glib2_gsettings_schema_postun
%endif

%files tools
%if 0%{?suse_version} >= 1500
%license COPYING COPYING.GPL-3
%else
%doc COPYING COPYING.GPL-3
%endif
%doc AUTHORS NEWS README
%{_bindir}/libunity-tool
%{_bindir}/unity-scope-loader
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.Lenses.gschema.xml
%{_datadir}/unity-scopes/
%{_datadir}/unity/

%files -n %{name}%{sover}
%{_libdir}/%{name}.so.%{sover}*
%{_libdir}/%{name}?*.so.*

%files -n %{typelib}
%{_libdir}/girepository-1.0/Unity-7.0.typelib

%files -n %{typelib_extras}
%{_libdir}/girepository-1.0/UnityExtras-7.0.typelib

%if 0%{?suse_version} >= 1500
%files -n python2-%{name}
%else
%files -n python-%{name}
%endif
%dir %{python_sitearch}/gi/
%dir %{python_sitearch}/gi/overrides/
%{python_sitearch}/gi/overrides/Unity.py*

%files -n python3-%{name}
%dir %{python3_sitearch}/gi/
%dir %{python3_sitearch}/gi/overrides/
%{python3_sitearch}/gi/overrides/Unity.py*
%dir %{python3_sitearch}/gi/overrides/__pycache__/
%{python3_sitearch}/gi/overrides/__pycache__/Unity.*

%files devel
%{_includedir}/unity/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/unity*

%changelog
