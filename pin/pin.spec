#
# spec file for package pin
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pin
Version:        0.40
Release:        0
Summary:        A tool for finding package information
License:        GPL-2.0+
Group:          Documentation/SUSE
Url:            http://www.hennevogel.de/scripts/pin/
Source:         pin
Source1:        pin.1.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Pin - Package InformatioN. Pin searches the installed packages (rpm
-qi, -ql) and the ARCHIVES.gz file for the desired information. It
shows README, README.SuSE, and FAQ, when available.

%prep
:

%build
:

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/pin.1.gz
install -d %{buildroot}/%{_localstatedir}/lib/%{name}
touch %{buildroot}/%{_localstatedir}/lib/%{name}/ARCHIVES.gz

%post
touch %{_localstatedir}/lib/%{name}/ARCHIVES.gz

%files
%defattr(-,root,root)
%{_bindir}/pin
%{_mandir}/man1/pin.1.gz
%dir %{_localstatedir}/lib/%{name}
%ghost %{_localstatedir}/lib/%{name}/ARCHIVES.gz

%changelog
