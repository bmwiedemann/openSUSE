#
# spec file for package libGLw
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define use_motif 1
%define libversion 1

Name:           libGLw
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
Url:            http://www.mesa3d.org
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xt/Motif OpenGL drawing area widget library shipped by the Mesa Project.



Authors:
--------
    Brian Paul

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
Requires:       pkgconfig(gl)
Summary:        Includes and more to develop MesaGLw applications
Group:          Development/Libraries/C and C++

%description devel
This package contains all necessary include files needed
to develop applications that require these.

%if 0%{?use_motif} != 0

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

%endif

%prep
%setup -q -n glw-%{version}
%patch1 -p1

%build
%__mkdir build-GLw; cd build-GLw; %{__ln_s} -f ../configure
%{configure} --srcdir=../
%__make %{?_smp_mflags} OPT_FLAGS="$RPM_OPT_FLAGS"
%if 0%{?use_motif} != 0
%__mkdir ../build-GLwM; cd ../build-GLwM; %{__ln_s} -f ../configure
%{configure} --srcdir=../ --enable-motif
%__make %{?_smp_mflags} OPT_FLAGS="$RPM_OPT_FLAGS"
%endif

%install
%if 0%{?use_motif} != 0
cd build-GLwM
DESTDIR=$RPM_BUILD_ROOT %__make install
i=$(echo $RPM_BUILD_ROOT%{_libdir}/libGLw.so.*.*.*); mv $i ${i/libGLw.so/libGLwM.so};
cd ..
%endif
cd build-GLw
DESTDIR=$RPM_BUILD_ROOT %__make install
i=$(echo $RPM_BUILD_ROOT%{_libdir}/libGLw.so.*.*.*); mv $i ${i/libGLw.so/libGLwXT.so};
rm -f $RPM_BUILD_ROOT/%{_libdir}/libGLw.la $RPM_BUILD_ROOT/%{_libdir}/libGLw.a $RPM_BUILD_ROOT/%{_libdir}/libGLw.so.? $RPM_BUILD_ROOT/%{_libdir}/libGLw.so

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc README
%{_libdir}/libGLwXT.so.* 

%files devel
%defattr(-,root,root)
/usr/include/GL
%{_libdir}/pkgconfig/glw.pc

%post devel
ln -sf $(readlink %{_libdir}/libGLw.so.%{libversion}) %{_libdir}/libGLw.so

%preun devel
 [ $1 -eq 0 ] && rm -f %{_libdir}/libGLw.so || true

%if 0%{?use_motif} != 0

%post -n %lname_m -p /sbin/ldconfig

%postun -n %lname_m -p /sbin/ldconfig

%files -n %lname_m
%defattr(-,root,root)
%doc README
%{_libdir}/libGLwM.so.1*

%endif

%clean
rm -rf build-GLwM build-GLw

%changelog
