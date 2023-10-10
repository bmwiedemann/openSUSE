#
# spec file for package xaos
#
# Copyright (c) 2023 SUSE LLC
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


%define alt_name XaoS
Name:           xaos
Version:        4.3.1
Release:        0
Summary:        Powerful fractal generator
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
URL:            https://xaos-project.github.io
Source0:        https://github.com/xaos-project/XaoS/archive/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
Provides:       %{alt_name}

%description
XaoS is a fast portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you to zoom smoothly into the fractal.  Various coloring modes
are provided for both the points inside and outside the selected set.
In addition, switching between Julia and Mandelbrot fractal types and
displaying planes is provided.

%prep
%setup -q -n XaoS-release-%{version}

%build
%qmake6 PREFIX=%{_prefix}
%qmake6_build

%install
# Binary
%qmake6_install

# Examples
mkdir -p %{buildroot}%{_datadir}/%{alt_name}
find examples -name \'*.xpf\' -exec cp {} %{buildroot}%{_datadir}/%{alt_name}/examples \;

# Data; Datapath forced to %%{alt_name} (not configurable)
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/%{alt_name}/catalogs catalogs/*.cat
cp --archive examples tutorial %{buildroot}%{_datadir}/%{alt_name}

# Icon, .desktop, AppData
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/metainfo xdg/%{name}.appdata.xml
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/applications xdg/*.desktop
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/pixmaps xdg/%{name}.png

# Man
install -D --mode 0644 --target-directory %{buildroot}%{_mandir}/man6 doc/%{name}.6

%fdupes %{buildroot}%{_datadir}/%{alt_name}/examples/

%files
%doc CREDITS.md NEWS doc/README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{alt_name}/
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
