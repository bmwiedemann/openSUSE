#
# spec file for package nekobox
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define core nekobox_core
Name:           nekobox
Version:        5.10.37
Release:        0%{?autorelease}
Summary:        Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
License:        GPL-3.0-only
URL:            https://github.com/qr243vbi/nekobox
Source0:        %{url}/releases/download/%{version}/nekobox-unified-source-%{version}.tar.xz
Source1:        nekobox-qt.spec.in
Source2:        nekobox-core.spec.in

%if 0%{?suse_version} > 0
BuildRequires:  patchelf
%else
BuildRequires:  (chrpath or patchelf)
%endif
BuildRequires:  cmake
BuildRequires:  %{!?nekobox_golang_package:golang >= 1.25}%{?nekobox_golang_package}
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  libacl-devel
BuildRequires:  thrift
BuildRequires:  (libboost-devel or boost-devel)
BuildRequires:  (libthrift-devel or thrift-devel)
BuildRequires:  (ninja or ninja-build)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

Requires:       %{name}-core
Requires:       %{name}-qt


%ifarch x86_64 aarch64 arm32 %arm32 %arm64 %x86_64 ppc64le %power64 %riscv riscv32 riscv64 riscv128 %ix86 i386 i486 i586 i686 pentium3 pentium4 athlon geode
%if 0%{?suse_version}%{?fedora} > 0

%bcond_without upx

%endif
%endif

%if %{with upx}
BuildRequires: upx
%endif

%if 0%{?suse_version} > 0
BuildRequires:  ccache
BuildRequires:  libboost_filesystem-devel
%endif

%files
%dir %{_libexecdir}/%{name}/public
%attr(0644, -, -) %{_libexecdir}/%{name}/public/*.*
%exclude %{_libexecdir}/%{name}/public/*.qm
%attr(0644, -, -) %{_datadir}/icons/hicolor/256x256/apps/nekobox.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%attr(0644, -, -) %{_datadir}/applications/%{name}.desktop
%license LICENSE

%if "%{?_vendor}" == "openEuler"
%define cmake_opts -S . -B %__builddir -DUSE_HOTKEYS=OFF
%endif

%package lang
Summary:        %{summary}

%description
%{summary}.

%description lang
%{summary}.

%files lang
%attr(0644, -, -) %{_libexecdir}/%{name}/public/*.qm

%prep
%autosetup -p1 -n nekobox-unified-source-%{version}
%if 0%{?suse_version} > 0
rm res/public/emoji.ttf
%endif

%{?!%__builddir:%define __builddir %__cmake_builddir}
%{?!%__cmake_builddir:%define __cmake_builddir build}
%if %{undefined optflags}
%define optflags -O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables
%endif

%build
GOFLAGS='-mod=vendor %{?gobuildflags}'

(
%cmake -GNinja "-DPROGRAMPREFIX=%{_libexecdir}/%{name}" "-DNKR_DEFAULT_VERSION=%{version}" %{?cmake_opts}
)

ninja -C "$(realpath %__builddir)" -v -j %{_smp_build_ncpus}

%if %{with upx}
(
echo '%%define nekobox_qt_reqs %%{expand:'
echo %__builddir/nekobox | %_rpmconfigdir/find-requires | sed 's@^@Requires: @g'
echo '}'
echo '%%define nekobox_core_reqs %%{expand:'
echo %__builddir/nekobox_core | %_rpmconfigdir/find-requires | sed 's@^@Requires: @g'
echo '}'
) > %{specpartsdir}/nekobox.specpart

cat %{SOURCE1} >> %{specpartsdir}/nekobox.specpart
cat %{SOURCE2} >> %{specpartsdir}/nekobox.specpart

%else
%{lua:

function print_source(source)
local file = io.open(rpm.expand(source), "r")
if file then
    local content = file:read("*a")  -- read entire file
    file:close()
    print(rpm.expand(content))
end
end

print_source('%{SOURCE1}')
print_source('%{SOURCE2}')

}
%endif

%install
DESTDIR="%{buildroot}" ninja -C "$(realpath %__builddir)" -v  install

%if %{with upx}
for i in nekobox nekobox_core
do
u='%{buildroot}%{_libexecdir}/%{name}/'"${i}"
strip "${u}"
upx "${u}"
done
%endif

%changelog


