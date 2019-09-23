#
# spec file for package gnu-jaf
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


%define official_name activation
Name:           gnu-jaf
Version:        1.1.1
Release:        0
Summary:        GNU implementation of the JavaBeans Activation Framework
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            http://java.sun.com/products/javabeans/glasgow/jaf.html
Source:         %{official_name}-%{version}.tar.bz2
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  java-devel >= 1.8
BuildRequires:  unzip
Requires(post): update-alternatives
Provides:       jaf = %{version}
Obsoletes:      jaf <= 1.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
GNU JAF is a framework for declaring what beans operate on what MIME
type data. Content handler beans can be defined to handle particular
MIME content. The JAF unites internet standards for declaring content
with JavaBeans. The JAF defines two mechanisms within the framework.
The first, the file type map, specifies the MIME content type for a
given file. The default implementation of this uses the UNIX mime.types
format to map filename extensions to MIME types. The second mechanism,
the command map, specifies the actions that can be applied to a given
MIME content type. The default implementation of this uses the standard
mailcap format to map actions to JavaBean&#8482; classes. These beans
can then view, edit, print, or perform whatever other action is
required on the underlying resource.

%prep
%setup -q -n %{official_name}-%{version}

%build
export CLASSPATH=$(build-classpath glibj):$CLASSPATH
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist

%install
mkdir -p %{buildroot}/%{_javadir}
cp activation.jar %{buildroot}/%{_javadir}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/jaf.jar %{buildroot}%{_javadir}/jaf.jar

%post
%{_sbindir}/update-alternatives --install %{_javadir}/jaf.jar jaf %{_javadir}/activation.jar 111

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/update-alternatives --remove jaf %{_javadir}/activation.jar
fi

%files
%defattr(-,root,root)
%{_javadir}/*
%{_javadir}/jaf.jar
%ghost %{_sysconfdir}/alternatives/jaf.jar

%changelog
