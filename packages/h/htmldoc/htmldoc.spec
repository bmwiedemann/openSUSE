#
# spec file for package htmldoc
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           htmldoc
Version:        1.9.23
Release:        0
Summary:        HTML Processor that Generates HTML, PostScript, and PDF Files
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/HTML/Tools
URL:            https://michaelrsweet.github.io/htmldoc/index.html
Source:         https://github.com/michaelrsweet/htmldoc/releases/download/v%{version}/htmldoc-%{version}-source.tar.gz
Source2:        https://github.com/michaelrsweet/htmldoc/releases/download/v%{version}/htmldoc-%{version}-source.tar.gz.sig
# https://www.msweet.org/pgp.html
Source3:        %{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  fltk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
BuildRequires:  cups-devel
%else
BuildRequires:  pkgconfig(cups)
%endif

%description
HTMLDOC converts HTML source files into indexed HTML, PostScript, or
Portable Document Format (PDF) files that can be viewed online or printed.

%prep
%autosetup -p1

%build
%configure \
  --with-gui
%make_build

%install
%make_install
# Workaround faulty installation
mv -f %{buildroot}%{buildroot}/* \
  %{buildroot}
# Get rid of unvanted files
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%license COPYING
%doc CHANGES.md README.md
%{_bindir}/htmldoc
%{_datadir}/htmldoc
%{_datadir}/icons/hicolor/*x*/apps/htmldoc.png
%{_datadir}/mime/packages/htmldoc.xml
%{_datadir}/applications/htmldoc.desktop
%{_mandir}/man1/htmldoc.1%{?ext_man}

%changelog
