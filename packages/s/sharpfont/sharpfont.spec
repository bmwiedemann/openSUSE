#
# spec file for package sharpfont
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

Name:           sharpfont
Version:        4.0.1
Release:        0
Url:            https://github.com/Robmaister/SharpFont
Summary:        Cross-platform FreeType bindings for .NET
License:        MIT
Source:         https://github.com/Robmaister/SharpFont/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  pkgconfig(mono)

%description
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.


%package devel
Summary:        Cross-platform FreeType bindings for .NET
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description devel
SharpFont is a library that provides FreeType bindings for .NET.
Everything from format-specific APIs to the caching subsystem are included.

%prep
%setup -q -n SharpFont-%{version}

%build
pushd Source/SharpFont
xbuild /p:TargetFrameworkVersion=v4.5 /p:Configuration=Debug

%install
#manually sign delay-signed assemblies
find "Binaries/SharpFont/Debug" \( -name "*.dll" -o -name "*.exe" \) -print0 | while IFS= read -r -d $'\0' target; do
  sn -v "$target" || if [[ $? = 1 ]]; then
    echo "manually signing assembly: $target"
    sn -R "$target" "Source/SharpFont.snk"
  fi
done

mkdir -p %{buildroot}%{_prefix}/lib/mono/gac/
gacutil -i Binaries/SharpFont/Debug/SharpFont.dll -f -package %{name} -root %{buildroot}%{_prefix}/lib
cp -p Source/SharpFont.dll.config %{buildroot}%{_prefix}/lib/mono/%{name}/SharpFont.dll.config

mkdir -p %{buildroot}/%{_datadir}/pkgconfig
pc_file="%{buildroot}/%{_datadir}/pkgconfig/%{name}.pc"
# text strings entered with "cat <<EOT" constructs sometimes may be SILENTLY broken by spec files validators used by OSC
echo "Name: SharpFont" > "$pc_file"
echo "Description: %{summary}" >> "$pc_file"
echo "Version: %{version}" >> "$pc_file"
echo "Requires:" >> "$pc_file"
echo "Libs: -r:%{_prefix}/lib/mono/%{name}/SharpFont.dll" >> "$pc_file"
echo "Libraries=%{_prefix}/lib/mono/%{name}/SharpFont.dll" >> "$pc_file"

%fdupes %{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/mono/gac/SharpFont
%{_prefix}/lib/mono/%{name}/

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
