#
# spec file for package eclipse-swt
#
# Copyright (c) 2025 SUSE LLC
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


%global major_version   4
%if %{__isa_bits} == 32
%global minor_version   9
%global other_minor_version 29
%else
%global minor_version   29
%global other_minor_version 9
%endif
%global tag R%{major_version}_%{minor_version}
%global other_tag R%{major_version}_%{other_minor_version}
%global swtsrcdir       bundles/org.eclipse.swt
Name:           eclipse-swt
Version:        %{major_version}.%{minor_version}
Release:        0
Summary:        Eclipse SWT: The Standard Widget Toolkit for GTK+
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/eclipse-platform/eclipse.platform.swt
Source0:        https://codeload.github.com/eclipse-platform/eclipse.platform.swt/tar.gz/refs/tags/%{tag}#/eclipse.platform.swt-%{tag}.tar.gz
Source1:        classpath.xls
Source2:        https://github.com/eclipse-platform/eclipse.platform.swt/raw/refs/tags/R4_29/LICENSE
Source3:        https://github.com/eclipse-platform/eclipse.platform.swt/raw/refs/tags/R4_29/NOTICE
# These two are the other sources, listed here to appease bots
Source100:      https://codeload.github.com/eclipse-platform/eclipse.platform.swt/tar.gz/refs/tags/%{other_tag}#/eclipse.platform.swt-%{other_tag}.tar.gz
Source101:      eclipse-swt-avoid-javascript-at-build-%{major_version}_%{other_minor_version}.patch
Source102:      eclipse-swt-gcc15-%{major_version}_%{other_minor_version}.patch
Patch0:         eclipse-swt-avoid-javascript-at-build-%{major_version}_%{minor_version}.patch
Patch1:         eclipse-swt-rm-eclipse-tasks-and-customize-build.patch
Patch2:         eclipse-swt-fedora-build-native.patch
Patch3:         eclipse-gcc10.patch
Patch4:         eclipse-swt-no-werror.patch
Patch5:         eclipse-swt-gcc15-%{major_version}_%{minor_version}.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  webkit2gtk3-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xt)
Obsoletes:      %{name}-bootstrap

%description
SWT is an open source widget toolkit for Java designed to provide
efficient, portable access to the user-interface facilities of the
operating systems on which it is implemented.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n eclipse.platform.swt-%{tag}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%if %{__isa_bits} == 32
%patch -P 3 -p2
%else
%patch -P 4 -p1
%endif
%patch -P 5 -p1
mkdir -p %{swtsrcdir}/tasks
cp %{SOURCE1} %{swtsrcdir}/tasks
cp %{SOURCE2} %{SOURCE3} .

cp %{swtsrcdir}/Eclipse\ SWT/common/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT/common/version.txt %{swtsrcdir}/
cp %{swtsrcdir}/Eclipse\ SWT\ PI/{common,cairo}/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ OpenGL/glx/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ WebKit/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/
cp %{swtsrcdir}/Eclipse\ SWT\ AWT/gtk/library/* %{swtsrcdir}/Eclipse\ SWT\ PI/gtk/library/

%build

cd %{swtsrcdir}

# Build native part
export SWT_LIB_DEBUG=1
export CFLAGS="%{optflags} -fPIC"
export LFLAGS="${RPM_LD_FLAGS}"
ant -f buildSWT.xml build_local \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dbuild_dir=Eclipse\ SWT\ PI/gtk/library \
    -Dtargets="-gtk3 install" -Dclean= -Dcflags="%{optflags}" \
    -Dlflags="${RPM_LD_FLAGS}" -Dswt.arch=%{_arch}

# Build Java part
ant -f buildSWT.xml check_compilation_all_platforms \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Drepo.src=../../

# Build Jar file
ant -f build.xml \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8

%install
# Install Maven metadata for SWT
# jar
JAR=%{swtsrcdir}/org.eclipse.swt_*.jar
VER=$(echo $JAR | sed -e "s/.*_\(.*\)\.jar/\1/")
install -dm 0755 %{buildroot}%{_jnidir}/eclipse
install -pm 0644 %{swtsrcdir}/org.eclipse.swt_*.jar %{buildroot}%{_jnidir}/swt.jar
ln -s -f ../swt.jar %{buildroot}%{_jnidir}/eclipse/swt.jar
%add_maven_depmap "org.eclipse.swt:org.eclipse.swt:jar:$VER" swt.jar -a "org.eclipse.swt:swt"
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r %{swtsrcdir}/docs/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# fix so permissions
find %{swtsrcdir}/*.so -name *.so -exec chmod a+x {} \;

install -d 755 %{buildroot}/%{_libdir}/%{name}
cp -a %{swtsrcdir}/*.so %{buildroot}/%{_libdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%{_jnidir}/eclipse
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
