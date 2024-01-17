#
# spec file for package xcwd
#
# Copyright (c) 2020 SUSE LLC
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           xcwd
Version:        1.0
Release:        0
Summary:        X current working directory
License:        BSD-3-Clause
Group:          System/X11/Utilities
URL:            https://github.com/schischi/xcwd
Source:         https://github.com/schischi/xcwd/archive/v1.0.tar.gz
BuildRequires:  libX11-devel

%description
xcwd is a simple tool which print the current working directory of the currently focused window.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
%make_install prefix=%{buildroot}/%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/xcwd

%changelog
