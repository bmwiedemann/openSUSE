#
# spec file for package libwhich
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libwhich
Version:        1.2.0
Release:        0
Summary:        Which for Dynamic Libraries
License:        MIT
URL:            https://github.com/vtjnash/libwhich
Source0:        https://github.com/vtjnash/libwhich/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc

%description
A command line utility to locate shared libraries by name.

%prep
%setup -q

%build
%make_build

%install
install -D -m 755 libwhich %{buildroot}/%{_bindir}/libwhich

%files
%license LICENSE
%doc README.md
%{_bindir}/libwhich

%changelog
