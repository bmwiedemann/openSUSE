#
# spec file for package flocc
#
# Copyright (c) 2024 SUSE LLC
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
Name:           flocc
Version:        0.1
Release:        0
Summary:        The Fast Lines Of Code Counter
License:        GPL-2.0-or-later
URL:            https://github.com/joergroedel/flocc
Source0:        flocc-%{version}.tar.xz
BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  libgit2-devel
BuildRequires:  make
BuildRequires:  perl

%description
Count the lines of code, comments and blank lines in a source tree and
print detailed statistics.

%prep
%autosetup

%build
%make_build CXXFLAGS="%{optflags} -std=c++11"

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
make install BIN_DIR=%{buildroot}%{_bindir}/ MAN_DIR=%{buildroot}%{_mandir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
