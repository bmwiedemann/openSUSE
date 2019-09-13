#
# spec file for package netbeans-svnclientadapter
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


%global __jar_repack %{nil}
%global nb_            netbeans
%global nb_org         %{nb_}.org
%global nb_ver         6.7.1
%global svnCA          svnClientAdapter
%global svnCA_ver      1.6.0
Name:           netbeans-svnclientadapter
Version:        %{nb_ver}
Release:        0
Summary:        Subversion Client Adapter
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://subclipse.tigris.org/svnClientAdapter.html
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export --force --username guest -r4383 \
#     http://subclipse.tigris.org/svn/subclipse/trunk/svnClientAdapter/ \
#     svnClientAdapter-1.6.0
# tar -czvf svnClientAdapter-1.6.0.tar.gz svnClientAdapter-1.6.0
Source0:        %{svnCA}-%{svnCA_ver}.tar.bz2
Patch0:         %{svnCA}-%{svnCA_ver}-build.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-tools
BuildRequires:  subversion-javahl
Requires:       java >= 1.6.0
Requires:       javapackages-tools
Requires:       subversion
BuildArch:      noarch

%description
SVNClientAdapter is a high-level Java API for Subversion.

%prep
%setup -q -n %{svnCA}-%{svnCA_ver}

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -p1 -b .sav

ln -s -f %{_javadir}/svnkit-javahl.jar lib/svnjavahl.jar

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
ant \
    -verbose \
	-DtargetJvm=1.6 \
	svnClientAdapter.jar

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/svnClientAdapter.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc license.txt readme.txt
%{_javadir}/*

%changelog
