#
# spec file for package ratslap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_unconverted 0.2.3

Name:           ratslap
Version:        0.2.3
Release:        0
Summary:        Linux configuration tool for Logitech mice
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://gitlab.com/krayon/ratslap
Source:         https://gitlab.com/krayon/ratslap/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libusb-1_0-devel
BuildRequires:  xz

%description
RatSlap provides a way to configure configurable Logitech mice from
within Linux.

Currently, only G300/G300S is supported.

%prep
%setup -q
%autopatch -p1

%build
make manpage.1 ratslap \
	CARCH_FLAG=' ' \
	OPT_FLAGS="%{optflags}" \
	MAJVER="%{version}" \
	APPBRANCH="release" \
	APPVER="%{version}" \
	BUILD_DATE="2019-02-05 14:46:45+0000" \
	BUILD_MONTH="02" \
	BUILD_YEAR="2019" \
	BUILD_COMMIT="n/a"

%install
install -m 0755 -d %{buildroot}/%{_bindir}
install -m 0755 -d %{buildroot}/%{_mandir}/man1

install -m 0755 ratslap %{buildroot}/%{_bindir}
install -m 0644 manpage.1 %{buildroot}/%{_mandir}/man1/ratslap.1

%files
%defattr(-,root,root)
%doc AUTHORS.creole CONTRIBUTING.creole README.creole
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
