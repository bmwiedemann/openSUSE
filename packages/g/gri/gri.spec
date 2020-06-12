#
# spec file for package gri
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gri
Version:        2.12.23
Release:        0
Summary:        A language for scientific illustration
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://gri.sourceforge.net
Source:         %{name}-%{version}.tar.bz2
Patch0:         gfi-2.2.23-perl.patch
Patch1:         gri-texinfo-5.0.patch
# PATCH-FIX-UPSTREAM https://github.com/dankelley/gri/pull/10
Patch2:         reproducible.patch
# PATCH-FIX-UPSTREAM gri-invalid-char-to-pointer.patch badshah400@gmail.com -- Fix a char to char* conversion by replacing '\0' with NULL
Patch3:         gri-invalid-char-to-pointer.patch
# PATCH-FIX-UPSTREAM gri-perl-5.26.patch dimstar@opensuse.org -- Fix texinfo2HTML for usage with Perl 5.26
Patch4:         gri-perl-5.26.patch
# PATCH-FIX-UPSTREAM gri-texinfo-6.7-compat.patch -- Explicitly specify correct encoding for texi file, texinfo 6.+ assumes UTF-8 by default
Patch5:         gri-texinfo-6.7-compat.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  perl(Time::CTime)
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gri is a language for scientific graphics programming.  It is a
command-driven application, as opposed to a click/point application.
It is analogous to latex, and shares the property that extensive power
is the reward for tolerating a modest learning curve.  Gri output is
in industry-standard PostScript, suitable for incorporation in
documents prepared by various text processors.

Gri can make x-y graphs, contour-graphs, and image graphs.  In
addition to high-level capabilities, it has enough low-level
capabilities to allow users to achieve a high degree of customization.
Precise control is extended to all aspects of drawing, including
line-widths, colors, and fonts.  Text includes a subset of the tex
language, so that it is easy to incorporate Greek letters and
mathematical symbols in labels.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure
# BEGIN allow PS decoder for build [bsc#1109976]
mkdir -p ~/.config/ImageMagick
cat << EOPF > ~/.config/ImageMagick/policy.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policymap [
  <!ELEMENT policymap (policy)+>
  <!ATTLIST policymap xmlns CDATA #FIXED ''>
  <!ELEMENT policy EMPTY>
  <!ATTLIST policy xmlns CDATA #FIXED '' domain NMTOKEN #REQUIRED
    name NMTOKEN #IMPLIED pattern CDATA #IMPLIED rights NMTOKEN #IMPLIED
    stealth NMTOKEN #IMPLIED value CDATA #IMPLIED>
]>
<policymap>
  <policy domain="coder" rights="read" pattern="{PS}" />
</policymap>
EOPF
# END allow PS decoder for build [bsc#1109976]
# Parallel make does not work
make

%install
%make_install DESTDIR=%{buildroot}
# drop timestamp from texinfo
sed -i "s/<!-- [A-Z].. [A-Z].. .. ..:..:.. .... -->//" %{buildroot}%{_datadir}/%{name}/doc/html/index.html
%fdupes %{buildroot}%{_datadir}/%{name}/

%if 0%{?suse_version} <= 1500
%post
/sbin/install-info %{_infodir}/gri.info %{_infodir}/dir

%postun
/sbin/install-info --delete %{_infodir}/gri.info %{_infodir}/dir
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_bindir}/gri
%{_bindir}/gri_merge
%{_bindir}/gri_unpage
%{_datadir}/%{name}/
%{_datadir}/emacs/site-lisp/gri-mode.el
%{_infodir}/gri.info*
%{_mandir}/man1/gri*

%changelog
