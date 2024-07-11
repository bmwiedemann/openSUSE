#
# spec file for package siga
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010-7/2011 Sascha Manns <saigkill@opensuse.org>
# Copyright (c) 8/2011 - now open-slx GmbH <Sascha.Manns@open-slx.de>
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


%define _gitrev f692b3a

Name:           siga
Version:        12.101
Release:        0
Summary:        System Information GAthering
License:        GPL-2.0+
Group:          Documentation/SUSE
Url:            http://github.com/saigkill/siga
Source:         saigkill-%{name}-%{_gitrev}.tar.bz2
Requires:       w3m
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
SIGA stands for System Information GAthering. It collects various
system information and outputs it in HTML or ASCII format. Since it
needs root permissions, you will be asked for the root password. It is
very handy as an information source during installation support phone
calls.

%prep
%setup -q -n saigkill-siga-%{_gitrev}

%build

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install -m 755 siga %{buildroot}/%{_bindir}
install -m 644 siga.1.gz %{buildroot}/%{_mandir}/man1/siga.1.gz

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG README
%{_bindir}/siga
%{_mandir}/man1/siga.1.gz

%changelog
