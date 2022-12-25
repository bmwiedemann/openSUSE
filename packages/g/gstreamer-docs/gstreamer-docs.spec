#
# spec file for package gstreamer-docs
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


%define         gst_branch      1.0

Name:           gstreamer-docs
Version:        1.20.5
Release:        0
Summary:        GStreamer documentation
License:        (BSD-2-Clause OR LGPL-2.1-or-later OR MIT) AND OPL-1.0 AND CC-BY-SA-4.0

#  Tutorial source code:
#  All tutorial code is licensed under any of the following licenses (your choice):
#  2-clause BSD license ("simplified BSD license") (LICENSE.BSD)
#  MIT license (LICENSE.MIT)
#  LGPL v2.1 (LICENSE.LGPL-2.1)
#  Application Developer Manual and Plugin Writer's Guide:
#  Open Publication License v1.0 (LICENSE.OPL), for historical reasons.
#  Documentation:
#  Creative Commons CC-BY-SA-4.0 license, but some parts of the documentation
#  may still be licensed differently (e.g. LGPLv2.1) for historical reasons.

URL:            https://gstreamer.freedesktop.org/
Source:         %{url}/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
Obsoletes:      gstreamer-doc < %{version}
Obsoletes:      gstreamer-plugins-bad-doc < %{version}
Obsoletes:      gstreamer-plugins-base-doc < %{version}
Obsoletes:      gstreamer-plugins-good-doc < %{version}
Obsoletes:      gstreamer-plugins-libav-doc < %{version}
Obsoletes:      gstreamer-plugins-ugly-doc < %{version}
Obsoletes:      gstreamer-plugins-vaapi-doc < %{version}
Provides:       gstreamer-doc = %{version}
Provides:       gstreamer-plugins-bad-doc = %{version}
Provides:       gstreamer-plugins-base-doc = %{version}
Provides:       gstreamer-plugins-good-doc = %{version}
Provides:       gstreamer-plugins-libav-doc = %{version}
Provides:       gstreamer-plugins-ugly-doc = %{version}
Provides:       gstreamer-plugins-vaapi-doc = %{version}
BuildArch:      noarch

%description
GStreamer documentation.

%prep
%autosetup

%build

%install

# Move devhelp into the right directory
mkdir -p %{buildroot}%{_datadir}/gtk-doc/html/
cp -r devhelp/books/GStreamer %{buildroot}%{_datadir}/gtk-doc/html/GStreamer-%{gst_branch}

# Remove the search assets, we use devhelp search
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/GStreamer-%{gst_branch}/assets/js/search

# Rename the devhelp docs to include the version
cp -r %{buildroot}%{_datadir}/gtk-doc/html/GStreamer-%{gst_branch}/GStreamer.devhelp2 \
   %{buildroot}%{_datadir}/gtk-doc/html/GStreamer-%{gst_branch}/GStreamer-%{gst_branch}.devhelp2

# Remove duplicates
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE.BSD LICENSE.CC-BY-SA-4.0 LICENSE.LGPL-2.1 LICENSE.MIT LICENSE.OPL
%doc README.md
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/GStreamer-%{gst_branch}/

%changelog
