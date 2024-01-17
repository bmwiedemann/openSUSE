#
# spec file for package inwee
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           inwee
Version:        0.2.0
Release:        0
Summary:        Wrapper around WeeChat's FIFO pipe
License:        MIT
Group:          Productivity/Networking/IRC
Url:            https://github.com/susam/inwee
Source0:        https://github.com/susam/inwee/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       weechat
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Conveniently send text and commands from file or standard input to WeeChat with this wrapper around WeeChat's FIFO pipe

%prep
%setup -q

%build

%install
install -Dm755 inwee %{buildroot}%{_bindir}/inwee

%files
%{_bindir}/inwee
%doc CHANGES.md README.md
%license LICENSE.md

%changelog
