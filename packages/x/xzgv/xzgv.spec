#
# spec file for package xzgv
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xzgv
Version:        0.9.2
Release:        0
Summary:        A Fast Picture Viewer for the X Window System
License:        GPL-2.0+
Group:          Productivity/Graphics/Viewers
Url:            https://sourceforge.net/projects/xzgv
Source:         https://sourceforge.net/projects/xzgv/files/xzgv/%{version}/%{name}-%{version}.tar.gz
Patch2:         xzgv-0.9.1-iconify.patch
# PATCH-FIX-UPSTREAM xzgv-0.9.2-paths.patch -- create missing paths
Patch3:         xzgv-0.9.2-paths.patch
BuildRequires:  gtk2-devel
BuildRequires:  libexif-devel
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
BuildRequires:  update-desktop-files
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xzgv is a picture viewer for the X Window System with a thumbnail-based
file selector. It uses GTK+ and Imlib. Most file formats are supported,
and the thumbnails used are compatible with xv, zgv, and the Gimp. It
can also be used with `xzgv file(s)', to effectively bypass the file
selector. For more on how xzgv works and how to use it, do `info xzgv'
or `man xzgv' once it is installed.

%prep
%setup -q
%patch2
%patch3 -p1

%build
sed -i "s/^CFLAGS=.*/CFLAGS=%{optflags}/;" config.mk
make %{?_smp_mflags} PREFIX=%{_prefix}
# Make all doesn't build the info, but we need it for make install
# (fail the build when this is fixed)
test ! -f doc/xzgv.info.gz
make %{?_smp_mflags} info PREFIX=%{_prefix}

%install
make PREFIX=%{buildroot}%{_prefix} install
%suse_update_desktop_file -i %{name} Graphics Viewer
# Fix permission (fail the build when this is fixed)
test -x %{buildroot}%{_mandir}/man1/xzgv.1
chmod a-x %{buildroot}%{_mandir}/man1/xzgv.1

%post
%install_info --info-dir=%{_infodir} %{_infodir}/xzgv.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/xzgv.info.gz

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO
%{_bindir}/xzgv
%{_datadir}/applications/xzgv.desktop
%{_datadir}/pixmaps/xzgv.xpm
%{_mandir}/man1/xzgv.1%{ext_man}
%{_infodir}/xzgv.info%{ext_info}

%changelog
