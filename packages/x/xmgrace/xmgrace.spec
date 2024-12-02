#
# spec file for package xmgrace
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xmgrace
Version:        5.1.25
Release:        0
Summary:        A 2D-Plot-Program for Visualisation of Scientific Data
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://plasma-gate.weizmann.ac.il/Grace/
Source:         https://ftp.fu-berlin.de/unix/graphics/grace/src/grace5/grace-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        xmgrace.png
Patch1:         xmgrace-strip.patch
Patch2:         xmgrace-help.patch
Patch3:         reproducible.patch
Patch4:         grace-configure-c99.patch
Patch5:         grace-gcc14.patch
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openmotif-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)

%description
Grace is a WYSIWYG 2D plotting tool for the X Window System and M*tif.
Grace is a descendant of ACE/gr, also known as Xmgr. It knows a lot of
different graph types and supports a lot of output formats.

For examples, see %{_prefix}/lib/xmgrace/examples.

%package devel
Summary:        Grace library
Group:          Productivity/Graphics/Visualization/Graph

%description devel
Grace is a WYSIWYG 2D plotting tool for the X Window System and M*tif.
Grace is a descendant of ACE/gr, also known as Xmgr. It knows a lot of
different graph types and supports a lot of output formats. This devel
package contains a library to work with grace from other applications.

For further information consult the main package.

%prep
%setup -q -n grace-%{version}
%patch -P 1
%patch -P 2
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure \
  --enable-grace-home=%{_libdir}/xmgrace \
  --with-helpviewer="%{_bindir}/desktop-launch %{s}"
make %{?_smp_mflags}

%install
%make_install
make DESTDIR=%{buildroot} install links
mkdir -p %{buildroot}/%{_defaultdocdir}/xmgrace
rm -rf %{buildroot}%{_prefix}/man
mkdir -p %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_mandir}/man1/*.1
mv %{buildroot}%{_libdir}/xmgrace/doc/*.1 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_libdir}/xmgrace/doc %{buildroot}/%{_defaultdocdir}/xmgrace
%if "%{_lib}" == "lib64"
mv %{buildroot}%{_prefix}/lib/libgrace_np.a %{buildroot}%{_libdir}
%endif
cp CHANGES COPYRIGHT ChangeLog DEVELOPERS LICENSE README %{buildroot}/%{_defaultdocdir}/xmgrace
install -dm 755 %{buildroot}/%{_datadir}/pixmaps
install %{SOURCE2} -m 644 %{buildroot}/%{_datadir}/pixmaps
install -dm 755 %{buildroot}%{_datadir}/applications/
install %{SOURCE1} -m 644 %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/xmgrace.desktop Education Science Math

%files
%license LICENSE
%doc %{_defaultdocdir}/xmgrace
%{_mandir}/man1/*
%{_libdir}/xmgrace
%{_bindir}/gracebat
%{_bindir}/xmgrace
%{_bindir}/grace
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*png

%files -n xmgrace-devel
%license LICENSE
%{_includedir}/grace_np.h
%{_libdir}/libgrace_np.a

%changelog
