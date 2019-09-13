#
# spec file for package utfcpp
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


%define         uglyver 2_3_4
Name:           utfcpp
Version:        2.3.4
Release:        0
Summary:        A library for handling UTF-8 encoded strings
License:        BSL-1.0
Group:          Development/Libraries/C and C++
Url:            http://sourceforge.net/projects/utfcpp/
Source:         http://download.sourceforge.net/%{name}/utf8_v%{uglyver}.zip
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for handling UTF-8 encoded strings.

%prep
%setup -q -n source

%build

%install
install -d %{buildroot}/%{_includedir}/utf8
install -m0644 utf8.h %{buildroot}/%{_includedir}
install -m0644 utf8/{checked,unchecked,core}.h %{buildroot}/%{_includedir}/utf8

%package devel
Summary:        A library for handling UTF-8 encoded strings
Group:          Development/Libraries/C and C++

%description devel
A library for handling UTF-8 encoded strings.

%files devel
%defattr(-,root,root)
%{_includedir}/utf8/
%{_includedir}/utf8.h

%changelog
