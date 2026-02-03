#
# spec file for package pdfarranger
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2020 Karl Cheng <qantas94heavy@gmail.com>
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


%if 0%{?suse_version} >= 1600
%define pythons python3
%else
%define pythons python311
%endif

Name:           pdfarranger
Version:        1.13.0
Release:        0
Summary:        Merge, split, rotate, crop, and rearrange pages of PDF documents
License:        GPL-3.0-only
URL:            https://github.com/pdfarranger/pdfarranger
Source0:        https://github.com/pdfarranger/pdfarranger/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
# Section Tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module cairo}
BuildRequires:  %{python_module dateutil >= 2.4.0}
BuildRequires:  %{python_module gobject-Gdk}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pikepdf >= 6}
BuildRequires:  typelib-1_0-Gtk-3_0
BuildRequires:  typelib-1_0-Poppler-0_18
# /Section
Requires:       %{python_flavor}-cairo
Requires:       %{python_flavor}-dateutil >= 2.4.0
Requires:       %{python_flavor}-gobject-Gdk
Requires:       %{python_flavor}-packaging
Requires:       %{python_flavor}-pikepdf >= 6
Requires:       typelib-1_0-Gtk-3_0
Requires:       typelib-1_0-Poppler-0_18
Recommends:     %{python_flavor}-img2pdf >= 0.3.4
BuildArch:      noarch

%description
pdfarranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using a graphical interface. It is a frontend for pikepdf.

%lang_package

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}

%check
%pytest

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}*.*-info
%{_datadir}/applications/com.github.jeromerobert.pdfarranger.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/com.github.jeromerobert.pdfarranger.metainfo.xml

%files lang -f %{name}.lang

%changelog
