#
# spec file for package xmgrace
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmgrace
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openmotif-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
Version:        5.1.25
Release:        0
Summary:        A 2D-Plot-Program for Visualisation of Scientific Data
License:        GPL-2.0+
Group:          Productivity/Graphics/Visualization/Graph
Source:         ftp://ftp.fu-berlin.de/unix/graphics/grace/src/grace5/grace-%{version}.tar.gz
Source1:        %name.desktop
Source2:        xmgrace.png
Patch0:         xmgrace-null.patch
Patch1:         xmgrace-strip.patch
Patch2:         xmgrace-help.patch
Patch3:         reproducible.patch
Url:            http://plasma-gate.weizmann.ac.il/Grace/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Grace is a WYSIWYG 2D plotting tool for the X Window System and M*tif.
Grace is a descendant of ACE/gr, also known as Xmgr. It knows a lot of
different graph types and supports a lot of output formats.

For examples, see /usr/lib/xmgrace/examples.

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
%setup -n grace-%{version}
%patch0 -p0
%patch1 
%patch2
%patch3 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=/usr/%{_lib} --enable-grace-home=/usr/%{_lib}/xmgrace --bindir=/usr/bin --with-helpviewer="/usr/bin/desktop-launch %s" --mandir=%{_mandir}
make %{?_smp_mflags}

%install
# rm -rf %{_defaultdocdir}/xmgrace
# rm -rf /usr/%{_lib}/xmgrace
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install links
mkdir -p %{buildroot}/%{_defaultdocdir}/xmgrace
rm -rf %{buildroot}/usr/man
mkdir -p %{buildroot}/usr/share/man/man1
rm -f %{buildroot}/usr/share/man/man1/*.1
mv %{buildroot}/usr/%{_lib}/xmgrace/doc/*.1 %{buildroot}/usr/share/man/man1
mv %{buildroot}/usr/%{_lib}/xmgrace/doc %{buildroot}/%{_defaultdocdir}/xmgrace
%if "%{_lib}" == "lib64"
mv %{buildroot}/usr/lib/libgrace_np.a %{buildroot}/usr/%{_lib}
%endif
cp CHANGES COPYRIGHT ChangeLog DEVELOPERS LICENSE README %{buildroot}/%{_defaultdocdir}/xmgrace
install -dm 755 %{buildroot}/%{_datadir}/pixmaps
install %{SOURCE2} -m 644 %{buildroot}/%{_datadir}/pixmaps
install -dm 755 %{buildroot}%{_datadir}/applications/
install %{SOURCE1} -m 644 %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/xmgrace.desktop Education Science Math

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/xmgrace
%doc /usr/share/man/man1/*
# %{_defaultdocdir}/xmgrace
%{_libdir}/xmgrace
%{_bindir}/gracebat
%{_bindir}/xmgrace
%{_bindir}/grace
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*png

%files -n xmgrace-devel
%defattr(-,root,root)
%{_includedir}/grace_np.h
%{_libdir}/libgrace_np.a

%changelog
