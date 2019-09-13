#
# spec file for package htmldoc
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


Name:           htmldoc
Version:        1.9.1
Release:        0
Summary:        HTML Processor that Generates HTML, PostScript, and PDF Files
License:        LGPL-2.1+
Group:          Productivity/Publishing/HTML/Tools
Url:            https://michaelrsweet.github.io/htmldoc/index.html
Source:         https://github.com/michaelrsweet/htmldoc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libXpm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel

%description
HTMLDOC converts HTML source files into indexed HTML, PostScript, or
Portable Document Format (PDF) files that can be viewed online or printed.

%prep
%setup -q

%build
%configure \
  --with-gui
make %{?_smp_mflags} V=1

%install
%make_install
# Workaround faulty installation
mv -f %{buildroot}%{buildroot}/* \
  %{buildroot}
# Get rid of unvanted files
rm -rf %{buildroot}/home %{buildroot}%{_datadir}/doc/%{name}
# Update desktop file
%suse_update_desktop_file -r %{name} Development Documentation
%suse_update_desktop_file %{name} -G%{name}

%files
%doc CHANGES.md COPYING README.md
%{_bindir}/htmldoc
%{_datadir}/htmldoc
%{_datadir}/pixmaps/htmldoc.xpm
%{_datadir}/mime/packages/htmldoc.xml
%{_datadir}/applications/htmldoc.desktop
%{_mandir}/man1/htmldoc.1%{ext_man}

%changelog
