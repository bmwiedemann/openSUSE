#
# spec file for package hp2xx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hp2xx
Version:        3.4.4
Release:        0
Summary:        Converts HP-GL Plotter Language into a Variety of Formats
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Url:            https://www.gnu.org/software/hp2xx/hp2xx.html
Source:         https://ftp.gnu.org/gnu/hp2xx/hp2xx-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         hp2xx-3.4.2-fix.patch
# PATCH-FIX-SUSE  fixes rpm lint error
Patch1:         fix-stringcompare.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch2:         hp2xx-3.4.2-png-deprecated.patch
# PATCH-FIX-UPSTREAM hp2xx-texinfo-5.0.patch dimstar@opensuse.org -- Escape '@' in .texi file
Patch3:         hp2xx-texinfo-5.0.patch
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  xorg-x11-libX11-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif

%description
The hp2xx program is a versatile tool for converting vector graphics
data given in Hewlett-Packard's HP-GL plotter language into a variety
of popular graphics formats, both vector and raster.

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1
%patch2
%patch3 -p1

%build
make %{?_smp_mflags} CC="gcc" OPTFLAGS="%{optflags}" LFLAGS="-L/usr/X11R6/%{_lib}"

%install
mkdir -p %{buildroot}/{usr/bin,%{_infodir},%{_mandir}/man1}
make bindir=%{buildroot}%{_bindir} \
     infodir=%{buildroot}/%{_infodir} \
     mandir=%{buildroot}/%{_mandir} install STRIP=true

%files
%doc AUTHORS CHANGES README TODO copying doc/readme doc/changes doc/hp_cmds.lst
%{_bindir}/hp2xx
%{_mandir}/man1/hp2xx.1%{ext_man}
%{_infodir}/hp2xx.info%{ext_info}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%changelog
