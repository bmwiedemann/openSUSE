#
# spec file for package fhs
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

Name:           fhs
Version:        3.0
Release:        0
License:        SUSE-FHS
Group:          Documentation/Other
Summary:        Filesystem Hierarchy Standard
Url:            https://refspecs.linuxfoundation.org/fhs
BuildArch:      noarch
Source0:        fhs-%{version}.txt
Source1:        fhs-%{version}.pdf
Source2:        fhs-%{version}.html
Source3:        tip.gif

%description
This standard consists of a set of requirements and guidelines for file
and directory placement under UNIX-like operating systems.  The
guidelines are intended to support application interoperability, system
administration tools, development tools, and scripts as well as greater
uniformity of documentation for these systems.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/doc/FHS
install -m644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_datadir}/doc/FHS

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/FHS

%changelog
