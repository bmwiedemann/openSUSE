#
# spec file for package element-web
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


Name:           element-web
Version:        1.9.8
Release:        0
Summary:        A glossy Matrix collaboration client - web files
License:        Apache-2.0
URL:            https://github.com/vector-im/element-web
Source0:        element-%{version}.tar.gz
Source1:        https://github.com/vector-im/element-web/archive/v%{version}.tar.gz#/element-web-%{version}.tar.gz
Source2:        prepare_tarball.sh
BuildRequires:  nodejs-electron
BuildArch:      noarch

%description
A glossy Matrix collaboration client - web files

%prep
%autosetup -n element-%{version}

%build
tar xzvf %{SOURCE1} --strip-components 1 element-web-%{version}/LICENSE

%install
install -d %{buildroot}/{usr/share/webapps,etc/webapps}/element

cp -r * "%{buildroot}%{_datadir}/webapps/element/"
install -Dm644 config.sample.json -t "%{buildroot}%{_sysconfdir}/webapps/element/"

%files
%license LICENSE
%{_datadir}/webapps/element
%{_sysconfdir}/webapps/element

%changelog
