#
# spec file for package guake
#
# Copyright (c) 2025 SUSE LLC
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


# Need to re-define pythons to get pyproject_* macros working
%define pythons python3
Name:           guake
Version:        3.10
Release:        0
Summary:        Drop-down terminal for GNOME
License:        GPL-2.0-or-later
URL:            https://guake.github.io/
Source0:        https://files.pythonhosted.org/packages/source/g/guake/guake-%{version}.tar.gz
# Needed to install desktop app supporting files to FHS location; the PyPI
# source misses this, being geared towards installing everything to python module dir
Source1:        https://raw.githubusercontent.com/Guake/guake/%{version}/guake/paths.py.in
Source2:        %{name}.rpmlintrc
# PATCH-FEATURE-OPENSUSE guake-Makefile-generate-install-paths.patch badshah400@gmail.com -- Ensure data paths in python script point to the correct system installed paths
Patch0:         guake-Makefile-generate-install-paths.patch
BuildRequires:  fdupes
BuildRequires:  glib2-tools
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 57.5.0
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
%if 0%{?suse_version} < 1600
Requires:       libutempter0
%endif
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject-Gdk
Requires:       python3-pyaml
Requires:       python3-typing
Recommends:     %{name}-doc
BuildArch:      noarch
# SECTION BuildRequires for documentation
BuildRequires:  python3-Sphinx
BuildRequires:  python3-reno
BuildRequires:  python311-sphinx_rtd_theme
BuildRequires:  python311-sphinxcontrib-programoutput
# /SECTION

%lang_package

%description
Guake is a dropdown terminal made for the GNOME desktop environment.

%package doc
Summary:        Documentation for Guake
Requires:       %{name}

%description doc
Guake is a dropdown terminal made for the GNOME desktop environment.

This package provides the HTML documentation for Guake.

%prep
%autosetup -p1 -n guake-%{version}
cp %{SOURCE1} guake/

%build
# Note: At least `make generate-paths` needs to run before pyproject_wheel to set up the correct paths in guake/paths.py
%make_build PREFIX=%{_prefix} generate-desktop generate-mo generate-paths
%pyproject_wheel

# Build documentation
# non-parallel to avoid non-determinism in man/guake.1 from https://github.com/sphinx-doc/sphinx/issues/6714
make -C docs man html
rm docs/_build/html/.buildinfo

%install
%pyproject_install
%make_build DESTDIR=%{buildroot} PREFIX=%{_prefix} install-locale install-schemas

# Install documentation
mkdir -p %{buildroot}%{_docdir}/guake
cp -r docs/_build/html %{buildroot}%{_docdir}/guake/
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 docs/_build/man/*.1 %{buildroot}%{_mandir}/man1/guake.1

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{python3_sitelib}/guake/

%files
%doc README.rst
%license COPYING
%{_bindir}/guake
%{_bindir}/guake-toggle
%{_mandir}/man1/guake.1%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/guake/
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/pixmaps/*.png
%{python3_sitelib}/guake/
%{python3_sitelib}/guake-%{version}.dist-info

%files doc
%license COPYING
%doc %{_docdir}/guake/html

%files lang -f %{name}.lang
%license COPYING

%changelog
