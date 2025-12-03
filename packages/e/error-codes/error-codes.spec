#
# spec file for package error-codes
#
# Copyright (c) 2025 SUSE LLC
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

Name:           error-codes
Version:        0.2+git20251202.d72c330
Release:        0
Summary:        Lookup error codes and their description
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/error-codes
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libeconf)
Provides:       sudo = %{version}

%description
This command searches for error codes for errno, libeconf, and pam and displays the name of the error, its value, and its description.
Additionally, it is possible to search for words in the error description.
This can even be done for all language environments.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/error-codes
%{_mandir}/man1/error-codes.1%{?ext_man}

%changelog
