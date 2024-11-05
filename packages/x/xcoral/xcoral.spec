#
# spec file for package xcoral
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


Name:           xcoral
Version:        3.50.2
Release:        0
Summary:        X11 Editor with C/C++/Java Browser
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            http://xcoral.free.fr/
Source:         http://xcoral.free.fr/xcoral-%{version}.tar.gz
Patch0:         xcoral-compile.patch
Patch1:         0001-Fix-to-compile-with-latest-gcc-14.2.1.patch
BuildRequires:  libXft-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
Provides:       xcoral21

%description
Xcoral provides support for working with C, C++, Java, Perl, Ada, and
Fortran programs and for the creation of LaTeX and HTML documents.
With the help of the built-in "SMall Ansi C Interpreter" (SMAC),
xcoral can be configured and extended in almost arbitrary ways.
Examples can be found in the directory %{_prefix}/lib/xcoral. It has
a built-in C/C++/Java browser

Further information about Xcoral and SMAC is available in the detailed
online help system (also available Postscript format).

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure
# parallel build fails
%make_build --jobs=1

%install
install -d %{buildroot}%{_libdir}/%{name}
%make_install \
  prefix=%{buildroot}%{_prefix} \
  exec_prefix=%{buildroot}%{_prefix} \
  X_BINDIR=%{buildroot}%{_bindir} \
  XC_LIBDIR=%{buildroot}%{_libdir}/%{name}
find Doc "(" -name "*.ps" -o -name "*.pdf" ")" -exec bzip2 {} +
install -Dpm 0644 SmacLib/xcoralrc.lf \
  %{buildroot}%{_sysconfdir}/skel/.xcoralrc

%files
%doc Doc/*
%config(noreplace) %{_sysconfdir}/skel/.xcoralrc
%{_bindir}/xcoral
%{_libdir}/xcoral

%changelog
