#
# spec file for package ioquake3
#
# Copyright (c) 2023 SUSE LLC
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


%define _lto_cflags %{nil}
# Some arch have no VM (aarch64, ...)
%define arch_with_vm  %{ix86} x86_64 ppc ppc64 armv7l armv7hl
Name:           ioquake3
Version:        1.36+git.20221123
Release:        0
Summary:        Quake III
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://ioquake3.org
Source:         %{name}-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  curl-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)
ExcludeArch:    armv6l armv6hl

%package devel
Summary:        Quake III
Group:          Development/Tools/Building

%description
Quake III first person shooter. This package only includes the binary
files, you still need the data files from the original Quake III CD or
the Demo.

%description devel
Quake III development tools for creating mods: q3lcc, q3rcc, q3cpp,
q3asm

%prep
%setup -q
rm -rf code/SDL2 code/libs code/AL

%build
cat > dobuild <<'EOF'
#!/bin/sh
%make_build \
%ifarch armv7l armv7hl
    COMPILE_ARCH=armv7l \
%endif
%ifarch aarch64
    COMPILE_ARCH=aarch64 \
%endif
	VERSION=%{version} \
	RELEASE=%{release} \
	OPTIMIZE="%{optflags} -O3 -ffast-math -fno-strict-aliasing" \
	TOOLS_OPTIMIZE="%{optflags} -fno-strict-aliasing" \
	GENERATE_DEPENDENCIES=0 \
	USE_LOCAL_HEADERS=0 \
	V=1 \
	"$@"
EOF
chmod 755 dobuild

./dobuild release

%install
arch=`uname -m`
case $arch in
	i?86) arch=x86 ;;
esac
q3dir=%{buildroot}%{_prefix}/lib/ioquake3
install -d -m 755 $q3dir
%ifarch %{arch_with_vm}
install -d -m 755 $q3dir/baseq3/vm
%else
install -d -m 755 $q3dir/baseq3
%endif
install -d -m 755 $q3dir/demoq3
%ifarch %{arch_with_vm}
install -d -m 755 $q3dir/missionpack/vm
%else
install -d -m 755 $q3dir/missionpack
%endif
pushd build/release-linux-$arch/
install -m 755 ioquake3.$arch $q3dir/
install -m 755 ioq3ded.$arch $q3dir/
install -m 644 renderer_opengl1_$arch.so $q3dir/
install -m 644 renderer_opengl2_$arch.so $q3dir/
install -m 644 baseq3/*.so $q3dir/baseq3
%ifarch %{arch_with_vm}
install -m 644 baseq3/vm/*.qvm $q3dir/baseq3/vm
%endif
pushd $q3dir/demoq3
ln -s ../baseq3/*.so .
popd
install -m 644 missionpack/*.so $q3dir/missionpack
%ifarch %{arch_with_vm}
install -m 644 missionpack/vm/*.qvm $q3dir/missionpack/vm
%endif
popd

# icons and start scripts
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 misc/quake3.png %{buildroot}%{_datadir}/pixmaps
install -m 644 misc/setup/ioquake3.desktop %{buildroot}%{_datadir}/applications/ioquake3.desktop
install -m 755 misc/setup/ioq3demo.sh $q3dir/
install -m 755 misc/setup/ioquake3.sh $q3dir/

for i in ioq3demo ioquake3; do
	echo -e "#!/bin/sh\nexec %{_prefix}/lib/ioquake3/$i.sh \"\$@\"" > %{buildroot}%{_bindir}/$i
	chmod 755 %{buildroot}%{_bindir}/$i
done

# devel tools
%ifarch %{arch_with_vm}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 build/release-linux-$arch/tools/q3{lcc,cpp,rcc,asm} %{buildroot}%{_bindir}
%endif

%post
echo 'copy pak[0-8].pk3 to /usr/lib/ioquake3/baseq3/'

%files
%license COPYING.txt
%doc README* id-readme.txt
%doc voip-readme.txt opengl2-readme.md
%{_bindir}/ioq*
%{_prefix}/lib/ioquake3
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files devel
%doc code/tools/lcc/COPYRIGHT
%ifarch %{arch_with_vm}
%{_bindir}/q3*
%endif

%changelog
