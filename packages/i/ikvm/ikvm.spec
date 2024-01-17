#
# spec file for package ikvm
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ikvm
BuildRequires:  dos2unix mono-devel unzip
Version:        8.0.5449.1
Release:        1
License:        BSD-3-Clause
BuildArch:      noarch
Url:            http://www.ikvm.net
Source0:        http://www.frijters.net/ikvmbin-%{version}.zip
Summary:        A JVM Based on the Mono Runtime
Group:          Development/Tools/Other
Requires:       mono-ikvm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides IKVM.NET, an open source Java compatibility layer
for Mono, which includes a Virtual Machine, a bytecode compiler, and
various class libraries for Java, as well as tools for Java and Mono
interoperability.

%prep
%setup -q
# fix line endings for rpmlint
dos2unix LICENSE

%build
true

%install
# Create dirs
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/lib/ikvm
mkdir -p %{buildroot}%{_prefix}/share/pkgconfig
# Don't install the PdbWriter
rm -f bin/*PdbWriter*
# Install binaries
#  (do iname for JVM.DLL)
find bin -iname "*\.dll" -exec cp {} %{buildroot}%{_prefix}/lib/ikvm  \;
find bin -name "*\.exe" -exec cp {} %{buildroot}%{_prefix}/lib/ikvm  \;
# Install some in gac (By request of Jeroen)
OPENJDK=$(find bin -iname "IKVM.OpenJDK.*.dll" -exec basename '{}' ';')
for i in IKVM.AWT.WinForms.dll $OPENJDK IKVM.Runtime.dll ; do
	gacutil -i %{buildroot}%{_prefix}/lib/ikvm/$i -package ikvm -root %{buildroot}%{_prefix}/lib
	rm -f %{buildroot}%{_prefix}/lib/ikvm/$i
done
# Generate wrapper scripts
for f in `find bin . -name "*\.exe"` ; do
        script_name=%{buildroot}%{_bindir}/`basename $f .exe`
        cat <<EOF > $script_name
#!/bin/sh
exec mono %{_prefix}/lib/ikvm/`basename $f` "\$@"
EOF
        chmod 755 $script_name
done
# Generate .pc file
%define prot_name Name
%define prot_version Version
cat <<EOF > %{buildroot}%{_prefix}/share/pkgconfig/ikvm.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=\${prefix}/lib
%prot_name: IKVM.NET
Description: An implementation of Java for Mono and the Microsoft .NET Framework.
%prot_version: %{version}
Libs: -r:\${libdir}/mono/ikvm/IKVM.Runtime.dll -r:\${libdir}/mono/ikvm/IKVM.OpenJDK.ClassLibrary.dll
EOF

%files
%defattr(-, root, root)
%doc LICENSE
%_bindir/*
%_prefix/lib/ikvm
%_prefix/lib/mono/gac/IKVM*
%_prefix/lib/mono/ikvm
%_prefix/share/pkgconfig/ikvm.pc

%changelog
