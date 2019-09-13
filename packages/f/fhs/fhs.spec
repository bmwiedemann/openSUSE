#
# spec file for package fhs (Version 2.3)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Url:            http://www.pathname.com/fhs/

Name:           fhs
License:        SUSE-FHS
Group:          Documentation/Other
Summary:        File System Hierarchy Standard
Version:        2.3
Release:        178
BuildArch:      noarch
Source:         fhs-2.3.txt
Source1:        fhs-2.3.pdf
Source2:        fhs-2.3.html
Source3:        tip.gif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%prep

%install
rm -rf $RPM_BUILD_ROOT%{_docdir}/../FHS
mkdir -p $RPM_BUILD_ROOT%{_docdir}/../FHS
install -m644 %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 $RPM_BUILD_ROOT%{_docdir}/../FHS

%files
%defattr(644,root,root,755)
%doc %{_docdir}/../FHS

%description
This standard consists of a set of requirements and guidelines for file
and directory placement under UNIX-like operating systems.  The
guidelines are intended to support application interoperability, system
administration tools, development tools, and scripts as well as greater
uniformity of documentation for these systems.

%changelog
