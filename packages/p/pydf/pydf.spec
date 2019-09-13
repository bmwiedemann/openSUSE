#
# spec file for package pydf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pydf
Version:        12
Release:        0
Summary:        Fully colorized df clone written in python
License:        SUSE-Public-Domain
Group:          System/Monitoring
Url:            http://kassiopeia.juls.savba.sk/~garabik/software/pydf
Source:         http://kassiopeia.juls.savba.sk/~garabik/software/pydf/pydf_%{version}.tar.gz
BuildArch:      noarch

%description
pydf displays the amount of used and available space on your file systems,
just like df, but in colors. The output format is completely customizable.

%prep
%setup -q
# use python3 by default
sed -i "s|%{_bindir}/python|%{_bindir}/python3|g" pydf

%build

%install
install -Dpm 0755 pydf   \
  %{buildroot}%{_bindir}/pydf
install -Dpm 0644 pydfrc \
  %{buildroot}%{_sysconfdir}/pydfrc
install -Dpm 0644 pydf.1 \
  %{buildroot}%{_mandir}/man1/pydf.1

%files
%doc README COPYING
%config(noreplace) %{_sysconfdir}/pydfrc
%{_bindir}/pydf
%{_mandir}/man1/pydf.1%{ext_man}

%changelog
