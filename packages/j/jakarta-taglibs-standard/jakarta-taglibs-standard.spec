#
# spec file for package jakarta-taglibs-standard
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define short_name      taglibs-standard
Name:           jakarta-taglibs-standard
Version:        1.1.1
Release:        0
Summary:        Open Source Implementation of the JSP Standard Tag Library
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://tomcat.apache.org/taglibs/
Source0:        jakarta-taglibs-standard-%{version}-src.tar.bz2
Patch0:         %{name}-%{version}-build.patch
Patch1:         %{name}-java6-compatibility.patch
Patch2:         %{name}-%{version}-remove-enums.patch
Patch3:         jakarta-taglibs-standard-java7.patch
Patch4:         CVE-2015-0254.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  servletapi5
BuildRequires:  xalan-j2
Requires:       servletapi5 >= 5.0.16
Requires:       xalan-j2
BuildArch:      noarch

%description
This package contains releases for the 1.1.x versions of the Standard
Tag Library, Jakarta Taglibs's open source implementation of the JSP
Standard Tag Library (JSTL), version 1.1. JSTL is a standard under the
Java Community Process.

%package        javadoc
Summary:        Javadoc for jakarta-taglibs-standard
Group:          Development/Libraries/Java

%description    javadoc
This package contains the javadoc documentation for Jakarta Taglibs.

%prep
%setup -q -n %{name}-%{version}-src
%patch0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -p1
%patch4 -p1

cat > build.properties <<EOBP
build.dir=build
dist.dir=dist
servlet24.jar=$(build-classpath servletapi5)
jsp20.jar=$(build-classpath jspapi)
xalan.jar=$(build-classpath xalan-j2)
EOBP

%build
ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -f standard/build.xml \
  dist

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p standard/dist/standard/lib/jstl.jar %{buildroot}%{_javadir}/jakarta-taglibs-core-%{version}.jar
cp -p standard/dist/standard/lib/standard.jar %{buildroot}%{_javadir}/jakarta-taglibs-standard-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr standard/dist/standard/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc standard/README_src.txt standard/README_bin.txt standard/dist/doc/doc/standard-doc/*.html
%{_javadir}/*

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
