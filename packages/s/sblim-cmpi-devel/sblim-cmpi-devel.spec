#
# spec file for package sblim-cmpi-devel
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sblim-cmpi-devel
Version:        2.0.3
Release:        0
Url:            http://sblim.sf.net/
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
Provides:       cmpi-devel
Conflicts:      tog-pegasus < 2.11
Source0:        http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Source1:        Doxyfile
%if 0%{?mandriva_version}
Patch:          mandriva-docdir.patch
%else
Patch:          opensuse-docdir.patch
%endif
Patch1:         old-gcc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        SBLIM CMPI Provider Development Support
License:        EPL-1.0
Group:          Development/Libraries/C and C++

%description
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for C++
provider development it is also necessary to have tog-pegasus-devel
installed.



%package -n sblim-cmpi-c++-devel
Summary:        SBLIM CMPI Provider Development Support
Group:          Development/Libraries/C and C++
Requires:       %{name}
Requires:       libcmpiCppImpl0
Conflicts:      tog-pegasus

%description -n sblim-cmpi-c++-devel
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for C++
provider development it is also necessary to have tog-pegasus-devel
installed.



%package -n libcmpiCppImpl0
Summary:        SBLIM CMPI Provider Development Support
Group:          Development/Libraries/C and C++
Conflicts:      tog-pegasus

%description -n libcmpiCppImpl0
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for C++
provider development it is also necessary to have tog-pegasus-devel
installed.


%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%define cmpi_docdir %_docdir/%{name}-%{version}
%else
%define cmpi_docdir %_docdir/%{name}
%endif

%prep
%setup -T -b 0 -n %{name}-%{version}
%if 0%{?suse_version} || 0%{?mandriva_version}
# adapt docdir
%patch
%endif
%patch1 -p1

cp %{_sourcedir}/Doxyfile %{_builddir}/%{name}-%{version}/
mkdir %{_builddir}/%{name}-%{version}/autodocs

%build
autoreconf --verbose --force --install
%configure
make %{?_smp_mflags}
doxygen Doxyfile

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcmpiCppImpl.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcmpiCppImpl.la
mkdir -p $RPM_BUILD_ROOT/%{cmpi_docdir}
cp -r autodocs/ $RPM_BUILD_ROOT/%{cmpi_docdir}

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc %{cmpi_docdir}
%dir %{_includedir}/cmpi
%{_includedir}/cmpi/[a-z]*

%files -n sblim-cmpi-c++-devel
%defattr(-,root,root)
%{_libdir}/libcmpiCppImpl.so
%dir %{_includedir}/cmpi
%{_includedir}/cmpi/[A-Z]*

%files -n libcmpiCppImpl0
%defattr(-,root,root)
%{_libdir}/libcmpiCppImpl.so.0*

%post -n libcmpiCppImpl0 -p /sbin/ldconfig

%postun -n libcmpiCppImpl0 -p /sbin/ldconfig

%changelog
