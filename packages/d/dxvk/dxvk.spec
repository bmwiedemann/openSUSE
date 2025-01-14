#
# spec file for package dxvk
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


Name:           dxvk
Version:        2.5.3
Release:        0
Summary:        Vulkan-based Direct3D 8/9/10/11 implementation for Linux / Wine
License:        zlib-acknowledgement
Group:          System/Emulators/PC
URL:            https://github.com/doitsujin/dxvk
Source0:        %{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        setup_dxvk.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  wine
BuildRequires:  xz

%ifarch x86_64
BuildRequires:  mingw64-cross-cpp
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  mingw64-headers

#Require 32bit version
Requires:       %{name}-32bit
%else
BuildRequires:  mingw32-cross-cpp
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-gcc-c++
BuildRequires:  mingw32-headers
%endif

ExclusiveArch:  %{ix86} x86_64

%description
A Vulkan-based translation layer for Direct3D 8/9/10/11 which allows running 3D applications on Linux using Wine.

%prep
%setup -q

%build
export CFLAGS="%optflags -DNDEBUG -fPIC -O2 -pthread -fno-strict-aliasing -fpredictive-commoning -fuse-linker-plugin -fno-stack-protector -fno-stack-clash-protection -fno-lto"
export CXXFLAGS="${CFLAGS} -fpermissive"
export LDFLAGS="-fPIC -Wl,--sort-common -Wl,--gc-sections -Wl,-O1 -fuse-linker-plugin -fno-lto"

mkdir ../build

meson setup \
    --cross-file build-win$(arch | tail -c 3 | sed 's|86|32|g').txt \
    --strip \
    --buildtype "release" \
    --unity off \
    --prefix /%{name} \
    ../build

cd ../build
ninja

%install

#install wrapper scripts
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/%{name}/bin
sed \
    -e 's|basedir=.*|basedir="%{_libexecdir}/%{name}"|g' \
    -e 's|x32|lib|g' -e 's|x64|lib64|g' \
    %{SOURCE2}> %{buildroot}%{_libexecdir}/%{name}/bin/setup_dxvk.sh
ln -s %{_libexecdir}/%{name}/bin/setup_dxvk.sh %{buildroot}%{_bindir}/wine%{name}

#install dxvk proper
cd ../build
DESTDIR=%{buildroot}%{_libexecdir} ninja install

%ifarch x86_64
if [ -d %{buildroot}%{_libexecdir}/%{name}/lib ];then
    mv %{buildroot}%{_libexecdir}/%{name}/lib %{buildroot}%{_libexecdir}/%{name}/%{_lib}
fi
%endif
rm %{buildroot}%{_libexecdir}/%{name}/%{_lib}/*.dll.a && \
mv %{buildroot}%{_libexecdir}/%{name}/bin/*.dll %{buildroot}%{_libexecdir}/%{name}/%{_lib}/

%files
%defattr(644,root,root)
%doc README.md
%license LICENSE

%{_bindir}/wine%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{_lib}
%attr(755, root, root) %{_libexecdir}/%{name}/bin

%changelog
