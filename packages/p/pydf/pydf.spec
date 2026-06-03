#
# spec file for package pydf
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           pydf
Version:        16
Release:        0
Summary:        Fully colorized df clone written in python
License:        SUSE-Public-Domain
URL:            http://kassiopeia.juls.savba.sk/~garabik/software/pydf
Source:         https://deb.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.gz
BuildArch:      noarch

%description
pydf displays the amount of used and available space on your file systems,
just like df, but in colors. The output format is completely customizable.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -Dpm 0755 pydf   \
  %{buildroot}%{_bindir}/pydf
install -Dpm 0644 pydfrc \
  %{buildroot}%{_sysconfdir}/pydfrc
install -Dpm 0644 pydf.1 \
  %{buildroot}%{_mandir}/man1/pydf.1

%files
%license COPYING
%doc CHANGES README.md
%config(noreplace) %{_sysconfdir}/pydfrc
%{_bindir}/pydf
%{_mandir}/man1/pydf.1%{?ext_man}

%changelog
