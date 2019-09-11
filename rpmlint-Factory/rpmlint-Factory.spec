#
# spec file for package rpmlint-Factory
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


Name:           rpmlint-Factory
Requires:       rpmlint-mini
Summary:        RPM file correctness checker - openSUSE:Factory configuration
License:        GPL-2.0-or-later
Group:          System/Packages
Version:        1.0
Release:        0
Url:            http://rpmlint.zarb.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:        COPYING
Source2:        config
Source3:        config.strict
BuildArch:      noarch

%description
rpmlint is a tool to check common errors on RPM packages. This package
provides the configuration specific for SUSE Factory.

%package strict
Summary:        Conflict only applying to openSUSE:Factory itself
Group:          System/Packages

%description strict
The package contains additional rpmlint configuration that forbids
invalid licenses.

%prep
cp %{SOURCE1} .

%build

%install
install -m 644 -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/rpmlint/factory.config
install -m 644 -D %{SOURCE3} %{buildroot}/%{_sysconfdir}/rpmlint/factory-strict.config

%files
%defattr(-,root,root,0755)
%doc COPYING
%dir %{_sysconfdir}/rpmlint
%{_sysconfdir}/rpmlint/factory.config

%files strict
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/rpmlint
%{_sysconfdir}/rpmlint/factory-strict.config

%changelog
