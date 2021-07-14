#
# spec file for package autoyast_xml_validator
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


Name:           autoyast_xml_validator
Version:        1.0.9+gite8164d1
Release:        0
Summary:        Cross distribution and cross architecture autoyast XML syntax checker
License:        GPL-2.0-or-later
Group:          System/YaST
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  go-md2man
Requires:       jing
Requires:       libxml2-tools
Requires:       yast2-schema-collection
BuildArch:      noarch

%description
Developing autoyast XML files for autoinstallation, this checker comes in
really handy. It can compatibility check XML files and validate against
all recent released SUSE distributions.
Avoid time consuming fiddling and trial on error approaches.
When you already have valid autoyast configuration files and you want to
install more recent distributions, use this tool to verify that your XML
syntax is still backward compatible.
se this validator to make your XML autoyast files more robust and stable
before even starting an auto-installation.

%prep
%setup -q

%build
go-md2man -in README.md |gzip  >autoyast-xml-validate.1.gz

%install
install -m 0755 -D autoyast-xml-validate.py %{buildroot}%{_bindir}/autoyast-xml-validate
install -m 0644 -D autoyast-xml-validate.1.gz %{buildroot}%{_mandir}/man1/autoyast-xml-validate.1.gz

%files
%doc README.md
%license LICENSE
%{_bindir}/autoyast-xml-validate
%{_mandir}/man1/autoyast-xml-validate*

%changelog
