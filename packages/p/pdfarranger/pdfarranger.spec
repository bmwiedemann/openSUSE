#
# spec file for package pdfarranger
#
# Copyright (c) 2022 SUSE LLC
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


Name:           pdfarranger
Version:        1.9.2
Release:        0
Summary:        Merge, split, rotate, crop, and rearrange pages of PDF documents
License:        GPL-3.0-only
URL:            https://github.com/pdfarranger/pdfarranger
Source:         https://github.com/pdfarranger/pdfarranger/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       gtk3
Requires:       python3-cairo
Requires:       python3-dateutil >= 2.4.0
Requires:       python3-gobject-Gdk
Requires:       python3-pikepdf >= 2.8.0
Requires:       typelib-1_0-Gtk-3_0
Requires:       typelib-1_0-Poppler-0_18
Recommends:     python3-img2pdf >= 0.3.4
BuildArch:      noarch

%description
pdfarranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using a graphical interface. It is a frontend for pikepdf.

pdfarranger is a fork of Konstantinos Poulios’s pdfshuffler. It is
a humble attempt to make the project a bit more active.

%lang_package

%prep
%autosetup -p1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%suse_update_desktop_file -r com.github.jeromerobert.pdfarranger Graphics VectorGraphics
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/applications/com.github.jeromerobert.pdfarranger.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/com.github.jeromerobert.pdfarranger.metainfo.xml

%files lang -f %{name}.lang

%changelog
