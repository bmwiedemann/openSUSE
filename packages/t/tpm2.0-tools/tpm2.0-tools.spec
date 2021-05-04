#
# spec file for package tpm2.0-tools
#
# Copyright (c) 2021 SUSE LLC
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


Name:           tpm2.0-tools
Version:        5.0
Release:        0
Summary:        Trusted Platform Module (TPM) 2.0 administration tools
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-tools/releases
Source0:        https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/tpm2-tools-%{version}.tar.gz
Patch0:         fix_bogus_warning.patch
Patch1:         fix_warnings.patch
Patch2:         fix_pie_linking.patch
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
%if 0%{?is_opensuse}
# releases prior to 3.0.4 required pandoc for building the man pages. On SLE
# we don't have pandoc and it requires a complete haskell stack so adding it
# is out of the question just for man pages.
#
# since 3.0.4 the man pages are shipped with the distribution tarball and we
# don't need to generate them any more. On openSUSE we can still keep this
# dependency for having fresh builds of the man pages (if that helps
# anything?).
#
# Update: In the 3.1.0 a required patch is still missing and the man pages
# won't be installed. they're shipped, though. so if pandoc isn't installed we
# need to install them explicitly.
BuildRequires:  pandoc
%endif
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  tpm2.0-abrmd-devel
BuildRequires:  unzip
Recommends:     tpm2.0-abrmd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm2.0-tools package
provides tools for enablement and configuration of the TPM 2.0 and
associated interfaces.

%prep
%setup -q -n tpm2-tools-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# TODO: remove autoreconf once fix_pie_linking patch is no longer needed
# until then we need to repair the version specification which configure.ac
# wants to read from GIT which isn't there.
sed -i 's/m4_esyscmd_s([^)]\+)/%{version}/g' configure.ac
autoreconf -fvi
%configure --disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%doc README.md doc/CHANGELOG.md
%license doc/LICENSE
/usr/bin/tpm2*
/usr/bin/tss2*
%{_mandir}/man1/tpm2*
%{_mandir}/man1/tss2*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*

%changelog
