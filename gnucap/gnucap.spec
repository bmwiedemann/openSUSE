#
# spec file for package gnucap
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnucap
Version:        0.35
Release:        0
Summary:        Gnu Circuit Analysis Package
License:        GPL-2.0+
Group:          Productivity/Scientific/Electronics
Url:            http://www.gnu.org/software/gnucap/
Source:         %{name}-%{version}.tar.bz2
Source1:        gnucap-modelgen.1
# PATCH-FIX-UPSTREAM -- fix build with GCC 4.3
Patch1:         gnucap-0.35-gcc43.patch
# PATCH-FIX-UPSTREAM -- ACS -> Gnucap
Patch2:         gnucap-0.34-debian.patch
# PATCH-FIX-OPENSUSE -- move documentation and example to the standard directories
Patch3:         gnucap-docpath.patch
# PATCH-FIX-OPENSUSE -- from Debian: add shebang, and explicitly call gnucap
Patch4:         gnucap-fix_runall.patch
# PATCH-FIX-UPSTREAM -- Fix build with GCC 6
Patch5:         gnucap-0.35-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
%if 0%{?suse_version}
%if 0%{?suse_version} > 1020
BuildRequires:  texlive-devel
BuildRequires:  texlive-latex
%else
BuildRequires:  te_latex
BuildRequires:  tetex
%endif
%endif
%if 0%{?mandriva_version}
BuildRequires:  tetex
BuildRequires:  tetex-latex
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The primary component is a general purpose circuit simulator. It
performs nonlinear dc and transient analyses, fourier analysis, and ac
analysis. Spice compatible models for the MOSFET (level 1-7), BJT, and
diode are included in this release.

Gnucap is not based on Spice, but some of the models have been derived
from the Berkeley models.

Unlike Spice, the engine is designed to do true mixed-mode
simulation. Most of the code is in place for future support of event
driven analog simulation, and true multi-rate simulation.

%prep
%setup -q
# use ncurses instead of termcap
sed -i 's/-ltermcap/-lncurses/g' configure
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1
rm INSTALL

%build
%configure --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_defaultdocdir}/%{name}/INSTALL
install -Dm644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/gnucap-modelgen.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/manual
%doc %{_datadir}/%{name}/manual/*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}*

%changelog
