#
# spec file for package python-veusz
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%bcond_without  test
Name:           python-veusz
Version:        3.0.1
Release:        0
Summary:        Scientific plotting library for Python
# The entire source code is GPL-2.0+ except helpers/src/_nc_cntr.c which is Python-2.0
License:        GPL-2.0+ and Python-2.0
Group:          Productivity/Scientific/Other
Url:            https://veusz.github.io/
Source0:        https://pypi.io/packages/source/v/veusz/veusz-%{version}.tar.gz
Source3:        veusz_256.png
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sip}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
%if %{with test}
BuildRequires:  %{python_module h5py}
%endif
Requires:       python-numpy
Requires:       python-qt5
Recommends:     python-h5py
%ifpython3
Recommends:     veusz
%endif
ExcludeArch:    i586

%python_subpackages

%description
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%package -n veusz
Summary:        GUI scientific plotting package
Group:          Productivity/Scientific/Other
Requires:       python3-veusz = %{version}
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Obsoletes:      veusz3 < %{version}
Provides:       veusz3 = %{version}

%description -n veusz
Veusz is a scientific plotting package, designed to create
publication-ready Postscript/PDF/SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with errors, keys, labels, stacked plots,
multiple plots, contours, shapes and fitting data.

%prep
%setup -q -n veusz-%{version}
find -name \*~ | xargs rm -f

# Remove hashbangs from eventually non-executable scripts
sed -E -i "/\#!\/usr\/bin\/env python/d" veusz/veusz_{listen,main}.py

%build
# no-strict-aliasing required for python2
%ifpython2
export CFLAGS="%{optflags} -fno-strict-aliasing"
%else
export CFLAGS="%{optflags}"
%endif

%python_build

%install
%python_install

# Install .desktop, mime and appdata files from upstream tarball
install -Dm0644 support/veusz.appdata.xml %{buildroot}%{_datadir}/appdata/veusz.appdata.xml
install -Dm0644 support/veusz.xml %{buildroot}/%{_datadir}/mime/packages/veusz.xml
desktop-file-install -m 0644 \
  --dir=%{buildroot}/%{_datadir}/applications/ \
  --add-category=2DGraphics \
  support/veusz.desktop

# move icon files to /usr/share/pixmaps/veusz
%python_expand install -m 0644 %{SOURCE3} %{buildroot}%{$python_sitearch}/veusz/icons/veusz_256.png
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

%fdupes %{buildroot}%{python_sitearch}/veusz/
%fdupes %{buildroot}%{python3_sitearch}/veusz/

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
QT_QPA_PLATFORM=minimal $python -B tests/runselftest.py
}
%endif

%post -n veusz
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications
%icon_theme_cache_post

%postun -n veusz
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database %{_datadir}/applications
%icon_theme_cache_postun

%files %{python_files}
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
%doc Documents/manual/html
%{python_sitearch}/veusz-%{version}-py*.egg-info
%{python_sitearch}/veusz/

%files -n veusz
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_bindir}/veusz
%{_datadir}/applications/veusz.desktop
%{_datadir}/pixmaps/veusz/
%dir %{_datadir}/appdata
%{_datadir}/appdata/veusz.appdata.xml
%{_datadir}/icons/hicolor/*/apps/veusz.*
%{_datadir}/mime/packages/veusz.xml
%{_mandir}/man1/*

%changelog
