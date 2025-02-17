#
# spec file for package xsane
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


%if 0%{?suse_version} <= 1600
%bcond_without gimp
%else
%bcond_with gimp
%endif

Name:           xsane
Version:        0.999
Release:        0
Summary:        A GTK-Based Graphical Scanning Front-End for SANE
License:        GPL-2.0-or-later
Group:          Hardware/Scanner
URL:            http://www.xsane.org/
# URL for Source0: http://www.xsane.org/download/xsane-0.998.tar.gz
Source0:        http://www.xsane.org/download/xsane-%{version}.tar.gz
Patch0:         xsane-memory-leak.diff
Patch1:         xsane-libpng15.patch
Patch2:         xsane-0.999-lcms2.patch
Patch3:         001-xdg-open-as-default-browser.patch
Patch4:         002-close-fds.patch
Patch5:         004-ipv6-support.patch
Patch7:         006-preview-selection.patch
Patch8:         100-remove-non-working-help.patch
Patch9:         101-xsane_fix_pdf_floats.patch
Patch10:        200-fix_options_handling_fix.patch
Patch11:        201-fix_pdf_xref.patch
Patch12:        901-desktop-file.patch
Patch13:        902-license-dialog.patch
Patch14:        903-fix_broken_links.patch
Patch18:        907-fix_spin_button_pagesize.patch
Patch19:        908-no-file-selected.patch
Patch20:        0010-fix_missing_sane-config.patch
Patch21:        0005-m4.patch
Patch22:        909-gcc15.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
%if %{with gimp}
BuildRequires:  gimp-devel
%else
BuildRequires:  gtk2-devel
%endif
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  sane-backends-devel
BuildRequires:  update-desktop-files
Requires:       sane-backends
Requires:       xdg-utils
Provides:       gimp-2.0-scanner-plugin

%description
XSane does not support any scanners itself. XSane uses the SANE library
to talk to scanners that are supported by SANE.

XSane is designed for acquiring images with scanners (there are other
devices like cameras and video devices supported by SANE, but XSane is
not designed for that purpose). You can scan to file, make a photocopy,
create a fax, and start XSane from the GIMP as a GIMP plug-in.

XSane may not work correctly or you may not be able to take full
advantage of all functions if you do not configure XSane correctly. See
the documentation at %{_datadir}/sane/xsane/doc/sane-xsane-doc.html.

The XSane home page is http://www.xsane.org/.

%prep
%setup -q
# zh is not valid locale. In fact it is zh_TW:
mv po/zh.po po/zh_TW.po
mv po/zh.gmo po/zh_TW.gmo
sed -i "s/ zh / zh_TW /" configure.in configure
%autopatch -p1

mv configure.in configure.ac

%build
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -fno-strict-aliasing"
ACLOCAL="aclocal -I m4" autoreconf -f -i
%configure\
%if %{with gimp}
	--enable-gimp
%else
	--disable-gimp
%endif
make %{?_smp_mflags}

%install
%make_install
# Create GIMP plugin link:
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins
ln -sf %{_bindir}/xsane %{buildroot}%{_libdir}/gimp/2.0/plug-ins/xsane
%suse_update_desktop_file %{name}
%find_lang %{name}
%fdupes %{buildroot}

%files -f %{name}.lang
%doc xsane.[A-HJ-VX-Z]*
%{_bindir}/xsane
%dir %{_datadir}/sane
%{_datadir}/sane/xsane
%{_mandir}/man1/xsane.1*
%dir %{_libdir}/gimp/
%dir %{_libdir}/gimp/2.0/
%dir %{_libdir}/gimp/2.0/plug-ins/
%{_libdir}/gimp/2.0/plug-ins/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm

%changelog
