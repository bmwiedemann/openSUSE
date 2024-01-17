#
# spec file for package libGLw
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


%define use_motif 1
%define libversion 1

Name:           libGLw
URL:            http://www.mesa3d.org
Provides:       Mesa:%{_libdir}/libGLw.so.1
Version:        8.0.0
Release:        0
%define date	20130123
%define sha1	c4f7cdf
Summary:        Xt/Motif OpenGL drawing area widget library
License:        MIT
Group:          Development/Libraries/C and C++
Source:         glw-%{version}_%{date}_%{sha1}.tar.bz2
Source1:        baselibs.conf
Patch1:         n_Use-newly-introduced-GLAPIVAR-for-variables.patch
# Needs to be set in buildservice project, see 'osc meta prjconf X11:XOrg'
# for an example
%if 0%{?use_motif} != 0
%define lname_m	libGLwM%{libversion}
BuildRequires:  openmotif-devel
%endif
%define lname	libGLw%{libversion}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)

%description
Xt/Motif OpenGL drawing area widget library shipped by the Mesa Project.

%package -n %lname
Summary:        Xt OpenGL drawing area widget library
# O/P added in 12.2
Group:          System/Libraries
Provides:       GLw%{libversion} = %version-%release
Provides:       MesaGLw = %version-%release
Obsoletes:      MesaGLw < %version-%release
Conflicts:      libGLwM%{libversion}

%description -n %lname
Xt OpenGL drawing area widget library shipped by the Mesa Project.

%package devel
Requires:       GLw%{libversion} = %version
Requires:       GLw%{libversion} = %version-%release
Requires:       pkgconfig(gl)
Summary:        Includes and more to develop MesaGLw applications
Group:          Development/Libraries/C and C++

%description devel
This package contains all necessary include files needed
to develop applications that require these.

%package -n %lname_m
Summary:        Motif OpenGL drawing area widget library
# O/P added in 12.2
Group:          System/Libraries
Provides:       GLw%{libversion} = %version-%release
Provides:       MesaGLw = %version-%release
Obsoletes:      MesaGLw < %version-%release
Conflicts:      libGLw%{libversion}
Requires:       openmotif

%description -n %lname_m
Motif OpenGL drawing area widget library shipped by the Mesa Project.

%prep
%autosetup -p1 -n glw-%{version}

%build
mkdir build-GLw; cd build-GLw; ln -sf ../configure
%{configure} --srcdir=../
%make_build OPT_FLAGS="%{optflags}"
%if 0%{?use_motif}
mkdir ../build-GLwM; cd ../build-GLwM; ln -sf ../configure
%{configure} --srcdir=../ --enable-motif
%make_build OPT_FLAGS="%{optflags}"
%endif

%install
%if 0%{?use_motif} != 0
cd build-GLwM
%make_install
i=$(echo %{buildroot}/%{_libdir}/libGLw.so.*.*.*); mv $i ${i/libGLw.so/libGLwM.so};
cd ..
%endif
cd build-GLw
%make_install
i=$(echo %{buildroot}/%{_libdir}/libGLw.so.*.*.*); mv $i ${i/libGLw.so/libGLwXT.so};
rm -f %{buildroot}/%{_libdir}/libGLw.la %{buildroot}/%{_libdir}/libGLw.a %{buildroot}/%{_libdir}/libGLw.so.? %{buildroot}/%{_libdir}/libGLw.so

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%doc README
%{_libdir}/libGLwXT.so.1.*

%files devel
/usr/include/GL
%{_libdir}/pkgconfig/glw.pc

%triggerin -n libGLw-devel -- %lname
ln -snf libGLw.so.1 %{_libdir}/libGLw.so

%triggerin -n libGLw-devel -- %lname_m
ln -snf libGLw.so.1 %{_libdir}/libGLw.so

%preun devel
 [ $1 -eq 0 ] && rm -f %{_libdir}/libGLw.so || true

%post -n %lname_m -p /sbin/ldconfig

%postun -n %lname_m -p /sbin/ldconfig

%if 0%{?use_motif}
%files -n %lname_m
%doc README
%{_libdir}/libGLwM.so.1.*

%endif

%changelog
