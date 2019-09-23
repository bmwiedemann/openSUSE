#
# spec file for package eclipse-swt
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


%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
%define	        version_suffix 4.3.3.3
%define	        so_suffix 4333
%define         libswt_version 4.333
Name:           eclipse-swt
Version:        4.3.1
Release:        0
Summary:        SWT Library for GTK2
License:        EPL-1.0
Group:          Development/Libraries/Other
URL:            http://www.eclipse.org/swt/
Source0:        libswt-%{libswt_version}.tar.bz2
Source1:        org.eclipse.swt-%{version}.tar.bz2
Source2:        build.xml
Patch0:         libswt-optflags.patch
Patch1:         libswt-includes.patch
Patch2:         libswt-build.patch
Patch3:         libswt-plugindir.patch
Patch4:         ppc64le.patch
Patch5:         ppc64le_path_for_jre_1_7_0.patch
Patch6:         libswt-4.333-libjawt.patch
Patch7:         libswt-bootclasspath.patch
Patch8:         aarch64.patch
BuildRequires:  Mesa-devel
BuildRequires:  ant
BuildRequires:  cairo
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  mozilla-nspr-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glu)
Requires:       java >= 1.8
Provides:       libswt3-gtk2 = %{version}

%description
SWT is the software component that delivers native widget functionality
for the Eclipse platform in an operating system independent manner.  It
is analogous to AWT/Swing in Java with a difference - SWT uses a rich
set of native widgets.

%prep
%setup -q -n libswt-%{libswt_version}
%patch0
%patch1
%patch2
pushd org/eclipse
tar -xjf %{SOURCE1}
%patch3
%patch7
popd
%patch4
%patch5 -p1
%patch6 -p1
%patch8
pushd org/eclipse/swt
cp %{SOURCE2} .
# remove all third party jars
find . -iname '*.jar' | xargs rm -rf
popd

%build
export LIBDIR=%{_libdir}
export NO_STRIP=TRUE
export JAVA_HOME="%{_sysconfdir}/alternatives/java_sdk"
./build.sh

pushd org/eclipse/swt
%{ant} -v \
%ifnarch %{ix86} %{aarch64} %{arm} ppc64le
    -Dswt.arch=%{_arch} \
%else
  %ifarch %{ix86}
    -Dswt.arch=x86 \
  %endif
  %ifarch %{arm}
    -Dswt.arch=arm \
  %endif
  %ifarch %{aarch64}
    -Dswt.arch=aarch64 \
  %endif
  %ifarch ppc64le
    -Dswt.arch=ppc64 \
  %endif
%endif
    -DjavacTarget=8 -DjavacSource=8 \
    -Dversion.suffix=%{version_suffix} \
    -Djar.filename=swt-%{version}.jar \
    build.jars
rm build.xml
popd
jar uf org/eclipse/swt/swt-%{version}.jar *.so

%install
install -d -m755 %{buildroot}%{_libdir}/eclipse
install -m644 *.so %{buildroot}%{_libdir}/eclipse
install -D -m644 org/eclipse/swt/swt-%{version}.jar %{buildroot}%{_jnidir}/swt-gtk-%{version}.jar
pushd %{buildroot}%{_libdir}/eclipse
  for i in atk-gtk awt-gtk cairo-gtk glx-gtk gtk gnome-gtk pi-gtk webkit-gtk; do
    ln -sf libswt-"$i"-%{so_suffix}.so libswt-"$i".so;
    ln -sf libswt-"$i"-%{so_suffix}.so swt-"$i".so;
  done
popd
pushd %{buildroot}%{_jnidir}
  ln -sf swt-gtk-%{version}.jar swt.jar
  ln -sf swt-gtk-%{version}.jar swt-gtk.jar
popd

%files
%{_libdir}/eclipse
%{_jnidir}
%doc about_files/*

%changelog
