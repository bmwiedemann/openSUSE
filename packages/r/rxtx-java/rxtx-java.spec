#
# spec file for package rxtx-java
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define src_name rxtx
%define upver 2.2
%define prever pre2
%define libversion 2
%define force_aqute_bnd 0
Name:           rxtx-java
Version:        %{upver}~%{prever}
Release:        0
Summary:        Full Java CommAPI implementation
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            http://rxtx.qbang.org/wiki/index.php/Main_Page
Source0:        http://rxtx.qbang.org/pub/rxtx/%{src_name}-%{upver}%{prever}.zip
Source1:        rxtx-osgi.bnd
Patch0:         rxtx-java-arduinouno.diff
Patch1:         rxtx-java-disable-crazy-version-tests.diff
Patch2:         rxtx-java-error.diff
Patch4:         rxtx-java-sysio.patch
Patch5:         rxtx-java-38400.patch
Patch6:         rxtx-java-version.patch
Patch7:         rxtx-java-missing-javah.patch
Patch8:         rxtx-yield.patch
BuildRequires:  automake
BuildRequires:  java-devel >= 1.8
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  pkgconfig(lockdev)
Requires:       librxtx%{libversion}
Obsoletes:      %{name}-src
%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550 || %{force_aqute_bnd}
BuildRequires:  aqute-bnd
BuildRequires:  javapackages-local
%else
BuildRequires:  javapackages-tools
%endif
%if 0%{?mdkversion}
Patch3:         rxtx-java-formatstring.patch
%endif

%description
RxTx is a Java library, using a native implementation (via JNI), providing serial
and parallel communication for the Java Development Toolkit (JDK). It is based on
the specification for Sun's Java Communications API.

%package javadoc
Summary:        Javadocs for rxtx-java
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
RxTx is a Java library, using a native implementation (via JNI), providing serial
and parallel communication for the Java Development Toolkit (JDK). It is based on
the specification for Sun's Java Communications API.

%package -n librxtx%{libversion}
Summary:        Full Java CommAPI implementation native library
Group:          Development/Libraries/C and C++
Obsoletes:      librxtx%{libversion}-devel

%description -n librxtx%{libversion}
RxTx is a Java library, using a native implementation (via JNI), providing serial
and parallel communication for the Java Development Toolkit (JDK). It is based on
the specification for Sun's Java Communications API.

%prep
%setup -q -n %{src_name}-%{upver}%{prever}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if 0%{?mdkversion}
%patch3 -p1
%endif
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export THREADS_FLAG=native
rm acinclude.m4 config.guess config.sub install-sh ltmain.sh missing mkinstalldirs aclocal.m4 Makefile.in ltconfig stamp-h.in
./autogen.sh
CFLAGS="%{optflags}" LDFLAGS=-s \
	%configure \
%if 0%{?suse_version} > 1130
	--enable-liblock=yes
%endif

%make_build

%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550 || %{force_aqute_bnd}
# Inject OSGi metadata
bnd wrap -p %{SOURCE1} -v %{upver} -o RXTXcomm-bnd.jar RXTXcomm.jar
mv RXTXcomm-bnd.jar RXTXcomm.jar
%endif

# build javadoc
mkdir -p javadoc
javadoc -d javadoc src/gnu/io/*.java

%install
install -dm 0755 %{buildroot}%{_jnidir} %{buildroot}%{_libdir}
make RXTX_PATH=%{buildroot}%{_libdir} JHOME=%{buildroot}%{_jnidir} install
find %{buildroot} -type f -name "*.la" -delete -print

find %{buildroot}%{_prefix} -xtype f -print | \
    sed "s@^$RPM_BUILD_ROOT@@g" > INSTALLED_FILES

if [ "$(cat INSTALLED_FILES)X" = "X" ] ; then
    echo "No files!"
    exit -1
fi

# install javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r javadoc %{buildroot}%{_javadocdir}/%{name}/

%files
%doc AUTHORS ChangeLog README RMISecurityManager.html INSTALL PORTING TODO
%{_jnidir}/RXTXcomm.jar

%files javadoc
%dir %{_javadocdir}
%{_javadocdir}
%license COPYING

%files -n librxtx%{libversion}
%defattr(755,root,root)
%{_libdir}/*.so
%license COPYING

%changelog
