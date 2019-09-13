#
# spec file for package svgcleaner
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           svgcleaner
Version:        0.9.5
Release:        0
Summary:        A software to remove unnecessary data from SVG files
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://github.com/RazrFalcon/svgcleaner
Source0:        v%{version}.tar.gz
Source1:        gui-v%{version}.tar.gz
Source2:        vendor.tar.xz
Patch0:         svgcleaner-gui-suse.patch
BuildRequires:  cargo
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  update-desktop-files
Requires:       %{name}-gui = %{version}
Requires:       p7zip

%description
Svgcleaner reduces the size of an SVG image by removing useless data such as
- temporary data used by the vector editing application
- non-optimal SVG structure representation
- unused and invisible graphical elements

%package -n svgcleaner-gui
Summary:        Graphical user interface to svgcleaner
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       p7zip

%description -n svgcleaner-gui
This package provides a Qt graphical user interface to svgcleaner.

%prep
%setup -q
%setup -q -a 1
%patch0 -p1
%setup -q -D -T -a 2
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export CARGO_HOME=`pwd`/cargo-home/
cargo build --release %{?_smp_mflags}
cd svgcleaner-gui-%{version}
%qmake5
%make_jobs
cd ..

%install
mkdir build
export CARGO_HOME=`pwd`/cargo-home/
cargo install --root=build
mkdir -p %{buildroot}%{_bindir}
install -Dm0775 build/bin/svgcleaner %{buildroot}%{_bindir}/svgcleaner
cd svgcleaner-gui-%{version}
%make_install INSTALL_ROOT=%{buildroot}
cd ..

%files
%license LICENSE.txt
%doc CHANGELOG.md FAQ.md data/help.txt
%attr(0755,-,-) %{_bindir}/svgcleaner

%files -n svgcleaner-gui
%{_bindir}/%{name}-gui
%attr(0644,-,-) %{_datadir}/applications/svgcleaner.desktop
%{_datadir}/icons/hicolor/scalable/apps/svgcleaner.svg

%changelog
