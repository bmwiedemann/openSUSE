#
# spec file for package udev-extra-rules
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


Name:           udev-extra-rules
Version:        0.2
Release:        0
Summary:        SUSE specific hardware tuning rules
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/udev-extra-rules.git
Source0:        %{name}-%{version}.tar.xz
Requires:       systemd
Provides:       system-tuning-common-SUSE = %{version}
Obsoletes:      system-tuning-common-SUSE < %{version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
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
