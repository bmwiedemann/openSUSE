#
# spec file for package mapi-header-php
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


%define _empty_manifest_terminate_build 0

Name:           mapi-header-php
Version:        1.6
Release:        0
Summary:        Common PHP MAPI header files for grommunio
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
#Git-Clone:     https://github.com/grommunio/mapi-header-php
Source:         https://github.com/grommunio/mapi-header-php/releases/download/%version/mapi-header-php-%version.tar.zst
Source2:        https://github.com/grommunio/mapi-header-php/releases/download/%version/mapi-header-php-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  zstd
BuildArch:      noarch

%description
PHP files shared between grommunio-web, grommunio-sync and other PHP
applications from the groupware suite.

%prep
%autosetup -p1

%build

%install
%make_install

%files
%_datadir/php-mapi/
%license LICENSE.txt

%changelog
