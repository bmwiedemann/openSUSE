#
# spec file for package vendored_licenses_packager
#
# Copyright (c) 2022 cunix
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

%define minisign_verify 0

Name:           vendored_licenses_packager
Version:        0.1.0
Release:        0
Summary:        Script to package legal files of vendored sources
License:        EUPL-1.2
Group:          Development/Tools/Building
Url:            https://codeberg.org/cunix/vendored_licenses_packager
Source0:        https://codeberg.org/attachments/23443436-3863-442e-9ba0-dac1ff13f646#/%{name}-%{version}.tar.xz
Source1:        https://codeberg.org/attachments/3b6f0375-36a8-4811-a83d-2d9f38bca835#/%{name}-%{version}.tar.xz.minisig
BuildArch:      noarch
%if 0%{?minisign_verify}
BuildRequires:  rsign2
%endif
Requires:       bash
Requires:       coreutils
Requires:       findutils

%description
This bash script with RPM macros may help packagers to include
some legal files of vendored dependencies.

%prep
%if 0%{?minisign_verify}
rsign verify \
  -P RWQ7vwLW5BF3r8teYKFPJuJb0NTCQi0OEhy3XvyySV78SIvlGE3ofPVx \
  -x %{SOURCE1} %{SOURCE0}
verified=$?
if [ $verified -ne 0 ];
  then
    echo source verification failed
    exit $verified
  else
    echo source verified
fi
%else
echo source not verified
%endif

%autosetup

%build

%install
install -D -p -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 macros.%{name} %{buildroot}%_rpmmacrodir/macros.%{name}

%files
%{_bindir}/%{name}
%_rpmmacrodir/macros.%{name}
%doc README.md
%license LICENCE.EUPL-1.2

%changelog
