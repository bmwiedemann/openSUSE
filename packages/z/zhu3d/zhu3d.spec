#
# spec file for package zhu3d
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2006 Víctor Fernández Martínez. Valencia, Spain.
# openSuse  (c) 2006 pnemec@novell.com
# Copyright (c) 2006 Pavel Nemec pnemec@suse.cz
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


Name:           zhu3d
Version:        4.2.6
Release:        0
Summary:        OpenGL-based equation viewer and solver
License:        GPL-3.0
Group:          Productivity/Scientific/Math
Url:            https://sourceforge.net/projects/zhu3d/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-pri.patch
# PATCH-FIX-OPENSUSE zhu3d-no-compilation-date.patch - fix "W: file-contains-current-date"
Patch2:         %{name}-no-compilation-date.patch
# PATCH-FIX-OPENSUSE zhu3d-ppc.patch - fixes ppc build
Patch3:         zhu3d-ppc.patch 
# PATCH-FIX-UPSTREAM zhu3d-4.2.6-qt5.patch -- courtesy of gentoo
Patch4:         %{name}-4.2.6-qt5.patch
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%if 0%{?suse_version} >= 1220
BuildRequires:  Mesa-libGLU-devel
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
%else
BuildRequires:  libqt4-devel > 4.3
BuildRequires:  libqt4-sql
BuildRequires:  libqt4-x11
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
With Zhu3D you can view, animate and solve up to three functions in
3D-space in a interactive manner. In addition, you further can observe
an independent parametric system. The OpenGL-viewer supports zooming,
scaling, rotating, translating as well as filed lightning,
transparency or surface-properties.

You have up to 8 independent lights or spotlights, background
settings, miscellaneous wire-modes or global illumination
models. Pictures are rendered as png or jpg and can have an arbitrary
size. Numerical solutions of an equation-system are found with a quite
fast and reliable adaptive random search.


%prep
%setup -q
%patch0
%patch2 -p1
%patch3 -p1
%if 0%{?suse_version} >= 1315
%patch4 -p1
%endif
find . -type f -print0|xargs -0 chmod -x
sed -i 's/\r//' readme.txt license.gpl src/changelog.txt

%build
%if 0%{?suse_version} >= 1315
%qmake5 SYSDIR=%{_datadir}
%else
qmake SYSDIR=%{_datadir} QMAKE_CFLAGS_RELEASE="%{optflags}" QMAKE_CXXFLAGS_RELEASE="%{optflags}"
%endif
make %{?_smp_mflags}

%install
# Program binary
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

# Other program files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a -f work system %{buildroot}%{_datadir}/%{name}

# Desktop entry
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Desktop icon
install -Dm0644 system/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -Dm0644 system/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc license.gpl readme.txt src/changelog.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/zhu3d.png

%changelog
