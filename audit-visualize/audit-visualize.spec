#
# spec file for package audit-visualize
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           audit-visualize
%define 	_name audit
Summary:        Visualization tools for the audit subsystem
License:        GPL-2.0+
Group:          System/Monitoring
Version:        1.5.2
Release:        0
Url:            http://people.redhat.com/sgrubb/audit/visualize/index.html
Source0:        audit-visualize.tar.gz
Patch0:         audit-visualize-fix-bashisms.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       audit
Requires:       gnuplot
Requires:       graphviz
BuildArch:      noarch

%description
The audit-visualize package contains scripts to produce flow graphs and
bar charts from audit data.

%prep
%setup -q -n audit-visualize
%patch0 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT/%_prefix/lib/%_name/visualize
mv README mkbar mkgraph $RPM_BUILD_ROOT/%_prefix/lib/%_name/visualize

%files
%defattr(-,root,root,-)
%dir %attr(755,root,root) %_prefix/lib/%_name
%dir %attr(755,root,root) %_prefix/lib/%_name/visualize
%attr(644,root,root) %_prefix/lib/%_name/visualize/README
%attr(755,root,root) %_prefix/lib/%_name/visualize/mkbar
%attr(755,root,root) %_prefix/lib/%_name/visualize/mkgraph

%changelog
