#
# spec file for package littlewizard-examples
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           littlewizard-examples
Version:        20071206
Release:        3
License:        SUSE-Public-Domain
Summary:        Example files for Little Wizard
Url:            http://littlewizard.sourceforge.net/
Group:          Development/Tools/IDE
Source0:        examples-%{version}.zip
BuildRequires:  unzip
Requires:       littlewizard
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Little Wizard is created especially for primary school children. It allows to
learn using main elements of present computer languages, including: variables,
expressions, loops, conditions, logical blocks. Every element of language is
represented by an intuitive icon. It allows program Little Wizard without
using keyboard, only mouse.

This package contains example files for Little Wizard.

%prep
%setup -q -n examples-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/littlewizard/examples
cp -a * %{buildroot}/%{_datadir}/littlewizard/examples/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/littlewizard
%dir %{_datadir}/littlewizard/examples
%{_datadir}/littlewizard/examples

%changelog
