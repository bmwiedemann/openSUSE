#
# spec file for package simutrans
#
# Copyright (c) 2020-2024 SUSE LLC
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


%define pkgver 124-1
Name:           simutrans
Version:        124.1
Release:        0
Summary:        Transport and Economic Simulation Game
License:        Artistic-1.0
Group:          Amusements/Games/Strategy/Real Time
URL:            http://sourceforge.net/projects/simutrans/
Source0:        http://downloads.sourceforge.net/simutrans/simutrans-src-%{pkgver}.zip
Source1:        config.default
Source2:        http://www.simutrans.com/images/resources/simutrans-square.svg
# PATCH-FIX-UPSTREAM http://forum.simutrans.com/index.php?topic=11173.0
Patch0:         simutrans-fhs-home-directory.patch
Patch1:         simutrans-makefile.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  freetype2-devel
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  hicolor-icon-theme
# Since now we have Leap > 15.4, we follow the advice here: https://forum.simutrans.com/index.php?action=post;quote=198369;topic=21320.0;last_msg=198369
BuildRequires:  fluidsynth-devel >= 2.1.0
Requires:       fluid-soundfont-gm
BuildRequires:  libzstd-devel
Recommends:     %{name}-pak128 >= 2.9.1
Suggests:       %{name}-pak128-german >= 2.2
Suggests:       %{name}-pak64 >= 124.1
Suggests:       %{name}-makeobj

%description
Simutrans is a transport and economic simulation with some ecological
aspects. The goal of the game is to build an infrastructure which
allows you to transport goods between the various industries and towns,
and to support the towns with water and energy. A second goal is to
become as rich as possible, but you will have to reinvest a good part
of your earned money to expand your infrastructure network.

%package makeobj
Summary:        Tool for compiling simutrans data packages
Group:          Development/Tools/Other
# Package was called simutrans previously
Obsoletes:      makeobj < %{version}-%{release}

%description makeobj
Makeobj is a easy to use software used to compile .dat files and .png pictures
to simutrans .pak files.

%prep
%autosetup -p1 -c -n simutrans

cp %{SOURCE1} .
# files with the wrong line-endings, which give a rpmlint warning:
dos2unix simutrans/*.txt

%build
export CFLAGS="%{optflags}"
export CCFLAGS="$CFLAGS"
%make_build all makeobj
# The next 3 lines did not function correctly; so now we use the available theme pak files:
# cd themes.src
# sed -i 's|../makeobj|../../build/default/makeobj/makeobj|g' build_themes.sh
# ./build_themes.sh

%install
# Create starter-wrapper script (not a source so we can use directory macros):
mkdir -vp %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec %{_libexecdir}/%{name}/sim -use_workdir \$@
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}
# Install the executable "sim":
install -vDm755 build/default/sim %{buildroot}%{_libexecdir}/%{name}/sim
# Install makeobj, avoid conflict with makeobj from kdesdk-scripts
install -vm755 build/default/makeobj/makeobj %{buildroot}%{_libexecdir}/%{name}/makeobj
ln -s %{_libexecdir}/%{name}/makeobj %{buildroot}%{_bindir}/makeobj-simutrans
# Install data
mkdir -vp %{buildroot}%{_datadir}/%{name}
cp -va simutrans/* %{buildroot}%{_datadir}/%{name}
# Create dummy directories addons
mkdir -vp %{buildroot}%{_datadir}/%{name}/addons
# Move docs to the correct place
mkdir -vp %{buildroot}%{_docdir}/%{name}
mv -v %{buildroot}%{_datadir}/%{name}/*.txt %{buildroot}%{_docdir}/%{name}
# Install icon and .desktop file
install -vDm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%if 0%{?suse_version}
%suse_update_desktop_file -c simutrans "Simutrans" "Transportation Simulation Game" "simutrans" simutrans Game StrategyGame
%fdupes %{buildroot}%{_datadir}/%{name}
%endif

%files
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sim
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%files makeobj
%{_bindir}/makeobj-simutrans
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/makeobj

%changelog
