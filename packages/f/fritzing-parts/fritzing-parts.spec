#
# spec file for package fritzing-parts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           fritzing-parts
Version:        0.9.3b
Release:        0
Summary:        Electronic components for use in the Fritzing app (aka the parts library)
License:        CC-BY-SA-3.0
Group:          Productivity/Scientific/Electronics
Url:            http://fritzing.org/
Source0:        https://github.com/fritzing/fritzing-parts/archive/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/fritzing/fritzing-app/master/LICENSE.CC-BY-SA
BuildArch:      noarch
BuildRequires:  fdupes

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fritzing is an open-source initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to actual product. It is in the spirit of Processing and Arduino which
allows users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

This packages contains the parts definitions for the electronic
components used in the Fritzing app.

%prep
%setup -q -n %{name}-%{version}

%build

%install
cp %{SOURCE1} .
mkdir -p %{buildroot}%{_datadir}/fritzing/parts/
cp -a * %{buildroot}%{_datadir}/fritzing/parts/

find %{buildroot}%{_datadir}/fritzing/ -type f -exec chmod -x {} \;
%fdupes %{buildroot}%{_datadir}/fritzing/parts

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.CC-BY-SA
%{_datadir}/fritzing/

%changelog
