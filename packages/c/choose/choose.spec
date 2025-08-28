#
# spec file for package choose
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           choose
Version:        1.3.7
Release:        0
Summary:        A human-friendly and fast alternative to cut and (sometimes) awk
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/theryangeary/choose
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel

%description
A human-friendly and fast alternative to cut and (sometimes) awk.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/%{name}

%changelog
