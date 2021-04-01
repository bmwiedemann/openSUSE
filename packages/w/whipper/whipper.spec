#
# spec file for package whipper
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1

Name:           whipper
Version:        0.9.0
Release:        0
Summary:        A CD ripper aiming for accuracy over speed
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            https://github.com/JoeLametta/whipper/
Source0:        https://github.com/JoeLametta/whipper/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libsndfile-devel
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  cd-paranoia >= 10.2
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module musicbrainzngs}
BuildRequires:  %{python_module mutagen}
BuildRequires:  %{python_module pycdio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  cdrdao
BuildRequires:  sox
# /SECTION
# nb: there is a difference between cd-paranoia [we want] and
#     cdparanoia [we don't]
Requires:       cd-paranoia >= 10.2
Requires:       %{python_module gobject}
Requires:       %{python_module musicbrainzngs}
Requires:       %{python_module mutagen}
Requires:       %{python_module pycdio}
Requires:       %{python_module requests}
Requires:       %{python_module ruamel.yaml}
Requires:       cdrdao
Requires:       flac
Requires:       sox
Conflicts:      morituri

%description
Whipper is an audio CD ripper that aims for accuracy over speed. It
automatically tags tracks using MusicBrainz data, takes drive offsets into
account, supports AccurateRip, and can rip certain hidden tracks.
It is written in Python 2. Whipper was forked from the Morituri project,
after Morituri development halted.

%prep
%setup -q

%build
echo "Version: %{version}" > PKG-INFO
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cd whipper/test/
# Don't run accurip tests since those needs a network connection to www.accuraterip.com
rm -f test_common_accurip.py
%python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
%pytest

%files
%doc CHANGELOG.md README
%license LICENSE
%{_bindir}/accuraterip-checksum
%{_bindir}/whipper
%{python_sitearch}/whipper
%{python_sitearch}/accuraterip.cpython*
%{python_sitearch}/%{name}-%{version}-py%{python_version}.egg-info
%{_datadir}/metainfo/com.github.whipper_team.Whipper.metainfo.xml

%changelog
