#
# spec file for package xa
#
# # Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

Name:           xa
Version:        2.3.14
Release:        0
Summary:        High-speed, two-pass portable 6502 cross-assembler
License:        GPL-2.0-or-later
Group:          Development/Languages/Other
URL:            https://www.floodgap.com/retrotech/xa/
Source:         https://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz
Patch0:         xa-fix-install.patch

%description
xa is a high-speed, two-pass portable cross-assembler for the 6502 CPU
with a C-like preprocessor. One of several popular 65xx assemblers, xa
is written in C and released under the GPL-2. It has been in continuous
development since 1989.

Other tools in the xa package are:
 * file65   - a tool for printing information about o65 object files.
 * ldo65    - a linker for o65 object files.
 * printcbm - a simple CBM BASIC detokenizer similar to the far more
              powerful petcat proviced by VICE.
 * reloc65  - a relocator for o65 object files.
 * uncpk    - a c64 cpk archive manager.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}%{_prefix}

%check
make test

%files
%license COPYING
%doc ChangeLog
%{_bindir}/file65
%{_bindir}/ldo65
%{_bindir}/printcbm
%{_bindir}/reloc65
%{_bindir}/uncpk
%{_bindir}/xa
%{_mandir}/man1/file65.1%{?ext_man}
%{_mandir}/man1/ldo65.1%{?ext_man}
%{_mandir}/man1/printcbm.1%{?ext_man}
%{_mandir}/man1/reloc65.1%{?ext_man}
%{_mandir}/man1/uncpk.1%{?ext_man}
%{_mandir}/man1/xa.1%{?ext_man}

%changelog
