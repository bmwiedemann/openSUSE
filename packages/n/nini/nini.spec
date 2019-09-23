#
# spec file for package nini
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           nini
Version:        1.1.0
Release:        0
Summary:        An uncommonly powerful .NET configuration library
License:        MIT
Group:          System/Libraries
Url:            http://nini.sourceforge.net/
Source:         Nini-%{version}.zip
BuildRequires:  mono-devel
BuildRequires:  nant
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Nini is an uncommonly powerful .NET configuration library designed to
help build highly configurable applications quickly.

%prep
%setup -q -n Nini

%build
cd Source
mcs -target:library -out:Nini.dll -reference:System.dll -reference:System.Xml.dll -define:MONO_1_1 -define:NOSTRONG AssemblyInfo.cs Ini/*.cs Config/*.cs Util/*.cs
cat << EOF > nini-1.1.pc
prefix=%{_prefix}
assemblies_dir=\${prefix}/lib/nini
Libraries=\${assemblies_dir}/Nini.dll

Name: Nini
Description: An uncommonly powerful .NET configuration library
Version: %{version}
Libs: -r:\${assemblies_dir}/Nini.dll
EOF

%install
cd Source
mkdir -p %{buildroot}%{_prefix}/lib/nini
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp Nini.dll %{buildroot}%{_prefix}/lib/nini/
cp nini-1.1.pc %{buildroot}%{_datadir}/pkgconfig/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/lib/nini/
%{_datadir}/pkgconfig/nini-1.1.pc

%changelog
