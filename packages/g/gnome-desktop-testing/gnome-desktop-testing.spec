#
# spec file for package gnome-desktop-testing
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gnome-desktop-testing
Version:        2021.1
Release:        0
Summary:        Runner for GNOME installed tests
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-desktop-testing
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(libsystemd)

%description
This package provides the gnome-desktop-testing-runner binary (also
symlinked as ginsttest-runner), the standard runner for the GNOME
installed-tests infrastructure. It discovers and executes test programs
installed under the system libexec installed-tests directory, using
the .test metadata files in the system data installed-tests directory.

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure \
    --disable-static
%make_build

%install
%make_install

%check
# gnome-desktop-testing-runner is a test runner, not a package with its own
# upstream test suite. Functional validation is done by running it against
# installed test packages (e.g. libxmlb-tests, graphene-tests) post-install.

%files
%license COPYING
%doc README.md
%{_bindir}/gnome-desktop-testing-runner
%{_bindir}/ginsttest-runner
%{_mandir}/man1/gnome-desktop-testing-runner.1%{?ext_man}
%{_mandir}/man1/ginsttest-runner.1%{?ext_man}

%changelog
