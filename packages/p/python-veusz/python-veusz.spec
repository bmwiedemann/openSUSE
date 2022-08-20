#
# spec file for package python-veusz
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


Name:           python-veusz
Version:        3.4
Release:        0
Summary:        Scientific plotting library for Python
# The entire source code is GPL-2.0+ except helpers/src/_nc_cntr.c which is Python-2.0
License:        GPL-2.0-or-later AND Python-2.0
URL:            https://veusz.github.io/
Source0:        https://files.pythonhosted.org/packages/source/v/veusz/veusz-%{version}.tar.gz
Source3:        veusz_256.png
# PATCH-FIX-UPSTREAM veusz-sip65.patch gh#veusz/veusz#595 -- fix build with SIP 6.5
Patch0:         veusz-sip65.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sip-devel
BuildRequires:  python3-toml
BuildRequires:  update-desktop-files
# SECTION For Tests
BuildRequires:  python3-astropy
BuildRequires:  python3-h5py
# /SECTION
ExcludeArch:    i586

%description
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%package     -n veusz
Summary:        GUI scientific plotting package
Requires:       python3-numpy
Requires:       python3-qt5
Recommends:     python3-astropy
Recommends:     python3-h5py
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun):desktop-file-utils
Requires(postun):shared-mime-info
Obsoletes:      veusz3 < %{version}-%{release}
Provides:       veusz3 = %{version}-%{release}
Obsoletes:      python3-veusz < %{version}-%{release}
Provides:       python3-veusz = %{version}-%{release}
Obsoletes:      %{primary_python}-veusz < %{version}-%{release}
Provides:       %{primary_python}-veusz = %{version}-%{release}

%description -n veusz
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%prep
%autosetup -p1 -n veusz-%{version}
find -name \*~ | xargs rm -f

# Remove hashbangs from eventually non-executable scripts
sed -E -i "/\#!\/usr\/bin\/env python/d" veusz/veusz_{listen,main}.py

%build
export CFLAGS="%{optflags}"
%python3_build

%install
%python3_install

# Install .desktop, mime and appdata files from upstream tarball
install -Dm0644 support/veusz.appdata.xml %{buildroot}%{_datadir}/appdata/veusz.appdata.xml
install -Dm0644 support/veusz.xml %{buildroot}/%{_datadir}/mime/packages/veusz.xml
desktop-file-install -m 0644 \
  --dir=%{buildroot}/%{_datadir}/applications/ \
  --add-category=2DGraphics \
  support/veusz.desktop

# move icon files to /usr/share/pixmaps/veusz
install -m 0644 %{SOURCE3} %{buildroot}%{python3_sitearch}/veusz/icons/veusz_256.png
mkdir -p %{buildroot}%{_datadir}/pixmaps/veusz
ln -s %{python3_sitearch}/veusz/icons %{buildroot}%{_datadir}/pixmaps/veusz

# hardlink main veusz icon also into hicolor-icon-theme dir (for desktop file)
for size in 16 32 48 64 128 256; do
    odir=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p $odir
    ln -s %{python3_sitearch}/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $odir
ln -s %{python3_sitearch}/veusz/icons/veusz.svg $odir/veusz.svg

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p Documents/man-page/veusz.1 -m 0644 %{buildroot}%{_mandir}/man1

# Remove an unneeded hidden file from documentation
rm Documents/manual/html/.buildinfo

%fdupes %{buildroot}%{python3_sitearch}/veusz/

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
QT_QPA_PLATFORM=minimal python3 -B tests/runselftest.py

%post -n veusz
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications
%icon_theme_cache_post

%postun -n veusz
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications
%icon_theme_cache_postun

%files -n veusz
%doc README.md AUTHORS ChangeLog
%doc Documents/manual/html
%license COPYING
%{_bindir}/veusz
%{_datadir}/applications/veusz.desktop
%{_datadir}/pixmaps/veusz/
%dir %{_datadir}/appdata
%{_datadir}/appdata/veusz.appdata.xml
%{_datadir}/icons/hicolor/*/apps/veusz.*
%{_datadir}/mime/packages/veusz.xml
%{_mandir}/man1/*
%{python3_sitearch}/veusz-%{version}*-info
%{python3_sitearch}/veusz/

%changelog
