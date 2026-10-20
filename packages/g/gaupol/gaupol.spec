#
# spec file for package gaupol
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


%define long_name io.otsaloma.gaupol
%define skip_python2 1
%bcond_without test
Name:           gaupol
Version:        2.0.1
Release:        0
Summary:        GTK Subtitle editor
License:        GPL-3.0-or-later
URL:            https://otsaloma.io/gaupol/
Source0:        https://github.com/otsaloma/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gaupol-1.7-desktop.patch prusnak@suse.cz -- add desktop category
Patch0:         gaupol-1.7-desktop.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
Requires:       python3
Requires:       python3-aeidon = %{version}
Requires:       python3-gobject >= 3.40
Requires:       typelib-1_0-Gtk-4_0 >= 4.12
Recommends:     iso-codes >= 3.67
Recommends:     typelib-1_0-Gst-1_0 >= 1.18
Recommends:     typelib-1_0-Spelling-1 >= 0.2
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitelib %{python3_sitelib}
%define python_files() -n python3-%{**}
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module charset-normalizer}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pytest}
BuildRequires:  myspell-en_US
BuildRequires:  typelib-1_0-Spelling-1
%endif

%description
Gaupol is an editor for text-based subtitle files. It supports multiple subtitle
file formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

Gaupol should run on all Unix-like (GNU/Linux, *BSD, etc.) operating systems and
on Windows. Technically it should be able to run on Mac as well, but that has
not been tested nor made convenient. Gaupol's user interface is based on the GTK
toolkit and has been designed to best fit the GNOME desktop environment.

%if 0%{?python_subpackage_only}
%package -n python-aeidon
Summary:        Package for reading, writing and manipulating text-based subtitle files
Requires:       %{python_module charset-normalizer > 2.0}

%description -n python-aeidon
This is a Python package for reading, writing and manipulating
text-based subtitle files. It is separate from the gaupol package,
which provides a subtitle editor application with a GTK
user interface.

%else

%package -n python3-aeidon
Summary:        Package for reading, writing and manipulating text-based subtitle files
Requires:       %{python_module charset-normalizer > 2.0}
Provides:       python-aeidon = %{version}
Obsoletes:      python-aeidon < %{version}

%description -n python3-aeidon
This is a Python package for reading, writing and manipulating
text-based subtitle files. It is separate from the gaupol package,
which provides a subtitle editor application with a GTK
user interface.
%endif

%prep
%setup -q
# -p0: patch paths (data/...) carry no a/ b/ prefix, -p1 would fail
%patch -P 0 -p0

%build
%make_build build
%pyproject_wheel

%install
%pyproject_install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} INCLUDE_AEIDON=no build install
# Upstream installs bin/gaupol with an /usr/bin/env shebang; normalize it.
sed -i '1s|^#!%{_bindir}/env python3|#!%{_bindir}/python3|' %{buildroot}%{_bindir}/gaupol

%find_lang %{name}
%fdupes %{buildroot}

%if %{with test}
%check
%pytest aeidon
%endif

%files -f %{name}.lang
%doc AUTHORS.md README.md NEWS.md
%license COPYING
%{_bindir}/gaupol
%{_datadir}/%{name}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{long_name}.appdata.xml
%{_datadir}/applications/%{long_name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{long_name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{long_name}-symbolic.svg
%{_mandir}/man1/gaupol.1%{?ext_man}

%files %{python_files aeidon}
%doc AUTHORS.md README.aeidon.md NEWS.md
%license COPYING
%{python_sitelib}/aeidon
%{python_sitelib}/aeidon-%{version}.dist-info

%changelog
