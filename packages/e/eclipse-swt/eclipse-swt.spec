#
# spec file for package eclipse-swt
#
# Copyright (c) 2020 SUSE LLC
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


%global eb_commit       44643cbda3dfd6f00fbf1b346dae7068df2a9ef9
%global eclipse_date    20180906
%global eclipse_time    0745
%global short_version   4.9
%global eclipse_tag     I%{eclipse_date}-%{eclipse_time}
%define __requires_exclude .*SUNWprivate_1\\.1.*
%ifarch %{ix86}
    %global eclipse_arch x86
%else
%ifarch %{arm}
    %global eclipse_arch arm
%else
%ifarch ppc64 ppc64p7
    %global eclipse_arch ppc64
%else
    %global eclipse_arch %{_arch}
%endif
%endif
%endif
Name:           eclipse-swt
Version:        %{short_version}.0
Release:        0
Summary:        SWT Library for GTK+
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/
# eclipse-create-tarball.sh
Source0:        eclipse-platform-sources-%{short_version}-clean.tar.xz
Source1:        http://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/snapshot/org.eclipse.linuxtools.eclipse-build-%{eb_commit}.tar.xz
Source10:       eclipse-swt-build.xml
Source100:      eclipse-create-tarball.sh
Patch4:         eclipse-secondary-arches.patch
Patch5:         eclipse-swt-optflags.patch
Patch33:        eclipse-ppc64.patch
Patch35:        eclipse-arm32.patch
Patch39:        eclipse-gcc10.patch
BuildRequires:  ant >= 1.10.5
BuildRequires:  gcc
BuildRequires:  javapackages-local
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rhino
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xt)
BuildConflicts: java-devel >= 9
Requires:       atk
Requires:       cairo
Requires:       gtk2
Requires:       libglvnd
Obsoletes:      %{name}-bootstrap
# Upstream Eclipse no longer supports non-64bit arches
ExclusiveArch:  s390 %{arm} %{ix86}

%description
SWT is the software component that delivers native widget functionality
for the Eclipse platform in an operating system independent manner.  It
is analogous to AWT/Swing in Java with a difference - SWT uses a rich
set of native widgets.

%prep
%setup -q -n eclipse-platform-sources-%{eclipse_tag}

# Extract linuxtools/eclipse-build sources
tar --strip-components=1 -xf %{SOURCE1}

cp %{SOURCE10} build.xml

%patch4 -p1
%patch5
%patch33 -p1
%patch35 -p1
%patch39 -p1

# This part generates secondary fragments using primary fragments
utils/ensure_arch.sh eclipse.platform.swt.binaries/bundles x86 arm
utils/ensure_arch.sh eclipse.platform.swt.binaries/bundles x86_64 aarch64 ppc64

%{mvn_alias} "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%{mvn_file} "org.eclipse.swt:org.eclipse.swt" swt
%{mvn_file} :{*} eclipse/@1

%build
export CLASSPATH=$(build-classpath js)
ant -Dswt.arch=%{eclipse_arch}

%{mvn_artifact} eclipse.platform.swt/bundles/org.eclipse.swt/pom.xml org.eclipse.swt.gtk.linux.%{eclipse_arch}.jar

%install
%mvn_install

%files -f .mfiles

%changelog
