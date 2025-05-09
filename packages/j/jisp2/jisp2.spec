#
# spec file for package jisp2
#
# Copyright (c) 2024 SUSE LLC
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
Name:           jisp2
Version:        2.5.1
Release:        0
Summary:        The Java Indexed Serialization Package
License:        Libpng
Group:          Development/Libraries/Java
URL:            http://www.coyotegulch.com/jisp/
Source0:        jisp-2.5.1-source.tar.bz2
Patch0:         jisp2-2.5.1-java5-enum.patch
Patch1:         jisp2-2.5.1-javac-flags.patch
Patch2:         jisp2-2.5.1-reproducible-jar-mtime.patch
# jisp-3.0.0 won't work with jakarta-turbine-jcs
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  make
Requires:       javapackages-tools
Requires(post): update-alternatives
Requires(pre):  update-alternatives
Provides:       hibernate_in_process_cache
BuildArch:      noarch

%description
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%package demo
Summary:        The Java Indexed Serialization Package
Group:          Development/Libraries/Java

%description demo
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%package javadoc
Summary:        The Java Indexed Serialization Package
Group:          Development/Libraries/Java

%description javadoc
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%prep
%setup -q -n jisp-%{version}
%patch -P 0 -p1
sed -i -e 's/\r$//g' svfl.txt
%patch -P 1 -b .java-cflags
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
%patch -P 2 -p1
%endif

%build
export CLASSPATH=
%make_build JAVAC_FLAGS=" -target 1.8 -source 1.8"
%make_build jars
%make_build docs

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p jisp.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
# demo
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}/lib
cp jisp-demo.jar %{buildroot}%{_datadir}/%{name}-%{version}/lib
cp *.java %{buildroot}%{_datadir}/%{name}-%{version}
cp *.txt %{buildroot}%{_datadir}/%{name}-%{version}
# hibernate_in_process_cache ghost symlink
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/hibernate_in_process_cache.jar %{buildroot}%{_javadir}/hibernate_in_process_cache.jar

%post
%{_sbindir}/update-alternatives --install %{_javadir}/hibernate_in_process_cache.jar \
  hibernate_in_process_cache %{_javadir}/%{name}.jar 30

%preun
if [ "$1" = "0" ]; then
  %{_sbindir}/update-alternatives --remove hibernate_in_process_cache %{_javadir}/%{name}.jar
fi

%files
%defattr(0644,root,root,0755)
%doc svfl.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/hibernate_in_process_cache.jar
%ghost %{_sysconfdir}/alternatives/hibernate_in_process_cache.jar

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-%{version}

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
