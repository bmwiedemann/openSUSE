#
# spec file for package unar
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


Name:           unar
Version:        1.10.7
Release:        0
Summary:        Multi-format unarchiver
License:        LGPL-2.1-or-later
URL:            https://unarchiver.c3.cx/commandline
Source0:        https://github.com/MacPaw/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  gcc-c++
BuildRequires:  gcc-objc
BuildRequires:  gnustep-base-devel
BuildRequires:  gnustep-make
BuildRequires:  libbz2-devel
BuildRequires:  libicu-devel
BuildRequires:  unzip
BuildRequires:  wavpack-devel
BuildRequires:  zlib-devel

%description
The Unarchiver is originally a Mac OS X application. This package
contains a command-line variant of it. Unarchiver handles ZIP, ZIPX,
RAR, 7z, tar, gzip, bzip2, lzma, xz, CAB, MSI, NSIS, some
self-extracting EXEs, cpio, and further obscure and old formats, as
well as disc images in ISO, BIN, MDF, NRG, CDI. It supports filenames
in foreign character sets.

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags}"
export OBJCFLAGS="$(gnustep-config --objc-flags)"
%make_build -C XADMaster -f Makefile.linux

%install
install -d %{buildroot}%{_bindir}
install -m755 XADMaster/lsar XADMaster/unar -t %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m644 XADMaster/Extra/lsar.1 XADMaster/Extra/unar.1 -t %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_datadir}/bash-completion/completions
install -m644 XADMaster/Extra/lsar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lsar
install -m644 XADMaster/Extra/unar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/unar

%files
%license LICENSE
%doc README.md
%{_bindir}/lsar
%{_bindir}/unar
%{_mandir}/man1/lsar.1%{?ext_man}
%{_mandir}/man1/unar.1%{?ext_man}
%{_datadir}/bash-completion/completions/lsar
%{_datadir}/bash-completion/completions/unar

%changelog
