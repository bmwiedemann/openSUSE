#
# spec file for package paperwork
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           paperwork
Version:        0.3.2
Release:        0
Summary:        Tool to make papers searchable
License:        GPL-3.0-only
Group:          Productivity
Url:            https://openpaper.work
Source:         https://github.com/jflesch/paperwork/archive/%{version}.tar.gz/#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/jflesch/paperwork/pull/497
Patch0:         desktop.patch
# PATCH-FIX-UPSTREAM https://github.com/jflesch/paperwork/pull/498
Patch1:         icon.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(zlib)
Requires:       poppler-tools
Requires:       python-Levenshtein
Requires:       python-Pillow
Requires:       python-Whoosh
Requires:       python-cairo
Requires:       python-enchant
Requires:       python-gobject
Requires:       python-gobject-cairo
Requires:       python-pip
Requires:       python-pycountry
Requires:       python-pyinsane
Requires:       python-pyocr
Requires:       python-scipy
Requires:       python-simplebayes
Requires:       python-termcolor
Recommends:     sane-backends
Recommends:     tesseract-ocr
BuildArch:      noarch

%description
The basic idea behind Paperwork is "scan & forget". You should be able to just
scan a new document and forget about it until the day you need it again. Let the
machine do most of the work.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
chmod +x localize.sh
sh localize.sh upd-po && sh localize.sh gen-mo
python setup.py build

%install
python setup.py install  --prefix=%{_prefix} --optimize=2  --root=%{buildroot}
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.markdown
%{_bindir}/*
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
