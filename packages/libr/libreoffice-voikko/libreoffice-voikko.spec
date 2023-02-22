#
# spec file for package libreoffice-voikko
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libreoffice-voikko
Version:        5.0
Release:        0
Summary:        LibreOffice spellchecker/hyphenator for finnish language
License:        GPL-3.0-or-later OR MPL-2.0
Group:          Productivity/Text/Spell
URL:            http://voikko.puimula.org/
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  libreoffice >= 4.1
BuildRequires:  libreoffice-sdk >= 4.1
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  pkgconfig(libvoikko)
Requires:       python3-libvoikko
Provides:       locale(libreoffice:fi)
ExclusiveArch:  aarch64 %{ix86} x86_64 ppc64le riscv64

%description
LibreOffice spellchecker/hyphenator for finnish language, which uses
libvoikko as backend.

%prep
%setup -q

%build
. %{_libdir}/libreoffice/sdk/setsdkenv_unix.sh
make oxt %{?_smp_mflags}

%install
voikko_pkg=$(pwd)/build/voikko.oxt
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions/voikko
cd %{buildroot}%{_libdir}/libreoffice/share/extensions/voikko
unzip $voikko_pkg

%files
%license COPYING
%doc README
%defattr(644,root,root,755)
%{_libdir}/libreoffice/share/extensions/voikko

%changelog
