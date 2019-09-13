#
# spec file for package schedtool
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Name:           schedtool
Version:        1.3.0
Release:        0
Summary:        Query and set CPU scheduling parameters
License:        GPL-2.0
Group:          System/Monitoring
Url:            http://freequaos.host.sk/schedtool/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
schedtool can set all CPU scheduling parameters Linux is capable
of or display information for given processes.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="$CXXFLAGS"
make %{?_smp_mflags}

%install
install -D -s -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{name}.8 %{buildroot}/%{_mandir}/man8/%{name}.8

# Docs
install -d %{buildroot}%{_docdir}/%{name}
install -m 0644 CHANGES LICENSE README SCHED_DESIGN TODO TUNING %{buildroot}%{_docdir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}
%doc %{_docdir}/%{name}

%changelog
