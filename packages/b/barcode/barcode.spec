#
# spec file for package barcode
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


Name:           barcode
Version:        0.99
Release:        0
Summary:        Text-Mode Barcode Creation Utility
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.gnu.org/software/barcode
Source0:        ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE barcode-0.99-info.patch
Patch2:         %{name}-0.99-info.patch
# PATCH-FIX-UPSTREAM barcode-0.98-leak-fix.patch bnc#537525 -- Fix memory leak by adding call to free.
Patch5:         %{name}-0.98-leak-fix.patch
# PATCH-FIX-UPSTREAM barcode-fix-renamed-include.patch malcolmlewis@opensuse.org -- Fix renamed gettext include header reference.
Patch6:         barcode-fix-renamed-include.patch
BuildRequires:  makeinfo
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU Barcode is meant to meet most barcode creation needs with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated in either PostScript or
Encapsulated PostScript format.

%package devel
Summary:        Text-Mode Barcode Creation Utility - Development files
Group:          Development/Libraries/C and C++

%description devel
GNU Barcode is meant to meet most barcode creation needs with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated in either PostScript or
Encapsulated PostScript format.

%prep
%setup -q
%patch2
%patch5
%patch6 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build

%install
%make_install
install -Dm0644 barcode.h %{buildroot}%{_includedir}/barcode.h
install -Dm0644 .libs/libbarcode.a %{buildroot}%{_libdir}/libbarcode.a

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING
%doc README TODO
%{_bindir}/barcode
%{_bindir}/sample
%{_infodir}/%{name}.info%{?ext_info}

%files devel
%{_includedir}/barcode.h
%{_libdir}/libbarcode.a

%changelog
