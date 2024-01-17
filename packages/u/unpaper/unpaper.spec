#
# spec file for package unpaper
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


Name:           unpaper
Version:        7.0.0
Release:        0
Summary:        Post-Processing Tool for Scanned Text Pages
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.flameeyes.eu/projects/unpaper
Source:         https://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
BuildRequires:  %{python_module Sphinx >= 3.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libxslt-tools
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
The unpaper command line tool helps with post-processing scanned text
pages, especially with	book pages scanned from photocopies. unpaper
tries to remove dark edges, corrects the rotation ("deskewing"), and
aligns the centering of pages.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/unpaper
%{_mandir}/man1/unpaper.1%{?ext_man}

%changelog
