#
# spec file for package libmicro
#
# Copyright (c) 2019 SUSE LLC
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


Name:           libmicro
Version:        0.4.2+hg.20120726
Release:        0
Summary:        LibMicro is a portable set of microbenchmarks
License:        CDDL-1.0
Group:          System/Benchmark
URL:            https://java.net/projects/libmicro
Source0:        %{name}-%{version}.tar.xz
Patch0:         find_binary.patch
Patch1:         removed_undefined_warning.patch
Patch2:         fix-link.diff
Patch3:         libmicro-implicit-fortify-decl.patch

%description
LibMicro is a portable set of microbenchmarks that many Solaris
engineers used during Solaris 10 development to measure the
performance of various system and library calls.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
rm bin-*/*.a
rm bin-*/*.h
rm bin-*/*.o
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/libMicro/bin
cp bin/* %{buildroot}%{_libexecdir}/libMicro/bin
cp bin-*/* %{buildroot}%{_libexecdir}/libMicro/bin
install -m 755 bench.sh %{buildroot}%{_bindir}
install -m 755 multiview.sh %{buildroot}%{_bindir}

%files
%license OPENSOLARIS.LICENSE
%doc README
%{_libexecdir}/libMicro
%{_bindir}/bench.sh
%{_bindir}/multiview.sh

%changelog
