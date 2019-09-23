#
# spec file for package xmorph
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmorph
Version:        20060817
Release:        0
Summary:        A morphing program
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            http://sourceforge.net/projects/xmorph/
Source:         %{name}_%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        acinclude.m4
Patch1:         xmorph-dirinfo.patch
Patch2:         xmorph-gcc_warnings.patch
Patch3:         xmorph-missing-include.patch
Patch4:         xmorph-20060817-autotools.patch
Patch5:         xmorph-automake-1.13.patch
Patch6:         xmorph-fixbuild.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ctags
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Requires(post): %{install_info_prereq}
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This morphing program reads two images in Targa format and computes the
transitions from one image to the other (arbitrarily many steps). To
avoid a simple fading effect, the program needs information about the
shapes contained in the two images. This is done by using a grid
consisting of connected checkpoints. The source grid is then
transformed into the destination grid during the morphing process.

%package devel
Summary:        Development Files For Xmorph
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q
cat %{SOURCE2} >>acinclude.m4
%patch1
%patch2
%patch3
%patch4
%patch5 -p1
%patch6 -p1

%build
autoreconf -fiv
%configure \
  --disable-static \
  --with-pic \
  --with-gtk2 \
  CFLAGS="%{optflags} -fgnu89-inline"
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file -i %{name} Graphics RasterGraphics
rm -r %{buildroot}%{_datadir}/xmorph/example
mkdir -p %{buildroot}%{_docdir}/xmorph/example
ln -s ../doc/packages/xmorph/example %{buildroot}%{_datadir}/xmorph/example
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%desktop_database_post

%postun
/sbin/ldconfig
%desktop_database_postun

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/xmorph
%doc README HISTORY example
%{_mandir}/man1/*
%{_infodir}/*info*.gz
%{_libdir}/libmorph.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/xmorph
%{_libdir}/libmorph.so

%changelog
