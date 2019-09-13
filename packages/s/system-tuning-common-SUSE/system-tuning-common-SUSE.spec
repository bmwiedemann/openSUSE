#
# spec file for package system-tuning-common-SUSE
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


Name:           system-tuning-common-SUSE
Version:        0.1
Release:        0
Summary:        SUSE specific udev tuning rules
License:        GPL-2.0-or-later
Group:          System/Base
Url:            https://github.com/openSUSE/system-tuning-SUSE
Source0:        %{name}-%{version}.tar.xz
Requires:       systemd
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains SUSE specific hardware tunings common to all SUSE brands.

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d/

for RULE in $(ls *.rules); do
    install -m 644 $RULE %{buildroot}/%{_prefix}/lib/udev/rules.d/
done

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%defattr(-,root,root)
%doc
%{_prefix}/lib/udev/rules.d/*.rules

%changelog
