#
# spec file for package sblim-cim-client2
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


%define project_folder %{name}-%{version}-src
%define archive_folder build
Name:           sblim-cim-client2
Version:        2.2.5
Release:        0
Summary:        Java CIM Client library
License:        EPL-1.0
Group:          Development/Libraries/Java
Url:            http://sourceforge.net/projects/sblim/
Source:         http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip
Source1:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-doc.zip
Patch1:         sblim-cim-client2-2.2.5-src.patch
BuildRequires:  ant >= 1.6
BuildRequires:  dos2unix
BuildRequires:  java-devel
BuildRequires:  jpackage-utils >= 1.5.32
BuildRequires:  unzip
Requires:       jpackage-utils >= 1.5.32
Obsoletes:      sblim-cim-client <= 1.3.5
Provides:       sblim-cim-client
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
%endif
%if 0%{?suse_version}
BuildRequires:  jaxp_parser_impl
BuildRequires:  update-alternatives
BuildRequires:  xml-commons-apis
%if 0%{?suse_version} < 1100
BuildRequires:  java-1_5_0-ibm-devel
BuildRequires:  java-1_5_0-ibm-fonts
%endif
%endif

%description
The purpose of this package is to provide a CIM Client Class Library
for Java applications. It complies to the DMTF standard CIM Operations
over HTTP and intends to be compatible with JCP JSR48 once it becomes
available. To learn more about DMTF visit http://www.dmtf.org. More
infos about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for sblim-cim-client2
Group:          Development/Libraries/Java

%description javadoc
Javadoc for sblim-cim-client2.

%package manual
Summary:        Manual and sample code for sblim-cim-client2
Group:          Development/Libraries/Java

%description manual
Manual and sample code for sblim-cim-client2.

%prep
%setup -q -n %{project_folder}
dos2unix COPYING NEWS README ChangeLog sblim-cim-client2.properties sblim-slp-client2.properties
find -type f \( -name "*.java" \) -exec dos2unix {} +
%if 0%{?suse_version} > 1200
# openjdk9 needs source and target 1.6 or larger
%patch1 -p1
%endif
# -----------------------------------------------------------------------------

%build
# export CLASSPATH=$(build-classpath)
export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version}\
        package java-doc
# -----------------------------------------------------------------------------

%install
# --- documentation ---
dstDocDir=%{buildroot}%{_docdir}/%{name}-%{version}
install -d $dstDocDir
install --mode=644 ChangeLog COPYING README NEWS $dstDocDir
# --- samples (also into _docdir) ---
cp -pr  smpl/org $dstDocDir
# --- config files ---
confDir=%{buildroot}%{_sysconfdir}/java
install -d $confDir
install --mode=664 sblim-cim-client2.properties sblim-slp-client2.properties $confDir
# --- jar ---
install -d %{buildroot}%{_javadir}
install %{archive_folder}/lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(
  cd %{buildroot}%{_javadir} &&
    ln -sf %{name}-%{version}.jar %{name}.jar;
)
# --- javadoc ---
mkdir -p %{buildroot}%{_javadocdir}
(cd %{buildroot}%{_javadocdir}; unzip %{SOURCE1})
#fix EOL encoding
find %{buildroot}%{_javadocdir}/%{name}-%{version}-doc -type f -exec sed -i 's/\r//' {} \;

install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr %{archive_folder}/doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%if 0%{?suse_version} > 1010
%fdupes %{buildroot}
%endif
# -----------------------------------------------------------------------------

%files
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/java/sblim-cim-client2.properties
%config %{_sysconfdir}/java/sblim-slp-client2.properties
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(0644,root,root,0755)
%docdir %{_javadocdir}/%{name}-%{version}-doc
%docdir %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}-%{version}-doc
%doc %{_javadocdir}/%{name}-%{version}

%files manual
%defattr(0644,root,root,0755)
%docdir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}
# -----------------------------------------------------------------------------

%changelog
