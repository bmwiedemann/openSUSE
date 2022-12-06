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


%define X_display ":98"

%define         skip_python2  1
%define         skip_python36 1
Name:           python-veusz
Version:        3.5.3
Release:        0
Summary:        Scientific plotting library for Python
# The entire source code is GPL-2.0+ except helpers/src/_nc_cntr.c which is Python-2.0
License:        GPL-2.0-or-later AND Python-2.0
URL:            https://veusz.github.io/
Source0:        https://files.pythonhosted.org/packages/source/v/veusz/veusz-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sip-devel}
BuildRequires:  %{python_module tomli}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  man
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-server-Xvfb
Requires:       python-numpy
Requires:       python-qt5
Requires:       veusz-common
Recommends:     python-astropy
Recommends:     python-h5py
Recommends:     veusz
ExcludeArch:    i586
# SECTION For Tests
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module h5py}
# /SECTION
%python_subpackages

%description
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%package     -n veusz
Summary:        GUI scientific plotting package
Requires:       python3-veusz = %{version}
Requires:       veusz-common
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun):desktop-file-utils
Requires(postun):shared-mime-info
Obsoletes:      veusz3 < %{version}
Provides:       veusz3 = %{version}

%description -n veusz
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%package -n veusz-common
Summary:        Common example and icons for all python flavors of veusz
BuildArch:      noarch

%description -n veusz-common
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output.

This package provides datafiles, examples, and icons used by all
python flavours of veusz.

%prep
%autosetup -p1 -n veusz-%{version}
find -name \*~ | xargs rm -f

# Remove hashbangs from eventually non-executable scripts
sed -E -i "/\#!\/usr\/bin\/env python/d" veusz/veusz_{listen,main}.py

%build
export CFLAGS="%{optflags}"
%python_build
%make_build -C Documents/ man

%install
%python_install

# Copy common files to /usr/share/ and...
mkdir -p %{buildroot}%{_datadir}/veusz
cp -pr examples icons %{buildroot}%{_datadir}/veusz/

%{python_expand # ...symlink them back into python_sitearch
rm -fr %{buildroot}%{$python_sitearch}/veusz/{examples,icons}
ln -s -t %{buildroot}%{$python_sitearch}/veusz/ %{_datadir}/veusz/{examples,icons}
}

# Install .desktop, mime and appdata files from upstream tarball
install -Dm0644 support/veusz.appdata.xml %{buildroot}%{_datadir}/appdata/veusz.appdata.xml
install -Dm0644 support/veusz.xml %{buildroot}/%{_datadir}/mime/packages/veusz.xml
desktop-file-install -m 0644 \
  --dir=%{buildroot}/%{_datadir}/applications/ \
  --add-category=2DGraphics \
  support/veusz.desktop

# link main veusz icon also into hicolor-icon-theme dir (for desktop file)
for size in 16 32 48 64 128; do
    odir=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p $odir
    ln -s %{_datadir}/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $odir
ln -s %{_datadir}/veusz/icons/veusz.svg $odir/veusz.svg

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p Documents/man-page/veusz.1 -m 0644 %{buildroot}%{_mandir}/man1

# Remove an unneeded hidden file from documentation
rm Documents/manual/html/.buildinfo

%python_expand %fdupes %{buildroot}%{$python_sitearch}/veusz/

%check
export DISPLAY="%{X_display}"
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B tests/runselftest.py
}

%pretrans
# icons/examples/tests were dirs from previous installations, need to rm these first
if [ $1 -gt 1 ]; then
  %python_expand rm -fr %{$python_sitearch}/veusz/{examples,icons}
fi

%files %{python_files}
%doc README.md AUTHORS ChangeLog
%doc Documents/manual/html
%license COPYING
%{python_sitearch}/veusz-%{version}-py%{python_version}.egg-info
%{python_sitearch}/veusz/

%files -n veusz
%license COPYING
%{_bindir}/veusz
%{_datadir}/applications/veusz.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/veusz.appdata.xml
%{_datadir}/icons/hicolor/*/apps/veusz.*
%{_datadir}/mime/packages/veusz.xml
%{_mandir}/man1/*

%files -n veusz-common
%license COPYING
%{_datadir}/veusz/

%changelog
